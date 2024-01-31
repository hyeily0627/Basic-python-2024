# file : test_17_input.py
# date : 2024 - 01- 31 
# desc : 다중입력

## 원래는 (in_a, in_b) 로 튜플로 데이터 받는 것이 정석이나, 생략하였음
# input_a, input_b = input('값을 2개 입력(공백으로 구분) > ').split(' ')
# input_a = int(input_a)
# input_b = int(input_b)

## map()함수 사용
input_a, input_b = map(int,input('값을 2개 입력(공백으로 구분) > ').split(' '))

print(f'입력값) {input_a},{input_b}')
print(f'더하기 결과) {input_a + input_b}')
