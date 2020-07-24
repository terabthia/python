'''
语法：
条件成立执行的表达式  if 条件 else 条件不成立执行的表达式
'''

a = 1
b = 2
c = a if a > b else b
print(c)

# 需求：有俩变量，比较大小，若变量1 大于 变量2，则输出 变量1 - 变量2；否则用变量2 — 变量1
aa = 10
bb = 9
cc = aa - bb if aa > bb else bb-aa
print(cc)

# 进阶版上述需求(带随机数)
import random
dd = random.randrange(0,88,4)
ee = random.randint(0, 99)
print(dd, ee)
ff = dd-ee if dd > ee else ee - dd
print(ff)
