# date : 2024 - 01 - 30
# desc : 흐름제어 if 

## 조건이 참일때와 거짓일때로 나누어서 어떤 일을 처리할 것인가
# if 조건 : 참인 조건
# else : 거짓인 조건 
# 입력 input() 함수 사용 - 터미널에 숫자 입력 가능하나, 해당 함수는 문자만 받음
# 따라서 int를 사용하여 문자 입력값을 정수로 변경해준다.

number = int(input('정수를 입력해주세요 > '))

if number > 0 :
    print('양수 입니다!')
elif number == 0 :
    print('0  입니다!')
else : 
    print('음수 입니다!')