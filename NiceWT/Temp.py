class Example(QWidget):

     #초기화해주는 메서드
    def __init__(self):
        super().__init__() #Super Class인 __main__에 해당하는 object 클래스를 초기화
        self.initUI() #QWidget.initUI를 초기화

    #Example 클래스 내의 UI를 생성하는 메서드
    def initUI(self):

        #폰트설정
        QToolTip.setFont(QFont('SansSerif', 10)) #Hold value(Non __init__)

        #UI설정
        self.setGeometry(300,300,300,200)
        self.setWindowIcon(QIcon('MIRO.png'))
        self.setWindowTitle('Test')
        self.resize(250,100)
        #self.move(250,100)
        self.center() #Display center Method

        #그냥 누르는 버튼만들기
        btn=QPushButton('PUSH',self) # This self is QPushButton
        btn.setToolTip('This is a <b>QPushButton</b> widget') #Information about Button
        btn.resize(btn.sizeHint()) #Button Position
        btn.move(50,50)

        #종료버튼만들기
        btn2=QPushButton('EXIT',self) # This self is QPushButton
        btn2.clicked.connect(QCoreApplication.instance().quit) #EXIT Method
        btn2.setToolTip('This is a <b>EXIT Button</b> widget') #Information about Button
        btn2.resize(btn.sizeHint()) #Button Position
        btn2.move(150,50)


        #GUI출력를 담당
        self.show()

     #종료시 나타나는 Event 메세지 출력을 위한 메서드
    def closeEvent(self, event): #close event

        reply=QMessageBox.question(self, 'Message', 'Really do you wanna EXIT?',
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        #yes, no 는 QMessageBox안에 들어 있는거다.
        if reply== QMessageBox.Yes:
            event.accept() #Quit
        else:
            event.ignore() #Return

     #데스크탑 상의 위젯의 위치를 가운데로 맞춰주는 메서드
    def center(self):

        qr = self.frameGeometry() #FrameGemotry on QWidget
        cp = QDesktopWidget().availableGeometry().center() #Application Potision
        qr.moveCenter(cp) #Size unchanged
        self.move(qr.topLeft())  #Standard potion


