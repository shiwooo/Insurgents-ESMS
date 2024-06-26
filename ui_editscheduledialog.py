# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editscheduledialogmLqVQV.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import psycopg2


class EditSchedDialog(QObject):
    sched_update = pyqtSignal()    
        
    def __init__(self, dialog, staff_id, date):
        super(EditSchedDialog, self).__init__()
        self.dialog = dialog
        self.staff_id = staff_id
        self.date = date

    def setupUi(self, Dialog):
        print(8)
        self.dialog1 = Dialog
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(529, 666)
        Dialog.setMinimumSize(QSize(529, 666))
        Dialog.setMaximumSize(QSize(529, 666))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.updatebtn = QPushButton(self.widget)
        self.updatebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updatebtn.setObjectName(u"updatebtn")
        self.updatebtn.setGeometry(QRect(290, 580, 151, 41))
        font = QFont()
        font.setPointSize(12)
        self.updatebtn.setFont(font)
        self.updatebtn.setStyleSheet(u"#updatebtn{\n"
"	background-color: #B10303;\n"
"	color: white;\n"
"	border: 1px solid #B10303;\n"
"	border-radius: 4px;\n"
"	padding: 7px;\n"
"}\n"
"\n"
"#updatebtn:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")
        self.cancelbtn = QPushButton(self.widget)
        self.cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelbtn.setObjectName(u"cancelbtn")
        self.cancelbtn.setGeometry(QRect(80, 580, 150, 40))
        self.cancelbtn.setFont(font)
        self.cancelbtn.setStyleSheet(u"#cancelbtn{\n"
"	background-color: rgb(236, 230, 230);\n"
"	color: #B10303;\n"
"	border: 1px solid #B10303;\n"
"	border-radius: 4px;\n"
"	padding: 7px;\n"
"}\n"
"\n"
"#cancelbtn:hover{\n"
"	background-color: #B10303;\n"
"	color: white;\n"
"}")
        self.fromlabel = QLabel(self.widget)
        self.fromlabel.setObjectName(u"fromlabel")
        self.fromlabel.setGeometry(QRect(40, 370, 57, 30))
        font1 = QFont()
        font1.setPointSize(15)
        self.fromlabel.setFont(font1)
        self.fromlabel.setStyleSheet(u"color: #B10303;")
        self.frominput = QComboBox(self.widget)
        self.frominput.addItem("")
        self.frominput.addItem("")
        self.frominput.addItem("")
        self.frominput.setObjectName(u"frominput")
        self.frominput.setGeometry(QRect(40, 410, 140, 40))
        self.frominput.setFont(font)
        self.frominput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 400, 41, 51))
        self.label_4.setFont(font1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 400, 41, 51))
        self.label_3.setFont(font1)
        self.toinput = QComboBox(self.widget)
        self.toinput.addItem("")
        self.toinput.addItem("")
        self.toinput.addItem("")
        self.toinput.setObjectName(u"toinput")
        self.toinput.setGeometry(QRect(310, 410, 140, 40))
        self.toinput.setFont(font)
        self.toinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(320, 40, 131, 41))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 171, 30))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: #B10303;")
        self.label.setAlignment(Qt.AlignCenter)
        self.namelabel = QLabel(self.widget)
        self.namelabel.setObjectName(u"namelabel")
        self.namelabel.setGeometry(QRect(40, 260, 71, 30))
        self.namelabel.setFont(font1)
        self.namelabel.setStyleSheet(u"color: #B10303;")
        self.nameinput = QLineEdit(self.widget)
        self.nameinput.setObjectName(u"nameinput")
        self.nameinput.setGeometry(QRect(40, 310, 441, 41))
        font3 = QFont()
        font3.setPointSize(8)
        self.nameinput.setFont(font3)
        self.nameinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.nameinput.setReadOnly(True)
        self.tolabel = QLabel(self.widget)
        self.tolabel.setObjectName(u"tolabel")
        self.tolabel.setGeometry(QRect(310, 370, 57, 30))
        self.tolabel.setFont(font1)
        self.tolabel.setStyleSheet(u"color: #B10303;")
        self.datlabel = QLabel(self.widget)
        self.datlabel.setObjectName(u"datlabel")
        self.datlabel.setGeometry(QRect(40, 160, 71, 30))
        self.datlabel.setFont(font1)
        self.datlabel.setStyleSheet(u"color: #B10303;")
        self.dateinput = QLineEdit(self.widget)
        self.dateinput.setObjectName(u"dateinput")
        self.dateinput.setGeometry(QRect(40, 210, 441, 41))
        self.dateinput.setFont(font3)
        self.dateinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.dateinput.setReadOnly(True)
        self.emp_id = QLabel(self.widget)
        self.emp_id.setObjectName(u"emp_id")
        self.emp_id.setGeometry(QRect(220, 130, 55, 16))
        
        self.sched_id = QLabel(self.widget)
        self.sched_id.setObjectName(u"sched_id")
        self.sched_id.setGeometry(QRect(220, 130, 55, 16))

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
        
        self.updatebtn.clicked.connect(self.update_staff)
        self.cancelbtn.clicked.connect(Dialog.close)
        
        
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.updatebtn.setText(QCoreApplication.translate("Dialog", u"Update", None))
        self.cancelbtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.fromlabel.setText(QCoreApplication.translate("Dialog", u"From", None))
        self.frominput.setItemText(0, QCoreApplication.translate("Dialog", u"10", None))
        self.frominput.setItemText(1, QCoreApplication.translate("Dialog", u"11", None))
        self.frominput.setItemText(2, QCoreApplication.translate("Dialog", u"12", None))

        self.label_4.setText(QCoreApplication.translate("Dialog", u"AM", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"PM", None))
        self.toinput.setItemText(0, QCoreApplication.translate("Dialog", u"7", None))
        self.toinput.setItemText(1, QCoreApplication.translate("Dialog", u"8", None))
        self.toinput.setItemText(2, QCoreApplication.translate("Dialog", u"9", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Regular", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Reserve", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Day off", None))

        self.label.setText(QCoreApplication.translate("Dialog", u"Edit Schedule", None))
        self.namelabel.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.tolabel.setText(QCoreApplication.translate("Dialog", u"To", None))
        self.datlabel.setText(QCoreApplication.translate("Dialog", u"Date", None))
        self.emp_id.setText("")
        self.emp_id.hide()
        # self.shift_date.setText("")
        self.sched_id.setText("")
        self.sched_id.hide()
        
    # retranslateUi
    
    
    def update_staff(self):
        status = self.comboBox.currentText()
        start_time = self.frominput.currentText()
        end_time = self.toinput.currentText()
        emp_id = self.emp_id.text()
        
        
        try:
                conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
                cursor = conn.cursor()
                
                update_query = """
                UPDATE schedules
                SET start_time = %s, end_time = %s, status = %s
                WHERE employee_id = %s AND shift_date = '"""+self.date+"""'
                """
                cursor.execute(update_query, (start_time, end_time, status, emp_id))
                conn.commit()

                cursor.close()
                conn.close()
                
                # Show a message box with success
                QMessageBox.information(None, "Success", "Schedule updated successfully!")
                self.sched_update.emit()
                self.dialog1.close()

        except Exception as e:
                QMessageBox.critical(None, "Database Error", f"Error: {str(e)}")


#     def delete_staff(self):
#         sched_id = self.sched_id.text()

#         try:
#                 conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
#                 cursor = conn.cursor()
                
#                 delete_query = """
#                 DELETE FROM schedules
#                 WHERE schedule_id = %s
#                 """
#                 cursor.execute(delete_query, (sched_id,))
#                 conn.commit()

#                 cursor.close()
#                 conn.close()
                
#                 # Show a message box with success
#                 QMessageBox.information(None, "Success", "Schedule deleted successfully!")
                
#                 self.dialog.close()

#         except Exception as e:
#                 QMessageBox.critical(None, "Database Error", f"Error: {str(e)}")
