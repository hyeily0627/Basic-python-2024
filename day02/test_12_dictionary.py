# date : 2024 - 01 - 30
# desc : 복합 자료형 딕셔너리 
# file : test12_dictionary

## 사전형 - key와 value쌍을 나열해놓은 자료형
# { key:value, key:value, key:value,... }

dict_movie = { 'name' : '어벤져스 엔드게임', 'type' : '히어로 무비', 'year' : 2019, 'director' : ['안소니 루소', '조 루소'] , 'cast': ['아이언맨', '타노스','헐크', '닥터스트레인지','블랙위도우']}

# 조회
print(dict_movie['name'])
print(dict_movie['year'])

# 추가 및 수정
dict_movie['producer'] = '케빈 파이기' 
print(dict_movie['producer'])

dict_movie['year'] = 2020
print(dict_movie['year'])

# 키에 대한 값 찾기 
if 'musucian' in dict_movie : 
    print(dict_movie['musucian'])
else :
    print('관련사항 없음!')

musucian = dict_movie.get('musucian') # 오류(예외)발생x 
print(musucian)     
#print(dict_movie['musucian']) # 오류(예외)발생O 

print('-----------------------------------')

# 반복문으로 출력
print('반복문 사용 1번')
for key in dict_movie:
    print(key,':', dict_movie[key])

print('            ')

print('반복문 사용 2번')

for key, value in dict_movie.items():
    print(key, ':', value)

