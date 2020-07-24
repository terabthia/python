'''
1. input

2. 检测input的数据类型str

3. 用int（）转换数据类型

4. 检测是否转换成功

'''

num1 = input('请输入第一个数字：')
print(num1)
print(type(num1))  # str

print(type(int(num1)))

num2 = input('请输入第二个数字:')
print(type(float(num2)))




