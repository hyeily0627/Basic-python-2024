# file : test_16_timestable.py
# desc : 구구단 프로그램
# spec : for 구문과 이중 for문의 이해 중요 

# 2 X 1 = 2 
# x X y

# # 2단 
# x = 2 
# for y in range (1,9) :
#     print(f'{x} x {y} = {x * y}')

# # 2단 자릿수 정렬
# x = 2 
# for y in range (1,9) :
#     print(f'{x} x {y} = {x * y:2d}') # 숫자 자릿수 정렬

# 2단~9단
for x in range(2,10) : 
    for y in range (1,10) :
        print(f'{x} x {y} = {x * y:2d}')


# 디버깅 : 벌레잡기 (최초의 컴퓨터는 코드를 꽂아 코딩했는데, 벌레(버그)로 인해 코딩이 안되는 경우가 있어 이를 제거함에서 유래하였다.)
# F9 : 중단점 토글
# F5 : 디버그 시작
# 조사식 확인!
# F10 : 한 줄씩 실행 
# F11 : 함수안으로 진입
# shift + F5 : 디버깅 종료

print('**구구단 시작!**')
for x in range(2,10) : # 2부터 9까지 반복
    print(f'<{x} 단 시작>')
    for y in range (1,10) : # 1부터 9까지 반복
        print(f'{x} x {y} = {x * y:2d}', end =' / ') # end = '' 엔터대신 공백으로 처리 / 삽입 
    print() # 안쪽 for문 종료시 마지막 엔터를 추가 