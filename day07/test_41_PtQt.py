# file : text_41_PyQt.py
# desc : PyQt 이미지 뷰어

import sys 
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class WinApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self):
        # 이미지 삽입
        pixmap = QPixmap('./images/python_004.jpg').scaledToWidth(800) # .scaledToHeight(800) 큰 해상도를 800으로 고정 
        
        lblImages = QLabel(self)
        lblImages.setPixmap(pixmap)
        
        lblSize = QLabel(self)
        lblSize.setFont(QFont('Century Schoolbook', 20))
        lblSize.setStyleSheet('color: #336600;') #RGB 색상표 참고 https://www.rapidtables.org/ko/web/color/RGB_Color.html
        lblSize.setText(f'This picture size {pixmap.width()} x {pixmap.height()}') #python_004.의 사이즈 width x height
        lblSize.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignCenter) # 가로중앙정렬 | 세로중앙정렬

        vbox = QVBoxLayout(self) # QtDesigner에서 verticalLayout 위젯 생성 
        vbox.addWidget(lblImages) # VL에 위젯 추가
        vbox.addWidget(lblSize)
        self.setLayout(vbox) 

        self.setWindowIcon(QIcon('./images/iot.png'))
        self.setWindowTitle('이미지 뷰어')
        rect = QRect (300, 300, 300, 300) #X, Y, w, h
        self.setGeometry(rect) # 같은 이름의 함수를 여러개 선언 후 골라쓰는 BR(오버로딩)
        # self.setGeometry(300,300,300,300)
        
        self.show()
        self.setCenter()
         # showFullScreen() 모니터를 꽉 채워서 출력 
    
    def setCenter(self) : # 윈앱을 화면 정중앙에 위치
        gm = self.frameGeometry() # 윈앱 자신의 위치값 
        cp = QDesktopWidget().availableGeometry().center() # 모니터 정중앙 값 출력
        gm.moveCenter(cp)
        self.move(gm.topLeft())
        
if __name__ =='__main__':
    app = QApplication(sys.argv)
    screen_rect = app.desktop().screenGeometry()
    width, height = screen_rect.width(), screen_rect.height() # 현재 모니터 해상도 출력
    print(width, 'x', height) # 현재 모니터 해상도 출력

    ins = WinApp()
   
    sys.exit(app.exec_()) # 종료시 리소스 반환 등 효율을 위해 사용



