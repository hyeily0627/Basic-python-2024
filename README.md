# Basic-python-2024
부경대학교 2024 IoT 개발자 과정 기초 프로그래밍 언어 - PYTHON

## 1일차 
- 개발환경 구축
    - 코딩폰트 - 나눔고딕코딩
    - Notepad++ 설치
    - Python 설치
    - Visual studio code 설치
    - Git 설치
        - TortoiseGit 설치
        - Github 가입
        - Github Desktop 설치 

- 파이썬 용어
    - 콘솔출력
    - 주석
    - 변수
    - 자료형
    - 연산자

   ```python
    # 이 부분은 주석입니다.
    var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
    print(var01) # 10
    print(type(var01)) # \ <class of 'int' >

    print( 5 + 4 / 2 ) # 7.0
    print(5==4) # Fasle
    ```
    
## 2일차
- 파이썬이란? 
    - 파이썬 제작자는 귀도 반 로섬이다.
- 파이썬 기초
    - 흐름제어
        - if문(if elif else / 응용_datetime / 짝수홀수 및 배수구하기)
        - for문(반복문 - 형식 : for i in 리스트) 
        - while문(반복문의 변형)
    - 복합자료형 + 연산자
        - 리스트 
            - 연산 +, * 만 사용
            - len( ) / append( ) / insert( ) / extend( ) / del / pop / clear( ) / sort( ) / in, not on
            - reverse( ), copy( ), count( ) ... 
            - (전개 연산자 *) 
        - 듀플
             ```python
            ## 튜플 - 리스트 변경, 리스트 조작가능 but 튜플은 조작 불가하다. 
            tuple_a = (1,3,5,7,9)

            for i in tuple_a : 
                #print(i)

            print(tuple_a[1])  

            ## tuple_a[1] = 4  # 'tuple' object does not support item assignment      
            ```
         - 딕셔너리 
            ```python
            ## 사전형 - key와 value쌍을 나열해놓은 자료형
            # { key:value, key:value, key:value,... }
            ```
        - 출력 포맷
        - 구구단 + 디버깅 
            ```python
            # 디버깅 : 벌레잡기 (최초의 컴퓨터는 코드를 꽂아 코딩했는데, 벌레(버그)로 인해 코딩이 안되는 경우가 있어 이를 제거함에서 유래하였다.)
            # F9 : 중단점 토글
            # F5 : 디버그 시작
            # 조사식 확인!
            # F10 : 한 줄씩 실행 
            # F11 : 함수안으로 진입
            # shift + F5 : 디버깅 종료

            print('**구구단 시작!**')
            for x in range(2,10) : # 2부터 9까지 반복
            print(f'<{x} 단 시작>')
            for y in range (1,10) : # 1부터 9까지 반복
            print(f'{x} x {y} = {x * y:2d}', end =' / ') # end = '' 엔터대신 공백으로 처리, / 삽입 
            print() # 안쪽 for문 종료시 마지막 엔터를 추가 
            ```

## 3일차 
- 파이썬 기초 
    - 입력 방법
    - 별찍기 
        - 단일 for문, 이중 for문 이용하기
        - 뒤집어서 출력하기
        - 트리 찍기
        - 마름모 찍기 (직접 구현해보기!)
    - 함수, 람다 함수는 나중에! 
    - 객체지향(object oriented programming) 개념
        - 객체는 명사와 동사의 집합이다.
        - 명사는 변수, 동사는 함수로 볼 수 있다.
        - 변수와 함수를 모두 모아둔 곳 : 클래스(Class)
        - 객체 = 클래스가 아님! '클래스에서 하나씩 생성된 객체'로 정의하자
        - 캡슐화 (__platenumber)

## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
     - pip 사용 (참고 사이트 : https://pypi.org/project/pip/)
        ```shell
        > pip --version # 버전확인
        > pip list # 현재 설치된 라이브러리 목록 확인
        > pip install 패키지명 # 패키지를 내 컴퓨터에 설치
        > pip unistall 패키지명 # 패키지를 삭제
        ```
    - 예외처리 : 비정상적인 프로그램 종료 막기 
         ```python
        def divide(x, y) :
            try : 
                return x / y 
        # 0을 넣었을때 예외 발생[zerodivision error]
            except ZeroDivisionError as e : 
                print('제수는 0이 될 수 없습니다!')
                return 0
         ``` 
    - 텍스트 파일 입출력
       ```python
      f = open('파일명', mode='r / w / a', encoding='cp949 / utf-8)
      f.read()
      f.readline() # 읽기
      f.write('text') # 쓰기
      f.close() # 파일은 반드시 닫는다.
       ```
- 파이썬 응용
    - jupyter_notebook
        - ctrl + shift + p 로 시작 ( > 명령팔레트 )
        - 사용방법(test_31_jupyter_notebook.ipynb)
    - folium 기본 사용
        - ![folium이미지사용법](https://raw.githubusercontent.com/hyeily0627/Basic-python-2024/main/Images/python_001.png)
        ```python
        # 지도 표시 
        map = folium.Map(location=[35.173999, 129.196649],zoom_start=20, tiles='cartodb positron')
        # 마커 표시
        folium.Marker([35.173999, 129.196649], popup='송정해수욕장').add_to(map)
        # 마커 변경 
        folium.Marker([35.173999, 129.196649], popup='송정해수욕장', icon=folium.Icon(color='pink',icon='heart-empty')).add_to(map) 
        
        #  아이콘 종류 참고 사이트 : https://getbootstrap.com/docs/3.3/components/
        ``` 
## 5일차
- 파이썬 응용
    - jupyter_notebook 활용 - 구글 코랩(Google Colab)
    - folium 계속~
    - json (JavaScript Object Notation) 입출력
        - #json 에서는 false가 소문자로 시작하나, 주피터로 출력시켜서 파이썬 출력되면 False로 출력
    - 응용 예제 연습
    
## 6일차 
- 파이썬 응용
    - Window App(PyQt)
    ```shell
    > pip install PyQt5
    > pip install PyQt5designer
    : 라이브러리 경로 c: - DEV - Langs - Python311 - Lib - site-packages - PyQt5 관련 폴더
    : PyQt5designer - designer.exe 실행 후 작업표시줄 고정
    ```
    - PyQt5 기본 실행 

    - Thread란 ? - 하나의 프로세스 내에서 여러 개의 실행 흐름(단일, 동시적, 병렬적)을 두어 작업을 효율적으로 처리하기 위한 모델 
        - [ ] GIL, 병렬프로세싱 더 학습할 것
    - ❗❗Thread 학습 : UI Thread와 Background Thread 분리
        ![Thread예제](https://raw.githubusercontent.com/hyeily0627/Basic-python-2024/main/Images/python_003.gif)

```python
     # 쓰레드 클래스에서 시그널 선언
    class BackWorker(QThread): # PyQt에서 스레드 클래스 상속
        initSignal = pyqtSignal(int) # 시그널을 UI스레드로 전달하기위한 변수객체
        setSignal = pyqtSignal(int)
        # ...

        def run(self) -> None: # 스레드 실행
            # 스레드로 동작할 내용
            maxVal = 1000001
            self.initSignal.emit(maxVal) # UI쓰레드로 보내기...
            # ...

    class qtwin_exam(QWidget):  # UI 스레드
        # ...
        def btnStartClicked(self):
            th = BackWorker(self)
            th.start() # BackWorker 내의 self.run() 실행
            th.initSignal.connect(self.initPgbTask) # 스레드에서 초기화 시그널이 오면 initPgbTask 슬롯함수가 대신 처리
            # ...    
        # 스레드에서 시그널이 넘어오면 UI처리를 대신 해주는 부분 : 슬롯함수 
        @pyqtSlot(int) # BackWorker 스레드에서 self.setLog.emit() 동작해서 실행
        def initpgbTask(self, maxVal) : 
            self.pgbTask.setValue(0)
            self.pgbTask.setRange(0, maxVal-1)
```

## 7일차 
- 파이썬 응용
    - 객체지향
        - 오버라이딩(override) 
            ```python
                # QWidget에 있는 closeEvent를 그대로 쓰면 바로 닫히기때문에 
                # 닫을지 말지 한번 더 물어보는 형태로 다시 구현하고자 재정의 함. 
                def closeEvent(self,QCloseEvent) -> None: #재정의(override)
                    re = QMessageBox.question(self, '종료확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
                    if re == QMessageBox.Yes: #닫기
                        QCloseEvent.accept()
                    else: 
                        QCloseEvent.ignore()    
            ```
        - 오버로드(overrode) : 한번에 같은 이름의 함수를 매개변수를 다르게 하여 사용가능 
            ```python
                # Widget 정의(F12)에서 확인 가능 
                @typing.overload
                def setGeometry(self, a0: QtCore.QRect) -> None: ...
                @typing.overload
                def setGeometry(self, ax: int, ay: int, aw: int, ah: int) -> None: ...
            ``` 
    - 가상환경 : python 버전이 다른 경우, 다른 버전을 가동시키는 환경
        - 1. 콘솔 - Set-ExecutionPolicy -ExecutionPolicy RemoteSigned 입력 - y 입력
        - 2. 다른 버전 설치 - 탐색기 sysdm.cpl - 시스템 속성 : 고급 - 환경변수 : 시스템변수 - path 에서 파이썬 311(원래 버전)을 위로 올리기
        - 3. VS Code 터미널 입력 방법 
                ![터미널 입력](https://raw.githubusercontent.com/hyeily0627/Basic-python-2024/main/Images/python_002.png)
        - 4. 파이썬 터미널 오른쪽 하단 버전 클릭시 변경 가능
    - PyQt와 응용예제 연습
        - 이미지 뷰어 
        - 이미지 에디터 
            ![PyQt예제](https://raw.githubusercontent.com/hyeily0627/Basic-python-2024/main/Images/python_006.png)

## 8일차 
- 파이썬 응용 
    - PyQt와 응용예제 연습 계속
- 파이썬 기본 코딩테스트 
    - Jupyter Notebook 활용


    - 객체지향
        - 상속, 다중 상속
        - 추상클래스, 인터페이스

## 추가
- 파이썬 실행파일 만들기 
    - PyQt ui 파일이나 이미지 파일의 경로가 절대경로로 지정 
    - pip install pyinstaller 패키지 설치 (명령프롬프트)
    - pyinstaller -w -F python(=파일명).py (-w : 콘솔창 없애기, -F: 실행파일 하나로 만들기)