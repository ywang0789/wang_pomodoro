# same but in pyqt5 ...

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMessageBox,
)
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont


class PomodoroTimer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("make_me_productive.exe")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer = PomodoroTimer()
    timer.show()
    sys.exit(app.exec_())
