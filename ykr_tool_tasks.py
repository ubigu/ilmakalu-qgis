import json

import requests
from PyQt5.QtCore import pyqtSignal  # type: ignore
from qgis.core import Qgis, QgsMessageLog, QgsTask  # type: ignore


class QueryTask(QgsTask):
    calcResult = pyqtSignal(list)

    def __init__(self, queries: list[dict], inputLayers: list[dict], connParams: dict):
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

    def run(self) -> bool:
        """Run the task

        :returns: A boolean indicating whether the calculation was successful or not
        """
        if self.exception:
            return False
        for i, query in enumerate(self.queries):
            self.setProgress(i / len(self.queries) * 100)
            if self.isCanceled():
                self.exception = "Laskenta keskeytetty"
                return False
            try:
                resp = (
                    requests.post(**(query | {"json": self.body}))
                    if len(self.body) > 0
                    else requests.get(**query)
                )
                result = resp.json()
                if not resp.ok:
                    print(result["detail"])
                    raise resp.raise_for_status() or Exception("An error occurred")
                self.results.append({"id": resp.headers["id"], "geojson": result})
            except Exception as e:
                print(f"Laskentavirhe: {e}")
                self.exception = e
                return False
        self.calcResult.emit(self.results)
        return True

    def finished(self, result: dict):
        if not result:
            QgsMessageLog.logMessage(
                "Laskentavirhe: " + str(self.exception), "YKRTool", Qgis.Critical
            )
            # raise self.exception
            self.cancel()
