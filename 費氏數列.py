n = int(input("n="))
l = [1,1]
for i in range(n-2):
    l.append(l[i]+l[i+1])
st = [str(a) for a in l]
print(" " . join(st))
