# 문자열의 연결
# + 연산자는 문자열 사이에 들어가게 되면 문자열을 연결해준다
first_name = "Dae Hyeon"
last_name = "Kim"
name = last_name + first_name
print(name)

# +연산자 사용시 각 type이 같아야만 한다.
# temp = "Person" + 100 # str 과 int
# temp = "Person" + 100.10 # str 과 float
# temp = "Person " + str(100)
# print(temp)

# 문자열을 숫자로 변경
# 정수일때
price = int("12345")
print(type(price))
# 실수일때
price = float("1234.5")
print(type(price))

# 문자열의 반복
# 문자열에서 * (곱하기) 연산자를 사용시에 그 숫자만큼 반복 된다.
arrow = "->" * 10
print(arrow)
arrow = "->"
print(arrow * 10)

# %s 는 문자열이나 숫자값을 변수에 대입, 형식을 지정하여서 상황에 맞게 변경 가능
# %s 에 정수 대입
price = 1000
print("가격 : %s" % price)
# %s 에 문자열 대입
time = "13:49"
print("현재 시간 : %s" % time)
# 복수의 값을 대입
# % 뒤에 (소괄호)로 묶어서 입력
temp = "현재 시간은 : %s시 %s분 %s초 입니다."
print(temp % (10, 38, 12)) # 순서대로 대입 된다.

