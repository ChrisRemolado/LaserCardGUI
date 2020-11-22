# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RFattenuator1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import serial

class Ui_dialogRFattenuator1(object):
    def setupUi(self, dialogRFattenuator1, comPort):
        dialogRFattenuator1.setObjectName("dialogRFattenuator1")
        dialogRFattenuator1.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(dialogRFattenuator1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(dialogRFattenuator1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(dialogRFattenuator1)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.btnSetRFatt1 = QtWidgets.QPushButton(dialogRFattenuator1)
        self.btnSetRFatt1.setObjectName("btnSetRFatt1")
        self.gridLayout.addWidget(self.btnSetRFatt1, 0, 3, 1, 1)

        # CONNECT TO GUI
        self.btnSetRFatt1.clicked.connect(lambda: self.setOutputDisplay(comPort))

        # INITIALIZE VALUES
        self.lineEdit.setText(self.setInitialDisplay("readRFattenuator1", comPort))

        self.retranslateUi(dialogRFattenuator1)
        QtCore.QMetaObject.connectSlotsByName(dialogRFattenuator1)

    def setOutputDisplay(self, COMPort):
        self.doCommand("setRFattenuator1 " + self.lineEdit.text(), COMPort)

    # Returns: Array of output strings
    def setInitialDisplay(self, overallInput, COMPort):
        untrimmedOutput = self.doCommand(overallInput, COMPort)
        trimmedOutput = untrimmedOutput[14:-2]
        return trimmedOutput

    # Returns: String of output
    def doCommand(self, input, COMPort):
        print("doCommand executed")

        # Get USB serial & run terminal code
        #portNum = Ui_MainWindow.getCOMPort()
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

    def retranslateUi(self, dialogRFattenuator1):
        _translate = QtCore.QCoreApplication.translate
        dialogRFattenuator1.setWindowTitle(_translate("dialogRFattenuator1", "RF Attenuator Properties"))
        self.label.setText(_translate("dialogRFattenuator1", "RFattenuator1:"))
        self.btnSetRFatt1.setText(_translate("dialogRFattenuator1", "setRFattenuator1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogRFattenuator1 = QtWidgets.QDialog()
    ui = Ui_dialogRFattenuator1()
    ui.setupUi(dialogRFattenuator1)
    dialogRFattenuator1.show()
    sys.exit(app.exec_())

