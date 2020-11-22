# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RFswitch.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import serial

class Ui_dialogRFswitch(object):
    def setupUi(self, dialogRFswitch, comPort):
        dialogRFswitch.setObjectName("dialogRFswitch")
        dialogRFswitch.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(dialogRFswitch)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(dialogRFswitch)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(dialogRFswitch)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)

        self.retranslateUi(dialogRFswitch)
        QtCore.QMetaObject.connectSlotsByName(dialogRFswitch)

        # CONNECT TO GUI
        self.checkBox.clicked.connect(lambda: self.doCheck(comPort))

        # INITIALIZE VALUES
        self.initialCheck(comPort)

    def initialCheck(self, COMPort):
        untrimmedOutput = self.doCommand("readRFswitch", COMPort)
        trimmedOutput = untrimmedOutput[9:]
        print(trimmedOutput)
        if (trimmedOutput == "ON"):
            self.checkBox.setChecked(True)
            self.checkBox.setText("RFSwitch is ON")
        else:
            self.checkBox.setChecked(False)
            self.checkBox.setText("RFSwitch is OFF")

    def doCheck(self, COMPort):
        if self.checkBox.isChecked():
            self.checkBox.setText("RFSwitch is ON")
            self.doCommand("setRFswitch ON", COMPort)
        else:
            self.checkBox.setText("RFSwitch is OFF")
            self.doCommand("setRFswitch OFF", COMPort)

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
            boxResponse = boxResponse[:-6]
            return boxResponse
        except:
            self.lineEdit.setText(
                "Chosen COM Port does not exist. Either replug your device or refresh your list of devices.\r\n\r\n\r\n")

    def retranslateUi(self, dialogRFswitch):
        _translate = QtCore.QCoreApplication.translate
        dialogRFswitch.setWindowTitle(_translate("dialogRFswitch", "RF Switch Properties"))
        self.label.setText(_translate("dialogRFswitch", "RFswitch:"))
        self.checkBox.setText(_translate("dialogRFswitch", "RFSwitch is ON"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogRFswitch = QtWidgets.QDialog()
    ui = Ui_dialogRFswitch()
    ui.setupUi(dialogRFswitch)
    dialogRFswitch.show()
    sys.exit(app.exec_())

