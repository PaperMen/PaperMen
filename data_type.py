message = 'dons\'t'
print(message)

print("c:\temp\name")
# >> c:	emp
#       ame
print(r"c:\temp\name")  # 문자열 앞에 r 을 붙히면 특수문자로 해석을 안함
# >> c:\temp\name

# %s = 형식지정자
price = 1000
print("상품의 가격은 %s원 입니다." % price)
#>>>> 상품의 가격은 1000원 입니다.

message = "오늘은 %s월 %s일이다."
print(message % (3, 1)) # 하나 이상의 값을 사용하기 위해서는 괄호로 묵어줘여한다.
# >> 오늘은 3월 1일이다.

