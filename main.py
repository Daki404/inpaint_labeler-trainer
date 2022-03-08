import sys, os, cv2
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# UI파일 연결
# UI파일 위치를 잘 적어 넣어준다.
form_class = uic.loadUiType("./untitled.ui")[0]
print(type(form_class))


# 프로그램 메인을 담당하는 Class 선언
class MainClass(QWidget, form_class):
    def __init__(self):
        self.img_stat = False
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        # 화면을 보여준다.

        self.open_btn.clicked.connect(self.openImageFile)

        self.show()

    def openImageFile(self):
        self.img_stat = True

        image_file, _ = QFileDialog.getOpenFileName(self, "Open Image", os.getenv('HOME'), "Images (*.png *.jpeg *.jpg *.bmp)")

        if image_file:
            print(image_file)
            self.img_label.open(image_file)
            '''
            self.image = QImage()
            self.image.load(image_file)
            self.converted_image = self.convertCVToQImage(image_file)
            self.label_9.open(self.converted_image)
            self.img_label.setPixmap(QPixmap.fromImage(self.converted_image).scaled(
                self.img_label.width(), self.img_label.height(), Qt.KeepAspectRatioByExpanding))
            self.adjustSize()'''

        else:
            QMessageBox.information(self, "Error", "No image was loaded.", QMessageBox.Ok)

    def convertCVToQImage(self, image_file):
        cv_image = cv2.imread(image_file)
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)

        height, width, channels = cv_image.shape
        bytes_per_line = width * channels

        converted_Qt_image = QImage(cv_image, width, height, bytes_per_line, QImage.Format_RGB888)
        return converted_Qt_image

    def resizeEvent(self, event):
        if self.img_stat:
            self.img_label.setPixmap(QPixmap.fromImage(self.image).scaled(
                self.img_label.width(), self.img_label.height(), Qt.KeepAspectRatioByExpanding, ))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()