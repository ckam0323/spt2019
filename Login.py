import getpass

username = input('username: ')
# 这种方式可以隐藏密码的输入
password = getpass.getpass('password: ')

if username == 'wu' and password == '123':
    print('\033[32;1mLogin successful\033[0m')
else:
    print('\033[33;1mLogin failure\033[0m')