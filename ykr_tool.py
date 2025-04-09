# -*- coding: utf-8 -*-
"""
/***************************************************************************
 YKRTool
                                 A QGIS plugin
 Tampereen tulevaisuuden yhdyskuntarakenteen ilmastovaikutusten arviointityökalu
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-05-05
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Gispo Ltd.
        email                : mikael@gispo.fi
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import getpass
import json
import os

# Import the code for the dialog
from collections.abc import Callable
from configparser import ConfigParser
from datetime import datetime
from typing import Any

from dotenv import load_dotenv
from PyQt5 import uic  # type: ignore
from PyQt5.QtCore import (  # type: ignore
    QCoreApplication,
    QSettings,
    QTranslator,
    qVersion,
)
from PyQt5.QtGui import QIcon  # type: ignore
from PyQt5.QtWidgets import QAction, QDialogButtonBox, QWidget  # type: ignore
from qgis.core import (  # type: ignore
    Qgis,
    QgsApplication,
    QgsFeature,
    QgsJsonExporter,
    QgsProject,
    QgsVectorLayer,
)
from qgis.gui import QgsFileWidget  # type: ignore

# Initialize Qt resources from file resources.py
from .resources import *  # noqa: F403
from .ykr_areas import YKRAreas
from .ykr_tool_tasks import QueryTask


class YKRTool:
    """QGIS Plugin Implementation."""

    def __init__(self, iface: Any):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        locale_path = os.path.join(
            self.plugin_dir, "i18n", "YKRTool_{}.qm".format(locale)
        )

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > "4.3.3":
                QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.connParams = {}
        self.menu = self.tr("&Ilmastovaikutusten arviointityökalu")

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        self.settingsDialog = uic.loadUi(
            os.path.join(self.plugin_dir, "ykr_tool_db_settings.ui")
        )
        self.mainDialog = uic.loadUi(os.path.join(self.plugin_dir, "ykr_tool_main.ui"))
        self.infoDialog = uic.loadUi(os.path.join(self.plugin_dir, "ykr_tool_info.ui"))

        self.targetYear = None
        self.futureAreasLayer = None
        self.futureNetworkLayer = None
        self.futureStopsLayer = None
        load_dotenv(dotenv_path=os.path.join(self.plugin_dir, ".env"))
        self.urlBase = os.getenv("API_URL", "")

    # noinspection PyMethodMayBeStatic
    def tr(self, message: str) -> str:
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.

        :returns: Translated version of message.
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate("YKRTool", message)

    def add_action(
        self,
        icon_path: str,
        text: str,
        callback: Callable,
        enabled_flag: bool = True,
        add_to_menu: bool = True,
        add_to_toolbar: bool = True,
        status_tip: str | None = None,
        whats_this: str | None = None,
        parent: QWidget | None = None,
    ) -> QAction:
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :param text: Text that should be shown in menu items for this action.
        :param callback: Function to be called when the action is triggered.
        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.
        :param parent: Parent widget for the new action. Defaults None.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ":/plugins/ykr_tool/icon.png"
        self.add_action(
            icon_path,
            text=self.tr("Ilmastovaikutusten arviointityökalu"),
            callback=self.run,
            parent=self.iface.mainWindow(),
        )

        # will be set False in run()
        self.first_start = True

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr("&Ilmastovaikutusten arviointityökalu"), action
            )
            self.iface.removeToolBarIcon(action)

    def run(self) -> bool | None:
        """Run method that performs all the real work"""
        md = self.mainDialog
        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start:
            self.first_start = False
            self.setupApplication()

        activeLayer = self.iface.activeLayer()
        # Check if features are selected
        if activeLayer is not None and activeLayer.selectedFeatures():
            md.onlySelectedFeats.setEnabled(True)
        else:
            md.onlySelectedFeats.setEnabled(False)
            md.onlySelectedFeats.setChecked(False)

        md.show()

        # Run the dialog event loop
        result = md.exec_()

        # See if OK was pressed
        if result:
            try:
                self.preProcess()
            except Exception as e:
                self.iface.messageBar().pushMessage(
                    "Virhe esikäsittelyssä", str(e), Qgis.Critical, duration=0
                )
                return False

    def preProcess(self):
        """Starts calculation"""
        self.sessionParams = self.generateSessionParameters()
        self.readProcessingInput()
        self.checkLayerValidity()
        self.layersToGeoJSON()
        self.runCalculation()

    def setupApplication(self):
        """Sets up the dialogs"""
        md = self.mainDialog

        md.peikkoScenario.addItems(["wemp", "wemh", "weml", "static"])

        md.onlySelectedFeats.setEnabled(False)
        md.futureBox.setEnabled(False)

        md.futureAreasLayerList.hide()
        md.futureNetworkLayerList.hide()
        md.futureStopsLayerList.hide()

        self.__toggleLoadFileButtonState(self.settingsDialog.configFileInput.filePath())
        self.__setEventListeners()

        self.areas = YKRAreas()
        md.inputReg.addItems(self.areas.regions())
        self.handleMunicipalityToggle()

    def __setEventListeners(self):
        md = self.mainDialog
        md.settingsButton.clicked.connect(self.displaySettingsDialog)
        md.infoButton.clicked.connect(lambda: self.infoDialog.show())
        md.futureAreasLoadLayer.clicked.connect(self.handleLayerToggle)
        md.futureNetworkLoadLayer.clicked.connect(self.handleLayerToggle)
        md.futureStopsLoadLayer.clicked.connect(self.handleLayerToggle)
        md.calculateFuture.clicked.connect(self.handleLayerToggle)
        md.inputReg.currentTextChanged.connect(self.handleRegionToggle)
        md.inputMun.itemSelectionChanged.connect(self.handleMunicipalityToggle)

        sd = self.settingsDialog
        sd.loadFileButton.clicked.connect(self.setConnectionParamsFromFile)
        sd.resetSettingsButton.clicked.connect(self.clearConnectionParams)
        sd.configFileInput.fileChanged.connect(self.__toggleLoadFileButtonState)

    def __toggleLoadFileButtonState(self, txt: str):
        self.settingsDialog.loadFileButton.setEnabled(len(txt) > 0)

    def displaySettingsDialog(self):
        """Sets up and displays the settings dialog"""
        self.settingsDialog.show()
        self.settingsDialog.configFileInput.setStorageMode(QgsFileWidget.GetFile)
        self.settingsDialog.configFileInput.setFilePath(
            QSettings().value("/YKRTool/configFilePath", "", type=str)
        )

        result = self.settingsDialog.exec_()
        if result:
            self.connParams = self.readConnectionParamsFromInput()
        else:
            self.restoreConnectionParams()

    def setConnectionParamsFromFile(self):
        """Reads connection parameters from file and sets them to the input fields"""
        filePath = self.settingsDialog.configFileInput.filePath()
        QSettings().setValue("/YKRTool/configFilePath", filePath)

        try:
            self.setConnectionParamsFromInput(self.parseConfigFile(filePath))
        except Exception as e:
            self.iface.messageBar().pushMessage(
                "Virhe luettaessa tiedostoa", str(e), Qgis.Warning, duration=10
            )

    def parseConfigFile(self, filePath: str) -> dict:
        """Reads configuration file and returns parameters

        :param filePath: A path to the configuration file
        :returns: Connection parameters as a dict
        """
        # Setup an empty dict with correct keys to avoid keyerrors
        dbParams = {
            "host": "",
            "port": "",
            "database": "",
            "username": "",
            "password": "",
        }
        if not os.path.exists(filePath):
            self.iface.messageBar().pushMessage(
                "Virhe", "Tiedostoa ei voitu lukea", Qgis.Warning
            )
            return dbParams

        parser = ConfigParser()
        parser.read(filePath)
        if parser.has_section("postgresql"):
            params = parser.items("postgresql")
            for param in params:
                dbParams[param[0]] = param[1]
        else:
            self.iface.messageBar().pushMessage(
                "Virhe",
                "Tiedosto ei sisällä\
                tietokannan yhteystietoja",
                Qgis.Warning,
            )

        return dbParams

    def clearConnectionParams(self):
        sd = self.settingsDialog
        sd.dbHost.setValue("")
        sd.dbPort.setValue("")
        sd.dbName.setValue("")
        sd.dbUser.setValue("")
        sd.dbPass.setText("")

        QSettings().setValue("/YKRTool/configFilePath", "")
        sd.configFileInput.setFilePath("")

    def __getConnectionParamValue(self, key: str) -> str:
        """Get the value of the connection parameter. If not found, return an empty string

        :param key: The name of the parameter
        :returns: The value of the parameter
        """
        return "" if key not in self.connParams else self.connParams[key]

    def restoreConnectionParams(self):
        sd = self.settingsDialog
        sd.dbHost.setValue(self.__getConnectionParamValue("host"))
        sd.dbPort.setValue(self.__getConnectionParamValue("port"))
        sd.dbName.setValue(self.__getConnectionParamValue("database"))
        sd.dbUser.setValue(self.__getConnectionParamValue("username"))
        sd.dbPass.setText(self.__getConnectionParamValue("password"))

    def setConnectionParamsFromInput(self, params: dict):
        """Sets connection parameters to input fields

        :param params: The connection parameters as a dictionary
        """
        sd = self.settingsDialog
        sd.dbHost.setValue(params["host"])
        sd.dbPort.setValue(params["port"])
        sd.dbName.setValue(params["database"])
        sd.dbUser.setValue(params["username"])
        sd.dbPass.setText(params["password"])

    def readConnectionParamsFromInput(self) -> dict:
        """Reads connection parameters from user input

        :returns: The connection parameters as a dictionary
        """
        sd = self.settingsDialog
        params = {}
        params["host"] = sd.dbHost.value()
        params["port"] = sd.dbPort.value()
        params["database"] = sd.dbName.value()
        params["username"] = sd.dbUser.value()
        params["password"] = sd.dbPass.text()
        return params

    def handleRegionToggle(self, region: str):
        """Update the list of municipalities when a new region is selected

        :param region: The name of the selected region
        """
        inputMun = self.mainDialog.inputMun
        inputMun.clear()
        inputMun.addItems(self.areas.municipalities(region))
        self.mainDialog.inputMun.setCurrentRow(0)

    def handleMunicipalityToggle(self):
        """Disable the OK button if no municipalities are selected"""
        self.mainDialog.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            len(self.mainDialog.inputMun.selectedItems()) > 0
        )

    def handleLayerToggle(self):
        """Toggle UI components visibility based on selection"""
        if self.mainDialog.futureAreasLoadLayer.isChecked():
            self.mainDialog.futureAreasLayerList.show()
            self.mainDialog.futureAreasFile.hide()
        else:
            self.mainDialog.futureAreasLayerList.hide()
            self.mainDialog.futureAreasFile.show()
        if self.mainDialog.futureNetworkLoadLayer.isChecked():
            self.mainDialog.futureNetworkLayerList.show()
            self.mainDialog.futureNetworkFile.hide()
        else:
            self.mainDialog.futureNetworkLayerList.hide()
            self.mainDialog.futureNetworkFile.show()
        if self.mainDialog.futureStopsLoadLayer.isChecked():
            self.mainDialog.futureStopsLayerList.show()
            self.mainDialog.futureStopsFile.hide()
        else:
            self.mainDialog.futureStopsLayerList.hide()
            self.mainDialog.futureStopsFile.show()

        self.mainDialog.futureBox.setEnabled(
            self.mainDialog.calculateFuture.isChecked()
        )

    def generateSessionParameters(self) -> dict:
        """Get necessary values for processing session

        :returns: The session parameters as a dict"""
        return {
            "user": getpass.getuser().replace(" ", "_"),
            "baseYear": datetime.now().year,
        }

    def readProcessingInput(self):
        """Read user input from main dialog"""
        md = self.mainDialog
        self.inputLayers = []
        self.inputMun = [
            self.areas.get_mun_code(mun.text())
            for mun in md.inputMun.selectedItems()
            if mun is not None
        ]
        self.inputReg = self.areas.get_reg_code(md.inputReg.currentText())
        self.onlySelectedFeats = md.onlySelectedFeats.isChecked()
        self.peikkoScenario = md.peikkoScenario.currentText()
        self.includeLongDistance = md.includeLongDistance.isChecked()
        self.includeBusinessTravel = md.includeBusinessTravel.isChecked()

        if not md.calculateFuture.isChecked():
            self.calculateFuture = False
        else:
            self.readFutureProcessingInput()

    def readFutureProcessingInput(self):
        """Reads user input for future processing from main dialog"""
        self.calculateFuture = True
        md = self.mainDialog
        if md.futureAreasLoadLayer.isChecked():
            self.futureAreasLayer = md.futureAreasLayerList.currentLayer()
        else:
            self.futureAreasLayer = QgsVectorLayer(
                md.futureAreasFile.filePath(), "aluevaraus_tulevaisuus", "ogr"
            )
        if md.futureNetworkLoadLayer.isChecked():
            self.futureNetworkLayer = md.futureNetworkLayerList.currentLayer()
        elif md.futureNetworkFile.filePath():
            self.futureNetworkLayer = QgsVectorLayer(
                md.futureNetworkFile.filePath(), "keskusverkko_tulevaisuus", "ogr"
            )
        else:
            self.futureNetworkLayer = None
        if md.futureStopsLoadLayer.isChecked():
            self.futureStopsLayer = md.futureStopsLayerList.currentLayer()
        elif md.futureStopsFile.filePath():
            self.futureStopsLayer = QgsVectorLayer(
                md.futureStopsFile.filePath(), "joukkoliikenne_tulevaisuus", "ogr"
            )
        else:
            self.futureStopsLayer = None
        self.targetYear = md.targetYear.value()

    def checkLayerValidity(self):
        """Checks that necessary layers are valid and raise an exception if needed"""
        if self.calculateFuture:
            self.checkFutureLayerValidity()

    def checkFutureLayerValidity(self):
        """Checks if future calculation input layers are valid"""
        if not (self.futureAreasLayer and self.futureAreasLayer.isValid()):
            raise Exception("Virhe ladattaessa tulevaisuuden aluevaraustietoja")
        if self.futureNetworkLayer:
            if not self.futureNetworkLayer.isValid():
                raise Exception("Virhe ladattaessa keskusverkkotietoja")
        if self.futureStopsLayer:
            if not self.futureStopsLayer.isValid():
                raise Exception("Virhe ladattaessa joukkoliikennepysäkkitietoja")

    def __featuresToGeoJSON(self, base: str, features: list[QgsFeature]):
        """Convert the QgsFeatures to the GeoJSON format.

        :param base: The name of the SQL table to which the features are associated
        :param features: The list of the QgsFeatures to convert
        :returns: The GeoJSON
        """
        return {
            "base": base,
            "features": json.loads(QgsJsonExporter().exportFeatures(features)),
        }

    def layersToGeoJSON(self):
        """Convert the input layers to GeoJSON"""
        if self.onlySelectedFeats:
            self.inputLayers.append(
                self.__featuresToGeoJSON(
                    "aoi", self.iface.activeLayer().selectedFeatures()
                )
            )
        if self.calculateFuture:
            self.futureLayersToGeoJSON()

    def futureLayersToGeoJSON(self):
        """Convert the future layers to GeoJSON"""
        if self.futureAreasLayer is not None:
            self.inputLayers.append(
                self.__featuresToGeoJSON(
                    "plan_areas", list(self.futureAreasLayer.getFeatures())
                )
            )
        if self.futureNetworkLayer is not None:
            self.inputLayers.append(
                self.__featuresToGeoJSON(
                    "plan_centers", list(self.futureNetworkLayer.getFeatures())
                )
            )
        if self.futureStopsLayer is not None:
            self.inputLayers.append(
                self.__featuresToGeoJSON(
                    "plan_transit", list(self.futureStopsLayer.getFeatures())
                )
            )

    def runCalculation(self) -> None | bool:
        """Runs the main calculation"""
        try:
            queries = self.getCalculationQueries()
            queryTask = QueryTask(queries, self.inputLayers, self.connParams)

            queryTask.calcResult.connect(self.addResultAsLayers)
            queryTask.taskCompleted.connect(self.postCalculation)
            queryTask.taskTerminated.connect(self.postError)

            """ A workaround for the function scope variable issue, see 
            https://gis.stackexchange.com/questions/296175/issues-with-qgstask-and-task-manager/325871#325871 """
            globals()["queryTask"] = queryTask
            QgsApplication.taskManager().addTask(globals()["queryTask"])

            self.iface.messageBar().pushMessage(
                "Lasketaan", "Laskenta käynnissä", Qgis.Info, duration=15
            )
        except Exception as e:
            self.iface.messageBar().pushMessage(
                "Virhe laskennassa", str(e), Qgis.Critical, duration=0
            )
            return False

    def getCalculationQueries(self) -> list[dict]:
        """Generate queries to call processing functions in database

        :returns: The list of queries as dicts
        """
        queries = []

        params = {
            "mun": self.inputMun,
            "calculationScenario": self.peikkoScenario,
            "includeLongDistance": self.includeLongDistance,
            "includeBusinessTravel": self.includeBusinessTravel,
            "outputFormat": "geojson",
            "writeSessionInfo": True,
        }
        query = (
            {
                "url": self.urlBase + "co2-calculate-emissions/",
                "params": params | {"calculationYear": self.sessionParams["baseYear"]},
            }
            if not self.calculateFuture
            else self.generateFutureQuery(params)
        )

        query["headers"] = {
            "user": self.sessionParams["user"],
        }
        queries.append(query)
        return queries

    def generateFutureQuery(self, params: dict) -> dict:
        """Constructs a query for future calculation

        :param params: The parameters that all the queries have in common
        :returns: A dict with future parameters added
        """
        return {
            "url": self.urlBase + "co2-calculate-emissions-loop/",
            "params": params
            | {
                "baseYear": self.sessionParams["baseYear"],
                "targetYear": self.targetYear,
            },
        }

    def postCalculation(self):
        """Called after QueryTask finishes"""
        self.iface.messageBar().pushMessage(
            "Valmis",
            "Laskentasessio on valmis",
            Qgis.Success,
            duration=0,
        )

    def addResultAsLayers(self, results: list[dict]):
        """Visualize results in the map if they include features

        :param results: Results as a list of dicts. Are expected to
        contain a key 'features'
        """
        try:
            layers = []
            layerNames = [
                ("CO2 sources", "docs/CO2_sources.qml"),
                ("CO2 grid", "docs/CO2_t_grid.qml"),
            ]
            for result in results:
                for name in layerNames:
                    # Do not add a layer if there are no features
                    geojson = result["geojson"]
                    if not (geojson["features"]):
                        continue
                    layer = QgsVectorLayer(
                        json.dumps(geojson),
                        name[0] + " " + result["id"],
                        "ogr",
                    )
                    layer.loadNamedStyle(os.path.join(self.plugin_dir, name[1]))
                    renderer = layer.renderer()
                    if renderer.type() == "graduatedSymbol":
                        renderer.updateClasses(
                            layer, renderer.mode(), len(renderer.ranges())
                        )
                    layers.append(layer)
            QgsProject.instance().addMapLayers(layers)
        except Exception as e:
            self.iface.messageBar().pushMessage(
                "Virhe lisättäessä tulostasoa:", str(e), Qgis.Warning, duration=0
            )

    def postError(self):
        """Called after querytask is terminated"""
        self.iface.messageBar().pushMessage(
            "Virhe laskentafunktiota suorittaessa",
            "Katso lisätiedot virhelokista",
            Qgis.Critical,
            duration=0,
        )
