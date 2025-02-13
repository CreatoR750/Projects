# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
from test2 import*


class Ui_Dialog(QWidget):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.file_choose = QtWidgets.QPushButton(Dialog)
        self.file_choose.setObjectName("file_choose")
        self.verticalLayout.addWidget(self.file_choose)
        self.file_record = QtWidgets.QPushButton(Dialog)
        self.file_record.setObjectName("file_record")
        self.verticalLayout.addWidget(self.file_record)
        self.label_soundimage = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_soundimage.sizePolicy().hasHeightForWidth())
        self.label_soundimage.setSizePolicy(sizePolicy)
        self.label_soundimage.setText("")
        self.label_soundimage.setScaledContents(True)
        self.label_soundimage.setObjectName("label_soundimage")
        self.verticalLayout.addWidget(self.label_soundimage)
        self.label_image = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setText("")
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")
        self.verticalLayout.addWidget(self.label_image)
        self.label_result = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_result.sizePolicy().hasHeightForWidth())
        #self.label_result.setFixedSize(200,50)

        self.label_result.setText("")
        self.label_result.setFont(QtGui.QFont("Times", 15))
        self.label_result.adjustSize()
        self.label_result.setScaledContents(True)
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)


        self.file_choose.clicked.connect(self.get_image_file)
        self.file_record.clicked.connect(self.record)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.file_choose.setText(_translate("Dialog", "Выбор файла"))
        self.file_record.setText(_translate("Dialog", "Запись"))

    def get_image_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"E:\\Diplom\\Program\\data\\")
        if file_name.endswith('.wav'):
            print(file_name)
            wavelet_test = wavelet_solo(file_name)
            NN = neuralNet('data/test/test.png')

            pixmap=QPixmap('data/test/sound.png')
            small_pixmap=pixmap.scaled(500, 400, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            pixmap2=QPixmap('data/test/show_test.png')

            self.label_soundimage.setPixmap(pgitixmap)
            #self.label_soundimage.scaled(64, 64, QtCore.Qt.KeepAspectRatio)
            self.label_image.setPixmap(pixmap2)


            self.label_result.setText(NN)
        else:
            self.label_image.setPixmap(QPixmap(file_name))
            #self.label_image2.setText(file_name)
            NN = neuralNet(file_name)
            self.label_result.setText(NN)

    def record(self):
        record1 = record()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
