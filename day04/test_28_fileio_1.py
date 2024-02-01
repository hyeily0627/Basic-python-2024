# date : 2024 - 02 - 01
# file : test_28_fileio.py
# dese : 텍스트 파일 입출력

# mode : a(ppend : 내용 추가) r(ead : 파일 읽기) w(rite : 파일쓰기)
# encoding : cp949(한글), utf-8(만국공통어)

f= open('sample.txt', mode='w', encoding='utf8')
# mode a w
# 뭔가를 한다. write()에서 엔터를 추가하려면 마지막에 \n 추가
f.write('안녕하세요. 우리는 iot 개발자 과정입니다\n') 
f.write('안녕하세요')

f.close() # 파일은 무조건 마지막에 닫는다.
print('파일이 생성되었습니다')