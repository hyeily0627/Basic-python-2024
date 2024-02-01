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
    - 객체지향
        - 오버로딩, 오버라이딩(재정의)
        - 상속, 다중상속 
        - 추상클래스

## 4일차
- 파이썬 기초
    - 패키지, 모듈 계속
     - pip 사용
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
    - 가상환경
- 파이썬 활용
    - 주피터 노트북
    -