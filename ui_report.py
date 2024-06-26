# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reportaZQdNp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import datetime
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import psycopg2


conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
cursor = conn.cursor()

class ReportWindow(object):
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
        self.pushButton.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_2 = QGridLayout(self.widget_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.staffbtn = QPushButton(self.widget_4)
        self.staffbtn.setObjectName(u"staffbtn")
        self.staffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.staffbtn.setStyleSheet(u"#staffbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"#staffbtn:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")

        self.gridLayout_2.addWidget(self.staffbtn, 0, 0, 1, 1)

        self.schedbtn = QPushButton(self.widget_4)
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
        self.reportbtn.setObjectName(u"reportbtn")
        self.reportbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reportbtn.setStyleSheet(u"#reportbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"background-color: #B10303;\n"
"}\n"
"\n"
"#reportbtn:hover{\n"
"	color: black;\n"
"}")

        self.gridLayout_2.addWidget(self.reportbtn, 2, 0, 1, 1)


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
        self.widget_12 = QWidget(self.widget_7)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget_12)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_3)


        self.horizontalLayout_3.addWidget(self.widget_12)

        self.horizontalLayout_3.setStretch(0, 2)

        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_10 = QWidget(self.widget_9)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.widget_10)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_3 = QVBoxLayout(self.widget_23)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_23)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.widget_13)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_4)


        self.verticalLayout_3.addWidget(self.widget_13)

        self.widget_16 = QWidget(self.widget_23)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_5 = QLabel(self.widget_16)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_5)


        self.verticalLayout_3.addWidget(self.widget_16)


        self.horizontalLayout_7.addWidget(self.widget_23)

        self.widget_22 = QWidget(self.widget_10)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_4 = QVBoxLayout(self.widget_22)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.widget_22)
        self.widget_24.setObjectName(u"widget_24")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.startdate = QDateEdit(self.widget_24)
        self.startdate.setObjectName(u"startdate")
        self.startdate.setDisplayFormat("MM/dd/yyyy")  
        self.startdate.setDate(datetime.date.today())
        self.startdate.setDate(self.startdate.date().addDays(-7))
        self.startdate.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;")

        self.horizontalLayout_15.addWidget(self.startdate)


        self.verticalLayout_4.addWidget(self.widget_24)

        self.widget_17 = QWidget(self.widget_22)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.regularrate = QLineEdit(self.widget_17)
        self.regularrate.setObjectName(u"regularrate")
        self.regularrate.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;")

        self.horizontalLayout_16.addWidget(self.regularrate)


        self.verticalLayout_4.addWidget(self.widget_17)


        self.horizontalLayout_7.addWidget(self.widget_22)


        self.horizontalLayout_2.addWidget(self.widget_10)

        self.widget_14 = QWidget(self.widget_9)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_19 = QWidget(self.widget_14)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget_18 = QWidget(self.widget_19)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_5 = QVBoxLayout(self.widget_18)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_26 = QWidget(self.widget_18)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.widget_26)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.label_6)


        self.verticalLayout_5.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.widget_18)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_17 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_7 = QLabel(self.widget_27)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label_7)


        self.verticalLayout_5.addWidget(self.widget_27)


        self.horizontalLayout_10.addWidget(self.widget_18)

        self.widget_25 = QWidget(self.widget_19)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_6 = QVBoxLayout(self.widget_25)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_28 = QWidget(self.widget_25)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.enddate = QDateEdit(self.widget_28)
        self.enddate.setObjectName(u"enddate")
        self.enddate.setDisplayFormat("MM/dd/yyyy")
        self.enddate.setDate(datetime.date.today())
        
        self.enddate.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;")

        self.horizontalLayout_19.addWidget(self.enddate)


        self.verticalLayout_6.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_25)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.overtimerate = QLineEdit(self.widget_29)
        self.overtimerate.setObjectName(u"overtimerate")
        self.overtimerate.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;")

        self.horizontalLayout_18.addWidget(self.overtimerate)


        self.verticalLayout_6.addWidget(self.widget_29)


        self.horizontalLayout_10.addWidget(self.widget_25)


        self.horizontalLayout_5.addWidget(self.widget_19)


        self.horizontalLayout_2.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.widget_9)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.widget_15)

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_20 = QWidget(self.widget_11)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.searchinput = QLineEdit(self.widget_20)
        self.searchinput.setObjectName(u"searchinput")
        self.searchinput.setPlaceholderText("Search name...")
        self.searchinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;")

        self.horizontalLayout_14.addWidget(self.searchinput)


        self.horizontalLayout_12.addWidget(self.widget_20)

        self.widget_21 = QWidget(self.widget_11)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.searchbtn = QPushButton(self.widget_21)
        self.searchbtn.setObjectName(u"searchbtn")
        self.searchbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchbtn.setStyleSheet(u"#searchbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"}\n"
"\n"
"#searchbtn:hover{\n"
"	color: black;\n"
"}")

        self.horizontalLayout_13.addWidget(self.searchbtn)


        self.horizontalLayout_12.addWidget(self.widget_21)

        self.horizontalLayout_12.setStretch(0, 3)
        self.horizontalLayout_12.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.widget_11)

        self.horizontalLayout_2.setStretch(0, 0)
        self.horizontalLayout_2.setStretch(1, 0)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 6)

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

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 10)

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        

        QMetaObject.connectSlotsByName(MainWindow)
        
        self.searchbtn.clicked.connect(self.load_payroll)
        
        self.load_data()
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.staffbtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.schedbtn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.reportbtn.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Insurgents Payroll", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start Date", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Regular Rate/Hr", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"End Date", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Overtime Rate/Hr", None))
        self.searchbtn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
    
    
    def load_data(self):
        # Retrieve data from the employees table including the staff ID
        cursor.execute("""
                       SELECT
        employees.employee_id,
        employees.first_name, employees.last_name,
        SUM(CASE 
                WHEN seconds > 0 THEN
                        CASE 
                        WHEN (seconds / 3600) > 8 THEN 8 
                        ELSE seconds / 3600
                        END
                ELSE 0
                END) AS conditioned_seconds_sum,
        ROUND(SUM(GREATEST(seconds - 28800, 0) / 3600.0), 2) AS hours_over_28800
        FROM
        shift
        INNER JOIN schedules ON shift.schedule_id = CAST(schedules.schedule_id AS INTEGER)
        INNER JOIN employees ON employees.employee_id = CAST(schedules.employee_id AS INTEGER)
        WHERE
        shift_date BETWEEN '2024-06-17' AND '2024-06-19'
        GROUP BY
        employees.employee_id,
        employees.first_name,
        employees.last_name;
                       """)
        self.rows = cursor.fetchall()
        
        

        self.tableWidget.setColumnCount(8)  # Set the number of columns including the hidden ID column
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Regular Hrs Worked', 'Overtime Hrs Worked', 'Regular Pay', 'Overtime Pay', 'Total Pay'])
        

        

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        # Hide the ID column
        self.tableWidget.setColumnHidden(0, True)

        # Close the connection
        
        
   
    def load_payroll(self):
            
        if not self.regularrate.text():
            QMessageBox.warning(None, "Validation Error", "Regular rate per hour is required.")
            return
        if not self.overtimerate.text():
            QMessageBox.warning(None, "Validation Error", "Overtime rate per hour is required.")
            return
    
        start_date_obj = datetime.datetime.strptime(self.startdate.text(), "%m/%d/%Y")
        end_date_obj = datetime.datetime.strptime(self.enddate.text(), "%m/%d/%Y")
        
        regular_rate = self.regularrate.text()
        overtime_rate = self.overtimerate.text()
        name_input = self.searchinput.text().lower()
        end_date = end_date_obj.strftime("%Y-%m-%d")
        start_date = start_date_obj.strftime("%Y-%m-%d")

        
        
        if name_input == "":
                # Retrieve data from the employees table including the staff ID
                cursor.execute("""
                        SELECT
                employees.employee_id,
                employees.first_name, employees.last_name,
                SUM(CASE 
                        WHEN seconds > 0 THEN
                                CASE 
                                WHEN (seconds / 3600) > 8 THEN 8 
                                ELSE seconds / 3600
                                END
                        ELSE 0
                        END) AS conditioned_seconds_sum,
                SUM(GREATEST(seconds - 28800, 0) / 3600) AS hours_over_28800
                FROM
                shift
                INNER JOIN schedules ON shift.schedule_id = CAST(schedules.schedule_id AS INTEGER)
                INNER JOIN employees ON employees.employee_id = CAST(schedules.employee_id AS INTEGER)
                WHERE
                shift_date BETWEEN %s AND %s
                GROUP BY
                employees.employee_id,
                employees.first_name,
                employees.last_name;
                        """, (start_date, end_date))
                self.rows = cursor.fetchall()
        else:
                cursor.execute("""
                               
                               SELECT
                    employees.employee_id,
                    employees.first_name, employees.last_name,
                    SUM(CASE 
                            WHEN seconds > 0 THEN
                                CASE 
                                    WHEN (seconds / 3600) > 8 THEN 8 
                                    ELSE seconds / 3600
                                END
                            ELSE 0
                        END) AS conditioned_seconds_sum,
                    SUM(GREATEST(seconds - 28800, 0) / 3600) AS hours_over_28800
                FROM
                    shift
                    INNER JOIN schedules ON shift.schedule_id = CAST(schedules.schedule_id AS INTEGER)
                    INNER JOIN employees ON employees.employee_id = CAST(schedules.employee_id AS INTEGER)
                WHERE
                    (shift_date BETWEEN %s AND %s) AND 
                    (lower(first_name) LIKE %s OR lower(last_name) LIKE %s)
                GROUP BY
                    employees.employee_id,
                    employees.first_name,
                    employees.last_name;

                               
                               """, (start_date, end_date,'%'+name_input+'%', '%'+name_input+'%'))
                self.rows = cursor.fetchall()
        
        self.tableWidget.setRowCount(len(self.rows))  # Set the number of rows
            
        from decimal import Decimal  # Import Decimal from decimal module

        # Inside your load_payroll function
        for row_idx, row_data in enumerate(self.rows):
                regular_hours = row_data[3]  # Assuming regular hours are at index 3
                overtime_hours = row_data[4]  # Assuming overtime hours are at index 4
                
                # Convert Decimal objects to float or Decimal (whichever is appropriate for your use case)
                regular_hours = Decimal(regular_hours)
                overtime_hours = Decimal(overtime_hours)
                
                # Convert regular_rate to Decimal if necessary
                regular_rate = Decimal(self.regularrate.text())
                overtime_rate = Decimal(self.overtimerate.text())
                
                # Calculate regular salary and overtime salary
                regular_salary = regular_rate * regular_hours
                overtime_salary = overtime_rate * overtime_hours
                
                # Calculate total salary
                total_salary = regular_salary + overtime_salary
                
                # Set the salary values in the respective columns
                regular_salary_item = QTableWidgetItem(str(round(regular_salary, 2)))
                regular_salary_item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(row_idx, 5, regular_salary_item)  # Regular Salary
                
                overtime_salary_item = QTableWidgetItem(str(round(overtime_salary, 2)))
                overtime_salary_item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(row_idx, 6, overtime_salary_item)  # Overtime Salary
                
                total_salary_item = QTableWidgetItem(str(round(total_salary, 2)))
                total_salary_item.setTextAlignment(Qt.AlignCenter)
                self.tableWidget.setItem(row_idx, 7, total_salary_item)  # Total Salary
                
                # Set the other data (employee ID, names, etc.)
                for col_idx, col_data in enumerate(row_data):
                        if isinstance(col_data, datetime.date):
                                col_data = col_data.strftime('%Y-%m-%d')  # Convert the date to string
                        item = QTableWidgetItem(str(col_data))
                        item.setTextAlignment(Qt.AlignCenter)
                        self.tableWidget.setItem(row_idx, col_idx, item)


        # cursor.close()
        # conn.close()