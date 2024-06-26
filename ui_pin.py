# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pinKykjbe.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QRegularExpression)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QRegularExpressionValidator)
from PyQt5.QtWidgets import *
import psycopg2


class PIN_Dialog(object):
    def __init__(self, emp_id, dialog):
        super(PIN_Dialog, self).__init__()
        self.dialog = dialog 
        self.emp_id = emp_id
    
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(347, 342)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 60, 181, 31))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.pininput = QLineEdit(self.widget)
        regex = QRegularExpression("^[0-9]{4}$")
        regex_validator = QRegularExpressionValidator(regex, self.pininput)
        self.pininput.setValidator(regex_validator)
        self.pininput.setObjectName("pininput")
        self.pininput.setMaxLength(4)
        self.pininput.setGeometry(QRect(40, 130, 261, 41))
        self.pininput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(50, 240, 241, 71))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.cancelbtn = QPushButton(self.widget_2)
        self.cancelbtn.setObjectName(u"cancelbtn")
        self.cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelbtn.setStyleSheet(u"background-color: rgb(236, 230, 230);\n"
"color: #B10303;\n"
"border: 1px solid #B10303;\n"
"border-radius: 4px;\n"
"padding: 7px;")

        self.horizontalLayout_2.addWidget(self.cancelbtn)

        self.confirmbtn = QPushButton(self.widget_2)
        self.confirmbtn.setObjectName(u"confirmbtn")
        self.confirmbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.confirmbtn.setStyleSheet(u"#confirmbtn{\n"
"background-color: #B10303;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"#confirmbtn:hover{\n"
"color:black;\n"
"}")

        self.horizontalLayout_2.addWidget(self.confirmbtn)


        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
        
        self.cancelbtn.clicked.connect(Dialog.reject)
        self.confirmbtn.clicked.connect(self.check_pin)
        
        print(self.emp_id)
        
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Enter your PIN", None))
        self.cancelbtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.confirmbtn.setText(QCoreApplication.translate("Dialog", u"Confirm", None))
    # retranslateUi
    
    def check_pin(self):
        pin = self.pininput.text()
        
        conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
        cursor = conn.cursor()

        cursor.execute('SELECT employee_id FROM employees WHERE emp_pin = %s AND employee_id = %s', (pin, self.emp_id))
        rows = cursor.fetchall()
        
        if rows:
            self.dialog.accept()  # PIN matches, accept the dialog
        else:
            self.dialog.reject()  # PIN doesn't match, reject the dialog
    

