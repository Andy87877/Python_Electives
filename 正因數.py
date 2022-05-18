n = int(input("請輸入正整數:"))
l = []
for i in range(1,n+1):
    if ((n % i) == 0):
        l.append(i)
print(n,"的因數有", l)

if (len(l) == 2):
    print(n,"是質數")
else:
    print(n,"不是質數")