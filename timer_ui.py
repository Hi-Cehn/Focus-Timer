from PySide6.QtCore import QCoreApplication, QMetaObject, Slot
from PySide6.QtWidgets import QGridLayout, QLCDNumber, QPushButton, QApplication, QWidget
from sys import argv
import timer, main
import datetime, time

class Ui_Focus_Timer(object):
    def setupUi(self, Focus_Timer):
        if not Focus_Timer.objectName():
            Focus_Timer.setObjectName(u"Focus_Timer")
        Focus_Timer.resize(400, 300)
        self.gridLayout_2 = QGridLayout(Focus_Timer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lcdNumber = QLCDNumber(Focus_Timer)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.display("00:00")
        

        self.gridLayout.addWidget(self.lcdNumber, 0, 0, 1, 2)

        self.pushButton = QPushButton(Focus_Timer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.pressed.connect(self.start_timer)

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(Focus_Timer)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Focus_Timer)

        QMetaObject.connectSlotsByName(Focus_Timer)
    # setupUi

    def retranslateUi(self, Focus_Timer):
        Focus_Timer.setWindowTitle(QCoreApplication.translate("Focus_Timer", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Focus_Timer", u"Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("Focus_Timer", u"Stop", None))
    # retranslateUi
            
        
    def start_timer(self, focus_duration=2700):
        end_time, prev = main.start(focus_duration)
        self.lcdNumber.display(timer.timer_visual(focus_duration))

        while True:
            current = datetime.datetime.now()

            delta = current - prev

            if delta.total_seconds() >= 1:
                new_time = timer.visual_update(focus_duration)
                self.lcdNumber.display(new_time)
                
            if end_time <= current:
                print("Time's up.")
                break

            time.sleep(0.01)

class window(QWidget, Ui_Focus_Timer):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


def create_main_window():
    app = QApplication(argv)
    gui = window()
    gui.show()
    app.exec()

create_main_window()