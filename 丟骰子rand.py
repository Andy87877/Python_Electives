import random
l = []
for i in range(3):
    l.append(random.randint(1,6))
print("你三次擲骰子的點數為"+str(l)+"，總點數為："+str(sum(l)))
