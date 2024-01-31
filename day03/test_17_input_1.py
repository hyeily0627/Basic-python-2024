# file : test_17_input.py
# date : 2024 - 01- 31 
# desc : 콘솔 입력방법

## input('내용추가') 
## 출력 => 컴퓨터 화면, 프린터, 스피커, 빔프로젝터, VR...
## 입력 => *콘솔 입력(키보드), 마우스사용, 목소리, 조이스틱, 터치스크린...

temp_val = int(input('곱하고 싶은 수를 입력하세요> ')) # 문자열에서 정수로 변환(형변환)
print(f'입력값 = {temp_val}')

# 곱하기
result = (temp_val * 5)
print(f'결과 = {result}')

## 오류 잡아서 실행(정수가 아닌 경우)
temp_val = input('곱할 수 입력> ')
if temp_val.isnumeric() == True: # 숫자입력이 아니면 튕겨내기
    temp_val = int(temp_val)
    print(f'입력값 = {temp_val}')
    
    result = (temp_val * 5)
    print(f'결과 = {result}')
else :
    print('잘못된 입력이므로, 정수를 재입력하세요!')

