
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import sqlite3
import MainPage_ui


con = sqlite3.connect('DailyTasks.db')
cur = con.cursor()



class Ui_Form(object):
    def newTask(self):
        date = self.getDate()

        if self.TopicDD.currentText() == "Add a task to an already made topic" and self.TopicEF.text() != "":
            if self.TaskEF.text() !="":
                topic = self.TopicEF.text()
                task = self.TaskEF.text()
                details = self.textEdit.toPlainText()

                res = cur.execute("INSERT INTO 'main'.'Topic' ('Label') VALUES ('"+str(topic)+"'")
                con.commit()
                id = cur.lastrowid
                res = cur.execute("INSERT INTO 'main'.'Tasks' ('"+id+"', '"+str(task)+"', '"+str(details)+"') VALUES (1, 'Bug Fixes', 'Need to do extensive tests to find any bugs');")
                con.commit()
            return
        elif self.TopicEF.text() == "" and self.TopicDD.currentText() != "Add a task to an already made topic":
            return
            
           # res = cur.execute("INSERT INTO 'main'.'Tasks' ('TopicID', 'Task', 'Details') VALUES (1, 'Bug Fixes', 'Need to do extensive tests to find any bugs');")

#con.commit()

    def getDropDown(self):
        date = self.getDate()

        res = cur.execute("SELECT * FROM Topic")
        AllTopics = res.fetchall()

        for row, topic in enumerate(AllTopics):
            topicDate = datetime.strptime(topic[2][:10],"%Y-%m-%d")
            if topicDate == date:
                self.TopicDD.addItem("")
                self.TopicDD.setItemText(row, str(topic[1]))




    def getDate(self):
        date = datetime.now()
        date = str(date)[:10]
        date = datetime.strptime(date,"%Y-%m-%d")
        return date

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 600)
        MainWindow.setStyleSheet("background-color:rgb(210, 225, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")

        
        self.TopicLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.TopicLabel.setFont(font)
        self.TopicLabel.setObjectName("TopicLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.TopicLabel)


        self.TopicEF = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.TopicEF.setFont(font)
        self.TopicEF.setStyleSheet("background-color: white;\n"
"border-radius: 5;\n"
"border: 2px solid rgb(199, 199, 199);")
        self.TopicEF.setObjectName("TopicEF")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.TopicEF)


        self.OrLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.OrLabel.setFont(font)
        self.OrLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.OrLabel.setObjectName("OrLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.OrLabel)


        self.TopicDD = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setBold(True)
        font.setPointSize(10)
        self.TopicDD.setFont(font)
        self.TopicDD.setStyleSheet("background-color: white;\n"
"border-radius: 5;\n"
"border: 2px solid rgb(199, 199, 199);")
        self.TopicDD.setPlaceholderText("Add a task to an already made topic")
        self.TopicDD.setObjectName("TopicDD")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.TopicDD)
        self.getDropDown()


        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole, spacerItem)


        self.TaskLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.TaskLabel.setFont(font)
        self.TaskLabel.setObjectName("TaskLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.TaskLabel)


        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, spacerItem1)


        self.TaskEF = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.TaskEF.setFont(font)
        self.TaskEF.setStyleSheet("background-color: white;\n"
"border-radius: 5;\n"
"border: 2px solid rgb(199, 199, 199);")
        self.TaskEF.setObjectName("TaskEF")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.TaskEF)


        self.DetailsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.DetailsLabel.setFont(font)
        self.DetailsLabel.setObjectName("DetailsLabel")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.DetailsLabel)


        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: white;\n"
"border-radius: 15;\n"
"border: 2px solid rgb(199, 199, 199);")
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.textEdit)


        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(14, QtWidgets.QFormLayout.FieldRole, spacerItem3)


        self.SaveBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Gadugi")
        font.setPointSize(10)
        self.SaveBtn.setFont(font)
        self.SaveBtn.setStyleSheet("QPushButton{\n"
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
        self.SaveBtn.setObjectName("SaveBtn")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.SaveBtn)


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TopicLabel.setText(_translate("MainWindow", "Topic:"))
        self.OrLabel.setText(_translate("MainWindow", "Or"))
        self.TaskLabel.setText(_translate("MainWindow", "Task:"))
        self.DetailsLabel.setText(_translate("MainWindow", "Details:"))
        self.SaveBtn.setText(_translate("MainWindow", "Save"))
