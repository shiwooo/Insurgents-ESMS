# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedule1mMSQze.ui'
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


class ScheduleTab(object):
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
        self.schedbtn = QPushButton(self.widget_4)
        self.schedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.schedbtn.setObjectName(u"schedbtn")
        self.schedbtn.setStyleSheet(u"#schedbtn{\n"
"background-color: #B10303;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 40px;\n"
"padding: 7px;\n"
"color: white;\n"
"}")

        self.gridLayout_2.addWidget(self.schedbtn, 1, 0, 1, 1)

        self.staffbtn = QPushButton(self.widget_4)
        self.staffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.staffbtn.setObjectName(u"staffbtn")
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

        self.widget_11 = QWidget(self.widget_9)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_4 = QGridLayout(self.widget_11)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.addschedbtn = QPushButton(self.widget_11)
        self.addschedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addschedbtn.setObjectName(u"addschedbtn")
        self.addschedbtn.setStyleSheet(u"#addschedbtn{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"margin: 0 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"}\n"
"\n"
"#addschedbtn:hover{\n"
"	color: black;\n"
"}")

        self.gridLayout_4.addWidget(self.addschedbtn, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.widget_11)

        self.horizontalLayout_2.setStretch(0, 9)
        self.horizontalLayout_2.setStretch(1, 1)

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
        self.calendarWidget = QCalendarWidget(self.table)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setStyleSheet(u"/* Calendar Widget General */\n"
"QCalendarWidget {\n"
"    background-color: #ffffff;  /* Background color of the entire calendar widget */\n"
"    border: 1px solid #a1a1a1;  /* Border of the calendar widget */\n"
"    font-family: 'Arial', sans-serif;  /* Font family for the calendar text */\n"
"    font-size: 12px;  /* Font size for the calendar text */\n"
"    color: #333333;  /* Text color */\n"
"}\n"
"\n"
"/* Navigation Bar */\n"
"QCalendarWidget QToolButton {\n"
"    height: 30px;  /* Height of the navigation buttons */\n"
"    width: 100px;  /* Width of the navigation buttons */\n"
"    color: #ffffff;  /* Text color of the navigation buttons */\n"
"    background-color: #4a90e2;  /* Background color of the navigation buttons */\n"
"    border: none;  /* Remove border of the navigation buttons */\n"
"    margin: 10px;  /* Margin around the navigation buttons */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton::hover {\n"
"    background-color: #357ab8;  /* Background color of the navigation buttons on hover"
                        " */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_prevmonth {\n"
"    qproperty-icon: url(left_arrow.png);  /* Path to your left arrow icon */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton#qt_calendar_nextmonth {\n"
"    qproperty-icon: url(right_arrow.png);  /* Path to your right arrow icon */\n"
"}\n"
"\n"
"/* Header Section (Month and Year) */\n"
"QCalendarWidget QSpinBox {\n"
"    width: 80px;  /* Width of the month/year selector */\n"
"    color: #ffffff;  /* Text color of the month/year selector */\n"
"    background-color: #4a90e2;  /* Background color of the month/year selector */\n"
"    border: none;  /* Remove border of the month/year selector */\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-button {\n"
"    subcontrol-origin: border;  /* Origin of the up button control */\n"
"    subcontrol-position: top right;  /* Position of the up button control */\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::down-button {\n"
"    subcontrol-origin: border;  /* Origin of the down button control */\n"
"    subcon"
                        "trol-position: bottom right;  /* Position of the down button control */\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::up-arrow {\n"
"    width: 10px;  /* Width of the up arrow */\n"
"    height: 10px;  /* Height of the up arrow */\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox::down-arrow {\n"
"    width: 10px;  /* Width of the down arrow */\n"
"    height: 10px;  /* Height of the down arrow */\n"
"}\n"
"\n"
"/* Weekdays Section */\n"
"QCalendarWidget QTableView {\n"
"    alternate-background-color: #f2f2f2;  /* Alternate row background color */\n"
"}\n"
"\n"
"QCalendarWidget QTableView QHeaderView::section {\n"
"    background-color: #4a90e2;  /* Background color of the weekdays header */\n"
"    color: #ffffff;  /* Text color of the weekdays header */\n"
"    padding: 5px;  /* Padding for the weekdays header */\n"
"    border: none;  /* Remove border of the weekdays header */\n"
"}\n"
"\n"
"/* Days Section */\n"
"QCalendarWidget QTableView::item {\n"
"    background-color: #ffffff;  /* Background color of the day cells "
                        "*/\n"
"    color: #333333;  /* Text color of the day cells */\n"
"    border: none;  /* Remove border of the day cells */\n"
"}\n"
"\n"
"QCalendarWidget QTableView::item:selected {\n"
"    background-color: #4a90e2;  /* Background color of the selected day cell */\n"
"    color: #ffffff;  /* Text color of the selected day cell */\n"
"}\n"
"\n"
"QCalendarWidget QTableView::item:disabled {\n"
"    color: #cccccc;  /* Text color of the disabled day cells */\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #4a90e2;  /* Background color of the navigation bar */\n"
"}\n"
"\n"
"QCalendarWidget QTableView::item:hover {\n"
"    background-color: #357ab8;  /* Background color of the day cells on hover */\n"
"    color: #ffffff;  /* Text color of the day cells on hover */\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.calendarWidget, 0, 0, 1, 1)


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
        self.printSelectedDate()
        
        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.schedbtn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.staffbtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.reportbtn.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.addschedbtn.setText(QCoreApplication.translate("MainWindow", u"Add Schedule", None))
    # retranslateUi
    
    def printSelectedDate(self):
        self.selected_date = self.calendarWidget.selectedDate().toString(Qt.ISODate)
        print(f"Selected date: {self.selected_date}")
        return self.selected_date

