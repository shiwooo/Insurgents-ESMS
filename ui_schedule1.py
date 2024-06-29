from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QDate)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class ScheduleTab(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 800)
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
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.logo = QLabel(self.widget_3)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(200, 100))
        self.logo.setPixmap(QPixmap(u"../Insurgents ESMS/image/Logo1.png"))
        self.logo.setScaledContents(True)

        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.schedbtn = QPushButton(self.widget_4)
        self.schedbtn.setObjectName(u"schedbtn")
        self.schedbtn.setGeometry(QRect(43, 81, 181, 32))
        self.schedbtn.setStyleSheet(u"QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background-color: #B10303;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: black;\n"
"}")
        self.staffbtn = QPushButton(self.widget_4)
        self.staffbtn.setObjectName(u"staffbtn")
        self.staffbtn.setGeometry(QRect(43, 26, 181, 32))
        self.staffbtn.setStyleSheet(u"QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")
        self.reportbtn = QPushButton(self.widget_4)
        self.reportbtn.setObjectName(u"reportbtn")
        self.reportbtn.setGeometry(QRect(43, 136, 181, 32))
        self.reportbtn.setStyleSheet(u"QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")

        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.logoutbtn = QPushButton(self.widget_6)
        self.logoutbtn.setObjectName(u"logoutbtn")
        self.logoutbtn.setGeometry(QRect(68, 130, 131, 32))
        self.logoutbtn.setStyleSheet(u"QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #B10303;\n"
"	color: black;\n"
"}")

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
        self.addschedbtn = QPushButton(self.widget_7)
        self.addschedbtn.setObjectName(u"addschedbtn")
        self.addschedbtn.setGeometry(QRect(1120, 50, 175, 40))
        self.addschedbtn.setStyleSheet(u"QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.calendarWidget = QCalendarWidget(self.widget_8)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(16, 16, 1301, 664))
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
"    height: 50px;  /* Height of the navigation buttons */\n"
"    width: 100px;  /* Width of the navigation buttons */\n"
"    color: #ffffff;  /* Text color of the navigation buttons */\n"
"    background-color: #b10303;  /* Background color of the navigation buttons */\n"
"    border: none;  /* Remove border of the navigation buttons */\n"
"    margin: 10px;  /* Margin around the navigation buttons */\n"
"}\n"
"\n"
"QCalendarWidget QToolButton:hover {\n"
"    background-color: #870202;  /* Background color of the navigation buttons on hover "
                        "*/\n"
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
"    background-color: #b10303;  /* Background color of the month/year selector */\n"
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
"    subcont"
                        "rol-position: bottom right;  /* Position of the down button control */\n"
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
"    background-color: #b10303;  /* Background color of the weekdays header */\n"
"    color: #ffffff;  /* Text color of the weekdays header */\n"
"    padding: 5px;  /* Padding for the weekdays header */\n"
"    border: none;  /* Remove border of the weekdays header */\n"
"}\n"
"\n"
"/* Days Section */\n"
"QCalendarWidget QTableView::item {\n"
"    background-color: #ffffff;  /* Background color of the day cells *"
                        "/\n"
"    color: #333333;  /* Text color of the day cells */\n"
"    border: none;  /* Remove border of the day cells */\n"
"}\n"
"\n"
"QCalendarWidget QTableView::item:selected {\n"
"    background-color: #b10303;  /* Background color of the selected day cell */\n"
"    color: #ffffff;  /* Text color of the selected day cell */\n"
"}\n"
"\n"
"QCalendarWidget QTableView::item:disabled {\n"
"    color: #cccccc;  /* Text color of the disabled day cells */\n"
"}\n"
"\n"
"QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"    background-color: #b10303;  /* Background color of the navigation bar */\n"
"}\n"
"\n"
"QCalendarWidget QTableView::item:hover {\n"
"    background-color: #870202;  /* Background color of the day cells on hover */\n"
"    color: #ffffff;  /* Text color of the day cells on hover */\n"
"}\n"
"")
        self.calendarWidget.setMinimumDate(QDate.currentDate())

        self.verticalLayout_2.addWidget(self.widget_8)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 7)

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
        self.logo.setText("")
        self.schedbtn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.staffbtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.reportbtn.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.logoutbtn.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.addschedbtn.setText(QCoreApplication.translate("MainWindow", u"Assign Schedule", None))
    # retranslateUi
    
    def printSelectedDate(self):
        self.selected_date = self.calendarWidget.selectedDate().toString(Qt.ISODate)
        print(f"Selected date: {self.selected_date}")
        return self.selected_date

