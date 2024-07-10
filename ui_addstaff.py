import psycopg2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt, pyqtSignal, QRegExp, QRegularExpression, QDate
from PyQt5.QtGui import QCursor, QFont, QRegExpValidator, QRegularExpressionValidator

class AddStaffDialog(QDialog):
    staff_add = pyqtSignal()
    
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(618, 616)
        self.dialog = Dialog
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(236, 230, 230);")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName("widget_7")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.widget_7.setFont(font)
        self.gridLayout_2 = QGridLayout(self.widget_7)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QLabel(self.widget_7)
        self.label.setObjectName("label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet("color: #B10303;"
                                 "font-size: 32px;")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_4)
        self.widget_8.setObjectName("widget_8")

        self.horizontalLayout.addWidget(self.widget_8)


        self.gridLayout_3.addWidget(self.widget_4, 0, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_3)
        self.widget_13.setObjectName("widget_13")
        self.verticalLayout_3 = QVBoxLayout(self.widget_13)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.fnamelabel = QLabel(self.widget_13)
        self.fnamelabel.setObjectName("fnamelabel")
        self.fnamelabel.setFont(font)
        self.fnamelabel.setStyleSheet("color: #B10303;")

        self.verticalLayout_3.addWidget(self.fnamelabel)

        self.fnameinput = QLineEdit(self.widget_13)
        self.fnameinput.setObjectName("fnameinput")
        self.fnameinput.setMaxLength(35)
        self.fnameinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")

        self.verticalLayout_3.addWidget(self.fnameinput)


        self.horizontalLayout_2.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.widget_3)
        self.widget_14.setObjectName("widget_14")
        self.verticalLayout_2 = QVBoxLayout(self.widget_14)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lnamelabel = QLabel(self.widget_14)
        self.lnamelabel.setObjectName("lnamelabel")
        self.lnamelabel.setFont(font)
        self.lnamelabel.setStyleSheet("color: #B10303;")

        self.verticalLayout_2.addWidget(self.lnamelabel)

        self.lnameinput = QLineEdit(self.widget_14)
        self.lnameinput.setObjectName("lnameinput")
        self.lnameinput.setMaxLength(35)
        self.lnameinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;")

        self.verticalLayout_2.addWidget(self.lnameinput)


        self.horizontalLayout_2.addWidget(self.widget_14)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_5)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_4 = QVBoxLayout(self.widget_12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.phonelabel = QLabel(self.widget_12)
        self.phonelabel.setObjectName("phonelabel")
        self.phonelabel.setFont(font)
        self.phonelabel.setStyleSheet("color: #B10303;")

        self.verticalLayout_4.addWidget(self.phonelabel)

        self.phoneinput = QLineEdit(self.widget_12)
        regex = QRegularExpression("^[0-9]{11}$")
        regex_validator = QRegularExpressionValidator(regex, self.phoneinput)
        self.phoneinput.setValidator(regex_validator)
        self.phoneinput.setObjectName("phoneinput")
        self.phoneinput.setMaxLength(11)
        self.phoneinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")

        self.verticalLayout_4.addWidget(self.phoneinput)


        self.horizontalLayout_3.addWidget(self.widget_12)

        self.widget_15 = QWidget(self.widget_5)
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_5 = QVBoxLayout(self.widget_15)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.emaillabel = QLabel(self.widget_15)
        self.emaillabel.setObjectName("emaillabel")
        self.emaillabel.setFont(font)
        self.emaillabel.setStyleSheet("color: #B10303;")

        self.verticalLayout_5.addWidget(self.emaillabel)

        self.emailinput = QLineEdit(self.widget_15)
        email_regex = QRegExp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        email_validator = QRegExpValidator(email_regex, self.emailinput)
        self.emailinput.setObjectName("emailinput")
        self.emailinput.setValidator(email_validator)
        self.emailinput.setMaxLength(35)
        self.emailinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")

        self.verticalLayout_5.addWidget(self.emailinput)


        self.horizontalLayout_3.addWidget(self.widget_15)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_16 = QWidget(self.widget_6)
        self.widget_16.setObjectName("widget_16")
        self.verticalLayout_7 = QVBoxLayout(self.widget_16)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.addresslabel = QLabel(self.widget_16)
        self.addresslabel.setObjectName("addresslabel")
        self.addresslabel.setFont(font)
        self.addresslabel.setStyleSheet("color: #B10303;")

        self.verticalLayout_7.addWidget(self.addresslabel)

        self.addressinput = QLineEdit(self.widget_16)
        self.addressinput.setObjectName("addressinput")
        self.addressinput.setMaxLength(70)
        self.addressinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")

        self.verticalLayout_7.addWidget(self.addressinput)


        self.horizontalLayout_4.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.widget_6)
        self.widget_17.setObjectName("widget_17")
        self.verticalLayout_6 = QVBoxLayout(self.widget_17)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pinlabel_2 = QLabel(self.widget_17)
        self.pinlabel_2.setObjectName("pinlabel_2")
        self.pinlabel_2.setFont(font)
        self.pinlabel_2.setStyleSheet("color: #B10303;")

        self.verticalLayout_6.addWidget(self.pinlabel_2)

        self.pininput = QLineEdit(self.widget_17)
        regex = QRegularExpression("^[0-9]{4}$")
        regex_validator = QRegularExpressionValidator(regex, self.pininput)
        self.pininput.setValidator(regex_validator)
        self.pininput.setObjectName("pininput")
        self.pininput.setMaxLength(4)
        self.pininput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"")

        self.verticalLayout_6.addWidget(self.pininput)


        self.horizontalLayout_4.addWidget(self.widget_17)

        self.horizontalLayout_4.setStretch(0, 5)
        self.horizontalLayout_4.setStretch(1, 5)

        self.verticalLayout.addWidget(self.widget_6)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.widget_9)
        self.widget_18.setObjectName("widget_18")
        self.verticalLayout_8 = QVBoxLayout(self.widget_18)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.hdlabel = QLabel(self.widget_18)
        self.hdlabel.setObjectName("hdlabel")
        self.hdlabel.setFont(font)
        self.hdlabel.setStyleSheet("color: #B10303;")

        self.verticalLayout_8.addWidget(self.hdlabel)

        self.dhinput = QDateEdit(self.widget_18)
        self.dhinput.setObjectName("dhinput")
        self.dhinput.setStyleSheet("background-color: rgb(255, 255, 255);"
        "border: 1px solid  #B10303;"
        "border-radius: 5px;"
        "padding: 4px;")
        self.dhinput.setDate(QDate.currentDate())
        self.dhinput.setDisplayFormat("MM/dd/yy")
        self.verticalLayout_8.addWidget(self.dhinput)



        self.horizontalLayout_5.addWidget(self.widget_18)

        self.widget_19 = QWidget(self.widget_9)
        self.widget_19.setObjectName("widget_19")
        self.verticalLayout_9 = QVBoxLayout(self.widget_19)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.deptlabel = QLabel(self.widget_19)
        self.deptlabel.setObjectName("deptlabel")
        self.deptlabel.setFont(font)
        self.deptlabel.setStyleSheet("color: #B10303;")



        self.horizontalLayout_5.addWidget(self.widget_19)


        self.verticalLayout.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.widget_2)
        self.widget_10.setObjectName("widget_10")

        self.verticalLayout.addWidget(self.widget_10)

        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.widget_20 = QWidget(self.widget_11)
        self.widget_20.setObjectName("widget_20")
        self.gridLayout_4 = QGridLayout(self.widget_20)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.cancelbtn = QPushButton(self.widget_20)
        self.cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelbtn.setObjectName("cancelbtn")
        self.cancelbtn.setStyleSheet("background-color: rgb(236, 230, 230);"
"color: #B10303;"
"border: 1px solid #B10303;"
"border-radius: 4px;"
"padding: 7px;")

        self.gridLayout_4.addWidget(self.cancelbtn, 0, 1, 1, 1)

        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName("widget_22")

        self.gridLayout_4.addWidget(self.widget_22, 0, 0, 1, 1)

        self.widget_23 = QWidget(self.widget_20)
        self.widget_23.setObjectName("widget_23")

        self.gridLayout_4.addWidget(self.widget_23, 0, 2, 1, 1)


        self.horizontalLayout_6.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.widget_11)
        self.widget_21.setObjectName("widget_21")
        self.gridLayout_5 = QGridLayout(self.widget_21)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget_24 = QWidget(self.widget_21)
        self.widget_24.setObjectName("widget_24")

        self.gridLayout_5.addWidget(self.widget_24, 0, 0, 1, 1)

        self.addbtn = QPushButton(self.widget_21)
        self.addbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addbtn.setObjectName("addbtn")
        self.addbtn.setStyleSheet("background-color: #B10303;"
"color: white;"
"border: 1px solid #B10303;"
"border-radius: 4px;"
"padding: 7px;")

        self.gridLayout_5.addWidget(self.addbtn, 0, 1, 1, 1)

        self.widget_25 = QWidget(self.widget_21)
        self.widget_25.setObjectName("widget_25")

        self.gridLayout_5.addWidget(self.widget_25, 0, 2, 1, 1)


        self.horizontalLayout_6.addWidget(self.widget_21)


        self.verticalLayout.addWidget(self.widget_11)


        self.gridLayout_3.addWidget(self.widget_2, 1, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 8)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(Dialog)
        
        self.addbtn.clicked.connect(self.add_employee)
        self.cancelbtn.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
        
        
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", "Add Staff", None))
        self.fnamelabel.setText(QCoreApplication.translate("Dialog", "First Name", None))
        self.lnamelabel.setText(QCoreApplication.translate("Dialog", "Last Name", None))
        self.phonelabel.setText(QCoreApplication.translate("Dialog", "Phone", None))
        self.emaillabel.setText(QCoreApplication.translate("Dialog", "Email", None))
        self.addresslabel.setText(QCoreApplication.translate("Dialog", "Address", None))
        self.pinlabel_2.setText(QCoreApplication.translate("Dialog", "PIN", None))
        self.hdlabel.setText(QCoreApplication.translate("Dialog", "Hire Date", None))
        self.cancelbtn.setText(QCoreApplication.translate("Dialog", "Cancel", None))
        self.addbtn.setText(QCoreApplication.translate("Dialog", "Add", None))
    # retranslateUi

    
    
    def add_employee(self):
        if not self.fnameinput.text():
            QMessageBox.warning(self, "Validation Error", "First Name is required.")
            return
        if not self.lnameinput.text():
            QMessageBox.warning(self, "Validation Error", "Last Name is required.")
            return
        if not self.phoneinput.hasAcceptableInput():
            QMessageBox.warning(self, "Validation Error", "Phone number is not valid.")
            return
        if not self.emailinput.hasAcceptableInput():
            QMessageBox.warning(self, "Validation Error", "Email is not valid.")
            return
        if not self.addressinput.text():
            QMessageBox.warning(self, "Validation Error", "Address is required.")
            return
        if not self.pininput.text():
            QMessageBox.warning(self, "Validation Error", "PIN is required.")
            return
            
            
        # Collect data from the input fields
        fname = self.fnameinput.text()
        lname = self.lnameinput.text()
        phone = self.phoneinput.text()
        email = self.emailinput.text()
        hire_date = self.dhinput.date().toString("yyyy-MM-dd")
        address = self.addressinput.text()
        pin = self.pininput.text()

        # Connect to the PostgreSQL database
        try:
            conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
            cursor = conn.cursor()
            
            # Insert data into the employees table
            insert_query = """
                INSERT INTO employees (first_name, last_name, phone, email, hire_date, address, emp_pin)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (fname, lname, phone, email, hire_date, address, pin))
            conn.commit()

            cursor.close()
            conn.close()

            # Show a message box with success
            QMessageBox.information(None, "Success", "Staff added successfully!")
            self.staff_add.emit()
            self.dialog.close()

        except Exception as e:
            QMessageBox.critical(None, "Database Error", f"Error: {str(e)}")
    