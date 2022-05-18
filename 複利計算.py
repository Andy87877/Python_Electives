money = eval(input("本金金額: "))
time = int(input("幾年後: "))
apr = eval(input("年利率: "))
apr /= 100
for i in range(time):
    money = money*(1+apr)
print("本金為:",money)