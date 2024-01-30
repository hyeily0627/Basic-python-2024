# date : 2024 - 01 - 30
# desc : if문 홀수/짝수 구분 또는 배수구하기

number = int(input('정수입력 > '))

if number % 2 == 0 : # ex) % 5 : 5로 나누었을때 나머지가 0
    print('짝수입니다!') # ('5의 배수')
else :
    print('홀수입니다!') # 5의 배수가 아님