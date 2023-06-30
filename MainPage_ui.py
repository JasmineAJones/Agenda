from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime
import sqlite3


con = sqlite3.connect('DailyTasks.db')
cur = con.cursor()

class Ui_Agenda(object):
    def greeting(self):
        time = str(datetime.now().time())[0:2]

        if int(time) < 7:
            self.GreetLabel.setText("Good Morning Early Bird!")
        elif int(time) >= 7 and int(time) < 12:
                self.GreetLabel.setText("Morning Jasmine!")
        elif int(time) >= 12 and int(time) < 16:
                self.GreetLabel.setText("Good Afternoon!")
        elif int(time) >= 16:
                self.GreetLabel.setText("You're here late.... go home?")

    def AddTask(self):
        #get selected date
        self.date = self.calendarWidget.selectedDate()
        self.date = self.date.toPyDate()
        self.date = str(self.date)[:10]
        self.date = datetime.strptime(self.date,"%Y-%m-%d")

        self.Add = QMainWindow()
        self.ui =Ui_Form()
        self.ui.setupUi(self.Add, self.date)
        self.Add.show()

    def LoadNotes(self):
        f = open('Notes.txt', 'r')
        narray = f.readlines()
        notes = ''
        for i in range(len(narray)):
                notes = notes+""+narray[i]

        return(notes)
    
    def SaveNotes(self):
         f = open('Notes.txt', 'w')

         Notes = self.Notes.toPlainText()
         print(Notes)
         f.write(Notes)
         f.close

    def getDate(self):
        self.date = datetime.now()
        self.date = str(self.date)[:10]
        self.date = datetime.strptime(self.date,"%Y-%m-%d")
        return self.date

    def LoadTasks(self, date):
        res = cur.execute("SELECT * FROM Topic")
        AllTopics = res.fetchall()
        self.TaskView.setRowCount(100)

        rowcount = 0
        for row, topic in enumerate(AllTopics):
            topicDate = datetime.strptime(topic[2][:10],"%Y-%m-%d")
            if topicDate == date:
                id=topic[0]
                #Printing topic
                font = QtGui.QFont()
                font.setFamily("Gadugi")
                font.setPointSize(10)
                font.setWeight(75)
                Item = QTableWidgetItem(str(topic[1])+":")
                Item.setFont(font)
                Item.setTextAlignment(Qt.AlignCenter)
                Item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.TaskView.setItem(rowcount,0,Item)

                rowcount = rowcount + 1

                res = cur.execute("SELECT * FROM Tasks WHERE TopicID = "+str(id))
                AllTasks = res.fetchall()

                for w, tasks in enumerate(AllTasks):

                        #Printing Task
                        font = QtGui.QFont()
                        font.setFamily("Gadugi")
                        font.setPointSize(10)
                        font.setWeight(75)
                        Item = QTableWidgetItem(str(tasks[2]))
                        Item.setFont(font)
                        Item.setTextAlignment(Qt.AlignCenter)
                        Item.setFlags(QtCore.Qt.ItemIsEnabled)
                        self.TaskView.setItem(rowcount,1,Item)

                        #Printing Detail
                        if str(tasks[3]) != 'None':
                                font = QtGui.QFont()
                                font.setFamily("Gadugi")
                                font.setPointSize(10)
                                font.setWeight(75)
                                Item = QTableWidgetItem(str(tasks[3]))
                                Item.setFont(font)
                                Item.setTextAlignment(Qt.AlignCenter)
                                Item.setFlags(QtCore.Qt.ItemIsEnabled)
                                self.TaskView.setItem(rowcount,2,Item)

                        rowcount = rowcount + 1
                rowcount = rowcount + 2

    def NewDate(self):
        self.date = self.calendarWidget.selectedDate()
        self.date = self.date.toPyDate()
        self.date = str(self.date)[:10]
        self.date = datetime.strptime(self.date,"%Y-%m-%d")

        #Clear table
        self.TaskView.setRowCount(0)
        #Load table
        self.LoadTasks(self.date)

    def setupUi(self, MainWindow):
        monitor = QDesktopWidget().screenGeometry(0)
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
        self.calendarWidget.selectionChanged.connect(self.NewDate)


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
        self.Notes.setText(str(self.LoadNotes()))
        self.Notes.textChanged.connect(lambda: self.SaveNotes())


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


        self.TaskView = QtWidgets.QTableWidget(self.centralwidget)
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
        self.TaskView.setColumnCount(3)
        self.TaskView.setRowCount(100)
        item = QtWidgets.QTableWidgetItem()
        self.TaskView.setHorizontalHeaderItem(0, item)
        self.TaskView.setColumnWidth(0, round((monitor.width())/10))
        item = QtWidgets.QTableWidgetItem()
        self.TaskView.setHorizontalHeaderItem(1, item)
        self.TaskView.setColumnWidth(1, round((monitor.width())/6))
        item = QtWidgets.QTableWidgetItem()
        self.TaskView.setHorizontalHeaderItem(2, item)
        self.TaskView.setColumnWidth(2, round((monitor.width())/4.5))
        self.gridLayout.addWidget(self.TaskView, 1, 0, 1, 6)
        self.LoadTasks(self.getDate())


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Agenda"))
        self.EditBtn.setText(_translate("MainWindow", "Edit"))
        self.AddBtn.setText(_translate("MainWindow", "Add New"))
        self.CopyBtn.setText(_translate("MainWindow", "Copy"))
        
        item = self.TaskView.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Topic"))
        item = self.TaskView.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Tasks"))
        item = self.TaskView.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Details"))

##### FORM PAGE ######

class Ui_Form(object):
    def newTask(self):
        if self.TopicDD.currentText() == "Add a task to an already made topic" and self.TopicEF.text() != "":
            #If were creating a new topic and tasks
            topic = self.TopicEF.text()
            task = self.TaskEF.text()
            details = self.textEdit.toPlainText()

            cur.execute("INSERT INTO 'main'.'Topic' ('Label', 'Date') VALUES ('"+str(topic)+"', '"+str(self.date)+"');")
            con.commit()
            id = cur.lastrowid
            cur.execute("INSERT INTO 'main'.'Tasks' ('TopicID', 'Task', 'Details', 'Date') VALUES ('"+str(id)+"', '"+str(task)+"', '"+str(details)+"', '"+str(self.date)+"');")
            con.commit()
            self.sig.emit(1)
            

        
        elif self.TopicEF.text() == "" and self.TopicDD.currentText() != "Add a task to an already made topic":
            #If were creating a task to an already make topic
            topic = self.TopicDD.currentText()
            task = self.TaskEF.text()
            details = self.textEdit.toPlainText()

            print(self.date)
            res = cur.execute("SELECT * FROM Topic WHERE Date LIKE '"+str(self.date)[:10]+"%'")
            allTopics =  res.fetchall()

            for t in allTopics:
                if t[1] == topic:
                    id = t[0]
                    cur.execute("INSERT INTO 'main'.'Tasks' ('TopicID', 'Task', 'Details', 'Date') VALUES ('"+str(id)+"', '"+str(task)+"', '"+str(details)+"', '"+str(self.date)+"');")
                    con.commit()
                    break
        
        else:
            #Error Msg
            return
     
    def getDropDown(self):
        res = cur.execute("SELECT * FROM Topic")
        AllTopics = res.fetchall()
        i = 0
        for row, topic in enumerate(AllTopics):
            topicDate = datetime.strptime(topic[2][:10],"%Y-%m-%d")
            if topicDate == self.date:
                self.TopicDD.addItem("")
                self.TopicDD.setItemText(i, str(topic[1]))
                i = i+1

    def setupUi(self, MainWindow, date):
        self.date = date
        self.sig = pyqtSignal(int)
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
        self.SaveBtn.clicked.connect(self.newTask)


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



if __name__ == "__main__": #### Creates Scene ####
    import sys
    app = QApplication(sys.argv)
    ui = Ui_Agenda()
    win = QtWidgets.QMainWindow()
    ui.setupUi(win)
    win.show()

    sys.exit(app.exec())
