# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
import xml.etree.ElementTree as etree
from urllib.parse import quote

numOfRows = '81'
pageSize = '10'
pageNo = '1'
startPage = '1'
dataTerm = 'DAILY'
sidoName = '경기'
stationName = '정왕동'

key = 'X9vGrzQmY%2FZKQE1aX8QfnF%2BsfHIxQOi%2BDFS%2F4c5XFKCn%2FIXFCVkM3T1NfnvWWi7RVJrthdiLVi2J6dpdxV12ZA%3D%3D'
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
key, numOfRows, pageSize, pageNo, startPage, quote(sidoName))

data = urllib.request.urlopen(url).read()

# print(data.decode('utf-8')) # xml 형태 출력

filename = "test.xml"
f = open(filename, "wb")
f.write(data)
f.close()

# 파싱하기
tree = etree.parse(filename)
root = tree.getroot()



class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

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
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 30, 161, 71))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 30, 161, 71))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(205, 109, 151, 51))
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 169, 241, 41))
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        #여기
        self.sidocomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.sidocomboBox.setGeometry(QtCore.QRect(150, 200, 76, 22))
        self.sidocomboBox.setObjectName("comboBox")
        for item in root.iter('item'):
            self.sidocomboBox.addItem(item.findtext('stationName'))


        #메인끝 미세먼지
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 670, 56, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 670, 56, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 449, 411, 51))
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
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
        self.label_10.setGeometry(QtCore.QRect(35, 590, 60, 60))
        self.label_10.setObjectName("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(155, 590, 60, 60))
        self.label_11.setObjectName("")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(270, 590, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 550, 70, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(150, 550, 70, 20))
        self.label_13.setObjectName("label_13")
        #미세먼지 메뉴 끝
        self.label_2.hide(),self.label_3.hide(),self.label_4.hide(),self.label_5.hide(),self.label_6.hide(),self.label_7.hide(),self.label_8.hide(),self.label_9.hide()
        self.label_10.hide(),self.label_11.hide(),self.label_12.hide(),self.label_13.hide(),self.line.hide()


        StartWindow.setCentralWidget(self.centralwidget)

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
        for item in root.iter('item'):
            if item.findtext('stationName') == stationName:
                self.label_2.setText(_translate("StartWindow", item.findtext('stationName'))) #초기값 정왕동
                self.label_6.setText(_translate("StartWindow", "미세먼지 농도 : " + item.findtext('pm10Value')))
                self.label_4.setText(_translate("StartWindow", item.findtext('o3Value')))
                self.label_5.setText(_translate("StartWindow", item.findtext('khaiValue')))
                if int(item.findtext('pm10Value')) >=0 and int(item.findtext('pm10Value')) <=30:
                    self.label_7.setPixmap(QtGui.QPixmap("Resource/smile2.png"))
                elif int(item.findtext('pm10Value')) >=31 and int(item.findtext('pm10Value')) <=80:
                    self.label_7.setPixmap(QtGui.QPixmap("Resource/smile3.png"))
                elif int(item.findtext('pm10Value')) >= 81 and int(item.findtext('pm10Value')) <= 150:
                    self.label_7.setPixmap(QtGui.QPixmap("Resource/smile1.png"))
                elif int(item.findtext('pm10Value')) >= 151:
                    self.label_7.setPixmap(QtGui.QPixmap("Resource/smile5.png"))
                if float(item.findtext('o3Value')) >= 0 and float(item.findtext('o3Value')) <= 0.030:
                    self.label_10.setPixmap(QtGui.QPixmap("Resource/smallsmile2.png"))
                elif float(item.findtext('o3Value')) >= 0.031 and float(item.findtext('o3Value')) <= 0.090:
                    self.label_10.setPixmap(QtGui.QPixmap("Resource/smallsmile3.png"))
                elif float(item.findtext('o3Value')) >= 0.091 and float(item.findtext('o3Value')) <= 0.150:
                    self.label_10.setPixmap(QtGui.QPixmap("Resource/smallsmile1.png"))
                elif float(item.findtext('o3Value')) >= 0.151:
                    self.label_10.setPixmap(QtGui.QPixmap("Resource/smallsmile5.png"))
                if int(item.findtext('khaiValue')) >= 0 and int(item.findtext('khaiValue')) <= 50:
                    self.label_11.setPixmap(QtGui.QPixmap("Resource/smallsmile2.png"))
                elif int(item.findtext('khaiValue')) >= 51 and int(item.findtext('khaiValue')) <= 100:
                    self.label_11.setPixmap(QtGui.QPixmap("Resource/smallsmile3.png"))
                elif int(item.findtext('khaiValue')) >= 101 and int(item.findtext('khaiValue')) <= 250:
                    self.label_11.setPixmap(QtGui.QPixmap("Resource/smallsmile1.png"))
                elif int(item.findtext('khaiValue')) >= 251:
                    self.label_11.setPixmap(QtGui.QPixmap("Resource/smallsmile5.png"))

        self.label_3.setText(_translate("StartWindow", root[1][0][0][1].text)) #현재 시간
        self.label_8.setText(_translate("StartWindow", "행동요령"))
        self.label_9.setText(_translate("StartWindow", "행동요령방안"))
        self.label_12.setText(_translate("StartWindow", "오존농도"))
        self.label_13.setText(_translate("StartWindow", "통합대기수치"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())

