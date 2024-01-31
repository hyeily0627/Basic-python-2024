# file : test_22_car.py
# date : 2024 - 01- 31 
# desc : 객체지향 Car 클래스 만들기

class Car :
    wheel_num = 4
    color = 'white'
    __plate_num = ''
    company = ''
    gear_type = ''

    # 전진, 후진, 좌회전, 우회전
    def moveforward(self):
        print(f'{self.__plate_num}이 전진합니다.')

    def moveback(self):
        print(f'{self.__plate_num}이 후진합니다.')
    
    def moveleft(self):
        print(f'{self.__plate_num}이 좌회전합니다.')

    def moveright(self):
        print(f'{self.__plate_num}이 우회전합니다.')

    def __init__(self, __plate_num, company, color, gear) -> None :
        self.__plate_num = __plate_num
        self.company = company
        self.color = color
        self.gear = gear

    def __str__(self) -> str: #print(객체) 출력되는 부분
        return f'제 차는 {self.__plate_num}입니다. {self.color}입니다.'

    def getplatenumber(self) : # 외부에서 접근할 수 없도록 막는 조치
        return self.__plate_num
    def setplatenumber(self, new_platenumber):
        self.__plate_num = new_platenumber


bungbung = Car('00라 4862','테슬라', '흰색', '자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있다.
print(bungbung)
print(f'차 번호는{bungbung.getplatenumber()}') #bungbung,getplatenumber()
print(f'차 색상은{bungbung.color}')
bungbung.moveforward()

# singsing = Car('27이 2312','현대자동차', '블랙', '자동')
# print(f'차 번호는{singsing.plate_num}')

bungbung.__plate_num = '9812' #악의적인 의도를 가지고 변경
print(bungbung)

bungbung.setplatenumber('231245')  # 캡슐화!
print(bungbung)