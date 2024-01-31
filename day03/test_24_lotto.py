# file : test_24_lotto
# desc : 로또

import random as rnd # random이 기니까 rnd로 정의 

# numbers = list(range(1,46))

# lottery = list()
# print(lottery)

# for i in range(6) : # 0 1 2 3 4 5 : 6번 반복
#     lottery.append(rnd.choice(numbers)) # 1~45까지 숫자 중 하나를 랜덤하게 뽑음
# lottery.sort() # 작은 수부터 정렬
# print(lottery)

# 가중치 주는 방법을... 
# 뽑힌 것을 튕겨내는 방법으로 가야할듯? 
numbers = weight = list(range(1,46))
lottery = list()
rnd.shuffle(weight) #가중치로 섞음

lottery = rnd.choices(numbers,weights=weight, k=6)
lottery.sort()
print(lottery)
