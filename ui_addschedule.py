from PyQt5.QtCore import QCoreApplication, QMetaObject, QSize, Qt, QRect
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import *
import datetime, psycopg2, os

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
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.logo = QLabel(self.widget_3)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(200, 100))
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "image", "Logo1.png")
        self.logo.setPixmap(QPixmap(image_path))
        self.logo.setScaledContents(True)

        self.gridLayout.addWidget(self.logo, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout.addWidget(self.widget_5)

        self.widget_L2 = QWidget(self.widget)
        self.widget_L2.setObjectName(u"widget_L2")
        self.widget_L2.setStyleSheet(u"")
        self.backbtn = QPushButton(self.widget_L2)
        self.backbtn.setObjectName(u"backbtn")
        self.backbtn.setGeometry(QRect(68, 130, 131, 32))
        self.backbtn.setMaximumSize(QSize(2313123, 16777215))
        self.backbtn.setStyleSheet("""
    QPushButton {
        border: 1px solid white;
        border-radius: 5px;
        color: white;
        font-family: Arial;
        font-weight: bold;
        font-size: 14px;
        background-color: transparent;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    QPushButton:hover {
        background-color: #B10303;
        color: black;
    }
    QPushButton:pressed {
        background-color: #7F0B0B;
        border: 1px solid #7F0B0B;
    }
    QPushButton:focus {
        outline: none;
    }
""")

        self.verticalLayout.addWidget(self.widget_L2)


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
        self.addstaffbtn = QPushButton(self.widget_9)
        self.addstaffbtn.setObjectName(u"addstaffbtn")
        self.addstaffbtn.setGeometry(QRect(720, 44, 175, 40))
        self.addstaffbtn.setStyleSheet("""
    QPushButton {
        border: 1px solid white;
        border-radius: 5px;
        background-color: #B10303;
        color: white;
        font-family: Arial;
        font-weight: bold;
        font-size: 14px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #D11A1A;
        color: black;
    }
    QPushButton:pressed {
        background-color: #7F0B0B;
        border: 1px solid #7F0B0B;
    }
    QPushButton:focus {
        outline: none;
    }
""")
        self.updateschedbtn = QPushButton(self.widget_9)
        self.updateschedbtn.setObjectName(u"updateschedbtn")
        self.updateschedbtn.setGeometry(QRect(920, 44, 175, 40))
        self.updateschedbtn.setStyleSheet("""
    QPushButton {
        border: 1px solid white;
        border-radius: 5px;
        background-color: #B10303;
        color: white;
        font-family: Arial;
        font-weight: bold;
        font-size: 14px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #D11A1A;
        color: black;
    }
    QPushButton:pressed {
        background-color: #7F0B0B;
        border: 1px solid #7F0B0B;
    }
    QPushButton:focus {
        outline: none;
    }
""")
        self.deletestaffbtn = QPushButton(self.widget_9)
        self.deletestaffbtn.setObjectName(u"deletestaffbtn")
        self.deletestaffbtn.setGeometry(QRect(1120, 44, 175, 40))
        self.deletestaffbtn.setStyleSheet("""
    QPushButton {
        border: 1px solid white;
        border-radius: 5px;
        background-color: #B10303;
        color: white;
        font-family: Arial;
        font-weight: bold;
        font-size: 14px;
        padding: 10px;
    }
    QPushButton:hover {
        background-color: #D11A1A;
        color: black;
    }
    QPushButton:pressed {
        background-color: #7F0B0B;
        border: 1px solid #7F0B0B;
    }
    QPushButton:focus {
        outline: none;
    }
""")

        self.verticalLayout_2.addWidget(self.widget_9)

        self.widget_8 = QWidget(self.widget_2)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"")
        self.tableWidget = QTableWidget(self.widget_8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(16, 16, 1301, 664))
        
        # Apply style to the table widget
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
        
        header = self.tableWidget.horizontalHeader()
        header.setFont(QFont("Arial", 12, QFont.Bold))
        header.setStyleSheet("QHeaderView::section { background-color: #B10303; color: white; }")

        self.verticalLayout_2.addWidget(self.widget_8)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 7)

        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.backbtn.clicked.connect(self.go_back)

        self.load_data()

        self.backbtn.setFocusPolicy(Qt.NoFocus)
        self.addstaffbtn.setFocusPolicy(Qt.NoFocus)
        self.updateschedbtn.setFocusPolicy(Qt.NoFocus)
        self.deletestaffbtn.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo.setText("")
        self.backbtn.setText(QCoreApplication.translate("MainWindow", u"BACK", None))
        self.addstaffbtn.setText(QCoreApplication.translate("MainWindow", u"Set Schedule", None))
        self.updateschedbtn.setText(QCoreApplication.translate("MainWindow", u"Modify Schedule", None))
        self.deletestaffbtn.setText(QCoreApplication.translate("MainWindow", u"Clear Schedule", None))
    # retranslateUi

    def go_back(self):
        self.stacked_widget.setCurrentIndex(self.previous_index)
    
    def load_data(self):
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
        self.tableWidget.setColumnCount(7)  # Set the number of columns including the hidden ID column
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'First Name', 'Last Name', 'Start Time', 'End Time', 'Schedule Category', 'Schedule ID'])
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
