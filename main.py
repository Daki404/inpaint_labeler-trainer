import sys, os, cv2
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from glob import glob
import numpy as np

from worker import Worker

form_class = uic.loadUiType("./main.ui")[0]


class PaintBrush(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.items = []

        self.start = QPointF()
        self.end = QPointF()

        self.pen = QPen(Qt.yellow, 20)

        self.graphicPixmap = None
        self.back_img = None
        self.draw_img = None

        self.setRenderHint(QPainter.HighQualityAntialiasing)

    def moveEvent(self, e):
        rect = QRectF(self.rect())
        rect.adjust(0, 0, -2, -2)

        self.scene.setSceneRect(rect)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.start = e.pos()
            self.end = e.pos()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            self.end = e.pos()
            path = QPainterPath()
            path.moveTo(self.start)
            path.lineTo(self.end)
            self.scene.addPath(path, self.pen)

            painter = QPainter(self.draw_img)
            painter.setPen(self.pen)
            painter.drawLine(self.start, e.pos())

            self.start = e.pos()

    def set_image(self, img_path):
        self.back_img = QPixmap(img_path)
        self.back_img = self.back_img.scaled(int(self.scene.width()), int(self.scene.height()))

        if self.graphicPixmap is not None:
            self.scene.removeItem(self.graphicPixmap)
        self.graphicPixmap = QGraphicsPixmapItem(self.back_img)
        self.scene.addItem(self.graphicPixmap)

        self.draw_img = QImage(QSize(int(self.scene.width()), int(self.scene.height())), QImage.Format_RGB32)
        self.draw_img.fill(Qt.black)


class MainClass(QWidget, form_class):
    def __init__(self):
        self.img_stat = False
        QMainWindow.__init__(self)
        self.setupUi(self)
        # QGraph의 그리는 화면
        self.img_show = PaintBrush(self)
        self.img_view.addWidget(self.img_show)

        self.file_path = None
        self.crop_cnt = 0
        self.crop_list = None

        # 파일 관리 모델
        self.file_model = QFileSystemModel()
        self.file_model.setFilter(QDir.NoDotAndDotDot | QDir.Files)
        self.dir_view.setModel(self.file_model)
        self.dir_view.setRootIndex(self.file_model.index(QDir.rootPath()))

        #버튼 관리
        self.open_btn.clicked.connect(self.openImageFile)
        self.open_dir_btn.clicked.connect(self.openDir)
        self.next_btn.clicked.connect(self.next_image)
        self.prev_btn.clicked.connect(self.prev_image)
        self.save_btn.clicked.connect(self.save_label)

        self.crop_btn.clicked.connect(self.crop_image)
        self.train_btn.clicked.connect(self.train_model)

        # Terminal - signal
        self.worker = Worker()
        self.worker.outSignal.connect(self.logging)
        self.show()

    def openImageFile(self, image_file=False):
        self.img_stat = True
        if not image_file:
            image_file, _ = QFileDialog.getOpenFileName(self, "Open Image", os.getenv('HOME'), "Images (*.png *.jpeg *.jpg *.bmp)")

        if image_file:
            self.img_show.set_image(image_file)
        else:
            QMessageBox.information(self, "Error", "No image was loaded.", QMessageBox.Ok)

    def openDir(self):
        self.dir_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.dir_view.setRootIndex(self.file_model.setRootPath(self.dir_path))

        self.file_path = glob(f'{self.dir_path}/*')
        self.file_idx = 0
        self.file_len = len(self.file_path)
        self.openImageFile(self.file_path[self.file_idx])

    def next_image(self):
        if self.file_path is not None:
            self.file_idx += 1
            if self.file_idx < self.file_len:
                self.openImageFile(self.file_path[self.file_idx])
            else:
                QMessageBox.information(self, "Error", "End of images.", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Error", "No directory.", QMessageBox.Ok)

    def prev_image(self):
        if self.file_path is not None:
            self.file_idx -= 1
            if self.file_idx >= 0:
                self.openImageFile(self.file_path[self.file_idx])
            else:
                QMessageBox.information(self, "Error", "First of images.", QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Error", "No directory.", QMessageBox.Ok)

    def save_label(self):
        img = QPixmap(self.img_show.grab(self.img_show.sceneRect().toRect()))
        img.save('wow.jpg')
        self.img_show.draw_img.save('wow2.jpg')

    def crop_image(self):
        self.crop_cnt = 0
        self.crop_list = []
        size = 100
        if ((y_scan := int(self.img_show.scene.height()) - size) < 0) or ((x_scan := int(self.img_show.scene.width()) - size) < 0):
            print("size error")
        else:
            self.img_show.draw_img.save('back_tmp.jpg')
            self.img_show.back_img.save('real_tmp.jpg')

            board_img, real_img = cv2.imread('back_tmp.jpg'), cv2.imread('real_tmp.jpg')

            for i in range(0, y_scan + 1, int(self.y_jump_in.text())):
                for j in range(0, x_scan + 1, int(self.x_jump_in.text())):
                    if len(np.unique(board_img[i: i + size, j: j + size])) == 1:
                        self.crop_cnt += 1
                        cropped_img = real_img[i: i + size, j: j + size]
                        self.crop_list.append(cropped_img)
                        #cv2.imwrite(f'crop_imgs/{self.crop_cnt}.jpg', cropped_img)

        self.cnt_label.setText(str(self.crop_cnt))

    def train_model(self):
        command = "python train.py --obj sillicon --data_path datasets"
        self.worker.run_command(command, shell=True)

    def logging(self, string):
        print('시그널 도착')
        self.terminal.append(string.strip())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainClass()
    app.exec_()