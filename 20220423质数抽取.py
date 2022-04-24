from numpy import *

active = True
answer = []  # 创建空的列表
while active:  # 定义循环，当active为True时进行
    try:
        number_min, number_max = map(int, input("请输入一个范围，用空格隔开:").split())  # 请求一个提取质数的范围，并进行试错，出错时返回重新进行
        int(number_min)
        int(number_max)
    except:
        print("输入有误，请重新输入")
    else:
        active = False
        if number_min > number_max:
            number_min, number_max = number_max, number_min  # 当数字为从大到小的范围时，交换上下限数据

for number in range(number_min, number_max + 1):  # 定义循环下限与上限，以number为为变量依次进行
    answer.append(number)  # 生成具有范围内全部数的列表，依次将number添加到answer中
    if number == 0:  # 0不是质数也不是合数，当范围内有0时提示
        print("实际上，0不是质数也不是合数")
    elif number == 1:  # 1不是质数，当范围内有1时提示
        print("1不是质数")
    else:
        if number < 0:  # 负数不是质数，自行移除answer中
            answer.remove(number)
        else:
            for number2 in range(2, number):  # 剔除1后依次求余数，如果存在有余数0零的结果，说明可以被自身和1以外的数整除，为合数
                if number % number2 != 0:
                    continue
                else:
                    answer.remove(number)  # 移除answer即全数列中的合数值，只留质数
                    break
if 0 in answer:
    answer.remove(0)  # 当0和1存在时，移除0和1的值
if 1 in answer:
    answer.remove(1)

print("从{}到{}的质数有{}\n一共{}个".format(number_min, number_max, answer, len(answer)))
