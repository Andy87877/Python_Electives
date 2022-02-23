a,b,c = map(eval, input().split())
D = (b**2)-(4*a*c)
if (D < 0):
    print("無解")
elif (D == 0):
    s = -b/2*a
    print("重根為: ",s)
else:
    D**=0.5
    s1 = (-b+D)/(2*a)
    s2 = (-b-D)/(2*a)
    print("兩相異實根為:",s1,s2)
