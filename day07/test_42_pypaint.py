# file : test43_pypaint.py
# date : 2024 - 02 - 06
# desc : 그림판 만들기

import sys
from PyQt5 import uic   #Qt디자이너 호출시 필요
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import *

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()
        self.initSignal()

    def initUI(self): # 화면 초기화 
        # uic.loadUi('./day07/pyPaint.ui', self)
        uic.loadUi('C:/Sources/Basic-python-2024/day07/pyPaint.ui', self) # 실행파일 생성시에는 절대 경로 사용 
        self.setWindowIcon(QIcon('C:/Sources/Basic-python-2024/day07/images/iot.png'))
        self.setWindowTitle('py 그림판')

        # 캔버스 초기화
        self.brushColor = Qt.black # Black B 대문자 안됨! 
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('white'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background : #808080')
        self.btn_red.setStyleSheet('background : #ff9999')
        self.btn_blue.setStyleSheet('background : #99ccff')

        self.show()
        self.setCenter()

    def initSignal(self): # 동작 초기화
        self.btn_black.clicked.connect(self.buttonClicked)
        self.btn_red.clicked.connect(self.buttonClicked)
        self.btn_blue.clicked.connect(self.buttonClicked)
        self.btn_clear.clicked.connect(self.buttonClicked)
    # 기능추가 (이미지 로드 및 저장버튼 추가)
        self.btn_load.clicked.connect(self.btnLoadClicked) # 이미지 로드
        self.btn_save.clicked.connect(self.btnSaveClicked) # 이미지 저장
    
    def btnLoadClicked(self): 
        image = QFileDialog.getOpenFileName(None,'이미지 로드','','Image file(*.jpg;*.png)')
        imagePath = image[0]
        # print(imagePath)
        pixmap = QPixmap(imagePath).scaledToHeight(380) # 파일 경로에 있는 이미지를 읽어서 pixmap 객체에 담기
        self.lb_canvas.setPixmap(pixmap)
        self.lb_canvas.adjustSize() # 이미지를 라벨크기에 맞추기

    def btnSaveClicked(self):
        filePath, _ = QFileDialog.getSaveFileName(self,'이미지 저장','','Image file(*.jpg;*.png)')
        if filePath == '' : return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)


    def buttonClicked(self) : 
        btn_val = self.sender().objectName()
        print(btn_val)
        if btn_val == 'btn_black' : # 검은 버튼 클릭
            self.brushColor = Qt.black
        elif btn_val == 'btn_red' :
            self.brushColor = QColor('#ff9999')
        elif btn_val == 'btn_blue' :
            self.brushColor = QColor('#99ccff')
        elif btn_val == 'btn_clear' : 
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap(self.canvas)

    ## 위 구문을 써서 밑 구문을 쓰지 않아도 괜찮음. 

    # def btnBlackClicked(self):
    #     btn_val = self.sender().objectName() # self.sender() -> btn_black이라는 스트링이 넘어옴
    #     print(btn_val)
    #     self.brushColor = Qt.black

    # def btnRedClicked(self):
    #     btn_val = self.sender().objectName() 
    #     print(btn_val)
    #     self.brushColor = Qt.red

    # def btnBlueClicked(self):
    #     btn_val = self.sender().objectName() 
    #     print(btn_val)
    #     self.brushColor = Qt.blue

        # self.canvas.fill(QColor('white'))
        # self.lb_canvas.setPixmap(self.canvas)


    def mouseMoveEvent(self,e) -> None: # 마우스 클릭시 클릭된 좌표 출력
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap())
        brush.setPen(QPen(self.brushColor,10, Qt.SolidLine, Qt.RoundCap)) # RoundCap 끝을 둥그렇게 처리 
        brush.drawPoint(e.x(),e.y())
        brush.end
        self.update() # 화면 업데이트
    

    def setCenter(self): 
        gm = self.frameGeometry() 
        cp = QDesktopWidget().availableGeometry().center() 
        gm.moveCenter(cp)
        self.move(gm.topLeft())
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ins = WinApp()
    sys.exit(app.exec_())
