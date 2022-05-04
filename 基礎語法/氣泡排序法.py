list = []
for i in range(5):
    n = eval(input("請輸入整數: "))
    list.append(n)

print("排序前:",list)

for i in range(5):
    for j in range(4-i):
        if (list[j] > list[j+1]):
            list[j] , list[j+1] = list[j+1], list[j]
    print(list)
print("排序後:",list)