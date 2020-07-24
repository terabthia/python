# 需求：求1-100之间的数字累加和

i = 1  # 没必要从0开始
result = 0  #这里必须从0开始累积

while i < 101:
    result += i
    i += 1

# 这里result与i的顺序得注意

print(result)  # 5050