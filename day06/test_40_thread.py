# file : test_40_thread.py
# desc : Qt Thread로 동작

# 오타 txv - > txb가 맞음 (textbox)

import sys
from PyQt5 import QtGui, QtWidgets,uic
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

class BackWorker (QThread) : # PyQt에서 스레드 클래스 상속
    initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기 위한 변수객체
    setSignal = pyqtSignal(int)
    setLog = pyqtSignal(str)
    
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.parent = parent # BackWorker에서 사용할 멤버 변수 

    def run(self) -> None: # 스레드 실행 
        # 스레드로 동작할 내용 기입 
        maxVal = 1000001
        self.initSignal.emit(maxVal)
        ### self.parent.pgbTask.setValue(0) ## 프로그레스바 0부터 시작! QThread에서는 uI 관련한 처리를 할 수 없음
        ### self.parent.pgbTask.setRange(0, maxVal-1)
        for i in range(maxVal) :  # 0 ~ 100까지
            print_str = f'Thread 출력 >> {i}'
            print(print_str)
            self.setSignal.emit(i)
            self.setLog.emit(print_str)
            ### self.parent.txvLog.append(print_str)
            ### self.parent.pgbTask.setValue(i)

class qtwin_exam (QWidget) : # UI 스레드 :  QWidget을 [상속] 받음 = QWidget이 가진 모든 것을 사용할 수 있다 
    def __init__(self) -> None: #self : 내 자신
        super().__init__() #super : 부모 
        uic.loadUi('./day06/ThreadAPP.ui', self) #qtdesigner에서 만든 ui를 로드 
        #버튼에 대한 시그널 처리 
        self.btnStart.clicked.connect(self.btnStartClicked)           

    def btnStartClicked(self):
        th = BackWorker(self)
        th.start() # BackWorker 내의 self.run() 실행 
        th.initSignal.connect(self.initpgbTask) # 스레드에서 초기화 시그널이 오면 initpgbTask 슬롯함수가 대신 처리
        th.setSignal.connect(self.setpgbTask)
        th.setLog.connect(self.settxvLog)

    def closeEvent(self,QCloseEvent) -> None: #재정의(override)
        re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: #닫기
            QCloseEvent.accept()
        else: 
            QCloseEvent.ignore()    


    # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 부분 : 슬롯함수 
    @pyqtSlot(int) # BackWorker 스레드에서 self.setLog.emit() 동작해서 실행
    def initpgbTask(self, maxVal) : 
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal-1)

    @pyqtSlot(str) # BackWorker 스레드에서 self.setLog.emit() 동작해서 실행
    def settxvLog(self,msg) : 
        self.txvLog.append(msg)

    @pyqtSlot(int)
    def setpgbTask(self, val) : 
        self.pgbTask.setValue(val)    

if __name__ == '__main__' : 
    loop = QApplication(sys.argv) # 내 소스위치로 앱을 생성
    instance = qtwin_exam() # QWidget을 상속한 qtwin_exam 객체를 생성 
    instance. show()
    loop.exec_()
