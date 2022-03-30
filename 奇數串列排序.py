numbers=[21,4,35,1,8,7,3,6,9,15,26,33]
l = []
for i in numbers:
    if ((i % 2) == 1):
        l.append(i)
print("奇數串列由小到大排序：",sorted(l))