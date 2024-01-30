# date : 2024 - 01 - 30
# desc : for 반복문 
# file : test10_for.py

std = [80, 90, 100, 50, 60, 55 ,77, 88, 99, 100]
kor_sum = 0

for i in std : # std 리스트에 값을 하나씩 i 에 넣어서 반복할 요소가 있을때까지 출력
    kor_sum = kor_sum + i

print(kor_sum) # 합산 
print(kor_sum / len(std)) # len을 활용하여 std의 수가 얼마가 늘어나든 평균 산출  

print('-----------------------------------------')

# 2차원 리스트
list_a = [[1,3,5],[2,4,8],[10,15,20]] 
for i in list_a : 
    print(i)

for i in list_a:
    for j in i : 
        print(j)
