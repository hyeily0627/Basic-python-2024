# file : test_14_while.py
# dese : while문 

## while 참인 조건 : 
## 공통점 if 조건 : elif 조건 : else : , for in range():, while 조건 : 

count = 0 

# while count < 10 : #count 변수값이 10보다 작거나 같은 동안 반복
while True : # 무한루프 : window os, 모바일os, 네비게이션, 라즈베리파이, 아두이노, 게임, winform 개발... 
    count = count + 1 
    print ('나무찍기', count)
    if count == 10: 
        break # 이 반복문을 빠져나가라!
print ('나무찍기 끝!')

print('--------3 6 9 게임 (구글링)----------')
n = int(input("input number: "))

for i in range(1, n+1) : 
    s = str(i)
    count = 0 

    for x in s : 
        if ( x == '3') or ( x == '6') or (x == '9') : 
            count += 1 
    if count == 0 : 
        print(i, end= ' ')
    else : 
        print(count*'X', end=' ')    
print ('<3 6 9 게임 끝>')

print('--------3 6 9 게임 강사님 정답----------')

number = 0
while True : 
    number = number + 1 
    if str(number).count('3') >= 1 or \
        str(number).count('6') >= 1 or \
        str(number).count('9') >= 1 : # 숫자를 문자열로 바꾼 값안에 3 6 9 
        print ('짝!') # 짝! 대신 continue로 변경해보기~
    else : 
        print(number)

    if number > 30 : break 