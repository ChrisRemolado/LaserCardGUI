# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAlarmMask.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

##TO-DO LIST:
#/GET COMPORT FOR DIALOG
#/REFRESH COMMANDS IN MAIN GUI

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import serial

class Ui_dialogAlarmMask(object):
    def setupUi(self, dialogAlarmMask, comPort):
        dialogAlarmMask.setObjectName("dialogAlarmMask")
        dialogAlarmMask.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(dialogAlarmMask)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(dialogAlarmMask)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(dialogAlarmMask)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.btnWriteAlarmsMask = QtWidgets.QPushButton(dialogAlarmMask)
        self.btnWriteAlarmsMask.setObjectName("btnWriteAlarmsMask")
        self.gridLayout.addWidget(self.btnWriteAlarmsMask, 0, 3, 1, 1)

        # CONNECT TO GUI
        self.btnWriteAlarmsMask.clicked.connect(lambda:self.setOutputDisplay(comPort))

        # INITIALIZE VALUES
        self.lineEdit.setText(self.setInitialDisplay("readAlarmMask", comPort))

        self.retranslateUi(dialogAlarmMask)
        QtCore.QMetaObject.connectSlotsByName(dialogAlarmMask)

    def setOutputDisplay(self, COMPort):
        self.doCommand("writeAlarmMask " + self.lineEdit.text(), COMPort)

    # Returns: Array of output strings
    def setInitialDisplay(self, overallInput, COMPort):
        untrimmedOutput = self.doCommand(overallInput, COMPort)
        trimmedOutput = untrimmedOutput[10:]
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

    def retranslateUi(self, dialogAlarmMask):
        _translate = QtCore.QCoreApplication.translate
        dialogAlarmMask.setWindowTitle(_translate("dialogAlarmMask", "Alarm Mask Properties"))
        self.label.setText(_translate("dialogAlarmMask", "Alarm Mask:"))
        self.btnWriteAlarmsMask.setText(_translate("dialogAlarmMask", "writeAlarmMode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogAlarmMask = QtWidgets.QDialog()
    ui = Ui_dialogAlarmMask()
    ui.setupUi(dialogAlarmMask)
    dialogAlarmMask.show()
    sys.exit(app.exec_())

