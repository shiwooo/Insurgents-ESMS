# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deletestaffdialogVSFCds.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, pyqtSignal)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *
import psycopg2


class DeleteSchedDialog(QObject):
    delete_update = pyqtSignal()
    
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 207)
        self.dialog = Dialog
        Dialog.setMinimumSize(QSize(375, 207))
        Dialog.setMaximumSize(QSize(375, 207))
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(236, 230, 230);")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.sched_id = QLabel(self.widget_4)
        self.sched_id.setObjectName(u"sched_id")
        self.sched_id.setGeometry(QRect(10, 30, 55, 16))

        self.horizontalLayout_3.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cancelbtn = QPushButton(self.widget_5)
        self.cancelbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelbtn.setObjectName(u"cancelbtn")
        self.cancelbtn.setStyleSheet(u"#cancelbtn{\n"
"background-color: #ECE6E6;\n"
"border: 1px solid #B10303;\n"
"color: #B10303;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.cancelbtn)


        self.horizontalLayout_3.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.deletebtn = QPushButton(self.widget_6)
        self.deletebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletebtn.setObjectName(u"deletebtn")
        self.deletebtn.setStyleSheet(u"#deletebtn{\n"
"background-color: #B10303;\n"
"border: 1px solid white;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"color: white;\n"
"}\n"
"\n"
"#deletebtn:hover{\n"
"color:black;\n"
"}")

        self.horizontalLayout_5.addWidget(self.deletebtn)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")

        self.horizontalLayout_3.addWidget(self.widget_7)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
        
        self.deletebtn.clicked.connect(self.delete_staff)
        self.cancelbtn.clicked.connect(Dialog.close)
        
        
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Are  you sure you want to delete this schedule?", None))
        self.sched_id.setText("")
        self.sched_id.hide()
        self.cancelbtn.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.deletebtn.setText(QCoreApplication.translate("Dialog", u"Delete", None))
    # retranslateUi
    
    
    def delete_staff(self):
        sched_id = self.sched_id.text()

        try:
                conn = psycopg2.connect(host='localhost', dbname='insurgent_db', user='postgres', password='admin', port='5432')
                cursor = conn.cursor()
                
                delete_query = """
                DELETE FROM schedules
                WHERE schedule_id = %s
                """
                cursor.execute(delete_query, (sched_id,))
                conn.commit()

                cursor.close()
                conn.close()
                
                # Show a message box with success
                QMessageBox.information(None, "Success", "Schedule deleted successfully!")
                self.delete_update.emit()
                self.dialog.close()

        except Exception as e:
                QMessageBox.critical(None, "Database Error", f"Error: {str(e)}")

