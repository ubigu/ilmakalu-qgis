import json

import requests
from PyQt5.QtCore import pyqtSignal
from qgis.core import Qgis, QgsMessageLog, QgsTask


class QueryTask(QgsTask):
    calcResult = pyqtSignal(list)

    def __init__(self, queries, inputLayers, connParams):
        super().__init__("Suoritetaan laskentaa", QgsTask.CanCancel)
        self.exception = None
        self.queries = queries
        self.results = []

        self.body = {}
        if len(inputLayers) > 0:
            self.body["layers"] = json.dumps(inputLayers)
        if len(connParams) > 0 and not all(
            len(str(p or "")) <= 0 for p in connParams.values()
        ):
            self.body["connParams"] = json.dumps(connParams)

    def run(self):
        if self.exception:
            return False
        for i, query in enumerate(self.queries):
            self.setProgress(i / len(self.queries) * 100)
            if self.isCanceled():
                self.exception = "Laskenta keskeytetty"
                return False
            try:
                result = (
                    requests.post(**(query | {"json": self.body}))
                    if len(self.body) > 0
                    else requests.get(**query)
                )
                if result.ok:
                    self.results.append(result.json())
                else:
                    raise Exception(f"{result.status_code}: {result.text}")
            except Exception as e:
                print(f"Virhe yhdistettäessä rajapintaan ({e})")
                self.exception = e
                return False
        self.calcResult.emit(self.results)
        return True

    def finished(self, result):
        if not result:
            QgsMessageLog.logMessage(
                "Laskentavirhe: " + str(self.exception), "YKRTool", Qgis.Critical
            )
            # raise self.exception
            self.cancel()
