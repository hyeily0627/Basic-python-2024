# date : 2024 - 01 - 29
# desc : 자료형

## 기본 자료형 - 숫자형, 문자형, 불형, None형 ... 
## 복합(추가) 자료형 - 리스트형, 튜플형, 딕셔너리, 집합 ... 

## 1. None 형 == Null (c, c++, c#, java, SQL) 
## 값은 값인데 아무것도 지정할 수 없는 값 (어떠한 값도 가지고 있지 않다.)

apple = None 
print(apple)

print(None == 0)

## 2. 숫자형 : 정수형, 실수형, 진수형
### 정수
ten = 10
hundred = 100
temp = -8 
test_val = 2 ** 10
print(test_val)

### 실수
pi = 3.141592
tax_rate = 10.0
emp_earn_rate = 3.3 

### 진수(2, 8, 16진수)
bit142 = 0b10001110
# 0=0 / 1=1 / 10=2 / 11=3 / 100=4 / 101=5 / 110=6 / 111=7 / 1000=8
oct9 = 0o11
# 0 1 2 3 4 5 6 7 10 11 12 13 14 15 16 17 20 77 100
hex255 = 0xff
# 0 1 2 3 4 5 6 7 8 9 A B C D E F
print(bit142)
print(oct9)
print(0xff)

## 3. 문자형 - Python에서는 문자, 문자열에 차이가 없음 
# 홑따옴표, 쌍따옴표 모두 문자를 나타냄
greeting = 'hello'
greeting = "hello" 
print(greeting)
multi_str = '''Hello
My name is hyejin 
Have a nice day.''' 
print(multi_str)
multi_str = """Hello
My name is hyejin 
Have a nice day.""" 
print(multi_str)

multi_str2 = ('Line\n'
              'Line2'
              'Line3')
print(multi_str2)
multi_str2 = 'Line\n'\
              'Line2'\
              'Line3'
print(multi_str2)
# ()를 다쓰거나, 문장 끝마다 \를 붙이기

## 4. 불형 (Bool/ Boolean)
# True 와 False 값만 가질 수 있음. 
ischeck = False
print(ischeck)

ischeck = True
print(ischeck)

answer = (3 == 6)
print(answer)

answer = (3.0 == 3)
print(answer)

## 자료형이 어떤 타입인지 체크하는 방법
print(type(apple)) # 위에서 None으로 정의

print(type(hundred)) # int

print(type(test_val)) # int

print(type(hex255)) # int

print(type(greeting)) # str

print(type(ischeck)) # bool
      
