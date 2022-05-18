num=[256,731,943,389,142,645,829,945]
name=["林小虎","王中森","邵木淼","李大同","陳子孔","鄭美麗","曾溫柔","錢來多"]
n = int(input("請輸入中獎者的編號："))

flag = False
for i in range(len(name)):
    if (n == num[i]):
        flag = True
        break
if (flag):
    print("中獎者的姓名為：",name[i])
else:
    print("無此中獎號碼!")
print("共比對 %d次"%(i+1))
