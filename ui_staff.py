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
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(40, 38, 38);")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.logo = QLabel(self.widget_3)
        self.logo.setObjectName("logo")
        self.logo.setMaximumSize(QSize(200, 100))
        self.logo.setPixmap(QPixmap("../Insurgents ESMS/image/Logo1.png"))
        self.logo.setScaledContents(True)

        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.widget_4.setStyleSheet("")
        self.staffbtn = QPushButton(self.widget_4)
        self.staffbtn.setObjectName("staffbtn")
        self.staffbtn.setGeometry(QRect(43, 26, 181, 32))
        self.staffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.staffbtn.setStyleSheet("QPushButton{"
"border: 1px solid white;"
"border-radius: 5px;"
"color: white;"
"background-color: #B10303;"
"}"
""
"QPushButton:hover{"
"	color: black;"
"}")
        self.schedbtn = QPushButton(self.widget_4)
        self.schedbtn.setObjectName("schedbtn")
        self.schedbtn.setGeometry(QRect(43, 81, 181, 32))
        self.schedbtn.setStyleSheet("#schedbtn{"
"border: 1px solid white;"
"border-radius: 5px;"
"color: white;"
"}"
""
"#schedbtn:hover{"
"	background-color: #B10303;"
"	color: black;"
"}")
        self.reportbtn = QPushButton(self.widget_4)
        self.reportbtn.setObjectName("reportbtn")
        self.reportbtn.setGeometry(QRect(43, 136, 181, 32))
        self.reportbtn.setStyleSheet("QPushButton{"
"border: 1px solid white;"
"border-radius: 5px;"
"padding: 7px;"
"color: white;"
"}"
""
"QPushButton:hover{"
"	background-color: #B10303;"
"	color: black;"
"}")

        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.verticalLayout.addWidget(self.widget_5)

        self.widget_L2 = QWidget(self.widget)
        self.widget_L2.setObjectName("widget_L2")
        self.widget_L2.setStyleSheet("")
        self.logoutbtn = QPushButton(self.widget_L2)
        self.logoutbtn.setObjectName("logoutbtn")
        self.logoutbtn.setGeometry(QRect(68, 130, 131, 32))
        self.logoutbtn.setMaximumSize(QSize(2313123, 16777215))
        self.logoutbtn.setStyleSheet("#logoutbtn{"
"border: 1px solid white;"
"border-radius: 5px;"
"padding: 7px;"
"color: white;"
"}"
""
"#logoutbtn:hover{"
"	background-color: #B10303;"
"	color: black;"
"}")

        self.verticalLayout.addWidget(self.widget_L2)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("background-color: rgb(236, 230, 230);")
        self.verticalLayout_2 = QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName("widget_9")
        self.widget_9.setStyleSheet("background-color: rgb(236, 230, 230);")
        self.addstaffbtn = QPushButton(self.widget_9)
        self.addstaffbtn.setObjectName("addstaffbtn")
        self.addstaffbtn.setGeometry(QRect(720, 50, 175, 40))
        self.addstaffbtn.setStyleSheet("QPushButton{"
"border: 1px solid white;"
"border-radius: 5px;"
"background-color: #B10303;"
"color: white;"
"}"
""
"QPushButton:hover{"
"	color: black;"
"}")
        self.updatestaffbtn = QPushButton(self.widget_9)
        self.updatestaffbtn.setObjectName("updatestaffbtn")
        self.updatestaffbtn.setGeometry(QRect(920, 50, 175, 40))
        self.updatestaffbtn.setStyleSheet("QPushButton{"
"border: 1px solid white;"
"border-radius: 5px;"
"padding: 7px;"
"background-color: #B10303;"
"color: white;"
"}"
""
"QPushButton:hover{"
"	color: black;"
"}")
        self.deletestaffbtn = QPushButton(self.widget_9)
        self.deletestaffbtn.setObjectName("deletestaffbtn")
        self.deletestaffbtn.setGeometry(QRect(1120, 50, 175, 40))
        self.deletestaffbtn.setStyleSheet("QPushButton{"
"border: 1px solid white;"
"border-radius: 5px;"
"padding: 7px;"
"background-color: #B10303;"
"color: white;"
"}"
""
"QPushButton:hover{"
"	color: black;"
"}")

        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName("widget_8")
        self.widget_8.setStyleSheet("")
        self.tableWidget = QTableWidget(self.widget_8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QRect(16, 16, 1301, 664))

        self.verticalLayout_2.addWidget(self.widget_8)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 7)

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.load_data()
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "MainWindow", None))
        self.logo.setText("")
        self.staffbtn.setText(QCoreApplication.translate("MainWindow", "Staff", None))
        self.schedbtn.setText(QCoreApplication.translate("MainWindow", "Schedule", None))
        self.reportbtn.setText(QCoreApplication.translate("MainWindow", "Report", None))
        self.logoutbtn.setText(QCoreApplication.translate("MainWindow", "LOGOUT", None))
        self.addstaffbtn.setText(QCoreApplication.translate("MainWindow", "Add Staff", None))
        self.updatestaffbtn.setText(QCoreApplication.translate("MainWindow", "Update Info", None))
        self.deletestaffbtn.setText(QCoreApplication.translate("MainWindow", "Delete Staff", None))
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

