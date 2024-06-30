from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, QRect, QSize, Qt, pyqtSignal
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import *
import psycopg2


class AddScheduleDialog(QObject):
    sched_add = pyqtSignal()
    
    def __init__(self, dialog):
        super(AddScheduleDialog, self).__init__()
        self.dialog = dialog 
    
    
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(529, 666)
        Dialog.setMinimumSize(QSize(529, 666))
        Dialog.setMaximumSize(QSize(529, 666))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(236, 230, 230);")
        self.addbtn = QPushButton(self.widget)
        self.addbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addbtn.setObjectName("addbtn")
        self.addbtn.setGeometry(QRect(290, 580, 151, 41))
        font = QFont()
        font.setPointSize(12)
        self.addbtn.setFont(font)
        self.addbtn.setStyleSheet("background-color: #B10303;"
"color: white;"
"border: 1px solid #B10303;"
"border-radius: 4px;"
"padding: 7px;")
        self.cancelbtn = QPushButton(self.widget)
        self.cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelbtn.setObjectName("cancelbtn")
        self.cancelbtn.setGeometry(QRect(80, 580, 150, 40))
        self.cancelbtn.setFont(font)
        self.cancelbtn.setStyleSheet("background-color: rgb(236, 230, 230);"
"color: #B10303;"
"border: 1px solid #B10303;"
"border-radius: 4px;"
"padding: 7px;")
        self.fromlabel = QLabel(self.widget)
        self.fromlabel.setObjectName("fromlabel")
        self.fromlabel.setGeometry(QRect(40, 370, 57, 30))
        font1 = QFont()
        font1.setPointSize(15)
        self.fromlabel.setFont(font1)
        self.fromlabel.setStyleSheet("color: #B10303;")
        self.frominput = QComboBox(self.widget)
        self.frominput.addItem("")
        self.frominput.addItem("")
        self.frominput.addItem("")
        self.frominput.setObjectName("frominput")
        self.frominput.setGeometry(QRect(40, 410, 140, 40))
        self.frominput.setFont(font)
        self.frominput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(190, 400, 41, 51))
        self.label_4.setFont(font1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(460, 400, 41, 51))
        self.label_3.setFont(font1)
        self.toinput = QComboBox(self.widget)
        self.toinput.addItem("")
        self.toinput.addItem("")
        self.toinput.addItem("")
        self.toinput.setObjectName("toinput")
        self.toinput.setGeometry(QRect(310, 410, 140, 40))
        self.toinput.setFont(font)
        self.toinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setGeometry(QRect(320, 40, 131, 41))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(40, 50, 171, 30))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet("color: #B10303;")
        self.label.setAlignment(Qt.AlignCenter)
        self.namelabel = QLabel(self.widget)
        self.namelabel.setObjectName("namelabel")
        self.namelabel.setGeometry(QRect(40, 260, 71, 30))
        self.namelabel.setFont(font1)
        self.namelabel.setStyleSheet("color: #B10303;")
        self.nameinput = QLineEdit(self.widget)
        self.nameinput.setObjectName("nameinput")
        self.nameinput.setGeometry(QRect(40, 310, 441, 41))
        font3 = QFont()
        font3.setPointSize(8)
        self.nameinput.setFont(font3)
        self.nameinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")
        self.nameinput.setReadOnly(True)
        self.tolabel = QLabel(self.widget)
        self.tolabel.setObjectName("tolabel")
        self.tolabel.setGeometry(QRect(310, 370, 57, 30))
        self.tolabel.setFont(font1)
        self.tolabel.setStyleSheet("color: #B10303;")
        self.datlabel = QLabel(self.widget)
        self.datlabel.setObjectName("datlabel")
        self.datlabel.setGeometry(QRect(40, 160, 71, 30))
        self.datlabel.setFont(font1)
        self.datlabel.setStyleSheet("color: #B10303;")
        self.dateinput = QLineEdit(self.widget)
        self.dateinput.setObjectName("dateinput")
        self.dateinput.setGeometry(QRect(40, 210, 441, 41))
        self.dateinput.setFont(font3)
        self.dateinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")
        self.dateinput.setReadOnly(True)
        self.emp_id = QLabel(self.widget)
        self.emp_id.setObjectName("emp_id")
        self.emp_id.setGeometry(QRect(220, 130, 55, 16))

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
        
        self.addbtn.clicked.connect(self.add_schedule)
        self.cancelbtn.clicked.connect(Dialog.close)
        
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.addbtn.setText(QCoreApplication.translate("Dialog", "Add", None))
        self.cancelbtn.setText(QCoreApplication.translate("Dialog", "Cancel", None))
        self.fromlabel.setText(QCoreApplication.translate("Dialog", "From", None))
        self.frominput.setItemText(0, QCoreApplication.translate("Dialog", "10", None))
        self.frominput.setItemText(1, QCoreApplication.translate("Dialog", "11", None))
        self.frominput.setItemText(2, QCoreApplication.translate("Dialog", "12", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", "AM", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", "PM", None))
        self.toinput.setItemText(0, QCoreApplication.translate("Dialog", "7", None))
        self.toinput.setItemText(1, QCoreApplication.translate("Dialog", "8", None))
        self.toinput.setItemText(2, QCoreApplication.translate("Dialog", "9", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", "Regular", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", "Reserve", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", "Day off", None))

        self.label.setText(QCoreApplication.translate("Dialog", "Set Schedule", None))
        self.namelabel.setText(QCoreApplication.translate("Dialog", "Name", None))
        self.tolabel.setText(QCoreApplication.translate("Dialog", "To", None))
        self.datlabel.setText(QCoreApplication.translate("Dialog", "Date", None))
        self.emp_id.setText("")
        self.emp_id.hide()
    # retranslateUi


    def add_schedule(self):
        
        
        status = self.comboBox.currentText()
        shift_date = self.dateinput.text()
        start_time = self.frominput.currentText()
        end_time = self.toinput.currentText() 
        emp_id = self.emp_id.text()
        
        try:
            conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
            cursor = conn.cursor()
            

            insert_query = """
                INSERT INTO schedules (employee_id, shift_date, start_time, end_time, status)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (emp_id, shift_date, start_time, end_time, status))
            conn.commit()

            cursor.close()
            conn.close()
            
            
            # Show a message box with success
            QMessageBox.information(None, "Success", "Schedule added successfully!")
            self.sched_add.emit()
            self.dialog.close()

        except Exception as e:
            QMessageBox.critical(None, "Database Error", f"Error: {str(e)}")
        
    
