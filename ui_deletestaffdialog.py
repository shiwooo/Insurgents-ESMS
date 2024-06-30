from PyQt5.QtCore import QCoreApplication, QMetaObject, QObject, QRect,  Qt, pyqtSignal
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import *
import psycopg2

class DeleteStaffDialog(QObject):
    staff_deleted = pyqtSignal()  # Signal defined as a class attribute

    def __init__(self, dialog):
        super(DeleteStaffDialog, self).__init__()
        self.dialog = dialog 

    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(375, 207)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: rgb(236, 230, 230);")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName("label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.widget_2.setStyleSheet("background-color: rgb(236, 230, 230);")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.emp_id = QLabel(self.widget_4)
        self.emp_id.setObjectName("emp_id")
        self.emp_id.setGeometry(QRect(10, 30, 55, 16))

        self.horizontalLayout_3.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancelbtn = QPushButton(self.widget_5)
        self.cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelbtn.setObjectName("cancelbtn")
        self.cancelbtn.setStyleSheet("#cancelbtn{"
"background-color: #ECE6E6;"
"border: 1px solid #B10303;"
"color: #B10303;"
"border-radius: 5px;"
"padding: 7px;"
"}")

        self.horizontalLayout_4.addWidget(self.cancelbtn)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.deletebtn = QPushButton(self.widget_6)
        self.deletebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletebtn.setObjectName("deletebtn")
        self.deletebtn.setStyleSheet("#deletebtn{"
"background-color: #B10303;"
"border: 1px solid white;"
"border-radius: 5px;"
"padding: 7px;"
"color: white;"
"}"
""
"#deletebtn:hover{"
"color:black;"
"}")

        self.horizontalLayout_5.addWidget(self.deletebtn)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName("widget_7")

        self.horizontalLayout_3.addWidget(self.widget_7)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
        
        self.cancelbtn.clicked.connect(Dialog.close)
        self.deletebtn.clicked.connect(self.delete_staff)
        
        
        
        
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", "Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", "Are  you sure you want to delete this staff?", None))
        self.emp_id.setText("")
        self.emp_id.hide()
        self.cancelbtn.setText(QCoreApplication.translate("Dialog", "Cancel", None))
        self.deletebtn.setText(QCoreApplication.translate("Dialog", "Delete", None))
    # retranslateUi
    
    
    def delete_staff(self):
        emp_id = self.emp_id.text()
        
        try:
                conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
                cursor = conn.cursor()
                
                delete_query = """
                DELETE FROM employees
                WHERE employee_id = %s
                """
                cursor.execute(delete_query, (emp_id,))
                conn.commit()

                cursor.close()
                conn.close()
                
                # Show a message box with success
                QMessageBox.information(None, "Success", "Staff deleted successfully!")

                # Emit the signal
                self.staff_deleted.emit()
 
                self.dialog.close()

        except Exception as e:
                QMessageBox.critical(None, "Database Error", f"Error: {str(e)}")
