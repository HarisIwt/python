# coding=utf-8
# 注意 导入工具包的时候应该将导入的语句 放在文件的顶部
import random  # 导入工具包

computerInput = random.randint(1, 3) # 随机返回1-3的数字
userInput = int(input("请输入要出的拳 -- 石头1/剪刀2/布3 ："))
# if （）or（）or（）：
if ((userInput == 1 and computerInput == 2)
        or (userInput == 2 and computerInput == 3)
        or (userInput == 3 and computerInput == 1)):

    print("电脑出的是 %d， 玩家出的是%d" % (computerInput, userInput))
    print("win")

elif userInput == computerInput:
    print("电脑出的是 %d， 玩家出的是%d" % (computerInput, userInput))
    print("平局")
else:
    print("电脑出的是 %d， 玩家出的是%d" % (computerInput, userInput))
    print("玩家输了")
