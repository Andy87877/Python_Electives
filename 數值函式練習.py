l = []
for i in range(4):
    n = eval(input("請輸入第%d個月的支出金額:"%(i+1)))
    l.append(n)
print("支出最多的金額為:",max(l))
print("支出最少的金額為:",min(l))
print("支出的總額為:",sum(l))
print("支出金額由小到大排序:",sorted(l))