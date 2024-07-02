import sys
import psycopg2
import time
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication,QFrame, QWidget, QGridLayout, QLabel, QPushButton, QVBoxLayout, QDialog, QScrollArea, QMessageBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from datetime import datetime
from ui_pin import PIN_Dialog

connection = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
cursor = connection.cursor()

empF = []

class TimerThread(QThread):
    timer_updated = pyqtSignal(int)

    def __init__(self, emp_timer=0, parent=None):
        super().__init__(parent)
        self.running = False
        self.paused = False
        self.timer = emp_timer  # Initialize the timer with emp_timer value
        self.timer_limit = 10 * 3600  # 9 hours limit in seconds

    def run(self):
        while True:
            if self.running and not self.paused:
                self.timer += 1
                if self.timer >= self.timer_limit:
                    self.timer = self.timer_limit  # Set timer to the limit
                    self.running = False  # Stop the timer
                self.timer_updated.emit(self.timer)
            time.sleep(1)

    def start_timer(self):
        self.running = True

    def pause_timer(self):
        self.paused = True

    def resume_timer(self):
        self.paused = False

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.timer_limit = 0
        self.initUI()
        self.timers = {}  # Dictionary to store timers for each employee

        cursor.execute("""SELECT (first_name ||' '|| last_name),seconds,shift.status,s_id
                        FROM shift 
                        INNER JOIN schedules ON shift.schedule_id = cast(schedules.schedule_id as integer)
                        INNER JOIN employees ON employees.employee_id = cast(schedules.employee_id as integer)
						where shift_date = '"""+ self.date+"""' and schedules.status in('Reserve','Regular')
                        """)
        
        employee = cursor.fetchall()
        for eName, timerz, status, s_id in employee:
            if timerz != 0:
                timer_thread = TimerThread(emp_timer=timerz)  # Pass the initial timer value
                timer_thread.timer_updated.connect(lambda seconds, id=s_id: self.update_timer_label(seconds, id))
                self.timers[s_id] = timer_thread
                if(status == 1):
                    timer_thread.start()  # Start the timer thread immediately
                    timer_thread.start_timer()
                else:
                    timer_thread.start()  # Start the timer thread immediately

    def closeEvent(self, event):
        # Display the message box
        reply = QMessageBox.question(self, "Warning", 
                                    "Are you sure you want to close this program? The employee clock-in timer cannot run in the background and it may not track work hours accurately.", 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # Check the user's response
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(720, 30, 0, 0)
        self.setMinimumSize(720,720)
        
        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)  # Set spacing between widgets to 0
        grid_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to 0

        self.frame1 = QFrame(self)
        self.frame3 = QFrame(self)
        self.back_button = QPushButton("Back",self.frame3)
        self.back_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button.setStyleSheet("""
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
        }
        QPushButton:pressed {
            background-color: #7F0B0B;
            border: 1px solid #7F0B0B;
        }
        QPushButton:focus {
            outline: none;
        }
    """)
        self.back_button.hide()
        self.frame4 = QFrame(self)
        self.frame4.setStyleSheet("background-color:#ECE6E6;")
        self.start_button = QPushButton("Start", self.frame4)
        self.pause_button = QPushButton("Clock Out", self.frame4)
        self.resume_button = QPushButton("Clock In", self.frame4)
        self.start_button.setStyleSheet("""
        QPushButton {
            color: white;
            background-color: #B10303;
            border: 1px solid #B10303;  /* Add border for better contrast */
            border-radius: 5px;
            font-family: Arial;
            font-weight: bold;
            font-size: 14px;
            padding: 8px 16px;  /* Add padding for better button size */
            outline: none;  /* Remove outline on focus */
        }
        QPushButton:hover {
            background-color: #FF3D3D;  /* Lighten color on hover */
            border: 1px solid #FF3D3D;
        }
        QPushButton:pressed {
            background-color: #7F0000;  /* Darken color when pressed */
            border: 1px solid #7F0000;
        }
    """)

        self.pause_button.setStyleSheet("""
        QPushButton {
            color: white;
            background-color: #898989;
            border: 1px solid #898989;  /* Add border for better contrast */
            border-radius: 5px;
            font-family: Arial;
            font-weight: bold;
            font-size: 14px;
            padding: 8px 16px;  /* Add padding for better button size */
            outline: none;  /* Remove outline on focus */
        }
        QPushButton:hover {
            background-color: #B3B3B3;  /* Lighten color on hover */
            border: 1px solid #B3B3B3;
        }
        QPushButton:pressed {
            background-color: #6E6E6E;  /* Darken color when pressed */
            border: 1px solid #6E6E6E;
        }
    """)

        self.resume_button.setStyleSheet("""
            QPushButton {
                color: white;
                background-color: #8BC34A;
                border: 1px solid #8BC34A;  /* Add border for better contrast */
                border-radius: 5px;
                font-family: Arial;
                font-weight: bold;
                font-size: 14px;
                padding: 8px 16px;  /* Add padding for better button size */
                outline: none;  /* Remove outline on focus */
            }
            QPushButton:hover {
                background-color: #AED581;  /* Lighten color on hover */
                border: 1px solid #AED581;
            }
            QPushButton:pressed {
                background-color: #689F38;  /* Darken color when pressed */
                border: 1px solid #689F38;
            }
        """)

        self.frame4.hide()
        self.empScrollArea = QScrollArea(self)
        self.frame2 = QFrame()
        self.empLayout = QVBoxLayout(self.frame2)
        self.empScrollArea.setWidgetResizable(True)
        self.empScrollArea.setWidget(self.frame2)
        label1 = QLabel(self.frame3)
        label1.setText("""
            <html>
                <head/>
                <body>
                    <p style="color: white; font-size: 30px; font-weight: bold; text-align: center;">
                        <span style="color: rgb(254, 2, 1);">I</span>
                        <span>N S</span>
                        <span style="color: rgb(254, 2, 1);">U</span>
                        <span>R G</span>
                        <span style="color: rgb(254, 2, 1);">E</span>
                        <span>N T</span>
                        <span style="color: rgb(254, 2, 1);">S</span>
                        <span>&nbsp;&nbsp;K I</span>
                        <span style="color: rgb(254, 2, 1);">O</span>
                        <span>S K</span>
                    </p>
                </body>
            </html>
        """)

        frame3_layout = QVBoxLayout(self.frame3)
        frame3_layout.addWidget(label1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.frame3.setLayout(frame3_layout)
        self.frame3.setStyleSheet("background-color:#282626;")
        self.frame2.setStyleSheet("background-color:#ECE6E6;")
        self.frame1.setStyleSheet("background-color:#ECE6E6; border-right: 2px solid black;")
        grid_layout.addWidget(self.frame3, 0, 0, 1, 2)  
        grid_layout.addWidget(self.frame1, 1, 0)
        grid_layout.addWidget(self.empScrollArea, 1, 1)
        grid_layout.addWidget(self.frame4,1,1)
        self.setLayout(grid_layout)
        self.setFrame2()
        self.clock_label = QLabel(self.frame1)
        self.date_label = QLabel(datetime.now().strftime("%Y-%m-%d"), self.frame1)  # Add date label
        self.clock_label.setStyleSheet("font-size: 20px; color: black; border: none; font-weight: bold;")
        self.date_label.setStyleSheet("font-size: 20px; color: black; border: none; font-weight: bold;")
        self.name_label = QLabel("Name", self.frame4)
        self.name_label.setStyleSheet("""
        color: black;
        font-size: 24px; 
        font-weight: bold; 
    """)
        self.name_label.move(10, 20)
        self.name_label.setFixedWidth(200)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)  # Update every second
        self.update_clock()  # Initial update

    def update_clock(self):
        current_time = datetime.now().strftime("%I:%M:%S %p")
        self.clock_label.setText(current_time)

    def back_clicked(self):
        self.frame4.hide()
        self.empScrollArea.show()
        self.back_button.hide()
    
    def resizeEvent(self,event):
        global empF

        frame1W = int(self.width()*.20)
        self.frame1.setFixedWidth(frame1W)
        self.frame3.setFixedWidth(int(self.width()*1))
        self.frame3.setFixedHeight(int(self.height()*.20))
        self.back_button.setGeometry(int(self.frame3.width() * 0.84), int(self.frame3.height() * 0.06), int(self.frame3.width() * 0.15), int(self.frame3.height() * 0.30))
        self.empScrollArea.setGeometry(0,0,int(self.width()),int(self.height()))
        total_height = (len(empF)+2) * int(self.empScrollArea.height() * 0.10)

        self.frame2.setMinimumHeight(total_height)
        y = 0.
        cursor.execute("""select count(s_id) from shift inner join schedules ON shift.schedule_id = cast(schedules.schedule_id as integer)
						where shift_date = '"""+ self.date+"""'
                        """)
        length = cursor.fetchall()
        for a in range(length[0][0]):
            empF[a].setGeometry(int(self.empScrollArea.width()*.10),int(self.empScrollArea.height()* y),int(self.empScrollArea.width()*.60),int(self.empScrollArea.height()*.10))
            y += .11
        stra = str(int(self.frame1.width()*.125))
        self.clock_label.setStyleSheet("font-size: "+stra+"px; color: black; border: none; font-weight: bold;")
        self.date_label.setStyleSheet("font-size: "+stra+"px; color: black; border: none; font-weight: bold;")
        self.clock_label.setFixedSize(int(self.frame1.width()*.8),int(self.frame1.height()*.10)) 
        self.clock_label.move(int(self.frame1.width()*.10),0)
        self.date_label.setFixedSize(int(self.frame1.width()*.79),int(self.frame1.height()*.10))
        self.date_label.move(int(self.frame1.width()*.12),int(self.frame1.height()*.10))



    def setFrame2(self):
        global emp, empF
        
        cursor.execute("""SELECT employees.employee_id,(first_name ||' '|| last_name),seconds,shift.status,s_id
                        FROM shift 
                        INNER JOIN schedules ON shift.schedule_id = cast(schedules.schedule_id as integer)
                        INNER JOIN employees ON employees.employee_id = cast(schedules.employee_id as integer)
						where shift_date = '"""+ self.date+"""'
                        """)
        employee = cursor.fetchall()
        
        for emp_id, eName, timerz, status, s_id in employee:
            empFrame = QFrame(self.frame2)
            empFrame.setCursor(QCursor(Qt.PointingHandCursor))
            label = QLabel(eName, empFrame)
            
            empFrame.setStyleSheet("background-color: #D24242; border: 2px solid black; border-radius: 10px;") 
            label.setStyleSheet("border: none; color: white; font-size: 24px;") 
            empF.append(empFrame)
            label.move(20,20)
            empFrame.mousePressEvent = lambda event, emp_id=emp_id, name=s_id,asd = eName: self.on_empFrame_clicked(emp_id,name,asd)

        self.timer_labels = {}  # Dictionary to store timer labels for each employee
        # Create timer labels for each employee
        
        for emp_id, eName,timerz,status,s_id in employee:
            timer_label = QLabel("00:00:00", self.frame4)
            timer_label.setStyleSheet("color: red; font-size: 32px; font-weight: bold; qproperty-alignment: 'AlignCenter';")
            timer_label.move(190,50)
            self.timer_labels[s_id] = timer_label
            timer_label.hide()

        self.start_button.move(100, 150)
        self.pause_button.move(180, 150)
        self.resume_button.move(260, 150)

        # Connect buttons to functions
        self.start_button.clicked.connect(self.start_button_clicked)
        self.pause_button.clicked.connect(self.pause_button_clicked)
        self.resume_button.clicked.connect(self.resume_button_clicked)

    def back_clicked(self):
        self.frame4.hide()
        self.empScrollArea.show()
        self.back_button.hide()
        self.hide_timer_labels()
        
    

    def start_button_clicked(self):
        # Retrieve the employee id of the clicked frame
        cursor.execute("""SELECT (first_name ||' '|| last_name),seconds,shift.status,s_id
                        FROM shift 
                        INNER JOIN schedules ON shift.schedule_id = cast(schedules.schedule_id as integer)
                        INNER JOIN employees ON employees.employee_id = cast(schedules.employee_id as integer)
						where shift_date = '"""+ self.date+"""'
                        """)
        employee = cursor.fetchall()
        id = self.current_emp_id
        
        # Check if the timer thread exists for the current employee
        if id in self.timers:
            timer_thread = self.timers[id]
            if not timer_thread.running:
                # Check if there's a non-zero timer value for the current employee
                for eName,timerz,status,s_id in employee:
                    if s_id == id and timerz != 0:
                        timer_thread.timer = timerz
                        break
                timer_thread.start_timer()
                cursor.execute("""UPDATE shift
                        SET status = 1
                        WHERE s_id = %s
                         """, (id,))
                connection.commit()
        self.start_button.hide()
        self.pause_button.show()
        self.resume_button.hide()

    def pause_button_clicked(self):
        # Retrieve the employee id of the clicked frame
        id = self.current_emp_id

        # Check if the timer thread exists for the current employee
        if id in self.timers:
            timer_thread = self.timers[id]
            if timer_thread.running:
                timer_thread.pause_timer()
                cursor.execute("""UPDATE shift
                        SET status = 0
                        WHERE s_id = %s
                         """, (id,))
                connection.commit()
        self.start_button.hide()
        self.pause_button.hide()
        self.resume_button.show()

    def resume_button_clicked(self):
        # Retrieve the employee id of the clicked frame
        id = self.current_emp_id

        # Check if the timer thread exists for the current employee
        if id in self.timers:
            timer_thread = self.timers[id]
            if timer_thread.paused:
                timer_thread.resume_timer()
                cursor.execute("""UPDATE shift
                        SET status = 1
                        WHERE s_id = %s
                         """, (id,))
                connection.commit()

        if timer_thread.running == True:
            self.start_button.hide()
        elif timer_thread.paused == True:
            self.pause_button.hide()
        elif timer_thread.paused == False:
            self.resume_button.hide()
        
        self.start_button.hide()
        self.pause_button.show()
        self.resume_button.hide()

    def hide_timer_labels(self):
        for label in self.timer_labels.values():
            label.hide()

    def show_timer_label(self, id):
        if id in self.timer_labels:
            self.timer_labels[id].show()
    
    
    def open_staff_details_dialog(self, emp_id):
        self.pin = QDialog()
        self.pin_ui = PIN_Dialog(emp_id, self.pin)
        self.pin_ui.setupUi(self.pin)

        result = self.pin.exec()
        return result == QDialog.Accepted

    def on_empFrame_clicked(self, emp_id, id, fname):
        global emp
        
        if not self.open_staff_details_dialog(emp_id):
            QMessageBox.warning(self, "Incorrect PIN", "Please try again.")

            return
        
        self.current_emp_id = id
        self.empScrollArea.hide()
        self.frame4.show()
        self.back_button.show()
        self.back_button.clicked.connect(self.back_clicked)
        
        self.start_button.show()
        timer_thread = self.timers.get(id, None)
        if timer_thread:
            if timer_thread.running and not timer_thread.paused:
                self.pause_button.show()
                self.resume_button.hide()
                self.start_button.hide()
            elif timer_thread.paused:
                self.pause_button.hide()
                self.resume_button.show()
                self.start_button.hide()
            else:
                self.pause_button.hide()
                self.resume_button.hide()
        else:
            self.pause_button.hide()
            self.resume_button.hide()
            
        # Hide all existing timer labels
        self.hide_timer_labels()

        # Show the timer label for the clicked employee
        self.show_timer_label(id)

        self.name_label.setText(fname)
        self.name_label.show()

        # Create timer thread if it doesn't exist
        if id not in self.timers:
            timer_thread = TimerThread()
            timer_thread.timer_updated.connect(lambda seconds, id=id: self.update_timer_label(seconds, id))
            self.timers[id] = timer_thread

            # Create start, pause, and resume buttons
            self.start_button.move(100, 100)
            self.pause_button.move(180, 100)
            self.resume_button.move(260, 100)

            # Connect buttons to functions
            self.start_button.clicked.connect(lambda: self.start_button_clicked())
            self.pause_button.clicked.connect(lambda: self.pause_button_clicked())
            self.resume_button.clicked.connect(lambda: self.resume_button_clicked())

            timer_thread.start()




    def update_timer_label(self, total_seconds, id):
        # Calculate hours, minutes, and seconds from total_seconds
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        timer_string = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.timer_labels[id].setText(timer_string)

        # Fetch current employee details from the database
        cursor.execute("""SELECT (first_name ||' '|| last_name), seconds, shift.status, s_id
                        FROM shift 
                        INNER JOIN schedules ON shift.schedule_id = cast(schedules.schedule_id as integer)
                        INNER JOIN employees ON employees.employee_id = cast(schedules.employee_id as integer)
                        WHERE shift_date = %s""", (self.date,))
        employee = cursor.fetchall()

        # Update the corresponding dictionary in emp list
        for eName, timerz, status, s_id2 in employee:
            if s_id2 == id:
                cursor.execute("""UPDATE shift
                                SET seconds = %s
                                WHERE s_id = %s""", (total_seconds, s_id2))  # Use total_seconds here
                connection.commit()
                break

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    from kiosk import MainWindow
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.setWindowTitle("Insurgents Employee Kiosk")

    import os
    if hasattr(sys, '_MEIPASS'):
        script_dir = sys._MEIPASS
    else:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "image", "Logo.ico")
    from PyQt5.QtGui import QIcon
    icon = QIcon(image_path)
    window.setWindowIcon(icon)
    
    sys.exit(app.exec_())
