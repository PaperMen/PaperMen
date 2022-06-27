from math import *
# int 형
print(type(17))
# float 형
print(type(17.7))
# str 형
print(type('안녕'))

# 반지름이 r인 구의 부피는 4/3 * PI * r의 세제곱
r = 5.0
# volume = 4.0/3.0 * pi * r ** 3 # ** == 지수
volume = 4.0/3.0 * pi * pow(r, 3)
print(volume)

# 구의 겉넓이 : 4* pi * r의 제곱
outer_area = 4 * pi * pow(r, 2)
print(outer_area)