import sys
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.elapsed_centiseconds = 0
        self.setWindowTitle("Stopwatch")
        self.resize(200,180)

        self.time_label = QLabel("00:00:00",self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:32px;")

        self.start_button = QPushButton("Start",self)
        self.stop_button = QPushButton("Stop",self)
        self.reset_button = QPushButton("Reset",self)

        layout = QVBoxLayout()