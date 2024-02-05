# file : test_36_PyQt5_1.py
# desc : PyQt5 기본화면 만들기

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEngine, QPaintEvent, QPainter, QColor, QFont
from PyQt5.QtWidgets import QApplication, QWidget

# print(sys.argv) # 현재 파이썬 파일의 경로 표시 

class qtwin_exam (QWidget) : # QWidget을 [상속] 받음 = QWidget이 가진 모든 것을 사용할 수 있다 
    #생성자 
    def __init__(self) -> None: #self : 내 자신
        super().__init__() #super : 부모 
        self.initUI() #화면 초기화 함수를 호출

    def initUI(self):
        self.setGeometry((1920-400)//2, (1080-200)//2, 400, 200) # 넓이, 높이를 뺴줌으로써 중간에 창이 뜨도록 함 
#                        x 좌표            y좌표       넓이 높이
                         # 컴퓨터마다 해상도가 다르므로, 매번 설정할 수 없기에 해당 컴퓨터 해상도 당겨오는 방법을 적용해야 할 것임. 
        self.setWindowTitle('팝업을 출력합니다')
        self.text = ''
        self.show()

    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10 , 10)) #black / r255,g255,b255
        paint.setFont(QFont('nanumgothic', 15))
        paint.drawText((400-100)//2, (300-100)//2, 'Hello World') 
        paint.drawText(event.rect(), Qt.AlignCenter, self.text)
        # AlineLeft, AlignCenter, AlineRight 글자 정렬

    def paintEvent(self,Event) -> None: #재정의(override)
        paint = QPainter()
        paint.begin(self) # 열면 
        self.drawText(Event,paint)
        paint.end # 닫기 


    loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성
    instance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성 
    loop.exec_()