a = 1
b = 2
c = 3

# 1. and 与（都真才真，有假必假)
print((a < b )and (a > c))
print((a < b )and (a < c))

# 2. or 或（都假才假，有真必真）
print((a < b )or (a > c))
print((a > b) or (a > c))

# 3. not 非
print(not a > b)

# 注意：逻辑运算符之间通常加上（）来避免歧义

# 扩展：数字之间的逻辑运算，and运算只要有0结果必为0
#   or运算全部为0结果才是0，不全为0输出第一个不为0的数

print(0 and 1)  # 0
print(0 or 1)  # 1