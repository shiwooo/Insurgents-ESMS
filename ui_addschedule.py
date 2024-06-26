import datetime
import psycopg2
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *

from ui_addscheduledialog import AddScheduleDialog
from ui_editscheduledialog import EditSchedDialog


class AddStaffSchedule(QMainWindow):
    def __init__(self, stacked_widget, date, previous_index):
        super(AddStaffSchedule, self).__init__()
        self.stacked_widget = stacked_widget
        self.date = date
        self.previous_index = previous_index
        self.setupUi(self)

    
    
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1497, 849)
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
        self.backbtn = QPushButton(self.widget_4)
        self.backbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.backbtn.setObjectName(u"backbtn")
        self.backbtn.setStyleSheet(u"#backbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"background-color: #B10303;\n"
"}\n"
"\n"
"#backbtn:hover{\n"
"	color: black;\n"
"}")

        self.gridLayout_2.addWidget(self.backbtn, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")

        self.verticalLayout.addWidget(self.widget_6)


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
        self.updateschedbtn = QPushButton(self.widget_15)
        self.updateschedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateschedbtn.setObjectName(u"updateschedbtn")
        self.updateschedbtn.setStyleSheet(u"#updateschedbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"}\n"
"\n"
"#updateschedbtn:hover{\n"
"	color: black;\n"
"}")

        self.horizontalLayout_6.addWidget(self.updateschedbtn)


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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
        # self.updatestaffbtn.clicked.connect(self.open_update_dialog)
        
        self.backbtn.clicked.connect(self.go_back)
        self.load_data()
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.backbtn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.deletestaffbtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.updateschedbtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.addstaffbtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

    def go_back(self):
        self.stacked_widget.setCurrentIndex(self.previous_index)
    
    def load_data(self):
        print(self.date)
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
        cursor = conn.cursor()

        # Retrieve data from the employees table including the staff ID
        cursor.execute("""
            SELECT 
                employees.employee_id, 
                employees.first_name, 
                employees.last_name,
                COALESCE(schedules.start_time, NULL) AS start_time,
                COALESCE(schedules.end_time, NULL) AS end_time,
                COALESCE(schedules.status, NULL) AS status,
                schedules.schedule_id
            FROM 
                employees 
            LEFT JOIN 
                schedules 
            ON 
                employees.employee_id = schedules.employee_id 
            AND 
                schedules.shift_date = %s
            ORDER BY 
                CASE COALESCE(schedules.status, 'No Schedule') 
                    WHEN 'Regular' THEN 1
                    WHEN 'Reserve' THEN 2
                    WHEN 'Day off' THEN 3
                    ELSE 4
                END,
                schedules.start_time
        """, (self.date,))
        rows = cursor.fetchall()
        print(rows)
        self.tableWidget.setColumnCount(7)  # Set the number of columns including the hidden ID column
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Start Time', 'End Time', 'Status', 'Schedule ID'])
        self.tableWidget.setRowCount(len(rows))  # Set the number of rows

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                if col_idx == 3 or col_idx == 4:  # Start Time or End Time
                    if row_data[5] == 'Day off' or row_data[5] == 'Reserve' :  # Check if status is 'DAY OFF'
                        col_data = ''  # Set to empty string
                    elif isinstance(col_data, datetime.datetime):
                        col_data = col_data.strftime('%H:%M')  # Convert datetime to time string
                    elif isinstance(col_data, datetime.date):
                        col_data = col_data.strftime('%Y-%m-%d')  # Convert date to string
                item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(Qt.AlignCenter)  # Align text to center
                self.tableWidget.setItem(row_idx, col_idx, item)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        # Hide the ID column
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setColumnHidden(6, True)

        # Close the connection
        cursor.close()
        conn.close()
        
    # def open_update_dialog(self):
    #     self.edit_schedule_dialog = QDialog()
    #     self.ui = EditSchedDialog(self.edit_schedule_dialog)
    #     self.ui.setupUi(self.edit_schedule_dialog)
        
    #     self.ui.emp_id.setText(str(emp_id))
    #     self.ui.sched_id.setText(str(schedule_id))
    #     self.ui.dateinput.setText(date)
    #     self.ui.nameinput.setText(emp_name)
    #     # Ensure sTime and eTime are strings
    #     sTime = str(sTime)
    #     eTime = str(eTime)

    #     # Set sTime in the combobox
    #     sTimeIndex = self.ui.frominput.findText(sTime, Qt.MatchFixedString)
    #     if sTimeIndex >= 0:
    #         self.ui.frominput.setCurrentIndex(sTimeIndex)

    #     # Set eTime in the combobox
    #     eTimeIndex = self.ui.toinput.findText(eTime, Qt.MatchFixedString)
    #     if eTimeIndex >= 0:
    #         self.ui.toinput.setCurrentIndex(eTimeIndex)
            
    #     statusIndex = self.ui.comboBox.findText(status, Qt.MatchFixedString)
    #     if statusIndex >= 0:
    #         self.ui.comboBox.setCurrentIndex(statusIndex)
        
        
    #     self.edit_schedule_dialog.show()


    # def open_add_schedule_dialog(self, emp_id, emp_name, date):
        
        # Create an instance of the add staff dialog
        # self.add_schedule_dialog = QDialog()
        # self.ui = AddScheduleDialog(self.add_schedule_dialog)
        # self.ui.setupUi(self.add_schedule_dialog)

        # # Connect any signals or slots as needed
        # self.ui.nameinput.setText(emp_name)
        # self.ui.dateinput.setText(date)
        # self.ui.emp_id.setText(str(emp_id))

        # # Show the dialog
        # self.add_schedule_dialog.show()