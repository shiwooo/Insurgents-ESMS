# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'viewscheduleAuDRqT.ui'
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

class View_Schedule(QWidget):
    def __init__(self, stacked_widget):
        super(View_Schedule, self).__init__()
        self.stacked_widget = stacked_widget
        self.setupUi(self)
        self.load_data()  # Ensure data is loaded when the UI is initialized

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
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 250, 600, 300))
        self.label_3.setPixmap(QPixmap(u"../Insurgents ESMS/image/Logo1.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(199, 194, 194);")
        self.welcome = QLabel(self.widget_2)
        self.welcome.setObjectName(u"welcome")
        self.welcome.setGeometry(QRect(65, 75, 670, 80))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet(u"color: rgb(177, 3, 3);\n"
"font-size: 64px;")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(50, 260, 700, 500))
        self.tableWidget = QTableWidget(self.widget_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 140, 700, 360))
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 30, 90, 20))
        self.label.setStyleSheet(u"font-weight: bold;\n"
"font-size: 16px;")
        self.startdateinput = QDateEdit(self.widget_3)
        self.startdateinput.setObjectName(u"startdateinput")
        self.startdateinput.setGeometry(QRect(120, 20, 130, 40))
        self.startdateinput.setMaximumSize(QSize(120, 40))
        font1 = QFont()
        self.startdateinput.setFont(font1)
        current_date = QDate.currentDate()
        self.startdateinput.setDate(current_date)
        self.startdateinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"font-size: 14px;")
        self.enddateinput = QDateEdit(self.widget_3)
        self.enddateinput.setObjectName(u"enddateinput")
        self.enddateinput.setGeometry(QRect(120, 70, 130, 40))
        self.enddateinput.setMaximumSize(QSize(120, 40))
        end_date = current_date.addDays(7)
        self.enddateinput.setDate(end_date)
        self.enddateinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"font-size: 14px;")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 80, 50, 20))
        self.label_2.setStyleSheet(u"font-weight: bold;\n"
"font-size: 16px;")
        self.searchinput = QLineEdit(self.widget_3)
        self.searchinput.setObjectName(u"searchinput")
        self.searchinput.setGeometry(QRect(340, 45, 200, 40))
        self.searchinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"font-size: 14px;")
        self.searchbtn = QPushButton(self.widget_3)
        self.searchbtn.setObjectName(u"searchbtn")
        self.searchbtn.setGeometry(QRect(550, 45, 100, 40))
        self.searchbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchbtn.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(177, 3, 3);\n"
"   color: white;\n"
"   border-radius: 10px;\n"
"    padding: 10px 20px;\n"
"   font-size: 16px;\n"
"   font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(204, 0, 0); \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(139, 0, 0);\n"
"}")
        self.viewschedbtn = QPushButton(self.widget_2)
        self.viewschedbtn.setObjectName(u"viewschedbtn")
        self.viewschedbtn.setGeometry(QRect(400, 180, 170, 40))
        self.viewschedbtn.setFont(font1)
        self.viewschedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.viewschedbtn.setStyleSheet(u"#viewschedbtn{\n"
"	background-color: rgb(177, 3, 3);\n"
"	color: white;\n"
"	font-size: 20px;\n"
"	border-top-right-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"#viewschedbtn:hover{\n"
"	color: black;\n"
"}")
        self.loginstaffbtn = QPushButton(self.widget_2)
        self.loginstaffbtn.setObjectName(u"loginstaffbtn")
        self.loginstaffbtn.setGeometry(QRect(230, 180, 170, 40))
        self.loginstaffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginstaffbtn.setStyleSheet(u"#loginstaffbtn{\n"
"	background-color: #ECE6E6;\n"
"	border: 1px solid  #B10303;\n"
"	font-size: 20px;\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"#loginstaffbtn:hover{\n"
"	background-color: rgb(177, 3, 3);\n"
"	color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.widget_2)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.searchbtn.clicked.connect(self.search_staff)
        self.viewschedbtn.clicked.connect(self.load_data)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText("")
        self.welcome.setText(QCoreApplication.translate("Form", u"Upcoming Schedules", None))
        self.label.setText(QCoreApplication.translate("Form", u"From:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"To:", None))
        self.searchinput.setPlaceholderText(QCoreApplication.translate("Form", u"Search name...", None))
        self.searchbtn.setText(QCoreApplication.translate("Form", u"Search", None))
        self.viewschedbtn.setText(QCoreApplication.translate("Form", u"Staff Schedule", None))
        self.loginstaffbtn.setText(QCoreApplication.translate("Form", u"Admin Login", None))

    def load_data(self):
        try:
            start_date_obj = datetime.datetime.strptime(self.startdateinput.text(), "%d/%m/%Y")
            end_date_obj = datetime.datetime.strptime(self.enddateinput.text(), "%d/%m/%Y")

            start_date = start_date_obj.strftime("%Y-%m-%d")
            end_date = end_date_obj.strftime("%Y-%m-%d")

            cursor.execute("""
                SELECT e.employee_id, CONCAT(e.first_name, ' ', e.last_name) AS full_name, s.shift_date, s.start_time, s.end_time 
                FROM schedules s 
                NATURAL JOIN employees e 
                WHERE s.shift_date BETWEEN %s AND %s
            """, (start_date, end_date))

            rows = cursor.fetchall()
            print(f"Data fetched: {rows}")  # Debug print

            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(['ID', 'Name', 'Shift Date M/D/Y', 'Start Time', 'End Time'])
            self.tableWidget.setRowCount(len(rows))

            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data):
                    if isinstance(col_data, datetime.date):
                        col_data = col_data.strftime('%Y-%m-%d')
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.setColumnHidden(0, True)

        except Exception as e:
            print(f"Error loading data: {e}")  # Debug print

    def search_staff(self):
        try:
            start_date_obj = datetime.datetime.strptime(self.startdateinput.text(), "%d/%m/%Y")
            end_date_obj = datetime.datetime.strptime(self.enddateinput.text(), "%d/%m/%Y")

            start_date = start_date_obj.strftime("%Y-%m-%d")
            end_date = end_date_obj.strftime("%Y-%m-%d")
            searchinput = self.searchinput.text().lower()

            if searchinput == "":
                cursor.execute("""
                    SELECT e.employee_id, CONCAT(e.first_name, ' ', e.last_name) AS full_name, s.shift_date, s.start_time, s.end_time 
                    FROM schedules s 
                    NATURAL JOIN employees e 
                    WHERE s.shift_date BETWEEN %s AND %s
                """, (start_date, end_date))
            else:
                cursor.execute("""
                    SELECT e.employee_id, CONCAT(e.first_name, ' ', e.last_name) AS full_name, s.shift_date, s.start_time, s.end_time 
                    FROM schedules s 
                    NATURAL JOIN employees e 
                    WHERE (s.shift_date BETWEEN %s AND %s) AND (LOWER(e.first_name) LIKE %s OR LOWER(e.last_name) LIKE %s)
                """, (start_date, end_date, f'%{searchinput}%', f'%{searchinput}%'))

            rows = cursor.fetchall()
            print(f"Data fetched: {rows}")  # Debug print

            self.tableWidget.setColumnCount(5)
            self.tableWidget.setHorizontalHeaderLabels(['ID', 'Name', 'Shift Date M/D/Y', 'Start Time', 'End Time'])
            self.tableWidget.setRowCount(len(rows))

            for row_idx, row_data in enumerate(rows):
                for col_idx, col_data in enumerate(row_data):
                    if isinstance(col_data, datetime.date):
                        col_data = col_data.strftime('%m-%d-%Y')
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.setColumnHidden(0, True)

        except Exception as e:
            print(f"Error searching data: {e}")  # Debug print

