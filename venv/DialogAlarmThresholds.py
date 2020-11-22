# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAlarmThresholds.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import serial

VARIABLES = []

class Ui_dialogAlarmThresholds(object):
    def setupUi(self, dialogAlarmThresholds, comPort):
        dialogAlarmThresholds.setObjectName("dialogAlarmThresholds")
        dialogAlarmThresholds.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(dialogAlarmThresholds)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(dialogAlarmThresholds)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(dialogAlarmThresholds)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEditTempAlarmHi = QtWidgets.QLineEdit(dialogAlarmThresholds)
        self.lineEditTempAlarmHi.setObjectName("lineEditTempAlarmHi")
        self.gridLayout_2.addWidget(self.lineEditTempAlarmHi, 0, 1, 1, 1)
        self.btnSetTempAlarmHi = QtWidgets.QPushButton(dialogAlarmThresholds)
        self.btnSetTempAlarmHi.setObjectName("btnSetTempAlarmHi")
        self.gridLayout_2.addWidget(self.btnSetTempAlarmHi, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(dialogAlarmThresholds)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 6, 0, 1, 1)
        self.btnSetRFDetAlarmLo = QtWidgets.QPushButton(dialogAlarmThresholds)
        self.btnSetRFDetAlarmLo.setObjectName("btnSetRFDetAlarmLo")
        self.gridLayout_2.addWidget(self.btnSetRFDetAlarmLo, 3, 2, 1, 1)
        self.btnSetRFDetAlarmHi = QtWidgets.QPushButton(dialogAlarmThresholds)
        self.btnSetRFDetAlarmHi.setObjectName("btnSetRFDetAlarmHi")
        self.gridLayout_2.addWidget(self.btnSetRFDetAlarmHi, 2, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditTempAlarmLo = QtWidgets.QLineEdit(dialogAlarmThresholds)
        self.lineEditTempAlarmLo.setObjectName("lineEditTempAlarmLo")
        self.horizontalLayout_4.addWidget(self.lineEditTempAlarmLo)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(dialogAlarmThresholds)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEditRFDetAlarmLo = QtWidgets.QLineEdit(dialogAlarmThresholds)
        self.lineEditRFDetAlarmLo.setObjectName("lineEditRFDetAlarmLo")
        self.gridLayout_2.addWidget(self.lineEditRFDetAlarmLo, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(dialogAlarmThresholds)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.btnSetTempAlarmLo = QtWidgets.QPushButton(dialogAlarmThresholds)
        self.btnSetTempAlarmLo.setObjectName("btnSetTempAlarmLo")
        self.gridLayout_2.addWidget(self.btnSetTempAlarmLo, 1, 2, 1, 1)
        self.btnSetOptPwrAlarmHi = QtWidgets.QPushButton(dialogAlarmThresholds)
        self.btnSetOptPwrAlarmHi.setObjectName("btnSetOptPwrAlarmHi")
        self.gridLayout_2.addWidget(self.btnSetOptPwrAlarmHi, 4, 2, 1, 1)
        self.lineEditOptPwrAlarmHi = QtWidgets.QLineEdit(dialogAlarmThresholds)
        self.lineEditOptPwrAlarmHi.setObjectName("lineEditOptPwrAlarmHi")
        self.gridLayout_2.addWidget(self.lineEditOptPwrAlarmHi, 4, 1, 1, 1)
        self.lineEditRFDetAlarmHi = QtWidgets.QLineEdit(dialogAlarmThresholds)
        self.lineEditRFDetAlarmHi.setObjectName("lineEditRFDetAlarmHi")
        self.gridLayout_2.addWidget(self.lineEditRFDetAlarmHi, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(dialogAlarmThresholds)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)
        self.lineEditOptPwrAlarmLo = QtWidgets.QLineEdit(dialogAlarmThresholds)
        self.lineEditOptPwrAlarmLo.setObjectName("lineEditOptPwrAlarmLo")
        self.gridLayout_2.addWidget(self.lineEditOptPwrAlarmLo, 5, 1, 1, 1)
        self.label = QtWidgets.QLabel(dialogAlarmThresholds)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(dialogAlarmThresholds)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 7, 0, 1, 1)
        self.lineEditLaserBiasAlarmHi = QtWidgets.QLineEdit(dialogAlarmThresholds)
        self.lineEditLaserBiasAlarmHi.setEnabled(True)
        self.lineEditLaserBiasAlarmHi.setObjectName("lineEditLaserBiasAlarmHi")
        self.gridLayout_2.addWidget(self.lineEditLaserBiasAlarmHi, 6, 1, 1, 1)
        self.lineEditLaserBiasAlarmLo = QtWidgets.QLineEdit(dialogAlarmThresholds)
        self.lineEditLaserBiasAlarmLo.setEnabled(True)
        self.btnSetLaserBiasAlarmHi = QtWidgets.QPushButton(dialogAlarmThresholds)
        self.btnSetLaserBiasAlarmHi.setObjectName("btnSetLaserBiasAlarmHi")
        self.gridLayout_2.addWidget(self.btnSetLaserBiasAlarmHi, 6, 2, 1, 1)
        self.lineEditLaserBiasAlarmLo.setObjectName("lineEditLaserBiasAlarmLo")
        self.gridLayout_2.addWidget(self.lineEditLaserBiasAlarmLo, 7, 1, 1, 1)
        self.btnSetOptPwrAlarmLo = QtWidgets.QPushButton(dialogAlarmThresholds)
        self.btnSetLaserBiasAlarmLo = QtWidgets.QPushButton(dialogAlarmThresholds)
        self.btnSetLaserBiasAlarmLo.setObjectName("btnSetLaserBiasAlarmLo")
        self.gridLayout_2.addWidget(self.btnSetLaserBiasAlarmLo, 7, 2, 1, 1)
        self.btnSetOptPwrAlarmLo.setObjectName("btnSetOptPwrAlarmLo")
        self.gridLayout_2.addWidget(self.btnSetOptPwrAlarmLo, 5, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(dialogAlarmThresholds)
        QtCore.QMetaObject.connectSlotsByName(dialogAlarmThresholds)

        # CONNECT TO GUI
        self.btnSetTempAlarmHi.clicked.connect(lambda: self.setOutputDisplay(0, comPort))
        self.btnSetTempAlarmLo.clicked.connect(lambda: self.setOutputDisplay(1, comPort))
        self.btnSetRFDetAlarmHi.clicked.connect(lambda: self.setOutputDisplay(2, comPort))
        self.btnSetRFDetAlarmLo.clicked.connect(lambda: self.setOutputDisplay(3, comPort))
        self.btnSetOptPwrAlarmHi.clicked.connect(lambda: self.setOutputDisplay(4, comPort))
        self.btnSetOptPwrAlarmLo.clicked.connect(lambda: self.setOutputDisplay(5, comPort))
        self.btnSetLaserBiasAlarmHi.clicked.connect(lambda: self.setOutputDisplay(6, comPort))
        self.btnSetLaserBiasAlarmLo.clicked.connect(lambda: self.setOutputDisplay(7, comPort))

        # INITIALIZE VALUES
        self.setInitialDisplay("readAlarmThresholds", comPort)

    def setOutputDisplay(self, overallInput, COMPort):
        if overallInput == 0:
            VARIABLES[0] = self.lineEditTempAlarmHi.text()
        if overallInput == 1:
            VARIABLES[1] = self.lineEditTempAlarmLo.text()
        if overallInput == 2:
            VARIABLES[2] = self.lineEditRFDetAlarmHi.text()
        if overallInput == 3:
            VARIABLES[3] = self.lineEditRFDetAlarmLo.text()
        if overallInput == 4:
            VARIABLES[4] = self.lineEditOptPwrAlarmHi.text()
        if overallInput == 5:
            VARIABLES[5] = self.lineEditOptPwrAlarmLo.text()
        if overallInput == 6:
            VARIABLES[6] = self.lineEditLaserBiasAlarmHi.text()
        if overallInput == 7:
            VARIABLES[7] = self.lineEditLaserBiasAlarmLo.text()

        self.doCommand("writeAlarmThresholds " + VARIABLES[0] + " "
                       + VARIABLES[1] + " "
                       + VARIABLES[2] + " "
                       + VARIABLES[3] + " "
                       + VARIABLES[4] + " "
                       + VARIABLES[5] + " "
                       + VARIABLES[6] + " "
                       + VARIABLES[7], COMPort)


    # Returns: Array of output strings
    def setInitialDisplay(self, overallInput, COMPort):
        untrimmedOutput = self.doCommand(overallInput, COMPort)

        #EXTRACT VALS
        test = untrimmedOutput[(untrimmedOutput.find('Temperature Alarm Hi') + 21)]
        i = 22
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditTempAlarmHi.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('Temperature Alarm Lo') + 21)]
        i = untrimmedOutput.find('Temperature Alarm Lo') + 22
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditTempAlarmLo.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('RF Detector Alarm Hi') + 21)]
        i = untrimmedOutput.find('RF Detector Alarm Hi') + 22
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditRFDetAlarmHi.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('RF Detector Alarm Lo') + 21)]
        i = untrimmedOutput.find('RF Detector Alarm Lo') + 22
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditRFDetAlarmLo.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('Optical Power Alarm Hi') + 23)]
        i = untrimmedOutput.find('Optical Power Alarm Hi') + 24
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditOptPwrAlarmHi.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('Optical Power Alarm Lo') + 23)]
        i = untrimmedOutput.find('Optical Power Alarm Lo') + 24
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditOptPwrAlarmLo.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('Laser Bias Alarm Hi') + 20)]
        i = untrimmedOutput.find('Laser Bias Alarm Hi') + 21
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditLaserBiasAlarmHi.setText(test)
        VARIABLES.append(test)

        test = untrimmedOutput[(untrimmedOutput.find('Laser Bias Alarm Lo') + 20)]
        i = untrimmedOutput.find('Laser Bias Alarm Lo') + 21
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditLaserBiasAlarmLo.setText(test)
        VARIABLES.append(test)

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
            boxResponse = boxResponse[:-4]
            return boxResponse
        except:
            self.lineEdit.setText(
                "Chosen COM Port does not exist. Either replug your device or refresh your list of devices.\r\n\r\n\r\n")

    def retranslateUi(self, dialogAlarmThresholds):
        _translate = QtCore.QCoreApplication.translate
        dialogAlarmThresholds.setWindowTitle(_translate("dialogAlarmThresholds", "Alarm Thresholds Property"))
        self.label_3.setText(_translate("dialogAlarmThresholds", "Temperature Alarm High:"))
        self.label_4.setText(_translate("dialogAlarmThresholds", "Temperature Alarm Low:"))
        self.btnSetTempAlarmHi.setText(_translate("dialogAlarmThresholds", "Set TempAlarmHi"))
        self.label_2.setText(_translate("dialogAlarmThresholds", "Laser Bias Alarm High:"))
        self.btnSetRFDetAlarmLo.setText(_translate("dialogAlarmThresholds", "Set RFDetAlarmLo"))
        self.btnSetRFDetAlarmHi.setText(_translate("dialogAlarmThresholds", "Set RFDetAlarmHi"))
        self.label_6.setText(_translate("dialogAlarmThresholds", "RF Detector Alarm Low:"))
        self.label_5.setText(_translate("dialogAlarmThresholds", "RF Detector Alarm High:"))
        self.btnSetTempAlarmLo.setText(_translate("dialogAlarmThresholds", "Set TempAlarmLo"))
        self.btnSetOptPwrAlarmHi.setText(_translate("dialogAlarmThresholds", "Set OptPwrAlarmHi"))
        self.label_7.setText(_translate("dialogAlarmThresholds", "Optical Power Alarm High:"))
        self.label.setText(_translate("dialogAlarmThresholds", "Optical Power Alarm Low:"))
        self.label_8.setText(_translate("dialogAlarmThresholds", "Laser Bias Alarm Low:"))
        self.btnSetOptPwrAlarmLo.setText(_translate("dialogAlarmThresholds", "Set OptPwrAlarmLo"))
        self.btnSetLaserBiasAlarmHi.setText(_translate("dialogAlarmThresholds", "Set LaserBiasAlarmHi"))
        self.btnSetLaserBiasAlarmLo.setText(_translate("dialogAlarmThresholds", "Set LaserBiasAlarmLo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogAlarmThresholds = QtWidgets.QDialog()
    ui = Ui_dialogAlarmThresholds()
    ui.setupUi(dialogAlarmThresholds)
    dialogAlarmThresholds.show()
    sys.exit(app.exec_())

