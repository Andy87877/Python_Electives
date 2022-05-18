PM = {}
PM["台北市"] = 6
PM["台中市"] = 8
PM["新北市"] = 2
PM["台南市"] = 3
PM["桃園市"] = 5
PM["高雄市"] = 9
city = input("輸入要查詢的六都名稱:")
if city not in PM:
    print("六都中沒有[%s]城市!"%(city))
else:
    print(city,"今天的PM2.5值為:",PM[city])
