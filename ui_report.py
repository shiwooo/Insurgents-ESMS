import datetime
from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt, QDate
from PyQt5.QtGui import  QCursor,  QPixmap, QDoubleValidator
from PyQt5.QtWidgets import *
from decimal import Decimal
import psycopg2


conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
cursor = conn.cursor()

class ReportWindow(object):
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
        self.staffbtn = QPushButton(self.widget_4)
        self.staffbtn.setObjectName(u"staffbtn")
        self.staffbtn.setGeometry(QRect(43, 26, 181, 32))
        self.staffbtn.setCursor(QCursor(Qt.PointingHandCursor))
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
        self.schedbtn = QPushButton(self.widget_4)
        self.schedbtn.setObjectName(u"schedbtn")
        self.schedbtn.setGeometry(QRect(43, 81, 181, 32))
        self.schedbtn.setStyleSheet(u"QPushButton{\n"
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
        self.reportbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.reportbtn.setStyleSheet(u"QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"color: white;\n"
"background-color: #B10303;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
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
        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.title = QLabel(self.widget_9)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(498, 23, 337, 61))
        self.title.setStyleSheet(u"QLabel {\n"
"       font-weight: bold;\n"
"	font-size: 36px;\n"
"}")
        self.title.setAlignment(Qt.AlignCenter)
        self.searchinput = QLineEdit(self.widget_9)
        self.searchinput.setObjectName(u"searchinput")
        self.searchinput.setGeometry(QRect(815, 150, 300, 40))
        self.searchinput.setPlaceholderText("Search Name")
        self.searchinput.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;")
        self.overtimerate = QLineEdit(self.widget_9)
        self.overtimerate.setObjectName(u"overtimerate")
        self.overtimerate.setGeometry(QRect(500, 184, 80, 40))
        self.overtimerate.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;")
        self.regularrate = QLineEdit(self.widget_9)
        self.regularrate.setObjectName(u"regularrate")
        self.regularrate.setGeometry(QRect(500, 120, 80, 40))
        self.regularrate.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;")
        
        # Validator to accept only floating-point or integer input
        double_validator = QDoubleValidator()
        double_validator.setDecimals(2)  # Set maximum decimals allowed
        self.regularrate.setValidator(double_validator)
        self.overtimerate.setValidator(double_validator)

        self.startdate = QDateEdit(self.widget_9)
        self.startdate.setObjectName(u"startdate")
        self.startdate.setGeometry(QRect(150, 120, 120, 40))
        self.startdate.setDisplayFormat("MM/dd/yyyy")
        self.startdate.setDate(QDate.currentDate().addDays(-15))
        self.startdate.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"font-size: 14px;")
        self.enddate = QDateEdit(self.widget_9)
        self.enddate.setObjectName(u"enddate")
        self.enddate.setGeometry(QRect(150, 184, 120, 40))
        self.enddate.setDisplayFormat("MM/dd/yyyy")
        self.enddate.setDate(QDate.currentDate())
        self.enddate.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid  #B10303;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"font-size: 14px;")
        self.otlabel = QLabel(self.widget_9)
        self.otlabel.setObjectName(u"otlabel")
        self.otlabel.setGeometry(QRect(330, 194, 163, 20))
        self.otlabel.setStyleSheet(u"font-size: 20px;")
        self.reglabel = QLabel(self.widget_9)
        self.reglabel.setObjectName(u"reglabel")
        self.reglabel.setGeometry(QRect(330, 125, 149, 31))
        self.reglabel.setStyleSheet(u"font-size: 20px;")
        self.startdatelabel = QLabel(self.widget_9)
        self.startdatelabel.setObjectName(u"startdatelabel")
        self.startdatelabel.setGeometry(QRect(78, 131, 50, 16))
        self.startdatelabel.setStyleSheet(u"font-size: 20px;")
        self.enddatelabel = QLabel(self.widget_9)
        self.enddatelabel.setObjectName(u"enddatelabel")
        self.enddatelabel.setGeometry(QRect(78, 194, 50, 16))
        self.enddatelabel.setStyleSheet(u"\n"
"font-size: 20px;")
        self.searchbtn = QPushButton(self.widget_9)
        self.searchbtn.setObjectName(u"searchbtn")
        self.searchbtn.setGeometry(QRect(1124, 150, 131, 40))
        self.searchbtn.setStyleSheet(u"QPushButton{\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"background-color: #B10303;\n"
"color: white;\n"
"font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: black;\n"
"}")

        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.gridLayout_5 = QGridLayout(self.widget_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableWidget = QTableWidget(self.widget_8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMaximumSize(QSize(1301, 528))

        self.gridLayout_5.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_8)

        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 7)

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # Ensure the initial focus is on the regular rate input
        self.regularrate.setFocus()
        print("Initial focus set to regularrate")
        # Set initial focus and tab order
        MainWindow.setTabOrder(self.overtimerate, self.regularrate)
        MainWindow.setTabOrder(self.regularrate, self.overtimerate)

        # Exclude unnecessary buttons from tab order
        self.startdate.setFocusPolicy(Qt.NoFocus)
        self.enddate.setFocusPolicy(Qt.NoFocus)
        self.searchinput.setFocusPolicy(Qt.NoFocus)
        self.staffbtn.setFocusPolicy(Qt.NoFocus)
        self.schedbtn.setFocusPolicy(Qt.NoFocus)
        self.reportbtn.setFocusPolicy(Qt.NoFocus)
        self.logoutbtn.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.searchbtn.setFocusPolicy(Qt.NoFocus)

        self.searchbtn.clicked.connect(self.load_payroll)
        
        self.load_data()

        
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.staffbtn.setText(QCoreApplication.translate("MainWindow", u"Staff", None))
        self.schedbtn.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.reportbtn.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.logoutbtn.setText(QCoreApplication.translate("MainWindow", u"LOGOUT", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Insurgents Payroll", None))
        self.searchinput.setText("")
        self.otlabel.setText(QCoreApplication.translate("MainWindow", u"Overtime Rate/Hr", None))
        self.reglabel.setText(QCoreApplication.translate("MainWindow", u"Regular Rate/Hr", None))
        self.startdatelabel.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.enddatelabel.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.searchbtn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
    # retranslateUi
    
    def load_data(self):
        try:
            # Ensure you have a valid cursor and connection setup before executing queries
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

            self.tableWidget.setColumnCount(8)
            self.tableWidget.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Regular Hours', 'Overtime Hours', 'Regular Pay', 'Overtime Pay', 'Total Pay'])
            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.setColumnHidden(0, True)  # Hide the ID column

        except Exception as e:
            print(f"Error in load_data: {e}")
    
    def load_payroll(self):
        try:
            if not self.regularrate.text() or not self.overtimerate.text():
                QMessageBox.warning(None, "Validation Error", "Regular and Overtime rates per hour are required.")
                return

            start_date_obj = datetime.datetime.strptime(self.startdate.text(), "%m/%d/%Y")
            end_date_obj = datetime.datetime.strptime(self.enddate.text(), "%m/%d/%Y")
            start_date = start_date_obj.strftime("%Y-%m-%d")
            end_date = end_date_obj.strftime("%Y-%m-%d")

            regular_rate = Decimal(self.regularrate.text())
            overtime_rate = Decimal(self.overtimerate.text())
            name_input = self.searchinput.text().lower()

            if name_input == "":
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

            for row_idx, row_data in enumerate(self.rows):
                regular_hours = Decimal(row_data[3]) if row_data[3] else Decimal(0)
                overtime_hours = Decimal(row_data[4]) if row_data[4] else Decimal(0)

                regular_salary = regular_rate * regular_hours
                overtime_salary = overtime_rate * overtime_hours
                total_salary = regular_salary + overtime_salary

                 # Update table widget with salary information
                for col_idx, col_data in enumerate(row_data + (regular_salary, overtime_salary, total_salary)):
                    item = QTableWidgetItem(str(round(col_data, 2)) if isinstance(col_data, Decimal) else str(col_data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)

                # Populate other columns with employee data
                for col_idx, col_data in enumerate(row_data):
                    if isinstance(col_data, datetime.date):
                        col_data = col_data.strftime('%Y-%m-%d')
                    item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidget.setItem(row_idx, col_idx, item)

        except Exception as e:
            print(f"Error in load_payroll: {e}")