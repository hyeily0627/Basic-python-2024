# file : test_37_PyQt5_2.py
# DESC : PyQt5 이벤트(Signal)

import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QCloseEvent, QPainter, QColor, QFont 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) :
        btn01 = QPushButton('클릭', self)
        btn01. setGeometry(150, 70, 100, 40)
        btn01. clicked. connect(self.btn01_clicked) #버튼 클릭시(시그널) btn01_clicked 함수를 실행

        self.setGeometry(300, 200, 400, 200)
        self.setWindowTitle('버튼 시그널')
    
    def btn01_clicked(self) : 
        QMessageBox.about(self,'버튼클릭','버튼을 클릭했습니다.')

    def closeEvent(self,QCloseEvent) -> None: #재정의(override)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else: 
            QCloseEvent.ignore()    

if __name__ == '__main__' : # 메인엔트리 확인 조건 추가 
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()