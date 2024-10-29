import requests
from PyQt5.QtCore import pyqtSignal
from qgis.core import Qgis, QgsMessageLog, QgsTask


class QueryTask(QgsTask):
    calcResult = pyqtSignal(list)

    def __init__(self, queries):
        super().__init__("Suoritetaan laskentaa", QgsTask.CanCancel)
        self.exception = None
        self.queries = queries
        self.results = []

    def run(self):
        if self.exception:
            return False

        for i, query in enumerate(self.queries):
            self.setProgress(i / len(self.queries) * 100)
            if self.isCanceled():
                self.exception = "Laskenta keskeytetty"
                return False
            try:
                self.results.append(requests.get(**query).json())
            except Exception as e:
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
