import getpass

userdb={}
def register():
    "注册"
    username = input('new user: ').strip()
    if not username:
        print('\033[33;1musername is  null!\033[0m')
    elif username in userdb:
        print('\033[33;1muser is exists!\033[0m')
    else:
        password = input('new pass: ')
        userdb[username] = password
    # result =  subprocess.run(
    #     'id %s'% username,shell=True,
    #     stdout=subprocess.PIPE,stderr=subprocess.PIPE
    # )
    # if result.returncode == 0:
    #     print("%s is exists" % username)
    #     return
    # subprocess.run('useradd %s' % username,shell=True)
    # subprocess.run(
    #     'echo %s |passwd --stdin %s' % (username,password),
    #     shell=True
    # )
def login():
    "登陆"
    username = input('user: ')
    password = getpass.getpass('pass: ')
    # if username in userak and userak[username] == password:
    if userdb.get(username) == password:
        print('\033[32;1mLogin Successful!\033[0m')
    else:
        print('\033[33;1mLogin Failure!\033[0m')

def show_menu():
    "程序主菜单"
    cmds={'0':register,'1':login}
    prompt = """(0) register
(1) login
(2) quit
pls input your choice [0|1|2]> """
    while True:
        choice = input(prompt).strip()

        if choice == '2':
            print('\033[32;1mSee You\033[0m')
            break

        if choice not in ['0','1','2']:
            print('\033[31;1merr input,pls try again!\033[0m')
            continue
        cmds[choice]()

if __name__ == '__main__':
    show_menu()