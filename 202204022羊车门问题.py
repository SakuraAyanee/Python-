# 羊车门问题有3扇关闭的门，一扇门后停着汽车，另外两扇门后是山羊，主持人知道每扇门后是什么。
# 参赛者首先选择一扇门。在开启它之前，主持人会从另外两扇门中打开一扇门，露出门后的山羊。
# 此时，允许参赛者更换自己的选择。请问，参赛者更换选择后，能否增加猜中汽车的机会？
import random

from numpy import *
from random import *
times1 = 0
times2 = 0
time = eval(input("输入次数以开始："))
for i in range(time):
    print("第{}次进行".format(i))
    car_number = randint(1,3)
    print("中奖代码为：",car_number)
        # active = True
    # while active:
    #     choose = eval(input("输入您选择的门："))
    #     try:
    #         int(choose)
    #     except:
    #         "您输入的数不为整数，请重新输入"
    #     else:
    #         if 1 <= choose <= 3:
    #             print("好选择！您选择的是{}号门".format(choose))
    #             active = False
    #         else:
    #             print("请输入1-3的任意数")
    sheep_door = []
    for sheep in range(1,4):
        sheep_door.append(sheep)
    door = sheep_door.copy()
    sheep_door.remove(car_number)
    open_door = sample(sheep_door,1)
    print("主持人打开了：{}号门，里面是羊".format(open_door))
    last_door = open_door[0]
    door.remove(last_door)
    second_time = choice(door)
    print("重新选择了{}号门".format(second_time))
    if second_time == car_number:
        print("猜中了汽车！".format(times1))
        times1 += 1
    else:
         print("没猜中捏")

for i in range(time):
    car_number = randint(1, 3)
    try_number = randint(1, 3)
    if car_number == try_number:
        times2 += 1
        print("直接猜中第{}次".format(times2))
    else:
        print("没猜中捏。")

chance1 = times1 / time
chance2 = times2 / time
print("\n已各执行{}次".format(time))
print("开门重选中奖概率为：{:.2%}".format(chance1))
print("直接选择中奖概率为：{:.2%}".format(chance2))

