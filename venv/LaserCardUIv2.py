# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaserCardUI4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import sys
import time

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.outputBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputBox.setObjectName("outputBox")
        self.gridLayout_2.addWidget(self.outputBox, 5, 0, 1, 1)
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
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.dataSensors = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataSensors.setObjectName("dataSensors")
        self.gridLayout.addWidget(self.dataSensors, 3, 1, 1, 1)
        self.dataOptPwrCal = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataOptPwrCal.setObjectName("dataOptPwrCal")
        self.gridLayout.addWidget(self.dataOptPwrCal, 5, 3, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 7, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 6, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)
        self.dataAlarms = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataAlarms.setObjectName("dataAlarms")
        self.gridLayout.addWidget(self.dataAlarms, 6, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.dataRFatt1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataRFatt1.setObjectName("dataRFatt1")
        self.gridLayout.addWidget(self.dataRFatt1, 1, 3, 1, 1)
        self.dataAdc = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataAdc.setObjectName("dataAdc")
        self.gridLayout.addWidget(self.dataAdc, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 2, 1, 1)
        self.dataRFswitch = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataRFswitch.setObjectName("dataRFswitch")
        self.gridLayout.addWidget(self.dataRFswitch, 3, 3, 1, 1)
        self.dataControls = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataControls.setObjectName("dataControls")
        self.gridLayout.addWidget(self.dataControls, 5, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.dataAlarmThresholds = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataAlarmThresholds.setObjectName("dataAlarmThresholds")
        self.gridLayout.addWidget(self.dataAlarmThresholds, 8, 1, 1, 1)
        self.dataAlarmMask = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataAlarmMask.setObjectName("dataAlarmMask")
        self.gridLayout.addWidget(self.dataAlarmMask, 7, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 5, 2, 1, 1)
        self.dataRFdet = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataRFdet.setObjectName("dataRFdet")
        self.gridLayout.addWidget(self.dataRFdet, 6, 3, 1, 1)
        self.dataLaserAPC = QtWidgets.QTextBrowser(self.centralwidget)
        self.dataLaserAPC.setObjectName("dataLaserAPC")
        self.gridLayout.addWidget(self.dataLaserAPC, 7, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # LINKING UI TO INFO
        self.displayCOMports()
        self.btnCommand.clicked.connect(self.commandButtonResponse)
        self.btnRefresh.clicked.connect(self.displayCOMports)

        # RETRANSLATING
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ''''# SHOW READ DATA
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
        self.dataLaserAPC.setPlainText(self.doCommand("readLaserAPC"))'''

        #listVars, listVals = self.extractVars(self.dataLaserAPC.toPlainText())
        #self.outputBox.setPlainText(listVars + listVals)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Laser Card Test"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))
        self.label_2.setText(_translate("MainWindow", "Type command:"))
        self.btnCommand.setText(_translate("MainWindow", "Do Command"))
        self.label_3.setText(_translate("MainWindow", "Output:"))
        self.label.setText(_translate("MainWindow", "Choose COM Port:"))
        self.label_4.setText(_translate("MainWindow", "READ DATA:"))
        self.label_15.setText(_translate("MainWindow", "Laser APC:"))
        self.label_14.setText(_translate("MainWindow", "RF Detector Calibration:"))
        self.label_11.setText(_translate("MainWindow", "Alarm Mask:"))
        self.label_5.setText(_translate("MainWindow", "ADC:"))
        self.label_7.setText(_translate("MainWindow", "Sensors:"))
        self.label_8.setText(_translate("MainWindow", "RF Switch:"))
        self.label_6.setText(_translate("MainWindow", "RFattenuator1:"))
        self.label_9.setText(_translate("MainWindow", "Controls:"))
        self.label_10.setText(_translate("MainWindow", "Alarms:"))
        self.label_12.setText(_translate("MainWindow", "Alarm Thresholds:"))
        self.label_13.setText(_translate("MainWindow", "Optical Power Calibration:"))

    #EXTERNAL FUNCTIONS in class
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
            boxResponse = self.outputBox.toPlainText() #keeps current text as a log
            #boxResponse = ""
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
            ser.close()
            boxResponse = boxResponse[:-6]
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

