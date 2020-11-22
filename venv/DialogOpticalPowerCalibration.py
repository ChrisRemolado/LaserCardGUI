# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogOpticalPowerCalibration.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import serial

VARIABLES = []

class Ui_dialogOpticalPowerCalibration(object):
    def setupUi(self, dialogOpticalPowerCalibration, comPort):
        dialogOpticalPowerCalibration.setObjectName("dialogOpticalPowerCalibration")
        dialogOpticalPowerCalibration.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(dialogOpticalPowerCalibration)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEditWavelength = QtWidgets.QLineEdit(dialogOpticalPowerCalibration)
        self.lineEditWavelength.setObjectName("lineEditWavelength")
        self.gridLayout_2.addWidget(self.lineEditWavelength, 0, 1, 1, 1)
        self.lineEditIntercept = QtWidgets.QLineEdit(dialogOpticalPowerCalibration)
        self.lineEditIntercept.setObjectName("lineEditIntercept")
        self.horizontalLayout_4.addWidget(self.lineEditIntercept)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 1, 1, 1)
        self.btnSetWavelength = QtWidgets.QPushButton(dialogOpticalPowerCalibration)
        self.btnSetWavelength.setObjectName("btnSetWavelength")
        self.gridLayout_2.addWidget(self.btnSetWavelength, 0, 2, 1, 1)
        self.btnSetAlarmThresholdLo = QtWidgets.QPushButton(dialogOpticalPowerCalibration)
        self.btnSetAlarmThresholdLo.setObjectName("btnSetAlarmThresholdLo")
        self.gridLayout_2.addWidget(self.btnSetAlarmThresholdLo, 4, 2, 1, 1)
        self.btnSetSlope = QtWidgets.QPushButton(dialogOpticalPowerCalibration)
        self.btnSetSlope.setObjectName("btnSetSlope")
        self.gridLayout_2.addWidget(self.btnSetSlope, 2, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(dialogOpticalPowerCalibration)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(dialogOpticalPowerCalibration)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(dialogOpticalPowerCalibration)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEditSlope = QtWidgets.QLineEdit(dialogOpticalPowerCalibration)
        self.lineEditSlope.setObjectName("lineEditSlope")
        self.gridLayout_2.addWidget(self.lineEditSlope, 2, 1, 1, 1)
        self.lineEditAlarmThresholdLo = QtWidgets.QLineEdit(dialogOpticalPowerCalibration)
        self.lineEditAlarmThresholdLo.setObjectName("lineEditAlarmThresholdLo")
        self.gridLayout_2.addWidget(self.lineEditAlarmThresholdLo, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(dialogOpticalPowerCalibration)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.btnSetIntercept = QtWidgets.QPushButton(dialogOpticalPowerCalibration)
        self.btnSetIntercept.setObjectName("btnSetIntercept")
        self.gridLayout_2.addWidget(self.btnSetIntercept, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(dialogOpticalPowerCalibration)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.btnSetAlarmThresholdHi = QtWidgets.QPushButton(dialogOpticalPowerCalibration)
        self.btnSetAlarmThresholdHi.setObjectName("btnSetAlarmThresholdHi")
        self.gridLayout_2.addWidget(self.btnSetAlarmThresholdHi, 3, 2, 1, 1)
        self.lineEditAlarmThresholdHi = QtWidgets.QLineEdit(dialogOpticalPowerCalibration)
        self.lineEditAlarmThresholdHi.setObjectName("lineEditAlarmThresholdHi")
        self.gridLayout_2.addWidget(self.lineEditAlarmThresholdHi, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(dialogOpticalPowerCalibration)
        QtCore.QMetaObject.connectSlotsByName(dialogOpticalPowerCalibration)

        # CONNECT TO GUI
        self.btnSetWavelength.clicked.connect(lambda: self.setOutputDisplay(0, comPort))
        self.btnSetIntercept.clicked.connect(lambda: self.setOutputDisplay(1, comPort))
        self.btnSetSlope.clicked.connect(lambda: self.setOutputDisplay(2, comPort))
        self.btnSetAlarmThresholdHi.clicked.connect(lambda: self.setOutputDisplay(3, comPort))
        self.btnSetAlarmThresholdLo.clicked.connect(lambda: self.setOutputDisplay(4, comPort))

        # INITIALIZE VALUES
        self.setInitialDisplay("readCalOptPwr", comPort)

    def setOutputDisplay(self, overallInput, COMPort):
        if overallInput == 0:
            VARIABLES[0] = self.lineEditWavelength.text()
        if overallInput == 1:
            VARIABLES[1] = self.lineEditIntercept.text()
        if overallInput == 2:
            VARIABLES[2] = self.lineEditSlope.text()
        if overallInput == 3:
            VARIABLES[3] = self.lineEditAlarmThresholdHi.text()
        if overallInput == 4:
            VARIABLES[4] = self.lineEditAlarmThresholdLo.text()

        self.doCommand("writeCalOptPwr " + VARIABLES[0] + " "
                       + VARIABLES[1] + " "
                       + VARIABLES[2] + " "
                       + VARIABLES[3] + " "
                       + VARIABLES[4], COMPort)


    # Returns: Array of output strings
    def setInitialDisplay(self, overallInput, COMPort):
        untrimmedOutput = self.doCommand(overallInput, COMPort)

        #Extract wavelength
        test = untrimmedOutput[(untrimmedOutput.find('Wavelength') + 11)]
        i = 12
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditWavelength.setText(test)
        VARIABLES.append(test)

        #Extract intercept
        test = untrimmedOutput[(untrimmedOutput.find('Intercept') + 10)]
        i = untrimmedOutput.find('Intercept') + 11
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditIntercept.setText(test)
        VARIABLES.append(test)

        #Extract slope
        test = untrimmedOutput[(untrimmedOutput.find('Slope') + 6)]
        i = untrimmedOutput.find('Slope') + 7
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditSlope.setText(test)
        VARIABLES.append(test)

        #Extract AlarmThresholdHi
        test = untrimmedOutput[(untrimmedOutput.find('AlarmThresholdHi') + 17)]
        i = untrimmedOutput.find('AlarmThresholdHi') + 18
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditAlarmThresholdHi.setText(test)
        VARIABLES.append(test)

        #Extract AlarmThresholdLo
        test = untrimmedOutput[(untrimmedOutput.find('AlarmThresholdLo') + 17)]
        i = untrimmedOutput.find('AlarmThresholdLo') + 18
        while (untrimmedOutput[i] != '\r'):
            test += untrimmedOutput[i]
            i += 1
        self.lineEditAlarmThresholdLo.setText(test)
        VARIABLES.append(test)


        #test = untrimmmedOutput[untrimmedOutput.find('Wavelength')+10:untrimmedOutput.find('Wavelength')+14]
        #print(untrimmedOutput.find('Wavelength'))
        #self.lineEditWavelength.setText(test)
        #trimmedOutput[0] = untrimmmed[untrimmedOutput.find('Wavelength'):untrimmedOutput.find(b'\n')]
        #self.lineEditWavelength.setText(trimmedOutput)

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

    def retranslateUi(self, dialogOpticalPowerCalibration):
        _translate = QtCore.QCoreApplication.translate
        dialogOpticalPowerCalibration.setWindowTitle(_translate("dialogOpticalPowerCalibration", "Optical Power Calibration Properties"))
        self.btnSetWavelength.setText(_translate("dialogOpticalPowerCalibration", "Set Wavelength"))
        self.btnSetAlarmThresholdLo.setText(_translate("dialogOpticalPowerCalibration", "Set AlarmThresholdLo"))
        self.btnSetSlope.setText(_translate("dialogOpticalPowerCalibration", "Set Slope"))
        self.label_5.setText(_translate("dialogOpticalPowerCalibration", "Slope:"))
        self.label_3.setText(_translate("dialogOpticalPowerCalibration", "Wavelength:"))
        self.label_4.setText(_translate("dialogOpticalPowerCalibration", "Intercept:"))
        self.label_6.setText(_translate("dialogOpticalPowerCalibration", "AlarmThresholdLo:"))
        self.btnSetIntercept.setText(_translate("dialogOpticalPowerCalibration", "Set Intercept"))
        self.label_7.setText(_translate("dialogOpticalPowerCalibration", "AlarmThresholdHi:"))
        self.btnSetAlarmThresholdHi.setText(_translate("dialogOpticalPowerCalibration", "Set AlarmThresholdHi"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialogOpticalPowerCalibration = QtWidgets.QDialog()
    ui = Ui_dialogOpticalPowerCalibration()
    ui.setupUi(dialogOpticalPowerCalibration)
    dialogOpticalPowerCalibration.show()
    sys.exit(app.exec_())

