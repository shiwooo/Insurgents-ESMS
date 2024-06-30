from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PyQt5.QtGui import QCursor, QFont, QPixmap
from PyQt5.QtWidgets import *
import os, sys

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName("Form")
        Form.resize(800, 600)
        
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        self.widget = QWidget(Form)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(40, 38, 38);")
        
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(100, 250, 600, 300))
        if hasattr(sys, '_MEIPASS'):
            script_dir = sys._MEIPASS
        else:
            script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "image", "Logo1.png")
        self.label.setPixmap(QPixmap(image_path))
        self.label.setScaledContents(True)
        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("background-color: rgb(199, 194, 194);")
        
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        
        self.welcome = QLabel(self.widget_2)
        self.welcome.setObjectName("welcome")
        self.welcome.setGeometry(QRect(95, 95, 610, 55))
        self.welcome.setFont(font)
        self.welcome.setStyleSheet("color: rgb(177, 3, 3);font-size: 64px;")
        self.welcome.setAlignment(Qt.AlignCenter)
        
        self.viewschedbtn = QPushButton(self.widget_2)
        self.viewschedbtn.setObjectName("viewschedbtn")
        self.viewschedbtn.setGeometry(QRect(400, 180, 170, 40))
        self.viewschedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.viewschedbtn.setStyleSheet("""
        #viewschedbtn{
                background-color: #ECE6E6;
                border: 1px solid  #B10303;
                font-size: 20px;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
        }
                                        
        #viewschedbtn:hover{
                background-color: rgb(177, 3, 3);
                color: white;
        }""")
        
        self.loginstaffbtn = QPushButton(self.widget_2)
        self.loginstaffbtn.setObjectName("loginstaffbtn")
        self.loginstaffbtn.setGeometry(QRect(230, 180, 170, 40))
        self.loginstaffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginstaffbtn.setStyleSheet("""
        #loginstaffbtn {
                background-color: rgb(177, 3, 3);
                color: white;
                font-size: 20px;
                border-top-left-radius: 5px;
                border-bottom-left-radius: 5px;
        }
        
        #loginstaffbtn:hover {
                color: black;
        }
        """)

        
        self.error = QLabel(self.widget_2)
        self.error.setObjectName("error")
        self.error.setGeometry(QRect(270, 250, 260, 40))
        self.error.setFont(font)
        self.error.setStyleSheet("""
        QLabel {
                color: #B71C1C;
                font-size: 16px;
        }
        """)

        self.error.setAlignment(Qt.AlignCenter)
        
        self.labelPass = QLabel(self.widget_2)
        self.labelPass.setObjectName("labelPass")
        self.labelPass.setGeometry(QRect(225, 410, 110, 20))
        self.labelPass.setFont(font)
        self.labelPass.setStyleSheet("color: rgb(177, 3, 3);font-size: 22px;")
        
        self.btnLogin = QPushButton(self.widget_2)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.setGeometry(QRect(300, 530, 200, 50))
        self.btnLogin.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnLogin.setStyleSheet("""
        QPushButton {
                background-color: rgb(177, 3, 3);
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 20px;
                font-weight: bold;
        }
        
        QPushButton:hover {
                background-color: rgb(204, 0, 0);
        }
        
        QPushButton:pressed {
                background-color: rgb(139, 0, 0);
        }
        """)

        
        self.inputEmail = QLineEdit(self.widget_2)
        self.inputEmail.setObjectName("inputEmail")
        self.inputEmail.setGeometry(QRect(225, 345, 350, 40))
        self.inputEmail.setStyleSheet("""
                background-color: rgb(255, 255, 255);
                border: 1px solid #B10303;
                border-radius: 5px;
        """)

        self.inputEmail.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        
        self.labelEmail = QLabel(self.widget_2)
        self.labelEmail.setObjectName("labelEmail")
        self.labelEmail.setGeometry(QRect(225, 310, 110, 20))
        self.labelEmail.setFont(font)
        self.labelEmail.setStyleSheet("color: rgb(177, 3, 3);font-size: 22px;")
        
        self.inputPass = QLineEdit(self.widget_2)
        self.inputPass.setObjectName("inputPass")
        self.inputPass.setGeometry(QRect(225, 445, 350, 40))
        self.inputPass.setStyleSheet("""
                background-color: rgb(255, 255, 255);
                border: 1px solid #B10303;
                border-radius: 5px;
        """)

        self.inputPass.setEchoMode(QLineEdit.Password)
       
        
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(145, 750, 510, 20))
        font2 = QFont()
        font2.setPointSize(8)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        # Ensure the initial focus is on the email input
        self.inputEmail.setFocus()

        # Set initial focus and tab order
        Form.setTabOrder(self.inputPass, self.btnLogin)
        Form.setTabOrder(self.inputEmail, self.inputPass)
        Form.setTabOrder(self.btnLogin, self.viewschedbtn)
        Form.setTabOrder(self.viewschedbtn, self.inputEmail)

        # Exclude unnecessary buttons from tab order
        self.loginstaffbtn.setFocusPolicy(Qt.NoFocus)
        self.viewschedbtn.setFocusPolicy(Qt.NoFocus)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label.setText("")
        self.welcome.setText(QCoreApplication.translate("Form", "Welcome to IESMS", None))
        self.viewschedbtn.setText(QCoreApplication.translate("Form", "View Schedules", None))
        self.loginstaffbtn.setText(QCoreApplication.translate("Form", "Admin Login", None))
        self.error.setText("")
        self.labelPass.setText(QCoreApplication.translate("Form", "Password", None))
        self.btnLogin.setText(QCoreApplication.translate("Form", "Login", None))
        self.labelEmail.setText(QCoreApplication.translate("Form", "Username", None))
        self.label_2.setText(QCoreApplication.translate("Form", "Developed by: Jefferson Gonzales, Jhonce Stave Quinio, Kent Vincent De La Concepcion", None))
