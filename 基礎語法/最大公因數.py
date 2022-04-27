a, b = map(int, input().split())

for i in range(a, -1,-1):
    if (((a % i) == 0) and ((b % i) == 0)):
        ans = i
        break
print(ans)
