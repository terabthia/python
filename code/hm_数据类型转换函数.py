# 1. float() -- 将数据转换为浮点型
num1 = 1
str1 = '10'
print(type(float(num1)))  # float
print(float(num1))  # 1.0
print(float(str1))  # 10.0

# 2. str（）-- 将数据转换为字符串型
print(type(str(num1)))  # str

# 3. tuple() -- 将一个序列转换为元组
list1 = [10,20,30]
print(tuple(list1))

# 4. list() -- 将一个序列转化为列表
t1 = (10,20,30)
print(list(t1))

# 5. eval() -- 计算在字符串中的有效python表达式，并返回一个对象
str2 = '1'
str3 = '1.1'
str4 = '(1000,2000,3000)'
str5 = '[1000,2000,3000]'
# 即把字符串中给的数据转化为原有的类型
print(type(eval(str2)))
print(type(eval(str3)))


