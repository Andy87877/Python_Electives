try:
    print("***本程式進行A除以B的除法計算***")
    A = int(input("請輸入被除數A:"))
    B = int(input("請輸入除數B:"))
    print(A/B)
except ZeroDivisionError as z:
    print("跳至ZeroDivisionError區塊")
    print("錯誤原因:",z)
except ValueError as v:
    print("跳至ValueError區塊")
    print("錯誤原因:",v)
else:
    print("程式沒有發生除以0或字元型態的錯誤!")
finally:
    print("結束!")
