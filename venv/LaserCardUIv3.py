# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaserCardUI7.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, QDialog
from DialogAlarmMask import Ui_dialogAlarmMask
from DialogRFattenuator1 import Ui_dialogRFattenuator1
from DialogRFswitch import Ui_dialogRFswitch
from DialogOpticalPowerCalibration import Ui_dialogOpticalPowerCalibration
from DialogRFDetectorCalibration import Ui_dialogRFDetectorCalibration
from DialogAlarmThresholds import Ui_dialogAlarmThresholds
from DialogLaserAPC import Ui_dialogLaserAPC
from DialogControls import Ui_dialogControls

import serial
import sys
import time

#TO-DO:
#/UPDATE UI's WITH MULTIPLE VALS W/ LABELS
#OTHER SUB UIS: -RFDet, -LaserAPC, -Alarm Thresholds, Controls, ADC
#/DO FOR RX
#FIGURE OUT REFRESHING MECHANIC
#/FIGURE OUT SIZING CONSTRAINTS

# Gets all COM ports connected
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

class Ui_MainWindow(object):
    #my_signal = QtCore.pyqtSignal(str)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 721)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)
        self.btnRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName("btnRefresh")
        self.gridLayout_2.addWidget(self.btnRefresh, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.btnCommand = QtWidgets.QPushButton(self.centralwidget)
        self.btnCommand.setAutoDefault(True)
        self.btnCommand.setDefault(True)
        self.btnCommand.setObjectName("btnCommand")
        self.gridLayout_2.addWidget(self.btnCommand, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.outputBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputBox.setObjectName("outputBox")
        self.gridLayout_2.addWidget(self.outputBox, 5, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.dataAlarms = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataAlarms.setObjectName("dataAlarms")
        self.gridLayout.addWidget(self.dataAlarms, 6, 1, 1, 1)
        self.dataRFatt1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataRFatt1.setObjectName("dataRFatt1")
        self.gridLayout.addWidget(self.dataRFatt1, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.dataSensors = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataSensors.setObjectName("dataSensors")
        self.gridLayout.addWidget(self.dataSensors, 3, 1, 1, 1)
        self.dataOptPwrCal = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataOptPwrCal.setObjectName("dataOptPwrCal")
        self.gridLayout.addWidget(self.dataOptPwrCal, 5, 3, 1, 1)
        self.dataAlarmThresholds = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataAlarmThresholds.setObjectName("dataAlarmThresholds")
        self.gridLayout.addWidget(self.dataAlarmThresholds, 8, 1, 1, 1)
        self.dataAlarmMask = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataAlarmMask.setObjectName("dataAlarmMask")
        self.gridLayout.addWidget(self.dataAlarmMask, 7, 1, 1, 1)
        self.dataRFdet = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataRFdet.setObjectName("dataRFdet")
        self.gridLayout.addWidget(self.dataRFdet, 6, 3, 1, 1)
        self.dataLaserAPC = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataLaserAPC.setObjectName("dataLaserAPC")
        self.gridLayout.addWidget(self.dataLaserAPC, 7, 3, 1, 1)
        self.btnAdc = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdc.setObjectName("btnAdc")
        self.gridLayout.addWidget(self.btnAdc, 1, 0, 2, 1)
        self.btnControls = QtWidgets.QPushButton(self.centralwidget)
        self.btnControls.setObjectName("btnControls")
        self.gridLayout.addWidget(self.btnControls, 5, 0, 1, 1)
        self.btnSensors = QtWidgets.QPushButton(self.centralwidget)
        self.btnSensors.setObjectName("btnSensors")
        self.gridLayout.addWidget(self.btnSensors, 3, 0, 1, 1)
        self.dataAdc = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataAdc.setObjectName("dataAdc")
        self.gridLayout.addWidget(self.dataAdc, 1, 1, 1, 1)
        self.dataControls = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataControls.setObjectName("dataControls")
        self.gridLayout.addWidget(self.dataControls, 5, 1, 1, 1)
        self.dataRFswitch = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataRFswitch.setObjectName("dataRFswitch")
        self.gridLayout.addWidget(self.dataRFswitch, 3, 3, 1, 1)
        self.btnAlarms = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlarms.setObjectName("btnAlarms")
        self.gridLayout.addWidget(self.btnAlarms, 6, 0, 1, 1)
        self.btnAlarmsMask = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlarmsMask.setObjectName("btnAlarmsMask")
        self.gridLayout.addWidget(self.btnAlarmsMask, 7, 0, 1, 1)
        self.btnAlarmThresholds = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlarmThresholds.setObjectName("btnAlarmThresholds")
        self.gridLayout.addWidget(self.btnAlarmThresholds, 8, 0, 1, 1)
        self.btnRFattenuator1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnRFattenuator1.setObjectName("btnRFattenuator1")
        self.gridLayout.addWidget(self.btnRFattenuator1, 1, 2, 1, 1)
        self.btnRFswitch = QtWidgets.QPushButton(self.centralwidget)
        self.btnRFswitch.setObjectName("btnRFswitch")
        self.gridLayout.addWidget(self.btnRFswitch, 3, 2, 1, 1)
        self.btnOptPwrCal = QtWidgets.QPushButton(self.centralwidget)
        self.btnOptPwrCal.setObjectName("btnOptPwrCal")
        self.gridLayout.addWidget(self.btnOptPwrCal, 5, 2, 1, 1)
        self.btnRFdet = QtWidgets.QPushButton(self.centralwidget)
        self.btnRFdet.setObjectName("btnRFdet")
        self.gridLayout.addWidget(self.btnRFdet, 6, 2, 1, 1)
        self.btnLaserAPC = QtWidgets.QPushButton(self.centralwidget)
        self.btnLaserAPC.setObjectName("btnLaserAPC")
        self.gridLayout.addWidget(self.btnLaserAPC, 7, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 6, 0, 1, 1)
        self.btnRefreshData = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefreshData.setObjectName("btnRefreshData")
        self.gridLayout_2.addWidget(self.btnRefreshData, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.btnAdc.setEnabled(False)
        self.btnSensors.setEnabled(False)
        self.btnAlarms.setEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnGetInfo = QtWidgets.QPushButton(self.centralwidget)
        self.btnGetInfo.setObjectName("btnGetInfo")
        self.verticalLayout.addWidget(self.btnGetInfo)
        self.btnClearAlarms = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearAlarms.setObjectName("btnClearAlarms")
        self.verticalLayout.addWidget(self.btnClearAlarms)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.verticalLayout.addWidget(self.btnSave)
        self.btnReset = QtWidgets.QPushButton(self.centralwidget)
        self.btnReset.setObjectName("btnReset")
        self.verticalLayout.addWidget(self.btnReset)
        self.gridLayout_2.addLayout(self.verticalLayout, 5, 1, 1, 1)


        # LINKING UI TO INFO
        self.displayCOMports()
        self.btnCommand.clicked.connect(self.commandButtonResponse)
        self.btnRefreshData.clicked.connect(self.refreshData)
        self.btnRefresh.clicked.connect(self.displayCOMports)
        self.btnGetInfo.clicked.connect(lambda: self.outputBox.setText(self.doCommand("info")))
        self.btnSave.clicked.connect(lambda: self.outputBox.setText(self.doCommand("save")))
        self.btnReset.clicked.connect(lambda: self.outputBox.setText(self.doCommand("reset")))
        self.btnClearAlarms.clicked.connect(lambda: self.outputBox.setText(self.doCommand("clearAlarms")))

        self.btnAlarmsMask.clicked.connect(lambda: self.showDialog("AlarmsMask"))
        self.btnRFattenuator1.clicked.connect(lambda: self.showDialog("RFattenuator1"))
        self.btnRFswitch.clicked.connect(lambda: self.showDialog("RFswitch"))
        self.btnOptPwrCal.clicked.connect(lambda: self.showDialog("OptPwrCal"))
        self.btnRFdet.clicked.connect(lambda: self.showDialog("RFdet"))
        self.btnAlarmThresholds.clicked.connect(lambda: self.showDialog("AlarmThresholds"))
        self.btnLaserAPC.clicked.connect(lambda: self.showDialog("LaserAPC"))
        self.btnControls.clicked.connect(lambda: self.showDialog("Controls"))

        #self.comboBox.currentIndexChanged.connect(lambda: self.refreshData)

        # RETRANSLATING
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.dataAdc.setPlainText(self.doCommand("readAdc"))
        self.dataSensors.setPlainText(self.doCommand("readSensors"))
        self.dataControls.setPlainText(self.doCommand("readControls"))
        self.dataAlarms.setPlainText(self.doCommand("readAlarms"))
        self.dataAlarmMask.setPlainText(self.doCommand("readAlarmMask"))
        self.dataAlarmThresholds.setPlainText(self.doCommand("readAlarmThresholds"))
        self.dataRFatt1.setPlainText(self.doCommand("readRFattenuator1"))
        self.dataRFswitch.setPlainText(self.doCommand("readRFswitch"))
        self.dataOptPwrCal.setPlainText(self.doCommand("readCalOptPwr"))
        self.dataRFdet.setPlainText(self.doCommand("readCalRFDet"))
        self.dataLaserAPC.setPlainText(self.doCommand("readLaserAPC"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Laser Card Test"))
        self.label.setText(_translate("MainWindow", "Choose COM Port:"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh Port List"))
        self.label_2.setText(_translate("MainWindow", "Type command:"))
        self.btnCommand.setText(_translate("MainWindow", "Do Command"))
        self.label_3.setText(_translate("MainWindow", "Output:"))
        self.label_4.setText(_translate("MainWindow", "Laser Card Data:"))
        self.btnAdc.setText(_translate("MainWindow", "ADC:"))
        self.btnControls.setText(_translate("MainWindow", "Controls:"))
        self.btnSensors.setText(_translate("MainWindow", "Sensors:"))
        self.btnAlarms.setText(_translate("MainWindow", "Alarms:"))
        self.btnAlarmsMask.setText(_translate("MainWindow", "Alarms Mask:"))
        self.btnAlarmThresholds.setText(_translate("MainWindow", "Alarm Thresholds:"))
        self.btnRFattenuator1.setText(_translate("MainWindow", "RFattenuator1:"))
        self.btnRFswitch.setText(_translate("MainWindow", "RF Switch:"))
        self.btnOptPwrCal.setText(_translate("MainWindow", "Optical Power Calibration:"))
        self.btnRFdet.setText(_translate("MainWindow", "RF Detector Calibration:"))
        self.btnLaserAPC.setText(_translate("MainWindow", "Laser APC:"))
        self.btnRefreshData.setText(_translate("MainWindow", "Refresh Data"))
        self.btnGetInfo.setText(_translate("MainWindow", "Get Info"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnReset.setText(_translate("MainWindow", "Reset"))
        self.btnClearAlarms.setText(_translate("MainWindow", "Clear Alarms"))


#EXTERNAL FUNCTIONS in class
    def showDialog(self, id):
        # INSTANTIATE DIALOG
        dialog = QtWidgets.QDialog()

        # CHOOSE WHICH UI
        if (id == "AlarmsMask"):
            ui = Ui_dialogAlarmMask()
        if (id == "RFattenuator1"):
            ui = Ui_dialogRFattenuator1()
        if (id == "RFswitch"):
            ui = Ui_dialogRFswitch()
        if (id == "OptPwrCal"):
            ui = Ui_dialogOpticalPowerCalibration()
        if (id == "RFdet"):
            ui = Ui_dialogRFDetectorCalibration()
        if (id == "AlarmThresholds"):
            ui = Ui_dialogAlarmThresholds()
        if (id == "LaserAPC"):
            ui = Ui_dialogLaserAPC()
        if (id == "Controls"):
            ui = Ui_dialogControls()

        ui.setupUi(dialog, self.getCOMPort())  # Send COM info to other dialog

        dialog.show()
        dialog.exec_()

        # ON EXIT
        self.refreshData()

    def getCOMPort(self):
        return self.comboBox.currentText()

    def refreshData(self):
        # SHOW READ DATA
        self.dataAdc.setPlainText(self.doCommand("readAdc"))
        self.dataSensors.setPlainText(self.doCommand("readSensors"))
        self.dataControls.setPlainText(self.doCommand("readControls"))
        self.dataAlarms.setPlainText(self.doCommand("readAlarms"))
        self.dataAlarmMask.setPlainText(self.doCommand("readAlarmMask"))
        self.dataAlarmThresholds.setPlainText(self.doCommand("readAlarmThresholds"))
        self.dataRFatt1.setPlainText(self.doCommand("readRFattenuator1"))
        self.dataRFswitch.setPlainText(self.doCommand("readRFswitch"))
        self.dataOptPwrCal.setPlainText(self.doCommand("readCalOptPwr"))
        self.dataRFdet.setPlainText(self.doCommand("readCalRFDet"))
        self.dataLaserAPC.setPlainText(self.doCommand("readLaserAPC"))

    def commandButtonResponse(self):
        print("Command Button Clicked")

        # Get USB serial & run terminal code
        portNum = self.comboBox.currentText()
        print(portNum)

        try:
            ser = serial.Serial(portNum, 115200)  # open serial port

            # To get rid of "garbage lines"
            # ser.write(bytes("\r", encoding='ascii'))

            # Receive command and write into buffer
            content = self.lineEdit.text()
            if (content is ""):
                return
            else:
                command = content + "\r\n"
                for i in range(len(command)):
                    b = bytes(command[i], encoding='ascii')
                    ser.write(b)

            # Post output --> detect till message is done
            #boxResponse = self.outputBox.toPlainText() #keeps current text as a log
            boxResponse = ""
            slash = 0
            while slash < 6: #\r\n\r\n\r\n
                response = ser.read_until('\r\n\r\n\r\n', 1)
                #print(response)
                boxResponse += str(response, 'ascii')
                if (response == b'\r' or response == b'\n'):
                    slash += 1
                else:
                    slash = 0

            # Output string
            print("Out of loop")
            #boxResponse = boxResponse[:-6]
            self.outputBox.setPlainText(boxResponse)

            #Done and refresh
            ser.close()
            self.refreshData
            #self.displayCOMports()
        except:
            self.outputBox.setPlainText("Chosen COM Port does not exist. Either replug your device or refresh your list of devices.\r\n\r\n\r\n")

    # Returns: List of string vars and list of string vals
    def extractVars(self, output):
        listVars = []
        listVals = []
        i = 0
        while i < len(output):
            currStr = ""
            while output[i] != '=' and i < len(output):
                currStr += output[i]
                i += 1
            listVars.append(currStr)
            currStr = ""
            i += 1
            while output[i] != '\n' and i < len(output):
                currStr += output[i]
                i += 1
            i += 1

        return listVars, listVals


    # Returns: String of output
    def doCommand(self, input):
        print("doCommand executed")

        # Get USB serial & run terminal code
        portNum = self.comboBox.currentText()
        print(portNum)

        try:
            ser = serial.Serial(portNum, 115200)  # open serial port

            # Receive command and write into buffer
            content = input
            if (content is ""):
                return
            else:
                command = content + "\r\n"
                for i in range(len(command)):
                    b = bytes(command[i], encoding='ascii')
                    ser.write(b)

            # Post output --> detect till message is done
            # boxResponse = self.outputBox.toPlainText()  # keeps current text as a log
            boxResponse = ""
            slash = 0

            ser.readline()  # to skip input line
            while slash < 6:  # \r\n\r\n\r\n
                response = ser.read_until('\r\n\r\n\r\n', 1)
                # print(response)
                boxResponse += str(response, 'ascii')
                if (response == b'\r' or response == b'\n'):
                    slash += 1
                else:
                    slash = 0

            # Done and refresh
            self.refreshData
            ser.close()
            #print(boxResponse)

            boxResponse = boxResponse[:-6]
            if (boxResponse == "Command not recognised.  Enter 'help' to view a list of available commands."):
                boxResponse = "This device does not have data for this category."
            return boxResponse
        except:
            self.outputBox.setPlainText(
                "Chosen COM Port does not exist. Either replug your device or refresh your list of devices.\r\n\r\n\r\n")

    def displayCOMports(self): #refreshes COM ports
        # STORE VARIABLES
        print(serial_ports())
        OPTIONS = serial_ports()

        # In case there is no connected devices
        if (len(OPTIONS) is 0):
            OPTIONS = ["NO COM Ports"]

        # Delete all combo items, then display in combo box
        self.comboBox.clear()
        self.comboBox.addItems(OPTIONS)

        # SHOW READ DATA
        '''self.dataAdc.setPlainText(self.doCommand("readAdc"))
        self.dataSensors.setPlainText(self.doCommand("readSensors"))
        self.dataControls.setPlainText(self.doCommand("readControls"))
        self.dataAlarms.setPlainText(self.doCommand("readAlarms"))
        self.dataAlarmMask.setPlainText(self.doCommand("readAlarmMask"))
        self.dataAlarmThresholds.setPlainText(self.doCommand("readAlarmThresholds"))
        self.dataRFatt1.setPlainText(self.doCommand("readRFattenuator1"))
        self.dataRFswitch.setPlainText(self.doCommand("readRFswitch"))
        self.dataOptPwrCal.setPlainText(self.doCommand("readCalOptPwr"))
        self.dataRFdet.setPlainText(self.doCommand("readCalRFDet"))
        self.dataLaserAPC.setPlainText(self.doCommand("readLaserAPC"))'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())