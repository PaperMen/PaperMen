# 자동 판매기를 시뮬레이션 하는 프로그램 작성
# 사용자는 천원권과 500원 100원 의 동전을 사용함.
# 물건 값을 사용자로 부터 입력을 받아서 천원과 500원 100원짜리 동전의 갯수를 입력하면 거스름돈을 계산 하여서 반환

item_price = int(input("물건 값을 입력 : "))
bills_1000 = int(input("1000원 갯수 : "))
coin_500 = int(input("500원짜리 갯수 : "))
coin_100 = int(input("100원짜리 갯수 : "))

# 거스름돈 계산
node_money = ((bills_1000 * 1000) + (coin_500 * 500) + (coin_100 * 100)) - item_price
print("거스름돈 : ", node_money)

# 거스름돈(500원 동전 개수를 계산
ncoin_500 = node_money // 500
node_money = node_money % 500

# 거스름돈(500원 동전 개수를 계산
ncoin_100 = node_money // 100
node_money = node_money % 100

# 거스름돈(500원 동전 개수를 계산
ncoin_50 = node_money // 50
node_money = node_money % 50

# 거스름돈(500원 동전 개수를 계산
ncoin_10 = node_money // 10
node_money = node_money % 10

print(f"500원 : {ncoin_500}개, 100원 : {ncoin_100}개, 50원 : {ncoin_50}개, 10원 : {ncoin_10}")
