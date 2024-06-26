import sys
import psycopg2

from PyQt5.QtGui import QResizeEvent, QCursor
from PyQt5.QtWidgets import QApplication,QFrame, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QDialog, QHBoxLayout, QMessageBox,QScrollArea
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
import time
from datetime import datetime

from ui_pin import PIN_Dialog
connection = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
cursor = connection.cursor()
current_date = datetime.now().strftime("%Y-%m-%d")
print(current_date)
emp = [
    {"name": "Juan", "timer": 0, "status": None},
    {"name": "Jack", "timer": 0, "status": None},
    {"name": "Joe", "timer": 0, "status": None},
    {"name": "James", "timer": 0, "status": None},
    {"name": "Emily", "timer": 0, "status": None},
    {"name": "John", "timer": 0, "status": None},
    {"name": "Emma", "timer": 0, "status": None},
    {"name": "Jacob", "timer": 0, "status": None},
    {"name": "Sophia", "timer": 0, "status": None},
    {"name": "Michael", "timer": 0, "status": None},
    {"name": "Cortes", "timer": 0, "status": None}
]

# Add id to each dictionary
for i, employee in enumerate(emp, start=1):
    employee["id"] = i

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
        # self.date = current_date
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
        print(employee)
        for eName,timerz,status,s_id in employee:
            if timerz != 0:
                timer_thread = TimerThread(emp_timer=timerz)  # Pass the initial timer value
                print(f"Creating timer thread for employee {eName} with timer value {timerz}")
                timer_thread.timer_updated.connect(lambda seconds, id=s_id: self.update_timer_label(seconds, id))
                self.timers[s_id] = timer_thread
                if(status == 1):
                    timer_thread.start()  # Start the timer thread immediately
                    timer_thread.start_timer()
                else:
                    timer_thread.start()  # Start the timer thread immediately
                
        


    def initUI(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(720, 30, 0, 0)
        self.setMinimumSize(720,720)
        self.setStyleSheet("background-color:black;")
        
        # Create grid layout
        grid_layout = QGridLayout()
        grid_layout.setSpacing(0)  # Set spacing between widgets to 0
        grid_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to 0

        self.frame1 = QFrame(self)
        self.frame3 = QFrame(self)
        self.back_button = QPushButton("Back",self.frame3)
        self.back_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_button.setStyleSheet("color:white;background-color:#B10303; border: 2px solid #B10303; border-radius: 10px;")
        self.back_button.hide()
        self.frame4 = QFrame(self)
        self.frame4.setStyleSheet("background-color:#ECE6E6;")
       
        self.start_button = QPushButton("Start", self.frame4)
        self.pause_button = QPushButton("Clock Out", self.frame4)
        self.resume_button = QPushButton("Clock In", self.frame4)
        # Set the text color to black
        self.start_button.setStyleSheet("color: white; background-color:#B10303")
        self.pause_button.setStyleSheet("color: white; background-color:#898989")
        self.resume_button.setStyleSheet("color: white; background-color:#8BC34A")
        self.frame4.hide()
        self.empScrollArea = QScrollArea(self)
        self.frame2 = QFrame()
        self.empLayout = QVBoxLayout(self.frame2)
        self.empScrollArea.setWidgetResizable(True)
        self.empScrollArea.setWidget(self.frame2)

        label1 = QLabel("INSURGENT KIOSK",self.frame3)
        label1.setStyleSheet("color:white; font-size:50px;")
        frame3_layout = QVBoxLayout(self.frame3)
        frame3_layout.addWidget(label1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.frame3.setLayout(frame3_layout)
        self.frame3.setStyleSheet("background-color:#282626;")
        self.frame2.setStyleSheet("background-color:#ECE6E6;")
        # self.frame1.setStyleSheet("background-color:white;")
        self.frame1.setStyleSheet("background-color:#ECE6E6; border-right: 2px solid black;")
        grid_layout.addWidget(self.frame3, 0, 0, 1, 2)  # Span frame3 across two columns
        grid_layout.addWidget(self.frame1, 1, 0)
        grid_layout.addWidget(self.empScrollArea, 1, 1)
        grid_layout.addWidget(self.frame4,1,1)
        
        self.setLayout(grid_layout)
        self.setFrame2()
        # Add clock and date to frame1
        self.clock_label = QLabel(self.frame1)
        self.date_label = QLabel(datetime.now().strftime("%Y-%m-%d"), self.frame1)  # Add date label
        self.clock_label.setStyleSheet("font-size: 18px; color: red; border: none; font-weight: bold;")
        self.date_label.setStyleSheet("font-size: 16px; color: red; border: none; font-weight: bold;")
        self.clock_label.move(20, 20)
        self.date_label.move(20, 50)  # Adjust position of the date label

        self.name_label = QLabel("Name", self.frame4)
        self.name_label.setStyleSheet("color: black; font-size: 16px;")
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
        self.back_button.setGeometry(int(self.frame3.width()*.82),int(self.frame3.height()*.10),int(self.frame3.width()*.15),int(self.frame3.height()*.30))
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
        self.clock_label.setStyleSheet("font-size: "+stra+"px; color: red; border: none; font-weight: bold;")
        self.date_label.setStyleSheet("font-size: "+stra+"px; color: red; border: none; font-weight: bold;")
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
        
        
        for emp_id, eName,timerz,status,s_id in employee:
            empFrame = QFrame(self.frame2)
            empFrame.setCursor(QCursor(Qt.PointingHandCursor))
            label = QLabel(eName, empFrame)
            
            empFrame.setStyleSheet("background-color: #D24242; border: 2px solid black; border-radius: 10px;") 
            label.setStyleSheet(" border: none; color: white;")
            empF.append(empFrame)
            label.move(20,20)
            empFrame.mousePressEvent = lambda event, emp_id=emp_id, name=s_id,asd = eName: self.on_empFrame_clicked(emp_id,name,asd)

        self.timer_labels = {}  # Dictionary to store timer labels for each employee
        # Create timer labels for each employee
        for emp_id, eName,timerz,status,s_id in employee:
            timer_label = QLabel("00:00:00", self.frame4)
            timer_label.setStyleSheet("color: red;")
            timer_label.move(190,50)
            self.timer_labels[s_id] = timer_label
            timer_label.hide()

        # Create start, pause, and resume buttons
        # self.start_button = QPushButton("Start", self.frame4)
        # self.pause_button = QPushButton("Pause", self.frame4)
        # self.resume_button = QPushButton("Resume", self.frame4)
        self.start_button.move(100, 100)
        self.pause_button.move(180, 100)
        self.resume_button.move(260, 100)
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
            # QMessageBox.warning(self, "Warning", "Incorrect PIN. Please try again.")
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
        print("Updating timer label...")

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

        # print(f"Updated timer for employee {id}: {timer_string}")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())