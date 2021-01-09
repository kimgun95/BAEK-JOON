# G번 - 기적의 매매법

# 초기 자본을 입력 받음
money = int(input())
# 14일 간 주식 값을 입력 받음
stock = [0] * 14
stock = input().split(' ')
for i in range(14):
    stock[i] = int(stock[i])
# 준과 성의 자본과 주식 갯수를 초기화
joon = money
sung = money
joon_stock = 0
sung_stock = 0

# 준의 주식 매수 법을 이용하여 계산
for i in range(14):
    while joon >= stock[i]:
        joon -= stock[i]
        joon_stock += 1

# 성의 주식 매수, 매도 법을 이용하여 계산
for i in range(3, 14):
    if stock[i] > stock[i - 1] and stock[i - 1] > stock[i - 2] and stock[i - 2] > stock[i - 3] and sung_stock > 0:
        sung = sung + stock[i] * sung_stock
        sung_stock = 0
    elif stock[i] < stock[i - 1] and stock[i - 1] < stock[i - 2] and stock[i - 2] < stock[i - 3]:
        while sung >= stock[i]:
            sung -= stock[i]
            sung_stock += 1

# 최종 준과 성의 보유 돈에 따른 출력
joon = joon + stock[13] * joon_stock
sung = sung + stock[13] * sung_stock
if joon > sung:
    print("BNP")
elif sung > joon:
    print("TIMING")
else:
    print("SAMESAME")