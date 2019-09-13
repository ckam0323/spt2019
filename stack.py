# 编写一个栈结构，实现压栈 出栈 查询，后进先出
stack = []

def push_it():          #压栈
    data = input('pls input data: ').strip()
    if data:        #如果输入的非空字符串,则追加到列表
        stack.append(data)

def pop_it():           #出栈
    if stack:
        print('\033[32;1mwhich pop: %s\033[0m' % stack.pop())
    else:
        print('\033[31;1mThis list is Null\033[0m')

def view_it():          #查询
    print('\033[33;1m%s\033[0m' % stack)

def show_menu():        #显示菜单
    #attention!函数后面不要有括号,是把函数放到字典中,不是把函数的执行结果放进去
    cmds = {'0': push_it, '1': pop_it,'2': view_it}
    prompt ="""(0) push it
(1) pop it
(2) view it
(3) quit
[Pls input your choice(0|1|2|3)]> """
    while True:
        choice = input(prompt).strip()[0]
        if choice == '3':
            print('\033[32;1mSee You\033[0m')
            break
        if choice not in ['0','1','2']:
            continue
        cmds[choice]()

if __name__ == '__main__':
    show_menu()
