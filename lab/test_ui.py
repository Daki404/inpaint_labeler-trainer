import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QGridLayout, QPushButton, QTextEdit, QWidget

from worker import Worker


class TestUI(QWidget):
    def __init__(self):
        super().__init__()
        self.worker = Worker()
        self.worker.outSignal.connect(self.logging)
        self.btn1 = QPushButton("Button1")
        self.btn2 = QPushButton("Button2")
        self.btn3 = QPushButton("Button3")
        self.result = QTextEdit()
        self.init_ui()

    def init_ui(self):
        self.btn1.clicked.connect(self.press_btn1)
        self.btn2.clicked.connect(self.press_btn2)
        self.btn3.clicked.connect(self.press_btn3)

        lay = QGridLayout(self)
        lay.addWidget(self.btn1, 0, 0)
        lay.addWidget(self.btn2, 0, 1)
        lay.addWidget(self.btn3, 0, 2)
        lay.addWidget(self.result, 1, 0, 1, 3)

    @pyqtSlot()
    def press_btn1(self):
        command1 = "dir"
        path = "/"
        self.worker.run_command(command1, cwd=path)

    @pyqtSlot()
    def press_btn2(self):
        command2 = "cd"
        path = "/"
        self.worker.run_command(command2, cwd=path, shell=True)

    @pyqtSlot()
    def press_btn3(self):
        command3 = "test.bat"
        path = "/"
        self.worker.run_command(command3, cwd=path, shell=True)

    @pyqtSlot(str)
    def logging(self, string):
        self.result.append(string.strip())


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    ex = TestUI()
    ex.show()
    sys.exit(APP.exec_())