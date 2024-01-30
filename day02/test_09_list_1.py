# date : 2024 - 01 - 30
# desc : 복합자료형 list_1

# s1 = 80
# s2 = 90
# s3 = 40 ... 
## s가 인원에 대한 점수라고 한다면, 6명에 대해서 값을 부여해야할 것임 
## 그러나 리스트로 정의해버리면 명령수가 줄어듦

#index= 0  1   2    3   4   5   = 컴퓨터는 0부터(0번째) 시작
#index=-6  -5  -4   -3  -2  -1   = 컴퓨터는 0부터(0번째) 시작
std = [80, 90, 40, 100, 95, 55]

std[0]
print(std[0])
# print(std[6]) # 6번째 인덱스가 없으므로 에러

list_1 = [265, 3.5, '문자열', True, False, [1,2,3,4], (3,4), std]
print(list_1)
print(list_1[3]) #3번째 인덱스는 True


list_1[6] = '바꾼값' #6번째 인덱스(3, 4)를 '바꾼 값'으로 변경 
print(list_1)

##리스트 연산 ** 헷갈리지말기!!
print(list_1[2:4]) # 콜론 뒤의 수는 출력하고 싶은 인덱스 +1 을 해야함
#즉 '문자열'과 True를 출력하고 싶으면 True가 3번이므로 +1한 4를 입력

print('--------------------------')

##마이너스 인덱스
print(list_1[-2])
print(list_1[-5:-3]) # 정말 헷갈리구나? 

## 이중 리스트
print(list_1[5][2]) # 결과값 3 

list_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_2[1][2]) # 결과값 6

print('--------------------------')

list_4 = [1, 2, 3]
list_5 = [4, 5, 6]

## 리스트 연산 +, * 만 사용 가능
print(list_4 + list_5) # +는 리스트를 연결
print(list_5 * 2) # *는 리스트를 반복

## 리스트 길이 함수 : len()
print(len(list_4))