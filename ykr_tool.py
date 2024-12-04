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
import uuid
from datetime import datetime

from PyQt5 import uic
from PyQt5.QtCore import QCoreApplication, QSettings, QTranslator, qVersion
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction
from qgis.core import (
    Qgis,
    QgsApplication,
    QgsJsonExporter,
    QgsProject,
    QgsVectorLayer,
)

from .municipalities import (
    get_mun_code,
    get_mun_names_by_reg,
    get_reg_code,
    get_reg_names,
)

# Initialize Qt resources from file resources.py
from .resources import *
from .ykr_tool_tasks import QueryTask


class YKRTool:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
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
        self.menu = self.tr("&Ilmastovaikutusten arviointityökalu")

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        self.mainDialog = uic.loadUi(os.path.join(self.plugin_dir, "ykr_tool_main.ui"))
        self.infoDialog = uic.loadUi(os.path.join(self.plugin_dir, "ykr_tool_info.ui"))

        self.targetYear = None
        self.futureAreasLayer = None
        self.futureNetworkLayer = None
        self.futureStopsLayer = None
        self.urlBase = "http://localhost:4000/"

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate("YKRTool", message)

    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None,
    ):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
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

    def run(self):
        """Run method that performs all the real work"""
        md = self.mainDialog
        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start:
            self.first_start = False
            self.setupMainDialog()

        # Check if features are selected
        if self.iface.activeLayer().selectedFeatures():
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

    def setupMainDialog(self):
        """Sets up the main dialog"""
        md = self.mainDialog

        md.inputReg.currentTextChanged.connect(self.handleRegionToggle)
        md.inputReg.addItems(get_reg_names())

        md.pitkoScenario.addItems(
            ["wem", "eu80", "kasvu", "muutos", "saasto", "static"]
        )
        md.emissionsAllocation.addItems(["hjm", "em"])
        md.elecEmissionType.addItems(["hankinta", "tuotanto"])

        md.onlySelectedFeats.setEnabled(False)
        md.futureBox.setEnabled(False)

        md.infoButton.clicked.connect(lambda: self.infoDialog.show())

        md.futureAreasLayerList.hide()
        md.futureNetworkLayerList.hide()
        md.futureStopsLayerList.hide()

        md.futureAreasLoadLayer.clicked.connect(self.handleLayerToggle)
        md.futureNetworkLoadLayer.clicked.connect(self.handleLayerToggle)
        md.futureStopsLoadLayer.clicked.connect(self.handleLayerToggle)

        md.calculateFuture.clicked.connect(self.handleLayerToggle)

    def handleRegionToggle(self, region):
        inputMun = self.mainDialog.inputMun
        inputMun.clear()
        inputMun.addItems(get_mun_names_by_reg(region))

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

        if self.mainDialog.calculateFuture.isChecked():
            self.mainDialog.futureBox.setEnabled(True)
        else:
            self.mainDialog.futureBox.setEnabled(False)

    def generateSessionParameters(self):
        """Get necessary values for processing session"""
        return {
            "user": getpass.getuser().replace(" ", "_"),
            "baseYear": datetime.now().year,
            "uuid": str(uuid.uuid4()),
        }

    def readProcessingInput(self):
        """Read user input from main dialog"""
        md = self.mainDialog
        self.inputLayers = []

        self.inputMun = [get_mun_code(md.inputMun.currentText())]
        self.inputReg = get_reg_code(md.inputReg.currentText())
        self.onlySelectedFeats = md.onlySelectedFeats.isChecked()
        self.pitkoScenario = md.pitkoScenario.currentText()
        self.emissionsAllocation = md.emissionsAllocation.currentText()
        self.elecEmissionType = md.elecEmissionType.currentText()
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
        if not self.futureAreasLayer.isValid():
            raise Exception("Virhe ladattaessa tulevaisuuden aluevaraustietoja")
        if self.futureNetworkLayer:
            if not self.futureNetworkLayer.isValid():
                raise Exception("Virhe ladattaessa keskusverkkotietoja")
        if self.futureStopsLayer:
            if not self.futureStopsLayer.isValid():
                raise Exception("Virhe ladattaessa joukkoliikennepysäkkitietoja")

    def __featuresToGeoJSON(self, base, features):
        return {
            "name": (self.sessionParams["uuid"] + "_" + base)[
                :49
            ],  # truncate tablename to under 63c
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

    def runCalculation(self):
        """Runs the main calculation"""
        try:
            queries = self.getCalculationQueries()
            queryTask = QueryTask(queries, self.inputLayers)

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

    def getCalculationQueries(self):
        """Generate queries to call processing functions in database"""
        queries = []

        params = {
            "mun": self.inputMun,
            "calculationScenario": self.pitkoScenario,
            "method": self.emissionsAllocation,
            "electricityType": self.elecEmissionType,
            "includeLongDistance": self.includeLongDistance,
            "includeBusinessTravel": self.includeBusinessTravel,
            "outputFormat": "geojson",
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
            "uuid": str(self.sessionParams["uuid"]),
            "user": self.sessionParams["user"],
        }
        queries.append(query)
        return queries

    def generateFutureQuery(self, params):
        """Constructs a query for future calculation"""
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
            "Laskentasessio " + str(self.sessionParams["uuid"]) + " on valmis",
            Qgis.Success,
            duration=0,
        )

    def addResultAsLayers(self, results):
        try:
            layers = []
            layerNames = [
                ("CO2 sources", "docs/CO2_sources.qml"),
                ("CO2 grid", "docs/CO2_t_grid.qml"),
            ]
            for result in results:
                for name in layerNames:
                    # Do not add a layer if there are no features
                    if not result["features"]:
                        continue
                    layer = QgsVectorLayer(
                        json.dumps(result),
                        name[0] + " " + self.sessionParams["uuid"],
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
