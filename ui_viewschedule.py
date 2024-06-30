from PyQt5.QtCore import QCoreApplication, QMetaObject, QRect, QSize, Qt, QDate, QTimer
from PyQt5.QtGui import QCursor, QFont, QPixmap
from PyQt5.QtWidgets import *
import datetime, psycopg2, os

conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
cursor = conn.cursor()

class View_Schedule(QWidget):
    def __init__(self, stacked_widget):
        super(View_Schedule, self).__init__()
        self.stacked_widget = stacked_widget
        self.setupUi(self)
        QTimer.singleShot(0, self.load_data)

    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName("Form")
        Form.resize(1600, 800)
        Form.setMinimumSize(QSize(1600, 800))
        Form.setMaximumSize(QSize(1600, 800))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName("widget")
        self.widget.setAcceptDrops(False)
        self.widget.setStyleSheet("background-color: rgb(40, 38, 38);")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QRect(100, 250, 600, 300))
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "image", "Logo1.png")
        self.label_3.setPixmap(QPixmap(image_path))
        self.label_3.setScaledContents(True)

        self.horizontalLayout.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("background-color: rgb(199, 194, 194);")
        self.welcome = QLabel(self.widget_2)
        self.welcome.setObjectName("welcome")
        self.welcome.setGeometry(QRect(65, 75, 670, 80))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.welcome.setFont(font)
        self.welcome.setStyleSheet("""
            color: rgb(177, 3, 3);
            font-size: 64px;
        """)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.widget_3.setGeometry(QRect(50, 260, 700, 500))
        self.tableWidget = QTableWidget(self.widget_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setGeometry(QRect(0, 140, 700, 360))
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                border: 1px solid #B10303;
                gridline-color: #B10303;
                background-color: #f5f5f5;
                font-family: Arial;
                font-size: 14px;
            }
            QTableWidget::item {
                border-right: 1px solid #B10303;
                border-bottom: 1px solid #B10303;
            }
            QTableWidget::item:selected {
                background-color: #B10303;
                color: white;
            }
            QHeaderView::section {
                background-color: #B10303;
                color: white;
                padding: 4px;
                border: 1px solid #B10303;
                font-size: 15px;
                font-weight: bold;
            }
        """)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName("label")
        self.label.setGeometry(QRect(50, 30, 90, 20))
        self.label.setStyleSheet("""
            font-weight: bold;
            font-size: 16px;
        """)

        self.startdateinput = QDateEdit(self.widget_3)
        self.startdateinput.setObjectName("startdateinput")
        self.startdateinput.setGeometry(QRect(120, 20, 130, 40))
        self.startdateinput.setMaximumSize(QSize(120, 40))
        font1 = QFont()
        self.startdateinput.setFont(font1)
        current_date = QDate.currentDate()
        self.startdateinput.setDate(current_date)
        self.startdateinput.setDisplayFormat("MM/dd/yyyy") 
        self.startdateinput.setStyleSheet("""
            background-color: rgb(255, 255, 255);
            border: 1px solid #B10303;
            border-radius: 5px;
            padding: 4px;
            font-size: 14px;
        """)

        self.enddateinput = QDateEdit(self.widget_3)
        self.enddateinput.setObjectName("enddateinput")
        self.enddateinput.setGeometry(QRect(120, 70, 130, 40))
        self.enddateinput.setMaximumSize(QSize(120, 40))
        end_date = current_date.addDays(7)
        self.enddateinput.setDate(end_date)
        self.enddateinput.setDisplayFormat("MM/dd/yyyy") 
        self.enddateinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"font-size: 14px;")
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.label_2.setGeometry(QRect(50, 80, 50, 20))
        self.label_2.setStyleSheet("font-weight: bold;"
"font-size: 16px;")
        self.searchinput = QLineEdit(self.widget_3)
        self.searchinput.setObjectName("searchinput")
        self.searchinput.setGeometry(QRect(340, 45, 200, 40))
        self.searchinput.setStyleSheet("background-color: rgb(255, 255, 255);"
"border: 1px solid  #B10303;"
"border-radius: 5px;"
"padding: 4px;"
"font-size: 14px;")
        self.searchbtn = QPushButton(self.widget_3)
        self.searchbtn.setObjectName("searchbtn")
        self.searchbtn.setGeometry(QRect(550, 45, 100, 40))
        self.searchbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchbtn.setStyleSheet("QPushButton {"
"  background-color: rgb(177, 3, 3);"
"   color: white;"
"   border-radius: 10px;"
"    padding: 10px 20px;"
"   font-size: 16px;"
"   font-weight: bold;"
"}"
"QPushButton:hover {"
"    background-color: rgb(204, 0, 0); "
"}"
"QPushButton:pressed {"
"    background-color: rgb(139, 0, 0);"
"}")
        self.viewschedbtn = QPushButton(self.widget_2)
        self.viewschedbtn.setObjectName("viewschedbtn")
        self.viewschedbtn.setGeometry(QRect(400, 180, 170, 40))
        self.viewschedbtn.setFont(font1)
        self.viewschedbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.viewschedbtn.setStyleSheet("#viewschedbtn{"
"	background-color: rgb(177, 3, 3);"
"	color: white;"
"	font-size: 20px;"
"	border-top-right-radius: 5px;"
"	border-bottom-right-radius: 5px;"
"}"
""
"#viewschedbtn:hover{"
"	color: black;"
"}")
        self.loginstaffbtn = QPushButton(self.widget_2)
        self.loginstaffbtn.setObjectName("loginstaffbtn")
        self.loginstaffbtn.setGeometry(QRect(230, 180, 170, 40))
        self.loginstaffbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginstaffbtn.setStyleSheet("#loginstaffbtn{"
"	background-color: #ECE6E6;"
"	border: 1px solid  #B10303;"
"	font-size: 20px;"
"	border-top-left-radius: 5px;"
"	border-bottom-left-radius: 5px;"
"}"
""
"#loginstaffbtn:hover{"
"	background-color: rgb(177, 3, 3);"
"	color: white;"
"}")

        self.horizontalLayout.addWidget(self.widget_2)

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.searchbtn.clicked.connect(self.search_staff)
        self.viewschedbtn.clicked.connect(self.load_data)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.label_3.setText("")
        self.welcome.setText(QCoreApplication.translate("Form", "Upcoming Schedules", None))
        self.label.setText(QCoreApplication.translate("Form", "From:", None))
        self.label_2.setText(QCoreApplication.translate("Form", "To:", None))
        self.searchinput.setPlaceholderText(QCoreApplication.translate("Form", "Search Name", None))
        self.searchbtn.setText(QCoreApplication.translate("Form", "Search", None))
        self.viewschedbtn.setText(QCoreApplication.translate("Form", "View Schedules", None))
        self.loginstaffbtn.setText(QCoreApplication.translate("Form", "Admin Login", None))

    def load_data(self):
        try:
            start_date_obj = datetime.datetime.strptime(self.startdateinput.text(), "%m/%d/%Y")
            end_date_obj = datetime.datetime.strptime(self.enddateinput.text(), "%m/%d/%Y")

            start_date = start_date_obj.strftime("%Y-%m-%d")
            end_date = end_date_obj.strftime("%Y-%m-%d")

            cursor.execute("""
                SELECT e.employee_id, CONCAT(e.first_name, ' ', e.last_name) AS full_name, s.shift_date, s.start_time, s.end_time 
                FROM schedules s 
                NATURAL JOIN employees e 
                WHERE s.shift_date BETWEEN %s AND %s
            """, (start_date, end_date))

            rows = cursor.fetchall()

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
            start_date_obj = datetime.datetime.strptime(self.startdateinput.text(), "%m/%d/%Y")
            end_date_obj = datetime.datetime.strptime(self.enddateinput.text(), "%m/%d/%Y")

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

