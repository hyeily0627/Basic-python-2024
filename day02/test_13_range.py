# date : 2024 - 01 - 30
# desc : 리스트 범위 지정
# file : test_13_range.py

list_a = [1,2,3,4,5,6,7,8,9,10]
# 만약 리스트를 10까지 뽑았는데 100까지 늘려야한다면? 

# 범위 지정 range(n), 0부터 n개의 범위 수를 생성 
print(range(5))

print(list(range(5)))
print(list(range(0,5))) 
# 위 2개 범위는 같다. 
print(list(range(101)))
print(list(range(2,21,2))) # 2부터 20(+1)까지 2씩 증가
print(list(range(1,20,2))) # 2부터 180(+1)까지 2씩 증가
print(list(range(10, -1, -1))) #카운트다운

list_a = list(range(1,101)) #range() 클래스
print(list_a)

list_a = [i for i in range(1,101)] #리프트 컨프리헨션
print(list_a)