# file : test_15_output.py
# desc : 콘솔 출력 포맷 양식 String Format

print(10)
print('10')
# 출력된 두 10 모두 문자이다. 

string_1 = '{}'.format(10) # {} 위치에 함수 뒤에 들어있는 값(현재는 10)을 치환 및 원하는 양식으로 표현 
print(type(string_1))

name = '오혜진' #input('이름을 입력하세요 > ')
string_2 = '안녕하세요, {} 입니다'. format(name)
print(string_2)

string_3 = '{} {} {}'. format(4000,'만','빌려주세요') #정수를 문자열 포맷
print(string_3)

string_4 = '______{:5d}______'.format(100) # d : 정수

string_4 = '______{:05d}______'.format(100) # 05 : 5자리 만들때 빈자리 0으로 채우기
print(string_4)

string_4 = '______{:=5d}______'.format(-100) # = : 기호와 숫자를 분리
print(string_4)

# 실수 문자열 포맷
string_5 = '_____{}______'.format(73.888888888)
print(string_5) 
string_5 = '_____{:7.2f}_____'.format(78.33333) # 전체자리수는 7자리로, 소수점 뒤는 2자리 fix;
print(string_5)

# 파이썬 3.6 이후 도입. format() 함수 사용하지 않음 
val = 78.333333333333
string_6 = f'_____{val:7.2f}_____'
print(string_6)

#upper case 및 lower case : 대소문자 변환
string_7 = 'hello, world'
print(string_7.upper()) 
string_7 = 'HELLO, WORLD'
print(string_7.lower())
#capitalize
string_7 = 'hello, world'
print(string_7.capitalize())

# splir('  ') : 특정한 단어로 자르는 함수 
print(string_7.split(','))

# 
string_08 = 'Hello, my name is hyejin. Have a good day'
words = string_08.split(' ')
print(words)
print(f'문장의 단어 갯수는 {len(words)}개 이다. ')

string_9 = 'A10'
print(string_9.isalnum()) # true 
print(string_9.isnumeric()) # false - A 알파벳 포함
string_9 = '10.5'
print(string_9.isdecimal()) # false - 정수가 아니므로  

print('안녕'in '안녕하세요') # 문장안에 단어가 있는지 확인