# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newloginacyLVG.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1600, 800)
        Form.setMinimumSize(QSize(1600, 800))
        Form.setMaximumSize(QSize(1600, 800))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setAcceptDrops(False)
        self.widget.setStyleSheet(u"background-color: rgb(40, 38, 38);")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 250, 600, 300))
        self.label.setPixmap(QPixmap(u"../Insurgents ESMS/image/Logo1.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(199, 194, 194);")
        self.welcome = QLabel(self.widget_2)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(95, 95, 610, 55))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet(u"color: rgb(177, 3, 3);\n"
"font-size: 64px;")
        self.welcome.setAlignment(Qt.AlignCenter)
        self.viewschedbtn = QPushButton(self.widget_2)
        self.viewschedbtn.setObjectName(u"viewschedbtn")
        self.viewschedbtn.setGeometry(QRect(400, 180, 170, 40))
        font1 = QFont()
        self.viewschedbtn.setFont(font1)
        self.viewschedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.viewschedbtn.setStyleSheet(u"#viewschedbtn{\n"
"	background-color: #ECE6E6;\n"
"	border: 1px solid  #B10303;\n"
"	font-size: 20px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#viewschedbtn:hover{\n"
"	background-color: rgb(177, 3, 3);\n"
"	color: white;\n"
"}\n"
"")
        self.loginstaffbtn = QPushButton(self.widget_2)
        self.loginstaffbtn.setObjectName(u"loginstaffbtn")
        self.loginstaffbtn.setGeometry(QRect(230, 180, 170, 40))
        self.loginstaffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginstaffbtn.setStyleSheet(u"#loginstaffbtn{\n"
"	background-color: rgb(177, 3, 3);\n"
"	color: white;\n"
"	font-size: 20px;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"#loginstaffbtn:hover{\n"
"	color: black;\n"
"}")
        self.error = QLabel(self.widget_2)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(280, 250, 250, 40))
        self.error.setFont(font)
        self.error.setStyleSheet(u"QLabel {\n"
"    color: #B71C1C; \n"
"    font-size: 16px;\n"
"}")
        self.error.setAlignment(Qt.AlignCenter)
        self.labelPass = QLabel(self.widget_2)
        self.labelPass.setObjectName(u"labelPass")
        self.labelPass.setGeometry(QRect(225, 410, 110, 20))
        self.labelPass.setFont(font)
        self.labelPass.setStyleSheet(u"color: rgb(177, 3, 3);\n"
"font-size: 22px;")
        self.btnLogin = QPushButton(self.widget_2)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(300, 570, 200, 50))
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(177, 3, 3);\n"
"   color: white;\n"
"   border-radius: 10px;\n"
"    padding: 10px 20px;\n"
"   font-size: 20px;\n"
"   font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(204, 0, 0); \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(139, 0, 0);\n"
"}")
        self.inputEmail = QLineEdit(self.widget_2)
        self.inputEmail.setObjectName(u"inputEmail")
        self.inputEmail.setGeometry(QRect(225, 345, 350, 40))
        self.inputEmail.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;")
        self.inputEmail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.labelEmail = QLabel(self.widget_2)
        self.labelEmail.setObjectName(u"labelEmail")
        self.labelEmail.setGeometry(QRect(225, 310, 110, 20))
        self.labelEmail.setFont(font)
        self.labelEmail.setStyleSheet(u"color: rgb(177, 3, 3);\n"
"font-size: 22px;")
        self.inputPass = QLineEdit(self.widget_2)
        self.inputPass.setObjectName(u"inputPass")
        self.inputPass.setGeometry(QRect(225, 445, 350, 40))
        self.inputPass.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;")
        self.inputPass.setEchoMode(QLineEdit.Password)
        self.inputPass.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.widget_2)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.welcome.setText(QCoreApplication.translate("Form", u"Welcome to IESMS", None))
        self.viewschedbtn.setText(QCoreApplication.translate("Form", u"Staff Schedule", None))
        self.loginstaffbtn.setText(QCoreApplication.translate("Form", u"Admin Login", None))
        self.error.setText("")
        self.labelPass.setText(QCoreApplication.translate("Form", u"Password", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", u"Login", None))
        self.labelEmail.setText(QCoreApplication.translate("Form", u"Username", None))
    # retranslateUi



