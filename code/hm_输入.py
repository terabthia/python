'''
1. 书写input
    input('提示信息')
2. 观察input的特点
    2.1 遇到input，等等待用户输入
    2.2 接受input，一般存变量方便使用
    2.3 input接收到的数据均为字符串
'''

password = input('请输入您的密码：')
print(f'您输入的密码是：{password}')

print(type(password))