# file : test_20_function.py
# date : 2024 - 01- 31 
# desc : 함수

# .하고 네임박스 뜨는 것 중 보라색 정사각형으로 뜨는 것 = 함수
# 구문 작성 후에는 연노랑색으로 색 변경
# print(매개변수(values)), input ...
# def add(x, y) => int : # 함수의 선언부
# 함수 = 메서드 = 프로시저 = 서브루틴    

# 함수 정의
def add(x, y) :
    result = x + y 
    return result

def minus(x, y) : 
    result = x - y
    return result

def multi(x, y) -> int : 
    result = x * y
    return result
    
def divide(x, y) -> float :
    result = x / y
    return result

# 리턴 값이 없는 경우(사실은 리턴 값이 None이나, 의미가 없으므로 생략)
def say_hello() ->  None : 
    print('hello')

say_hello()

print('계산을 진행합니다 -> ')
a, b = map(int,input('두 정수를 입력하세요> ').split(' '))
결과 = add(a, b) # 리턴은 함수 결과 값으로 바뀐다.
print(f'{a} + {b} = {결과}')
print(f'{a} - {b} = {minus(a,b)}')
print(f'{a} - {b} = {multi(a,b)}')
print(f'{a} - {b} = {divide(a,b)}')

