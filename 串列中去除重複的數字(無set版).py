l = [1,2,3,4,2,7,3,2,3]
ansl = []
sorted(l)
for i in l:
    if i not in ansl:
        ansl.append(i)
print(ansl)
# print(sorted(list(set(l))))