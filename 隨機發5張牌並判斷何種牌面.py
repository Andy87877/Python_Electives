# 以後在做
import random
deck = list(range(52))
random.shuffle(deck)
suits = ['黑桃',"紅心","鑽石","梅花"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
s = []
r = []
snumber = []
rnumber = []

def judge(): # 判斷
    # 參考 https://zh.m.wikipedia.org/zh-tw/%E6%92%B2%E5%85%8B%E7%89%8C%E5%9E%8B

    # 同花順 

    # 鐵支
    # flag = True
    # for i in range(4):
    #     if (s[i] != s[i+1]):
    #         flag = False
    #         break
    #     if (r[i].index != r[i+1].index-1):
    #         flag = False
    #         break
    # if (flag): return "鐵支"

    # 胡蘆

    # 同花
    flag = True
    for i in range(4):
        if (s[i] != s[i+1]):
            flag = False
            break
    if (flag): return "同花"
    # 順子

    # 三條

    # 兩隊

    # 對子

    return "散牌"



for i in range(5): # 生成
    suit = suits[deck[i]//13]
    rank = ranks[deck[i] % 13]
    print(suit,rank,"(第", deck[i]+1, "張牌)")
    # 為了判斷用
    s.append(suit)
    snumber.append(deck[i]//13)
    r.append(rank)
    rnumber.append(deck[i] % 13)
print(judge())