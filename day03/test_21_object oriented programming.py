# file : test_21_class
# date : 2024 - 01- 31 
# desc : 객체지향 클래스 만들기 

# 클래스(ex. 사람이라는 객체를 만들기 위한 청사진) 만들기
class person : # 사람 클래스 선언
    name = '' # 클래스 안에 변수 = '멤버 변수' 라고 한다.  
    age = 0
    gender = ''

    # 생성자 함수(스페셜 함수) 클래스의 객체를 생성할때 동작. 
    #init == initialization(초기화)
    def __init__(self) -> None:
        self.name = '홍길동'
        self.age = '29'
        self.gender = '남자'

    # 클래스를 호출할 떄 원하는 형태로 변환하여 보여줄 때 사용 : 매직메소드/스페셜메소드
    def __str__(self) -> str:
            strs = f'커스텀 출력, 이름 :{self.name} 객체생성!'
            return strs
        
    #멤버함수 매개변수 self 필수  
    def walk(self):
        print(f'{self.name}이(가) 걸어갑니다.')
    def stop(self):
        print(f'{self.name}이(가) 멈췄습니다.')
    
# 사람 객체 생성, Instance(사례, 예제)
# 클래스 생성때는 ()가 없지만, 사용시에 ()사용 = 문법이니 암기
p1 = person()
p2 = person()

p1.name = '오혜진' #객체명.멤버변수 = ...
p1.age = '27'
p1.gender = '여자'

p2.name = '이용석'
p2.age = '27'
p2.gender = '확인불가'

print(f'p1 => 이름:{p1.name} / 나이:{p1.age} / 성별:{p1.gender}')
print(f'p2 => 이름:{p2.name} / 나이:{p2.age} / 성별:{p2.gender}')

p1.walk()
print('1시간 동안 걸었습니다')
p1.stop()

p2.walk()
print('걷기 싫어합니다')
p2.stop()

print('----생성자 함수 추가 이후----')
p3 = person()
print(f'p3 => 이름:{p3.name} / 나이:{p3.age} / 성별:{p3.gender}')

print(p3)

print(type(p1)) # 결과값 <class '__main__.person'> 

# ## 클래스 증명
# print(id(p1))
# print(id(p2))
# # 위 구문 계속 실행시 출력값 다름 = 즉, 객체는 같을 수 없다. 



