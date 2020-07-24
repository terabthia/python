# 方法1（等差数列和）
i = 0
result = 0

while i < 101:
    result += i
    i += 2

# 这里result与i的顺序得注意

print(result)

# 方法2（条件语句取余）
i = 1
result = 0
while i < 101:
    if i % 2 == 0:  # 记得这里是双等号
        result += i
    i += 1
print(result)


