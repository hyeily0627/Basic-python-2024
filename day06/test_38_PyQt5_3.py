# file : test_38_PyQt5_3.py
# desc : Qt 디자이너 만든 ui와 연동

import sys
from PyQt5 import QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

class qtwin_exam (QWidget) : # QWidget을 [상속] 받음 = QWidget이 가진 모든 것을 사용할 수 있다 
    #생성자 
    def __init__(self) -> None: #self : 내 자신
        super().__init__() #super : 부모 
        uic.loadUi('./day06/test app.ui',self) #qtdesigner에서 만든 ui를 로드 
        #버튼에 대한 시그널 처리 
        self.BTNstart.clicked.connect(self.BTNstartClicked)
        self.BTNstop.clicked.connect(self.BTNstopClicked)

    def BTNstartClicked(self):
        print('시작버튼 클릭')
        self.LBLstatus.setText('상태 : 동작시작')
        QMessageBox.about(self,'동작', '***시스템이 시작되었습니다')

    def BTNstopClicked(self):
        print('종료버튼 클릭')
        self.LBLstatus.setText('상태 : 동작시작')
        QMessageBox.about(self,'동작', '***시스템이 종료되었습니다')

    def closeEvent(self,QCloseEvent) -> None: #재정의(override)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else: 
            QCloseEvent.ignore()    

if __name__ == '__main__' : 
    loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성
    instance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성 
    instance. show()
    loop.exec_()


