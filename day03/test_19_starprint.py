# file : test_19_starprint.py
# date : 2024 - 01- 31 
# desc : 별찍기(피라미드 만들기)

## 단일 for문으로 별찍기
# STAR = ['*']

# for i in range(1,6) : 
#     print ('*'*i)

# print ('왼쪽으로 별찍기 출력완료!')


# ## 이중 for문으로 별찍기
# for i in range (1, 6):
#     # i 가 1이면, range(1,2) 1번 반복
#     # i 가 2이면, range(1,3) 2번 반복
#     for j in range(1, i+1) : 
#       print('*', end='') # 엔터 대신 empty로 변환 
#     print() # 안쪽 for문이 끝나면 엔터    
# print('왼쪽으로 별찍기 출력!')

for i in range (1, 6):
    # i 가 1이면, range(1,2) 1번 반복
    # i 가 2이면, range(1,3) 2번 반복
    for j in range(1, 6-i+1) : 
      print('*', end='') # 엔터 대신 empty로 변환 
    print() # 안쪽 for문이 끝나면 엔터    
print('왼쪽으로 별찍기_뒤집어서 출력!')

# for i in range(1, 6) : 
#     for j in range(6-i) :  
#         print(' ' , end='')
#     for j in range(i) :
#         print('*' , end='')
#     print(' ')
# print('오른쪽으로 별찍기 출력완료!')

# # 강사님 풀이
# for i in range(1, 6) : 
#     for j in range(6-i) :  
#         print(' ' , end='')
#     for j in range(2*i-1) :
#         print('*' , end='')
#     print(' ')
# print('중앙으로 별찍기 출력완료!')
