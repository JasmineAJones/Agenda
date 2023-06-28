from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import sqlite3
import FormPage_ui


class Ui_Agenda(object):
    def greeting(self):
        time = str(datetime.now().time())[0:2]

        if int(time) < 7:
            self.GreetLabel.setText("Good Morning Early Bird!")
        elif int(time) >= 7 and int(time) < 12:
                self.GreetLabel.setText("Morning Jasmine!")
        elif int(time) >= 12 and int(time) < 15:
                self.GreetLabel.setText("Good Afternoon!")
        elif int(time) >= 15:
                self.GreetLabel.setText("You're here late.... go home?")

    def AddTask(self):
        self.Add = QMainWindow()
        self.ui =FormPage_ui.Ui_Form()
        self.ui.setupUi(self.Add)
        self.Add.show()
         

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1022, 777)
        MainWindow.setStyleSheet("background-color:rgb(210, 225, 255);")


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)


        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("QCalendarWidget QAbstractItemView{\n"
"background-color : rgb(221, 221, 221);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton{\n"
"background-color : rgb(230, 230, 230);\n"
"color: black;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::hover{\n"
"background-color : rgb(167, 198, 221);\n"
"}")
        self.calendarWidget.setObjectName("calendarWidget")


        self.gridLayout.addWidget(self.calendarWidget, 4, 0, 1, 5)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 4, 1, 2)


        self.Notes = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.Notes.setFont(font)
        self.Notes.setStyleSheet("QTextEdit{\n"
"            background-color: white;\n"
"            border-radius: 15;\n"
"            border: 2px solid rgb(199, 199, 199);\n"
"        }")
        self.Notes.setObjectName("Notes")
        self.gridLayout.addWidget(self.Notes, 4, 5, 1, 1)


        self.EditBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.EditBtn.setFont(font)
        self.EditBtn.setStyleSheet("QPushButton{\n"
"            background-color:rgb(223, 223, 223);\n"
"            border-radius: 8; \n"
"            border: 2px solid rgb(115, 115, 115); \n"
"            border-style: outset;\n"
"            padding: 5;\n"
"            padding-right: 10px;\n"
"            padding-left: 10px;\n"
"        }\n"
"\n"
"QPushButton:hover{\n"
"           background-color:rgb(182, 182, 182);\n"
"        }")
        self.EditBtn.setObjectName("EditBtn")
        self.gridLayout.addWidget(self.EditBtn, 2, 2, 1, 1)


        self.AddBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.AddBtn.setFont(font)
        self.AddBtn.setStyleSheet("QPushButton{\n"
"            background-color:rgb(223, 223, 223);\n"
"            border-radius: 8; \n"
"            border: 2px solid rgb(115, 115, 115); \n"
"            border-style: outset;\n"
"            padding: 5;\n"
"            padding-right: 10px;\n"
"            padding-left: 10px;\n"
"        }\n"
"\n"
"QPushButton:hover{\n"
"           background-color:rgb(182, 182, 182);\n"
"        }")
        self.AddBtn.setObjectName("AddBtn")
        self.gridLayout.addWidget(self.AddBtn, 2, 3, 1, 1)
        self.AddBtn.clicked.connect(self.AddTask)


        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)


        self.GreetLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(16)
        self.GreetLabel.setFont(font)
        self.GreetLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GreetLabel.setObjectName("GreetLabel")
        self.gridLayout.addWidget(self.GreetLabel, 0, 0, 1, 6)
        self.greeting()


        self.CopyBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.CopyBtn.setFont(font)
        self.CopyBtn.setStyleSheet("QPushButton{\n"
"            background-color:rgb(223, 223, 223);\n"
"            border-radius: 8; \n"
"            border: 2px solid rgb(115, 115, 115); \n"
"            border-style: outset;\n"
"            padding: 5;\n"
"            padding-right: 10px;\n"
"            padding-left: 10px;\n"
"        }\n"
"\n"
"QPushButton:hover{\n"
"           background-color:rgb(182, 182, 182);\n"
"        }")
        self.CopyBtn.setObjectName("CopyBtn")
        self.gridLayout.addWidget(self.CopyBtn, 2, 1, 1, 1)


        self.TaskView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.TaskView.setFont(font)
        self.TaskView.setStyleSheet("QTableView{\n"
"            background-color:white;\n"
"            border-radius: 15;\n"
"            border: 2px solid rgb(199, 199, 199);\n"
"        }")
        self.TaskView.setShowGrid(False)
        self.TaskView.setGridStyle(QtCore.Qt.NoPen)
        self.TaskView.setObjectName("TaskView")
        self.gridLayout.addWidget(self.TaskView, 1, 0, 1, 6)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agenda"))
        self.Notes.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gadugi\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\">Notes:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:7.8pt;\"><br /></p></body></html>"))
        self.EditBtn.setText(_translate("MainWindow", "Edit"))
        self.AddBtn.setText(_translate("MainWindow", "Add New"))
        #self.GreetLabel.setText(_translate("MainWindow", "Greeting"))
        self.CopyBtn.setText(_translate("MainWindow", "Copy"))



if __name__ == "__main__": #### Creates Scene ####
    import sys
    app = QApplication(sys.argv)
    ui = Ui_Agenda()
    win = QtWidgets.QMainWindow()
    ui.setupUi(win)
    win.show()

    sys.exit(app.exec())
