# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'staffdetailFCfQEb.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import datetime
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import psycopg2


class Staff_Details(object):
    def __init__(self, emp_id, dialog):
        super(Staff_Details, self).__init__()
        self.emp_id = emp_id  
        self.dialog = dialog 
    
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(500, 700)
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QSize(500, 700))
        self.widget.setMaximumSize(QSize(500, 700))
        self.widget.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 220, 481, 471))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 40, 251, 41))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.name = QLabel(self.widget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(10, 160, 200, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.name.setFont(font1)

        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
        
        self.load_data()
        
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Staff Schedule Details", None))
        self.name.setText("")
    # retranslateUi
    
    
    def load_data(self):
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
        cursor = conn.cursor()

        # Retrieve data from the employees table including the staff ID
        cursor.execute('SELECT shift_date, status, start_time, end_time FROM schedules WHERE employee_id = %s', (self.emp_id,))
        rows = cursor.fetchall()

        self.tableWidget.setColumnCount(4)  # Set the number of columns including the hidden ID column
        self.tableWidget.setHorizontalHeaderLabels(['Schedule Date', 'Status', 'Start Time', 'End Time'])
        self.tableWidget.setRowCount(len(rows))  # Set the number of rows

        for row_idx, row_data in enumerate(rows):
            for col_idx, col_data in enumerate(row_data):
                if col_idx == 0 and isinstance(col_data, datetime.date):
                    col_data = col_data.strftime('%Y-%m-%d')  # Convert the date to string
                    self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                elif col_idx == 1:
                    self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                    if col_data in ('Reserve', 'Day off'):
                        self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(''))  # Set Start Time to blank
                        self.tableWidget.setItem(row_idx, 3, QTableWidgetItem(''))  # Set End Time to blank
                else:
                    if row_data[1] not in ('Reserve', 'Day off'):
                        self.tableWidget.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        # Close the connection
        cursor.close()
        conn.close()

