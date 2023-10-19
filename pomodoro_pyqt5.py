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
        self.workTime = 20 * 5  # work time
        self.breakTime = 5 * 60  # break time
        self.isBreak = False
        self.isRunning = False
        self.timeRemaining = self.workTime

        # Layout and widgets
        layout = QVBoxLayout()
        self.label = QLabel(self.formatTime(self.timeRemaining))
        self.label.setFont(QFont("Arial", 48))
        layout.addWidget(self.label)

        self.start_button = QPushButton("▶️")
        self.start_button.setFont(QFont("Segoe UI Emoji", 12))
        self.start_button.clicked.connect(self.start)
        layout.addWidget(self.start_button)

        self.stop_button = QPushButton("⏸️")
        self.stop_button.setFont(QFont("Segoe UI Emoji", 12))
        self.stop_button.clicked.connect(self.stop)
        layout.addWidget(self.stop_button)

        self.quit_button = QPushButton("❌")
        self.quit_button.setFont(QFont("Segoe UI Emoji", 12))
        self.quit_button.clicked.connect(self.close)
        layout.addWidget(self.quit_button)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    timer = PomodoroTimer()
    timer.show()
    sys.exit(app.exec_())
