# date : 2024 - 01 - 30
# desc : 복합자료형 list_2

std = [80, 90, 40, 100, 95, 55]

list_1 = [265, 3.5, '문자열', True, False, [1,2,3,4], (3,4), std]

list_4 = [1, 2, 3]
list_5 = [4, 5, 6]

## append() : 리스트 마지막에 하나 추가
print(list_1)
list_1.append('Hello')
print(list_1)

## insert(index, val) 리스트의 indec 이후에 val 추가
list_1. insert(2,100) # 2번쨰 인덱스에 값을 추가(원래 값은 뒤로 밀림)
print(list_1)

## extend() 기존 리스트 확장
list_4.extend(list_5)
print(list_4)
print(list_5)

## 리스트 삭제 : del
del list_4[3] # 리스트의 인덱스 삭제
print(list_4)
del list_4 # 리스트 자체를 삭제
# print(list_4) # 윗 줄에서 리스트를 삭제 했으므로 출력 X

val = list_5.pop() # 마지막 값 꺼내오기 
print(val) # 결과값 : 6 
print(list_5) # 결과값 : [4,5]

# clear() : del은 완전 삭제(print 불가), clear는 내용만 삭제하므로 셀은 남음([])
list_5.clear()
print(list_5)  

# sort() 
print(list_1)
# list_1.sort() # 문자열, 숫자, 불 섞여있는 리스트는 정렬 안됨
std.sort(reverse=True) # 내림차순 정렬
print(std)

# in, not on
print(99 in std) # ture
print(98 not in std)  #false 

# reverse(), copy(), count() ... 

print('------------------------------')
# *를 list 에서 사용 : 전개 연산자 
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a, *list_b]
print(list_c)
# 위아래 차이 잘 이해하기
list_d = [list_a, list_b]
print(list_d)

