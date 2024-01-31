# file : test_23_module.py
# desc : 모듈 사용 

pi = 3.141592
radius = 5 
print(f'원의 크기는 {radius*radius*pi}')

import math
print(math.pi)

print(f'정확한 원의 크기는 {radius*radius*math.pi}')

print(f'cos(0) = {math.cos(0)}')
print(2 ** 10)
print(math.pow(2, 10))
print(math.ceil(3.1)) # 올림
print(math.floor(3.5)) # 내림
print(round(3.5)) # 반올림(자주 사용되기 때문에 math가 아닌 기본함수로 포함)

import math as m #math로 사용하던 모듈을 m 이라는 이름으로 사용 가능
print(m.sin(2))

from math import pi, pow # 조심해서 사용

print(pi)
print(pow(2,10))
