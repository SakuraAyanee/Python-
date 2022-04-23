# 4.1
from random import *

A = True
while A:
    answer = randint(0, 100)
    print("已生成0—100的随机数")
    active = True
    active2 = True
    time = 0
    while active:
        number_active = True
        while number_active:
            try:
                number = eval(input("请输入您猜的数："))
                int(number)
            except:
                print("输入有误，请检查是否为整数。")
            else:
                number_active = False

        if number > answer:
            time += 1
            print("答错了哦，答案应该更小。")

        elif number < answer:
            time += 1
            print("答错了哦，答案应该更大。")

        else:
            print("<<{:=^60}>>".format(""))
            print("答对了！！！！\n答案是{},您一共猜了{}次。".format(answer, time))
            active = False
            while active2:
                A = input("您想再玩一次吗？Y/N")
                if A == "y" or A =="Y":
                    active2 = False
                elif A == "N" or A == "n":
                    A = False
                    active2 = False
                else:
                    print("输入有误，请输入Y或N")
