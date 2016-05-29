# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(597, 697)
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Resource/weather.png"))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 30, 161, 71))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 30, 161, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 30, 161, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 140, 56, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 190, 56, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 640, 56, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(150, 640, 56, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 480, 56, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(180, 240, 230, 200))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(410, 590, 56, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 630, 56, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 590, 56, 12))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(150, 590, 56, 12))
        self.label_11.setObjectName("label_11")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(270, 590, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 550, 56, 12))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(150, 550, 56, 12))
        self.label_13.setObjectName("label_13")

        self.label_2.hide(),self.label_3.hide(),self.label_4.hide(),self.label_5.hide(),self.label_6.hide(),self.label_7.hide(),self.label_8.hide(),self.label_9.hide()
        self.label_10.hide(),self.label_11.hide(),self.label_12.hide(),self.label_13.hide(),self.line.hide()


        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)
        self.pushButton.clicked.connect(self.ClickFb)
        self.pushButton_2.clicked.connect(self.pushButton_3.click)

        QtCore.QMetaObject.connectSlotsByName(StartWindow)

    def ClickFb(self):
        self.label_2.show(), self.label_3.show(), self.label_4.show(), self.label_5.show(), self.label_6.show(), self.label_7.show(), self.label_8.show(), self.label_9.show()
        self.label_10.show(), self.label_11.show(), self.label_12.show(), self.label_13.show(), self.line.show()






    def retranslateUi(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "MainWindow"))
        self.pushButton.setText(_translate("StartWindow", "미세먼지"))
        self.pushButton_2.setText(_translate("StartWindow", "자외선"))
        self.pushButton_3.setText(_translate("StartWindow", "평균수치"))
        self.label_2.setText(_translate("StartWindow", "지역"))
        self.label_3.setText(_translate("StartWindow", "날짜"))
        self.label_4.setText(_translate("StartWindow", "초미수치"))
        self.label_5.setText(_translate("StartWindow", "통합수치"))
        self.label_6.setText(_translate("StartWindow", "미세먼지"))
        self.label_8.setText(_translate("StartWindow", "행동요령"))
        self.label_9.setText(_translate("StartWindow", "행동요령방안"))
        self.label_10.setText(_translate("StartWindow", "초미아이콘"))
        self.label_11.setText(_translate("StartWindow", "통합아이콘"))
        self.label_12.setText(_translate("StartWindow", "지금초미"))
        self.label_13.setText(_translate("StartWindow", "지금통합"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())

