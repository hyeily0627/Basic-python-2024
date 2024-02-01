# date : 2024 - 02 - 01
# file : test_27_exception handling
# dese : 예외발생 처리

def add(x, y) :
    return x + y 
  
def minus(x, y) : 
    return  x - y

def multi(x, y) :
    return  x * y

def divide(x, y) :
    try : 
        return x / y 
# 0을 넣었을때 예외 발생[zerodivision error]
    except ZeroDivisionError as e : 
        print('제수는 0이 될 수 없습니다!')
        return 0
    
def getoperands(): 
    #3.4를 넣었을 때 예외 발생[value errer]
    try : 
        a,b = map(int,input('두 숫자를 입력하세요(구분자 공백) > ').split())
        return a,b
    except ValueError as e :
        print(e) # 정확한 예외 메시지 출력
        print('입력 오류 : 정수만 입력하세요')
        return 1, 1

while True : 
    mnu = input('메뉴입력(p[덧셈],m[뺄셈],t[곱셈],d[나눗셈],x[종료]) >')

    if mnu == 'p':
        a, b = getoperands()
        print(f'덧셈 {a}+{b} = {add(a,b)}')
    elif mnu == 'm':
        a, b = getoperands()
        print(f'뺄셈 {a}-{b} = {minus(a,b)}')
    elif mnu == 't':
        a, b = getoperands()
        print(f'곱셈 {a}*{b} = {multi(a,b)}')
    elif mnu == 'd':
        a, b = getoperands()
        print(f'나눗셈 {a}/{b} = {divide(a,b)}')
    elif mnu == 'x':
        break 
    else : 
        continue # 다시 선택메뉴로 올라감 
        
