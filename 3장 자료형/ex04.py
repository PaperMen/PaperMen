# 문자열

welcome = "happy fucking new year"
# print(welcome)

welcome = 'happy fucking new year'
# print(welcome)

# 문자열안에 \', \" 를 사용할시 하나의 문자로 인식한다
message = '문장안에 따음표\' 출력하기'
# message = "문장안에 따음표 '' 사용하기 " # 쌍따음표 내에서 는 그냥 사용 가능
# print(message)

message  = "first\n Secnod\n Third" # 특수문자 \n 는 줄 바꿈을 뜻함
# print(message)

# 경로를 지정 해줄려고 할때
message = "c:\temp\name\a.txt" # \t == tab 입력 \a == 한칸 공백
# print(message)
# 특수문자를 무시하기 위해 " " 앞에 r 을 사용
message = r"c:\temp\name\a.txt"
# print(message)

# 문자열의 길이를 알자 len()
message = "world"
print(len(message))




