# date : 2024 - 02 - 01
# file : test_25_web.py
# dese : urllib 모듈 사용법

## urllib : 웹사이트 내용을 파이썬으로 불러오는 모듈 (url library)

from urllib.request import Request, urlopen  # request 모듈 전부다 끌고오고 싶으면 import 뒤에 * 
                          # 클래스  # 함수

req = Request('https://www.naver.com/') # 네이버 url 삽입
res = urlopen(req) # url주소로 웹사이트를 열라고 요청

print(f'응답코드 : {res.status}') #url로 요청된 웹사이트 응답 확인 #출력값 200 
# 응답코드 404(Not found), 500번대 등 나오면 가져올 수 없음 

print(res.read())

# urllib.request보다 성능이 조금 더 나은 모듈
# 아래 pip 패키지 명령프롬프트 미리 설치 후 구동가능

# # pip 사용
# shell
# > pip --version # 버전확인
# > pip list # 현재 설치된 라이브러리 목록 확인
# > pip install 패키지명 # 패키지를 내 컴퓨터에 설치
# > pip unistall 패키지명 # 패키지를 삭제

import requests 

res2 = requests.get('https://www.naver.com/') 

print(res2.status_code)
print(res2.text)

