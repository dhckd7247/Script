# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextTest.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
import xml.etree.ElementTree as etree
from urllib.parse import quote

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 531, 361))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        numOfRows = '81'
        pageSize = '10'
        pageNo = '1'
        startPage = '1'
        dataTerm = 'DAILY'
        sidoName = '경기'

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

        # print(root.tag, root.attrib)

        # for stationName in root.iter('stationName'):
        #   print(stationName.text)

        # for ele in root.findall("body/items/item/pm10Value"):
        #   print(ele.tag, ele.text)


        # print(root[1][0][0][2].tag, root[1][0][0][2].text) #배열순서(인덱스)로 접근하는방법

        for item in root.iter('item'):
            self.label.setText(_translate("MainWindow", item.findtext('stationName')))
            print(item.findtext('stationName'), item.findtext('pm10Value')) #item내의 지역명과 미세먼지농도를 모두 출력
            #if item.findtext('stationName') == '정왕동':  # 특정 동네의 정보가 보고싶다면
             #   self.label.setText(_translate("MainWindow",item.findtext('stationName') ))
              #  print(item.findtext('stationName'), item.findtext('pm10Value'))

        #self.label.setText(_translate("MainWindow", root[1][0][0][2].tag))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

