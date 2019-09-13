#!/usr/bin/python
# 仅限Linux环境
import sys
import randompass
import subprocess

def add_user(username,password,fname):
    #  判断用户是否已存在
    result = subprocess.run(
        'id %s' % username,shell=True,
        stdout=subprocess.PIPE,stderr=subprocess.PIPE
    )
    if result.returncode == 0:
        print('%s 已存在' % username)
        #函数遇到return就结束了,不会再向下执行
        return
    # 加sudo给命令前需要提升用户权限,/etc/sudoers
    # /usr/sbin/useradd,/bin/sh,/usr/bin/passwd
    subprocess.run('sudo useradd %s'% username,shell=True)
    subprocess.run('echo %s | sudo passwd --stdin %s' %(password,username),
                   shell=True
                   )

    #将用户信息写入文件
    uinfo = """userinfo:
user:%s
pass:%s
""" % (username,password)
    with open(fname,'a') as fobj:
        fobj.write(uinfo)
if __name__ == '__main__':
    username = sys.argv[1]
    password = randompass.randpass()
    add_user(username,password,'/tmp/users.txt')