from PySide6.QtCore import QCoreApplication, QMetaObject, QTimer, QTime
from PySide6.QtWidgets import QGridLayout, QLCDNumber, QPushButton, QApplication, QWidget
from PySide6.QtGui import QKeyEvent
from sys import argv

class Ui_Focus_Timer(object):
    def setupUi(self, Focus_Timer):
        if not Focus_Timer.objectName():
            Focus_Timer.setObjectName(u"Focus_Timer")
        Focus_Timer.resize(400, 300)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.handleTimeout)

        self.time = QTime(0, 0)
        self.time.setHMS(0, 45, 0)

        self.gridLayout_2 = QGridLayout(Focus_Timer)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.lcdNumber = QLCDNumber(Focus_Timer)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.display(self.time.toString('mm:ss'))

        self.pushButton = QPushButton(Focus_Timer)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.pressed.connect(self.countdown)

        self.pushButton_2 = QPushButton(Focus_Timer)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.lcdNumber, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Focus_Timer)
        QMetaObject.connectSlotsByName(Focus_Timer)

        self.handleTimeout()
    # setupUi

    def retranslateUi(self, Focus_Timer):
        Focus_Timer.setWindowTitle(QCoreApplication.translate("Focus_Timer", u"Focus Timer", None))
        self.pushButton.setText(QCoreApplication.translate("Focus_Timer", u"Start", None))
        self.pushButton_2.setText(QCoreApplication.translate("Focus_Timer", u"Stop", None))
    # retranslateUi
            
    def countdown(self):
        if not self.timer.isActive():
            self.timer.start()

    def handleTimeout(self):
        self.lcdNumber.display(self.time.toString('mm:ss'))
        if self.time.minute() or self.time.second():
            self.time = self.time.addSecs(-1)
        else:
            self.timer.stop()


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