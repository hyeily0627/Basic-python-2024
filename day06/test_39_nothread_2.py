# file : test_39_nothread.py
# desc : Qt 디자이너 만든 ui와 연동 
# (개인 복사본) 프로그레스바 1 ~ 100까지 출력

# 오타 txv - > txb가 맞음 (textbox)

import sys
from PyQt5 import QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

class qtwin_exam (QWidget) : # QWidget을 [상속] 받음 = QWidget이 가진 모든 것을 사용할 수 있다 
    #생성자 
    def __init__(self) -> None: #self : 내 자신
        super().__init__() #super : 부모 
        uic.loadUi('./day06/ThreadAPP.ui',self) #qtdesigner에서 만든 ui를 로드 
        #버튼에 대한 시그널 처리 
        self.btnStart.clicked.connect(self.btnStartClicked)

    def btnStartClicked(self):
        maxVal = 100001 #100001에서 오류
        print('시작버튼 클릭')
        self.pgbTask.setValue(0) # 프로그레스바 0 부터 시작
        self.pgbTask.setRange(0,maxVal-1)
        for i in range(maxVal) :  # 0 ~ 100까지
            print_str = f'NoThread 출력 >> {i}'
            print(print_str)
            self.txvLog.append(print_str)
            self.pgbTask.setValue(i)

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


