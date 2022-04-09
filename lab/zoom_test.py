from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self, *args):
        super().__init__(*args)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button_zoom_in = QPushButton('Zoom IN', self)
        self.button_zoom_in.clicked.connect(self.on_zoom_in)
        self.layout.addWidget(self.button_zoom_in)

        self.button_zoom_out = QPushButton('Zoom OUT', self)
        self.button_zoom_out.clicked.connect(self.on_zoom_out)
        self.layout.addWidget(self.button_zoom_out)

        self.pixmap = QPixmap('../imgs/sillicon.jpg')

        self.label = QLabel(self)
        self.label.setPixmap(self.pixmap)
        self.layout.addWidget(self.label)

        self.scale = 1

        self.show()

    def on_zoom_in(self, event):
        self.scale *= 2
        self.resize_image()

    def on_zoom_out(self, event):
        self.scale /= 2
        self.resize_image()

    def resize_image(self):
        size = self.pixmap.size()

        scaled_pixmap = self.pixmap.scaled(self.scale * size)

        self.label.setPixmap(scaled_pixmap)

# --- main ---

app = QApplication([])
win = MyApp()
app.exec()