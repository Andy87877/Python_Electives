'''
Simulation_Covid_School_Quarantine_Policy
模擬 觀察對象是否被隔離的比例
by: https://github.com/Andy87877
🟩 = No Quarantine (不用隔離者)
🟨 = Quarantine (隔離者)
🟥 = Covid (確診者)
🟦 = Object of observation (觀察對象)
'''
import random # 隨機數
import time # 等待時間

def judge(): # 模擬
    m = 7 # m=長 m >= 3
    n = 7 # n=寬 n >= 3
    have_case = 5 # 有多少位確診
    classroom = [] # 教室
    is_case = [] # 哪幾位確診

    for i in range(m): # 先讓所有人都不需隔離
        classroom.append([])
        for j in range(n):
            classroom[i].append("🟩")

    while (have_case != len(is_case)): # 產生確診者
        flag = True
        temp = random.randint(0,m*n-1) # 隨機
        for i in is_case:
            if (i == temp): # 已經確診過了(重選)
                flag = False 
        if (flag): # 未入確診名單(加入)
            is_case.append(temp)
            classroom[int(temp/n)][int(temp%n)] = "🟥" 
    
    for i in range(m): # 判斷是否被匡列 
        for j in range(n):
            if (classroom[i][j] != "🟥"): 
                if ((i == 0) and (j == 0)): 
                    if ((classroom[i+1][j] == "🟥") or (classroom[i+1][j+1] == "🟥") or (classroom[i][j+1] == "🟥")):
                        classroom[i][j] = "🟨"
                elif ((i == 0) and (j == n-1)): 
                    if ((classroom[i+1][j] == "🟥") or (classroom[i+1][j-1] == "🟥") or (classroom[i][j-1] == "🟥")):
                        classroom[i][j] = "🟨"
                elif ((i == m-1) and (j == 0)): 
                    if ((classroom[i-1][j] == "🟥") or (classroom[i-1][j+1] == "🟥") or (classroom[i][j+1] == "🟥")):
                        classroom[i][j] = "🟨"
                elif ((i == m-1) and (j == n-1)):
                    if ((classroom[i-1][j] == "🟥") or (classroom[i-1][j-1] == "🟥") or (classroom[i][j-1] == "🟥")):
                        classroom[i][j] = "🟨"
                elif (i == 0):
                    if ((classroom[i+1][j] == "🟥") or (classroom[i+1][j+1] == "🟥") or (classroom[i+1][j-1] == "🟥") or (classroom[i][j+1] == "🟥") or (classroom[i][j-1] == "🟥")):
                        classroom[i][j] = "🟨"
                elif (j == 0):
                    if ((classroom[i][j+1] == "🟥") or (classroom[i+1][j+1] == "🟥") or (classroom[i-1][j+1] == "🟥") or (classroom[i+1][j] == "🟥") or (classroom[i-1][j] == "🟥")):
                        classroom[i][j] = "🟨"
                elif (i == m-1):
                    if ((classroom[i-1][j] == "🟥") or (classroom[i-1][j+1] == "🟥") or (classroom[i-1][j-1] == "🟥") or (classroom[i][j+1] == "🟥") or (classroom[i][j-1] == "🟥")):
                        classroom[i][j] = "🟨"
                elif (j == n-1):
                    if ((classroom[i][j-1] == "🟥") or (classroom[i+1][j-1] == "🟥") or (classroom[i-1][j-1] == "🟥") or (classroom[i+1][j] == "🟥") or (classroom[i-1][j] == "🟥")):
                        classroom[i][j] = "🟨"
                else:
                    if ((classroom[i+1][j] == "🟥") or (classroom[i+1][j+1] == "🟥") or (classroom[i+1][j-1] == "🟥") or (classroom[i][j+1] == "🟥") or (classroom[i][j-1] == "🟥") or (classroom[i-1][j+1] == "🟥") or (classroom[i-1][j] == "🟥") or (classroom[i-1][j-1] == "🟥")):
                        classroom[i][j] = "🟨"

    # Sus position (判斷想觀察對象是否被隔離)
    while (is_case.count(temp) != 0): # 不是確診者
        temp = random.randint(0,m*n-1)
    if (classroom[int(temp/n)][int(temp%n)] == "🟨"): flag = True
    else: flag = False
    classroom[int(temp/n)][int(temp%n)] = "🟦" # 觀察對象為藍色
    print(temp)
    for i in range(m): # 顯示座位(看確診隔離情況)
        for j in range(n):
            print(classroom[i][j], end=" ")
        print()
    return flag # 回傳是否隔離

''' 這好像不太實用ww
def percent(n,m): # 求出最大公因數
    for i in range(2,n):
        while(n%i==0 and m%i==0):
            n=n//i # //為整除
            m=m//i
    return(str(n)+"/"+str(m))
'''

times = 1000 # 模擬次數
quar = 0 # 被隔離的次數
Simulation_txt = open('Simulation.txt', 'w+') # 要寫入的文字檔
for i in range(1,times+1):
    if (judge()):
        quar += 1
        #time.sleep(0.1) # 等待0.1秒
    print("隔離第%d次/模擬第%d次/隔離百分比為%5.2f"%(quar, i, quar/i))
    Simulation_txt.write("隔離第%d次/模擬第%d次/隔離百分比為%5.2f \n"%(quar, i, quar/i))

Simulation_txt.flush() 
Simulation_txt.close() 