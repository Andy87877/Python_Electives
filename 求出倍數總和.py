# 數值 1~100 中，所有是 3 或 7 倍數的數之總和 = 2208
total = 0;
for i in range(1, 101):
    if (((i % 3) == 0) or ((i % 7) == 0)):
        total += i;
print(total)