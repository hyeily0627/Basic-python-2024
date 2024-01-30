# date : 2024 - 01 - 30
# desc : 여러조건 if문 

date = input('날짜 입력(예: 12/31 즉, 월과 일만) >') # 12-31 문자열

month = date.split('/')[0] #12 
day = date.split('/')[1] #31

if month == '12' and day == '25':
    print('Merry Christmas!')
elif month == '01' and day == '01': 
    print('Happy New Year!')
elif month == '06' and day == '27':
    print('Happy Birthday Hyejin!')
else : 
    print('Common Day')

