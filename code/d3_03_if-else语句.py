'''
语法：
if 条件：
    执行满足条件后的代码
else:
    执行不满足if条件的代码
'''



# 网吧上网高阶版

age = int(input('您的年龄是：'))
if age >= 18:
    print(f'您的年龄是{age}，您已成年，可以上网')
else:
    print(f'您的年龄是{age}，小朋友快滚吧')

print('系统关闭')