# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import cv2


class Ui_Labler(object):
    def setupUi(self, Labler):
        Labler.setObjectName("Labler")
        #Labler.resize(1024, 640)

        Labler.setMinimumSize(QSize(1024, 640))
        Labler.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout_2 = QHBoxLayout(Labler)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QLabel(Labler)
        font = QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border: 4px solid black;\n"
"border-bottom: 2px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QLabel(Labler)
        font = QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 4px solid black;\n"
"border-bottom: 2px;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QLabel(Labler)
        font = QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: 4px solid black;\n"
"border-bottom: 2px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QLabel(Labler)
        font = QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: 4px solid black;\n"
"border-bottom: 2px;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QLabel(Labler)
        font = QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border: 4px solid black;\n"
"")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #self.label_9 = QLabel(Labler)
        self.label_9 = PaintBrush(Labler)
        self.label_9.setStyleSheet("border: 4px solid black;")
        self.label_9.setText("ho")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.horizontalLayout_3.setStretch(0, 5)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listView = QListView(Labler)
        self.listView.setObjectName("listView")
        self.verticalLayout_2.addWidget(self.listView)

        self.widget_2 = QWidget(Labler)
        self.widget_2.setObjectName("widget_2")

        self.crop_btn = QPushButton('Crop')
        self.crop_btn.clicked.connect(self.crop)
        self.crop_layout = QVBoxLayout()
        self.crop_layout.addWidget(self.crop_btn)
        self.verticalLayout_2.addLayout(self.crop_layout)

        self.widget = QWidget(Labler)
        self.widget.setStyleSheet("background-color: lemon;")
        self.widget.setObjectName("widget")
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Labler)
        QMetaObject.connectSlotsByName(Labler)

    def retranslateUi(self, Labler):
        _translate = QCoreApplication.translate
        Labler.setWindowTitle(_translate("Labler", "Form"))
        self.label.setText(_translate("Labler", "Open"))
        self.label_2.setText(_translate("Labler", "Open Dir"))
        self.label_3.setText(_translate("Labler", "Next Image"))
        self.label_4.setText(_translate("Labler", "Prev Image"))
        self.label_5.setText(_translate("Labler", "Save"))

    def crop(self, Labler):
        self.label_9.crop(100)


class PaintBrush(QLabel):
    def __init__(self, parent):
        self.img_stat = False
        super().__init__(parent)
        self.save_act = QShortcut(QKeySequence('Ctrl+S'), self)
        self.save_act.activated.connect(self.save)

        self.clear_act = QShortcut(QKeySequence('Ctrl+Z'), self)
        self.clear_act.activated.connect(self.clear)
        self.open('../imgs/sillicon.jpg')

    def open(self, image):
        print('open!')
        self.img_stat = True
        self.img = cv2.imread(image)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.h, self.w, self.c = self.img.shape

        self.image = QImage(self.img.data, self.w, self.h, self.w * self.c, QImage.Format_RGB888)
        self.origin = self.image.copy()
        self.board = QImage(self.w, self.h, QImage.Format_RGB888)
        self.board.fill(Qt.black)
        self.drawing = False
        self.brush_size = 30
        self.brush_color = Qt.yellow
        self.last_point = QPoint()
        self.resize(self.image.size())
        self.origin_size = self.width(), self.height()
        self.show()

    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.board, self.board.rect())
        canvas.drawImage(self.rect(), self.image, self.image.rect())

        painter = QPainter(self.image)
        painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = e.pos()

    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.last_point, e.pos())

            painter = QPainter(self.board)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.last_point, e.pos())

            self.last_point = e.pos()
            self.new_img = self.image.copy()
            self.update()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False


        '''if self.img_stat:
            self.img_label.setPixmap(QPixmap.fromImage(self.image).scaled(
                self.img_label.width(), self.img_label.height(), Qt.KeepAspectRatioByExpanding, ))'''

    def save(self):
        self.fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if self.fpath:
            self.board.save(self.fpath)

    def clear(self):
        self.image = self.origin
        self.origin = self.image.copy()
        self.board.fill(Qt.black)
        self.update()

    def crop(self, size):
        cnt = 0
        if ((y_scan := self.h - size) < 0) or ((x_scan := self.w - size) < 0):
            print("size error")
        else:
            board_img = cv2.imread(self.fpath)

            for i in range(0, y_scan + 1, 20):
                for j in range(0, x_scan + 1, 20):
                    if len(np.unique(board_img[i: i + size, j: j + size])) == 1:
                        cnt += 1
                        cropped_img = self.img[i: i + size, j: j + size]
                        cv2.imwrite(f'{self.fpath[:-4]}{cnt}{self.fpath[-4:]}', cropped_img)





if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Labler = QWidget()
    ui = Ui_Labler()
    ui.setupUi(Labler)
    Labler.show()
    sys.exit(app.exec_())
