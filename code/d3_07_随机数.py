"""
步骤
    1. 导入模块
    import random
    2. 使用这个模块中的功能
     2.1 random.randint() -- 随机整数
     2.2 random.uniform(下限，上限) -- 随机范围内浮点数
     2.3 random.random() -- 随机浮点数
     2.4 random.randrange(下限，上限，步长)-- 定步长随机整数
     2.5 rnadom.sample(字符串，随机选取的数量)-- 随机字符串中的字符
"""

import random

num1 = random.randint(0, 25)   # 0-25的随机整数
num2 = random.random()  # 随机浮点数
num3 = random.uniform(2, 10) # 2-10的随机浮点数
num4 = random.randrange(0, 99 ,3)  #0-99之间步长为3的数，即0,3,6...99中任意一个数
num5 = random.sample('bonjoursalut', 4)  # 随机选取字符串中四个私字符
print(num1, num2, num3, num4, num5)


