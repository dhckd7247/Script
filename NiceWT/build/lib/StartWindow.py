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
import mimetypes
import mysmtplib
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

###############################미세먼지#################################################################################################################################################
numOfRows = '81'
pageSize = '10'
pageNo = '1'
startPage = '1'
dataTerm = 'DAILY'
sidoName = '경기'
sidoList = [' ', '서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주']
stationName = '정왕동'
action = ''
stateBT = 0

key = 'X9vGrzQmY%2FZKQE1aX8QfnF%2BsfHIxQOi%2BDFS%2F4c5XFKCn%2FIXFCVkM3T1NfnvWWi7RVJrthdiLVi2J6dpdxV12ZA%3D%3D'#창주키
#'qvrSOFP%2FQaIF3w89WIvoxu%2BvcrCYf5q1ln7n75YYhPVW3WZP99mM1jrseOHDjFuVqPm3FEsH5HhzYx0LWg1m2Q%3D%3D'#영준키


url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
key, numOfRows, pageSize, pageNo, startPage, quote(sidoName))

data = urllib.request.urlopen(url).read()

#파일 저장
filename = "test.xml"
f = open(filename, "wb")
f.write(data)
f.close()

# 파싱하기
tree = etree.parse(filename)
root = tree.getroot()
########################################################################################################################################################################################



#################################자외선#################################################################################################################################################
sidoList2 = [' ', '1100000000', '2600000000', '2700000000', '2800000000', '2900000000', '3000000000', '3100000000', '4100000000', '4200000000',
             '4300000000', '4400000000', '4500000000', '4600000000', '4700000000', '4800000000', '5011000000']

key2 = 'X9vGrzQmY%2FZKQE1aX8QfnF%2BsfHIxQOi%2BDFS%2F4c5XFKCn%2FIXFCVkM3T1NfnvWWi7RVJrthdiLVi2J6dpdxV12ZA%3D%3D' #창주키
AreaNo = '1100000000'
url2 = 'http://203.247.66.146/iros/RetrieveLifeIndexService/getUltrvLifeList?ServiceKey=%s&AreaNo=%s&numOfRows=999&pageSize=999&pageNo=1&startPage=1' % (key2, AreaNo)

data2 = urllib.request.urlopen(url2).read()

#파일 저장
filename2 = "test2.xml"
f2 = open(filename2, "wb")
f2.write(data2)
f2.close()

#파싱하기
tree2 = etree.parse(filename2)
root2 = tree2.getroot()
#########################################################################################################################################################################################


###########메일 정보###############
host = "smtp.gmail.com" # Gmail STMP 서버 주소.
port = "587"

senderAddr = "dhckd7247@gmail.com"     # 보내는 사람 email 주소.
recipientAddr = "obregas@naver.com"   # 받는 사람 email 주소.

msg = MIMEBase("multipart", "alternative")
msg['Subject'] = "미세먼지 및 자외선 정보 메일입니다."
msg['From'] = senderAddr
msg['To'] = recipientAddr
str1, str2, str3, str4, str5 = ' ', ' ', ' ', ' ', ' '

#########################################

class Ui_StartWindow(object):
    global sidoName, stationName, filename, data, url, tree, root
    def setupUi(self, StartWindow):
        global stateBT
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)

        font2 = QtGui.QFont()
        font2.setFamily("맑은 고딕")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)

        font3 = QtGui.QFont()
        font3.setFamily("맑은 고딕")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)

        StartWindow.setObjectName("StartWindow")
        StartWindow.resize(597, 697)
        self.centralwidget = QtWidgets.QWidget(StartWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Resource/background.jpg"))
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
        self.pushButton_3.setGeometry(QtCore.QRect(410, 30, 161, 71))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(225, 109, 151, 51))
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(182, 169, 241, 41))
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        #콤보박스
        self.sidocomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.sidocomboBox.setGeometry(QtCore.QRect(30, 125, 50, 22))
        self.sidocomboBox.setObjectName("comboBox")
        for item in sidoList:
            self.sidocomboBox.addItem(item)


        self.stationcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.stationcomboBox.setGeometry(QtCore.QRect(80, 125, 90, 22))
        self.stationcomboBox.setObjectName("comboBox2")
        self.stationcomboBox.addItem(' ')
        for item in root.iter('item'):
            self.stationcomboBox.addItem(item.findtext('stationName'))

        #메인끝 미세먼지
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(45, 660, 56, 12))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(177, 660, 56, 12))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(95, 449, 411, 51))
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(190, 240, 230, 200))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(300, 550, 300, 130))
        self.label_8.setObjectName("label_8")
        self.label_8.setFont(font2)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(410, 630, 56, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(35, 590, 60, 60))
        self.label_10.setObjectName("")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(155, 590, 60, 60))
        self.label_11.setObjectName("")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(35, 560, 70, 20))
        self.label_12.setObjectName("label_12")
        self.label_12.setFont(font3)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(140, 560, 100, 20))
        self.label_13.setObjectName("label_13")
        self.label_13.setFont(font3)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 250, 401, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 350, 401, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 450, 401, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")


        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 250, 161, 20))
        self.label_14.setObjectName("label_14")
        self.label_14.setFont(font3)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(70, 350, 171, 20))
        self.label_15.setObjectName("label_15")
        self.label_15.setFont(font3)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(45, 450, 161, 20))
        self.label_16.setObjectName("label_16")
        self.label_16.setFont(font3)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(350, 500, 101, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setFont(font3)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 500, 101, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setFont(font3)

        #미세먼지 메뉴 끝
        self.label_2.hide(),self.label_3.hide(),self.label_4.hide(),self.label_5.hide(),self.label_6.hide(),self.label_7.hide(),self.label_8.hide(),self.label_9.hide()
        self.label_10.hide(),self.label_11.hide(),self.label_12.hide(),self.label_13.hide(), self.label_14.hide(), self.label_15.hide(), self.label_16.hide() , self.lineEdit.hide(), self.lineEdit_2.hide(), self.lineEdit_3.hide()
        self.pushButton_4.hide(), self.pushButton_5.hide()
        StartWindow.setCentralWidget(self.centralwidget)
        StartWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(StartWindow)
        self.pushButton.clicked.connect(self.ClickFb)
        self.pushButton_2.clicked.connect(self.ClickSb)
        self.pushButton_3.clicked.connect(self.ClickTb)
        self.pushButton_4.clicked.connect(self.SendMail)
        self.pushButton_5.clicked.connect(self.ResetBT)
        self.sidocomboBox.currentIndexChanged.connect(self.sido_select,self.sidocomboBox.currentIndex()) # 시도를 선택햇을때
        self.stationcomboBox.currentIndexChanged.connect(self.dustshow, self.stationcomboBox.currentIndex())
        QtCore.QMetaObject.connectSlotsByName(StartWindow)


    def sido_select(self,Indexnum):
        global numOfRows,pageSize,pageNo,startPage,dataTerm,sidoName,sidoList,stationName,action,f,filename,tree,root,key,url,data, sidoList2, data2, url2, key2, AreaNo, tree2, root2,stateBT, f2, filename2, str1, str2
        sidoName = sidoList[Indexnum]
        AreaNo = sidoList2[Indexnum]
        str1 = sidoList[Indexnum] # 시도 이름
        str2 = root[1][0][0][1].text # 현재 시간

        print(sidoName)
        print(AreaNo)

        url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey=%s&numOfRows=%s&pageSize=%s&pageNo=%s&startPage=%s&sidoName=%s' % (
            key, numOfRows, pageSize, pageNo, startPage, quote(sidoName))
        url2 = 'http://203.247.66.146/iros/RetrieveLifeIndexService/getUltrvLifeList?ServiceKey=%s&AreaNo=%s&numOfRows=999&pageSize=999&pageNo=1&startPage=1' % (key2, AreaNo)

        data = urllib.request.urlopen(url).read()
        data2 = urllib.request.urlopen(url2).read()

        # 파일 저장
        filename = "test.xml"
        f = open(filename, "wb")
        f.write(data)
        f.close()

        filename2 = "test2.xml"
        f2 = open(filename2, "wb")
        f2.write(data2)
        f2.close()

        # 파싱하기
        tree = etree.parse(filename)
        root = tree.getroot()

        tree2 = etree.parse(filename2)
        root2 = tree2.getroot()

        if(stateBT==1 or stateBT==0):
            self.stationcomboBox.clear()
            for item in root.iter('item'):
                self.stationcomboBox.addItem(item.findtext('stationName'))

        if stateBT == 2 :
            self.ultrashow(self.stationcomboBox.currentIndex())

        # if stateBT == 3 :
        #     self.SendMail()

    def dustshow(self,Indexnum):
        global numOfRows, pageSize, pageNo, startPage, dataTerm, sidoName, sidoList, stationName, action, f, filename, tree, root, key, url, data, str3, str4
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("StartWindow", root[1][0][Indexnum][0].text))
        stationName = root[1][0][Indexnum][0].text
        str3 = stationName
        #print(root[1][0][Indexnum][0].text)

        for item in root.iter('item'):
            if item.findtext('stationName') == stationName:
                self.label_2.setText(_translate("StartWindow", item.findtext('stationName')))  # 초기값 정왕동
                self.label_6.setText(_translate("StartWindow", "미세먼지 농도 : " + item.findtext('pm10Value') + " ㎍/㎥"))
                str4 = item.findtext('pm10Value')
                self.label_4.setText(_translate("StartWindow", item.findtext('o3Value')))
                self.label_5.setText(_translate("StartWindow", item.findtext('khaiValue')))
                if int(item.findtext('pm10Value')) >= 0 and int(item.findtext('pm10Value')) <= 30:
                    self.label_7.setPixmap(QtGui.QPixmap("Resource/smile2.png"))
                    action = "쾌적합니다.\n실외활동 마음껏 하세요."
                elif int(item.findtext('pm10Value')) >= 31 and int(item.findtext('pm10Value')) <= 80:
                    self.label_7.setPixmap(QtGui.QPixmap("Resource/smile3.png"))
                    action = "몸 상태에 따라 유의하세요."
                elif int(item.findtext('pm10Value')) >= 81 and int(item.findtext('pm10Value')) <= 150:
                    self.label_7.setPixmap(QtGui.QPixmap("Resource/smile1.png"))
                    action = "장시간 무리한 실외활동은 자제하세요.\n마스크 착용 권장합니다."
                elif int(item.findtext('pm10Value')) >= 151:
                    self.label_7.setPixmap(QtGui.QPixmap("Resource/smile5.png"))
                    action = "실내활동 하세요.\n마스크 필수 착용 권장합니다."
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

        self.label_3.setText(_translate("StartWindow", root[1][0][0][1].text))  # 현재 시간
        self.label_8.setText(_translate("StartWindow", action))
        # self.label_9.setText(_translate("StartWindow", "행동요령방안"))
        self.label_12.setText(_translate("StartWindow", "오존농도"))
        self.label_13.setText(_translate("StartWindow", "통합대기수치"))

    def ultrashow(self, Indexnum):
        global root2, AreaNo, sidoList2, url2, data2, filename2, tree2, sidoList, root, action, str5
        _translate = QtCore.QCoreApplication.translate
        print(root2[1][0][3].text) # 자외선수치
        str5 = root2[1][0][3].text
        for item in root2.iter('IndexModel'):
            print(sidoName)
            self.label_2.setText(_translate("StartWindow", sidoName))
            self.label_3.setText(_translate("StartWindow", root[1][0][0][1].text))
            if(int(item.findtext('tomorrow'))) < 10: # 수치를 아이콘 정 중앙에 맞추기 위한 코드
                self.label_4.setText(_translate("StartWindow", '   ' + item.findtext('tomorrow')))
            else:
                self.label_4.setText(_translate("StartWindow", '  ' + item.findtext('tomorrow')))
            if(int(item.findtext('theDayAfterTomorrow'))) < 10: # 수치를 아이콘 정 중앙에 맞추기 위한 코드
                self.label_5.setText(_translate("StartWindow", ' ' + item.findtext('theDayAfterTomorrow')))
            else:
                self.label_5.setText(_translate("StartWindow", item.findtext('theDayAfterTomorrow')))
            if int(item.findtext('today')) >= 0 and int(item.findtext('today')) <= 2:
                self.label_6.setText(_translate("StartWindow", "자외선 수치 : " + item.findtext('today') + " (낮음)"))
                self.label_7.setPixmap(QtGui.QPixmap("Resource/smile2.png"))
                action = "자외선 걱정하지 않으셔도 됩니다.\n실외활동 마음껏 하세요."
            elif int(item.findtext('today')) >= 3 and int(item.findtext('today')) <= 5:
                self.label_6.setText(_translate("StartWindow", "자외선 수치 : " + item.findtext('today') + " (보통)"))
                self.label_7.setPixmap(QtGui.QPixmap("Resource/smile3.png"))
                action = "2~3시간 노출시 피부 화상을 입을 수\n있습니다.\n자외선 차단제를 바르세요."
            elif int(item.findtext('today')) >= 6 and int(item.findtext('today')) <= 7:
                self.label_6.setText(_translate("StartWindow", "자외선 수치 : " + item.findtext('today') + " (높음)"))
                self.label_7.setPixmap(QtGui.QPixmap("Resource/smile1.png"))
                action = "1~2시간 노출시 피부 화상을 입을 수\n있습니다.\n자외선 차단제를 정기적으로 바르세요.\n긴 소매와 모자 착용을 권장합니다."
            elif int(item.findtext('today')) >= 8:
                self.label_6.setText(_translate("StartWindow", "자외선 수치 : " + item.findtext('today') + " (매우 높음)"))
                self.label_7.setPixmap(QtGui.QPixmap("Resource/sunglass.png"))
                action = "수십분만 노출해도 피부 화상을 입을 수\n있습니다.\n왠만하면 실내에 머무르세요.\n꼭 외출해야 된다면 자외선 차단제를\n무조건 바르시고 긴 소매와 모자,\n선글라스를 착용하세요."

            if int(item.findtext('tomorrow')) >= 0 and int(item.findtext('tomorrow')) <= 2:
                self.label_10.setPixmap(QtGui.QPixmap("Resource/smallsmile2.png"))
            elif int(item.findtext('tomorrow')) >= 3 and int(item.findtext('tomorrow')) <= 5:
                self.label_10.setPixmap(QtGui.QPixmap("Resource/smallsmile3.png"))
            elif int(item.findtext('tomorrow')) >= 6 and int(item.findtext('tomorrow')) <= 7:
                self.label_10.setPixmap(QtGui.QPixmap("Resource/smallsmile1.png"))
            elif int(item.findtext('tomorrow')) >= 8:
                self.label_10.setPixmap(QtGui.QPixmap("Resource/smallsunglass.png"))
            if int(item.findtext('theDayAfterTomorrow')) >= 0 and int(item.findtext('theDayAfterTomorrow')) <= 2:
                self.label_11.setPixmap(QtGui.QPixmap("Resource/smallsmile2.png"))
            elif int(item.findtext('theDayAfterTomorrow')) >= 3 and int(item.findtext('theDayAfterTomorrow')) <= 5:
                self.label_11.setPixmap(QtGui.QPixmap("Resource/smallsmile3.png"))
            elif int(item.findtext('theDayAfterTomorrow')) >= 6 and int(item.findtext('theDayAfterTomorrow')) <= 7:
                self.label_11.setPixmap(QtGui.QPixmap("Resource/smallsmile1.png"))
            elif int(item.findtext('theDayAfterTomorrow')) >= 8:
                self.label_11.setPixmap(QtGui.QPixmap("Resource/smallsunglass.png"))

        self.label_8.setText(_translate("StartWindow", action))
        self.label_12.setText(_translate("StartWindow", "   내일"))
        self.label_13.setText(_translate("StartWindow", "      모레"))

    def SendMail(self):
        global host, port, htmlFileName, senderAddr, recipientAddr, msg, str1, str2, str3, str4, str5, action, stateBT
        fromID, passwd, toID = ' ', ' ', ' '
        fromID = self.lineEdit.text()
        passwd = self.lineEdit_2.text()
        toID = self.lineEdit_3.text()

        # MIME 문서를 생성합니다.
        if stateBT == 1 : # 미세먼지
            msg_text = "위치 : " + str1 + ' ' + str3 + "\n시간 : " + str2 + "\n미세먼지 농도 : " + str4 + "\n행동 요령 : " + action
        if stateBT == 2 : # 자외선
            msg_text = "위치 : " + str1 + "\n시간 : " + str2 + "\n자외선 수치 : " + str5 + "\n행동 요령 : " + action

        content=MIMEText(msg_text)

        # 만들었던 mime을 MIMEBase에 첨부 시킨다.
        msg.attach(content)

        # 메일을 발송한다.
        s = mysmtplib.MySMTP(host,port)
        #s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(fromID,passwd)
        s.sendmail(senderAddr , [toID], msg.as_string())
        s.close()

    def ResetBT(self):
        self.lineEdit.clear(),self.lineEdit_2.clear(),self.lineEdit_3.clear()

    def ClickFb(self):
        global stateBT
        stateBT=1
        self.label.setPixmap(QtGui.QPixmap("Resource/background.jpg"))
        self.label_2.show(), self.label_3.show(), self.label_4.show(), self.label_5.show(), self.label_6.show(), self.label_7.show(), self.label_8.show(), self.label_9.show()
        self.label_10.show(), self.label_11.show(), self.label_12.show(), self.label_13.show(),self.sidocomboBox.show(), self.stationcomboBox.show(), self.label_14.hide(), self.label_15.hide(), self.label_16.hide(),
        self.pushButton_4.hide(), self.pushButton_5.hide(), self.lineEdit.hide(), self.lineEdit_2.hide(), self.lineEdit_3.hide()
        self.dustshow(self.stationcomboBox.currentIndex())


    def ClickSb(self):
        global stateBT
        stateBT=2
        self.label.setPixmap(QtGui.QPixmap("Resource/background.jpg"))
        self.label_2.show(), self.label_3.show(), self.label_4.show(), self.label_5.show(), self.label_6.show(), self.label_7.show(), self.label_8.show(), self.label_9.show()
        self.label_10.show(), self.label_11.show(), self.label_12.show(), self.label_13.show(),self.stationcomboBox.hide(), self.label_14.hide(), self.label_15.hide(), self.label_16.hide(),
        self.pushButton_4.hide(), self.pushButton_5.hide(), self.lineEdit.hide(), self.lineEdit_2.hide(), self.lineEdit_3.hide()
        self.ultrashow(self.stationcomboBox.currentIndex())

    def ClickTb(self):
        # global stateBT
        # stateBT=3
        self.label.setPixmap(QtGui.QPixmap("Resource/background2.jpg"))
        self.label_2.hide(), self.label_3.hide(), self.label_4.hide(), self.label_5.hide(), self.label_6.hide(), self.label_7.hide(), self.label_8.hide(), self.label_9.hide()
        self.label_10.hide(), self.label_11.hide(), self.label_12.hide(), self.label_13.hide(),self.sidocomboBox.hide(),self.stationcomboBox.hide(), self.label_14.show(), self.label_15.show(), self.label_16.show(),
        self.pushButton_4.show(), self.pushButton_5.show(), self.lineEdit.show(), self.lineEdit_2.show(), self.lineEdit_3.show()





    def retranslateUi(self, StartWindow):
        global action
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "MainWindow"))
        self.pushButton.setText(_translate("StartWindow", "미세먼지"))
        self.pushButton_2.setText(_translate("StartWindow", "자외선"))
        self.pushButton_3.setText(_translate("StartWindow", "메일 전송"))

        self.label_14.setText(_translate("MainWindow", "보내는 메일 주소"))
        self.label_15.setText(_translate("MainWindow", "비밀번호"))
        self.label_16.setText(_translate("MainWindow", "받을 메일주소"))
        self.pushButton_4.setText(_translate("MainWindow", "전송"))
        self.pushButton_5.setText(_translate("MainWindow", "초기화"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui.setupUi(StartWindow)
    StartWindow.show()
    sys.exit(app.exec_())