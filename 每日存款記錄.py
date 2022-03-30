l = []
for i in range(1,8):
    print("請輸入第",i,"天",end="")
    n = eval(input("的存款："))
    l.append(n)
print("存款總額：",sum(l),"元")
print(l)