from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import psycopg2  # Import psycopg2 for PostgreSQL operations
import datetime
from PyQt5.uic import loadUi
from ui_addstaff import AddStaffDialog
from ui_deletestaffdialog import DeleteStaffDialog
from ui_updatestaff import UpdateStaffDialog


class StaffTab(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(QSize(1600, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(40, 38, 38);")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border: none;")
        icon = QIcon()
        icon.addFile(u"image/Logo1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(200, 200))

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.staffbtn = QPushButton(self.widget_4)
        self.staffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.staffbtn.setObjectName(u"staffbtn")
        self.staffbtn.setStyleSheet(u"#staffbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"background-color: #B10303;\n"
"}\n"
"\n"
"#staffbtn:hover{\n"
"	color: black;\n"
"}")

        self.gridLayout_2.addWidget(self.staffbtn, 0, 0, 1, 1)

        self.schedbtn = QPushButton(self.widget_4)
        self.schedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.schedbtn.setObjectName(u"schedbtn")
        self.schedbtn.setStyleSheet(u"#schedbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"#schedbtn:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")

        self.gridLayout_2.addWidget(self.schedbtn, 1, 0, 1, 1)

        self.reportbtn = QPushButton(self.widget_4)
        self.reportbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reportbtn.setObjectName(u"reportbtn")
        self.reportbtn.setStyleSheet(u"#reportbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"#reportbtn:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")

        self.gridLayout_2.addWidget(self.reportbtn, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout.addWidget(self.widget_5)

        self.widget_L2 = QWidget(self.widget)
        self.widget_L2.setObjectName(u"widget_L2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_L2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_L = QWidget(self.widget_L2)
        self.widget_L.setObjectName(u"widget_L")

        self.verticalLayout_3.addWidget(self.widget_L)

        self.widget_L1 = QWidget(self.widget_L2)
        self.widget_L1.setObjectName(u"widget_L1")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_L1)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.logoutbtn = QPushButton(self.widget_L1)
        self.logoutbtn.setObjectName(u"logoutbtn")
        self.logoutbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutbtn.setStyleSheet(u"#logoutbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"#logoutbtn:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")

        self.horizontalLayout_7.addWidget(self.logoutbtn)


        self.verticalLayout_3.addWidget(self.widget_L1)


        self.verticalLayout.addWidget(self.widget_L2)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_13 = QWidget(self.widget_7)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.branchname = QWidget(self.widget_13)
        self.branchname.setObjectName(u"branchname")

        self.horizontalLayout_4.addWidget(self.branchname)


        self.horizontalLayout_3.addWidget(self.widget_13)

        self.widget_12 = QWidget(self.widget_7)
        self.widget_12.setObjectName(u"widget_12")

        self.horizontalLayout_3.addWidget(self.widget_12)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)

        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")

        self.horizontalLayout_2.addWidget(self.widget_10)

        self.widget_14 = QWidget(self.widget_9)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.deletestaffbtn = QPushButton(self.widget_14)
        self.deletestaffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletestaffbtn.setObjectName(u"deletestaffbtn")
        self.deletestaffbtn.setStyleSheet(u"#deletestaffbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"}\n"
"\n"
"#deletestaffbtn:hover{\n"
"	color: black;\n"
"}")

        self.horizontalLayout_5.addWidget(self.deletestaffbtn)


        self.horizontalLayout_2.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_9)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.updatestaffbtn = QPushButton(self.widget_15)
        self.updatestaffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updatestaffbtn.setObjectName(u"updatestaffbtn")
        self.updatestaffbtn.setStyleSheet(u"#updatestaffbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"}\n"
"\n"
"#updatestaffbtn:hover{\n"
"	color: black;\n"
"}")

        self.horizontalLayout_6.addWidget(self.updatestaffbtn)


        self.horizontalLayout_2.addWidget(self.widget_15)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_4 = QGridLayout(self.widget_11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.addstaffbtn = QPushButton(self.widget_11)
        self.addstaffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addstaffbtn.setObjectName(u"addstaffbtn")
        self.addstaffbtn.setStyleSheet(u"#addstaffbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"}\n"
"\n"
"#addstaffbtn:hover{\n"
"	color: black;\n"
"}")

        self.gridLayout_4.addWidget(self.addstaffbtn, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_11)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.table = QWidget(self.widget_8)
        self.table.setObjectName(u"table")
        self.table.setStyleSheet(u"")
        self.gridLayout_6 = QGridLayout(self.table)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget = QTableWidget(self.table)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_6.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.table, 0, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.widget_8)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 10)

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)
        
        
        # self.addstaffbtn.clicked.connect(self.open_add_staff_dialog)
        # self.updatestaffbtn.clicked.connect(self.open_update_staff_dialog)
        # self.deletestaffbtn.clicked.connect(self.open_delete_staff_dialog)
        

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Load data from the database
        self.load_data()

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.staffbtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.schedbtn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.reportbtn.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.logoutbtn.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.deletestaffbtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.updatestaffbtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.addstaffbtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))

    # retranslateUi

    def load_data(self):
        try:
            # Connect to the PostgreSQL database
            conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
            cursor = conn.cursor()

            # Retrieve data from the employees table including the staff ID
            cursor.execute('SELECT employee_id, first_name, last_name, address, hire_date, phone, email, emp_pin FROM employees')
            rows = cursor.fetchall()

            self.tableWidget.setColumnCount(8)  # Set the number of columns including the hidden ID column
            self.tableWidget.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Address', 'Hire Date', 'Phone', 'Email', 'PIN'])
            self.tableWidget.setRowCount(len(rows))  # Set the number of rows

            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data):
                    if isinstance(col_data, datetime.date):
                        col_data = col_data.strftime('%Y-%m-%d')  # Convert the date to string
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)
            # Hide the ID column
            self.tableWidget.setColumnHidden(0, True)

            # Close the connection
            cursor.close()
            conn.close()

        except Exception as e:
            print(f"Error loading data: {e}")  # Debug print



    # def open_add_staff_dialog(self):
    #     # Create an instance of the add staff dialog
    #     self.add_staff_dialog = QDialog()
    #     self.ui = AddStaffDialog()
    #     self.ui.setupUi(self.add_staff_dialog)


    #     # Show the dialog
    #     self.add_staff_dialog.show()
        
        
    
    # def open_delete_staff_dialog(self):
    #     selected_row = self.tableWidget.currentRow()
    #     if selected_row != -1:
    #         staff_id = self.tableWidget.item(selected_row, 0).text()  # Assuming ID is in the first column
    #         first_name = self.tableWidget.item(selected_row, 1).text()
    #         last_name = self.tableWidget.item(selected_row, 2).text()
            
            
    #         self.delete_staff_dialog = QDialog()
    #         self.ui = DeleteStaffDialog(self.delete_staff_dialog)
    #         self.ui.setupUi(self.delete_staff_dialog)
    #         self.ui.label.setText(f"Are you sure you want to delete {first_name} {last_name}?")
            
    #         self.ui.emp_id.setText(staff_id)
            
            
    #         self.delete_staff_dialog.exec_()
        
    # def open_update_staff_dialog(self):
    #     # Get the selected staff's information from the table
    #     selected_row = self.tableWidget.currentRow()
    #     if selected_row != -1:  # Ensure a row is selected
    #         staff_id = self.tableWidget.item(selected_row, 0).text()  # Assuming ID is in the first column
    #         first_name = self.tableWidget.item(selected_row, 1).text()
    #         last_name = self.tableWidget.item(selected_row, 2).text()
    #         address = self.tableWidget.item(selected_row, 3).text()
    #         hire_date = self.tableWidget.item(selected_row, 4).text()
    #         phone = self.tableWidget.item(selected_row, 5).text()
    #         email = self.tableWidget.item(selected_row, 6).text()
    #         emp_pin = self.tableWidget.item(selected_row, 7).text()

    #         # Create an instance of the update staff dialog
    #         self.update_staff_dialog = QDialog()
    #         self.ui = UpdateStaffDialog(staff_id, self.update_staff_dialog)
    #         self.ui.setupUi(self.update_staff_dialog)

    #         # Set the staff's information in the update staff dialog
    #         self.ui.fnameinput.setText(first_name)
    #         self.ui.lnameinput.setText(last_name)
    #         self.ui.addressinput.setText(address)
    #         self.ui.phoneinput.setText(phone)
    #         self.ui.emailinput.setText(email)
    #         self.ui.pinlabel.setText(emp_pin)
    #         self.ui.hdinput.setDate(QDate.fromString(hire_date, "yyyy-MM-dd"))

    #         # Connect any signals or slots as needed

    #         # Show the dialog
    #         self.update_staff_dialog.exec_()

        


# if __name__ == "__main__":
#     import sys

#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     ui = StaffTab()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
