# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogLaserAPC.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import serial

VARIABLES = []

class Ui_dialogLaserAPC(object):
    def setupUi(self, dialogLaserAPC, comPort):
        dialogLaserAPC.setObjectName("dialogLaserAPC")
        dialogLaserAPC.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(dialogLaserAPC)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(dialogLaserAPC)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(dialogLaserAPC)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(dialogLaserAPC)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEditLaserBiasDAC = QtWidgets.QLineEdit(dialogLaserAPC)
        self.lineEditLaserBiasDAC.setObjectName("lineEditLaserBiasDAC")
        self.gridLayout_3.addWidget(self.lineEditLaserBiasDAC, 1, 1, 1, 1)
        self.lineEditOptDetOffset = QtWidgets.QLineEdit(dialogLaserAPC)
        self.lineEditOptDetOffset.setObjectName("lineEditOptDetOffset")
        self.gridLayout_3.addWidget(self.lineEditOptDetOffset, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(dialogLaserAPC)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(dialogLaserAPC)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(dialogLaserAPC)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEditOptDetFeedback = QtWidgets.QLineEdit(dialogLaserAPC)
        self.lineEditOptDetFeedback.setEnabled(False)
        self.lineEditOptDetFeedback.setObjectName("lineEditOptDetFeedback")
        self.gridLayout_3.addWidget(self.lineEditOptDetFeedback, 2, 1, 1, 1)
        self.lineEditOptDetHyst = QtWidgets.QLineEdit(dialogLaserAPC)
        self.lineEditOptDetHyst.setEnabled(False)
        self.lineEditOptDetHyst.setObjectName("lineEditOptDetHyst")
        self.gridLayout_3.addWidget(self.lineEditOptDetHyst, 5, 1, 1, 1)
        self.lineEditOptDetTarget = QtWidgets.QLineEdit(dialogLaserAPC)
        self.lineEditOptDetTarget.setObjectName("lineEditOptDetTarget")
        self.gridLayout_3.addWidget(self.lineEditOptDetTarget, 4, 1, 1, 1)
        self.btnSetLaserBiasDAC = QtWidgets.QPushButton(dialogLaserAPC)
        self.btnSetLaserBiasDAC.setObjectName("btnSetLaserBiasDAC")
        self.gridLayout_3.addWidget(self.btnSetLaserBiasDAC, 1, 2, 1, 1)
        self.btnSetOptDetOffset = QtWidgets.QPushButton(dialogLaserAPC)
        self.btnSetOptDetOffset.setObjectName("btnSetOptDetOffset")
        self.gridLayout_3.addWidget(self.btnSetOptDetOffset, 3, 2, 1, 1)
        self.btnSetOptDetTarget = QtWidgets.QPushButton(dialogLaserAPC)
        self.btnSetOptDetTarget.setObjectName("btnSetOptDetTarget")
        self.gridLayout_3.addWidget(self.btnSetOptDetTarget, 4, 2, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(dialogLaserAPC)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 0, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.retranslateUi(dialogLaserAPC)
        QtCore.QMetaObject.connectSlotsByName(dialogLaserAPC)

        # CONNECT TO GUI
        self.checkBox.clicked.connect(lambda: self.doCheck(comPort))
        self.btnSetLaserBiasDAC.clicked.connect(lambda: self.setOutputDisplay(1, comPort))
        self.btnSetOptDetOffset.clicked.connect(lambda: self.setOutputDisplay(3, comPort))
        self.btnSetOptDetTarget.clicked.connect(lambda: self.setOutputDisplay(4, comPort))

        # INITIALIZE VALUES
        self.setInitialDisplay("readLaserAPC", comPort)
        self.initialCheck(comPort)

    def setOutputDisplay(self, overallInput, COMPort):
        if overallInput == 1:
            VARIABLES[1] = self.lineEditLaserBiasDAC.text()
            self.doCommand("writeDacLaserBias " + VARIABLES[1], COMPort)
        if overallInput == 3:
            VARIABLES[3] = self.lineEditOptDetOffset.text()
            self.doCommand("writeOptDetOffset " + VARIABLES[3], COMPort)
        if overallInput == 4:
            VARIABLES[4] = self.lineEditOptDetTarget.text()
            self.doCommand("writeOptDetTarget " + VARIABLES[4], COMPort)

    # Returns: Array of output strings
    def setInitialDisplay(self, overallInput, COMPort):
        untrimmedOutput = self.doCommand(overallInput, COMPort)

        # EXTRACT VALS
        test = untrimmedOutput[(untrimmedOutput.find('LaserAPC') + 9)]
        i = 10
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        # self.lineEditTempAlarmHi.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('LaserBiasDAC') + 13)]
        i = untrimmedOutput.find('LaserBiasDAC') + 14
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditLaserBiasDAC.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('OptDetFeedback') + 15)]
        i = untrimmedOutput.find('OptDetFeedback') + 16
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditOptDetFeedback.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('OptDetOffset') + 13)]
        i = untrimmedOutput.find('OptDetOffset') + 14
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditOptDetOffset.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('OptDetTarget') + 13)]
        i = untrimmedOutput.find('OptDetTarget') + 14
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditOptDetTarget.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('OptDetHyst') + 11)]
        i = untrimmedOutput.find('OptDetHyst') + 12
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditOptDetHyst.setText(test)
        VARIABLES.append(test)

    def initialCheck(self, COMPort):
        if (VARIABLES[0] == "ON"):
            self.checkBox.setChecked(True)
            self.checkBox.setText("LaserAPC is ON")
        else:
            self.checkBox.setChecked(False)
            self.checkBox.setText("LaserAPC is OFF")

    def doCheck(self, COMPort):
        if self.checkBox.isChecked():
            self.checkBox.setText("LaserAPC is ON")
            self.doCommand("setLaserAPC ON", COMPort)
            VARIABLES[0] = "ON"
        else:
            self.checkBox.setText("LaserAPC is OFF")
            self.doCommand("setLaserAPC OFF", COMPort)
            VARIABLES[0] = "OFF"

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

    def retranslateUi(self, dialogLaserAPC):
        _translate = QtCore.QCoreApplication.translate
        dialogLaserAPC.setWindowTitle(_translate("dialogLaserAPC", "Laser APC Properties"))
        self.label.setText(_translate("dialogLaserAPC", "OptDetHyst:"))
        self.label_3.setText(_translate("dialogLaserAPC", "LaserAPC:"))
        self.label_4.setText(_translate("dialogLaserAPC", "LaserBiasDAC:"))
        self.label_6.setText(_translate("dialogLaserAPC", "OptDetOffset:"))
        self.label_7.setText(_translate("dialogLaserAPC", "OptDetTarget:"))
        self.label_5.setText(_translate("dialogLaserAPC", "OptDetFeedback:"))
        self.btnSetLaserBiasDAC.setText(_translate("dialogLaserAPC", "Set LaserBiasDAC"))
        self.btnSetOptDetOffset.setText(_translate("dialogLaserAPC", "Set OptDetOffset"))
        self.btnSetOptDetTarget.setText(_translate("dialogLaserAPC", "Set OptDetTarget"))
        self.checkBox.setText(_translate("dialogLaserAPC", "LaserAPC is OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogLaserAPC = QtWidgets.QDialog()
    ui = Ui_dialogLaserAPC()
    ui.setupUi(dialogLaserAPC)
    dialogLaserAPC.show()
    sys.exit(app.exec_())

