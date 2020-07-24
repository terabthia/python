age = 18
name = 'TOM'

# 我的名字是x，今年x岁了
print('我的名字是%s，今年%s岁了' % (name, age))
print('我的名字是%s，今年%s岁了' % (name, age + 1))

# 语法 f'{表达式}'
print(f'我的名字是{name}，今年{age}岁了')  # 高效于%s方式
print(f'我的名字是{name}，明年{age + 1}岁了')