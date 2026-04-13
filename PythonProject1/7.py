
import sys

from PyQt5.QtCore import QTimer, Qt, QTime
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon

class   Digital_Clock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clock")
        self.setWindowIcon(QIcon("image0.jpg"))
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setGeometry(600,400,300,100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 100px;"
                                      "font-family: Arial;"
                                      "color: rgb(0, 255, 13);")
        self.setStyleSheet("background-color: black")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Digital_Clock()
    clock.show()
    sys.exit(app.exec_())