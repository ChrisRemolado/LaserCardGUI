# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogControls.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import serial

VARIABLES = []

class Ui_dialogControls(object):
    def setupUi(self, dialogControls, comPort):
        dialogControls.setObjectName("dialogControls")
        dialogControls.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(dialogControls)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(dialogControls)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEditRFattenuator1 = QtWidgets.QLineEdit(dialogControls)
        self.lineEditRFattenuator1.setObjectName("lineEditRFattenuator1")
        self.gridLayout_2.addWidget(self.lineEditRFattenuator1, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(dialogControls)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(dialogControls)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.btnSetRFattenuator1 = QtWidgets.QPushButton(dialogControls)
        self.btnSetRFattenuator1.setObjectName("btnSetRFattenuator1")
        self.gridLayout_2.addWidget(self.btnSetRFattenuator1, 2, 2, 1, 1)
        self.checkBoxAGCMode = QtWidgets.QCheckBox(dialogControls)
        self.checkBoxAGCMode.setEnabled(False)
        self.checkBoxAGCMode.setObjectName("checkBoxAGCMode")
        self.gridLayout_2.addWidget(self.checkBoxAGCMode, 0, 1, 1, 1)
        self.checkBoxRFswitch = QtWidgets.QCheckBox(dialogControls)
        self.checkBoxRFswitch.setObjectName("checkBoxRFswitch")
        self.gridLayout_2.addWidget(self.checkBoxRFswitch, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(dialogControls)
        QtCore.QMetaObject.connectSlotsByName(dialogControls)

        # CONNECT TO GUI
        #self.checkBoxAGCMode.clicked.connect(lambda: self.setOutputDisplay(0, comPort))
        self.checkBoxRFswitch.clicked.connect(lambda: self.doCheck(comPort, "RFswitch"))
        self.btnSetRFattenuator1.clicked.connect(lambda: self.setOutputDisplay(2, comPort))

        # INITIALIZE VALUES
        self.setInitialDisplay("readControls", comPort)

    def setOutputDisplay(self, overallInput, COMPort):
        if overallInput == 2:
            VARIABLES[2] = self.lineEditRFattenuator1.text()
            self.doCommand("setRFattenuator1 " + VARIABLES[2], COMPort)

    def setInitialDisplay(self, overallInput, COMPort):
        untrimmedOutput = self.doCommand(overallInput, COMPort)

        # EXTRACT VALS
        test = untrimmedOutput[(untrimmedOutput.find('AGCMode') + 8)]
        i = 9
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        VARIABLES.append(test)
        self.initialCheck(COMPort, "AGCMode")

        test = untrimmedOutput[(untrimmedOutput.find('RFswitch') + 9)]
        i = untrimmedOutput.find('RFswitch') + 10
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        VARIABLES.append(test)
        self.initialCheck(COMPort, "RFswitch")

        test = untrimmedOutput[(untrimmedOutput.find('RFattenuator1') + 14)]
        i = untrimmedOutput.find('RFattenuator1') + 15
        while (untrimmedOutput[i] != 'd'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditRFattenuator1.setText(test)
        VARIABLES.append(test)

    def initialCheck(self, COMPort, variable):
        if (variable == "AGCMode"):
            if (VARIABLES[0] == "ON"):
                self.checkBoxAGCMode.setChecked(True)
                self.checkBoxAGCMode.setText("AGCMode is ON")
            else:
                self.checkBoxAGCMode.setChecked(False)
                self.checkBoxAGCMode.setText("AGCMode is OFF")

        if (variable == "RFswitch"):
            if (VARIABLES[1] == "ON"):
                self.checkBoxRFswitch.setChecked(True)
                self.checkBoxRFswitch.setText("RFswitch is ON")
            else:
                self.checkBoxRFswitch.setChecked(False)
                self.checkBoxRFswitch.setText("RFswitch is OFF")

    def doCheck(self, COMPort, variable):
        if (variable == "RFswitch"):
            if self.checkBoxRFswitch.isChecked():
                self.checkBoxRFswitch.setText("RFswitch is ON")
                self.doCommand("setRFswitch ON", COMPort)
                VARIABLES[1] = "ON"
            else:
                self.checkBoxRFswitch.setText("RFswitch is OFF")
                self.doCommand("setRFswitch OFF", COMPort)
                VARIABLES[1] = "OFF"

    # Returns: String of output
    def doCommand(self, input, COMPort):
        print("doCommand executed")

        # Get USB serial & run terminal code
        # portNum = Ui_MainWindow.getCOMPort()
        portNum = COMPort
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
            boxResponse = boxResponse[:-4]
            return boxResponse
        except:
            self.lineEdit.setText(
                "Chosen COM Port does not exist. Either replug your device or refresh your list of devices.\r\n\r\n\r\n")

    def retranslateUi(self, dialogControls):
        _translate = QtCore.QCoreApplication.translate
        dialogControls.setWindowTitle(_translate("dialogControls", "Controls Properties"))
        self.label_3.setText(_translate("dialogControls", "RFattenuator1:"))
        self.label_2.setText(_translate("dialogControls", "RFswitch:"))
        self.label.setText(_translate("dialogControls", "AGCMode:"))
        self.btnSetRFattenuator1.setText(_translate("dialogControls", "Set RFattenuator1"))
        self.checkBoxAGCMode.setText(_translate("dialogControls", "AGCMode is OFF"))
        self.checkBoxRFswitch.setText(_translate("dialogControls", "RFswitch is OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogControls = QtWidgets.QDialog()
    ui = Ui_dialogControls()
    ui.setupUi(dialogControls)
    dialogControls.show()
    sys.exit(app.exec_())

