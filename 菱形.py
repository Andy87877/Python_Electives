n = int(input('n='))
n = int((n+1)/2)
# 高度應該都是奇數
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i*2-1):
        print("*",end="")
    print()