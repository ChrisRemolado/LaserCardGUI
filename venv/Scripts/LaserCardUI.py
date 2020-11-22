# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LaserCardUI3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

#TO-DO:
#Enter button = do command
'''Properties to buttons: wavelength,
Gain_X1_IDAC=2026mV, Gain_X2_IDAC=2036mV, Gain_X1_RFDET=836mV, Gain_X2_RFDET=1670mV, Gain_X1_OPWR=0mV, Gain_X2_OPWR=0mV
ATT1=0.00dB, ATT2=0.00dB
CAL=0
Param0=880
Param1=-6600
Param2=34130
Param3=-6600
Param4=17065

CAL=1
Param0=1550
Param1=0
Param2=2000
Param3=0
Param4=1000

CAL=2
Param0=1330
Param1=0
Param2=2000
Param3=0
Param4=1000

CAL=3
Param0=0
Param1=0
Param2=0
Param3=0
Param4=0

CAL=4
Param0=0
Param1=-500
Param2=2500
Param3=-3500
Param4=100

CAL=5
Param0=0
Param1=55
Param2=0
Param3=-20
Param4=0
'''

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
        MainWindow.resize(449, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.btnRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName("btnRefresh")
        self.gridLayout.addWidget(self.btnRefresh, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.btnCommand = QtWidgets.QPushButton(self.centralwidget)
        self.btnCommand.setObjectName("btnCommand")
        self.btnCommand.setDefault(True);
        self.btnCommand.setAutoDefault(True);
        self.gridLayout.addWidget(self.btnCommand, 2, 1, 2, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.outputBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.outputBox.setObjectName("outputBox")
        self.gridLayout.addWidget(self.outputBox, 5, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # LINKING UI TO INFO
        self.displayCOMports()
        self.btnCommand.clicked.connect(self.doCommand)
        self.btnRefresh.clicked.connect(self.displayCOMports)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Laser Card Test"))
        self.label.setText(_translate("MainWindow", "Choose COM Port:"))
        self.btnCommand.setText(_translate("MainWindow", "Do Command"))
        self.label_2.setText(_translate("MainWindow", "Type command:"))
        self.btnRefresh.setText(_translate("MainWindow", "Refresh"))
        self.label_3.setText(_translate("MainWindow", "Output:"))

    #EXTERNAL FUNCTIONS in class
    def doCommand(self):
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
            self.outputBox.setPlainText(boxResponse)

            #Done and refresh
            ser.close()
            #self.displayCOMports()
        except:
            self.outputBox.setPlainText("Chosen COM Port does not exist. Either replug your device or refresh your list of devices.\r\n\r\n\r\n")

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


# MAIN
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())

