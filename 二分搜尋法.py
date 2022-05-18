from ast import Is


num=[256,731,943,389,142,645,829,945,371,418]
name=["林小虎","王中森","邵木淼","李大同","陳子孔","鄭美麗","曾溫柔","錢來多","賈天良","吳水品"]

size = len(num)-1 # 串列長度-1
IsFound = False # 是否有被找到
min = 0
max = size
c = 0 # 計算比對次數

for i in range(size):
    for j in range(size-i):
        if (num[j] > num[j+1]):
            num[j],num[j+1] = num[j+1],num[j]
            name[j],name[j+1] = name[j+1], name[j]

no = input("請輸入中獎號碼：")
while(min <= max):
    mid = int((max-min)/2)
    c += 1
    if (num[mid] == no):
        IsFound = True
        break

    if (num[mid] > no):
        max = mid-1
    else:
        min = mid+1

if(IsFound):
    print("中獎者的姓名為：",name[mid])
else:
    print("無此中獎號碼！")
print("共比對",c,"次")