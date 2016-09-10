#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
import datetime
# import getpass

login_log = "login.log"
password_file = "password.txt"
lock_file = "lock_account.txt"
color_end = "\033[0m"
color_red = "\033[31;1m"
color_green = "\033[32;1m"
today = datetime.datetime.today().strftime("%Y:%m:%d %H:%M:%S")


def log_w(result_name, text):
    """
    进行文件日志记录
    :param result_name: 将内容记录到该文件中
    :param text: 要进行记录的内容
    :return: 默认值None
    """
    f_name = "%s" % result_name
    f_log = open(f_name, "a+")
    f_log.write(text)
    f_log.close()


def register(username, password):
    """
    用户注册功能
    :param username: 接收用户输入的账号
    :param password: 接受用户输入的密码
    :return: True注册成功，False注册失败
    """
    username_list = []
    with open(password_file, 'r') as pas:
        for user_list in pas.readlines():
            user_name, user_pass = user_list.strip('\n').split()
            username_list.append(user_name)
    if username_list.count(username) == 0:
        text = "%s %s\n" % (username, password)
        log_w(password_file, text)
        print(color_green + "账号注册成功" + color_end)
    else:
        print(color_red + "该用户名已经被注册" + color_end)


def login(username, password):
    """
    用户登录功能
    :param username: 接收用户输入的账号
    :param password: 接受用户输入的密码
    :return: True登录成功，False登录失败
    """
    count = 0
    flag = True
    while flag:
        if count < 3:                                         # 只要重试不超过三次就不断循环
            '''
             判断账号是否在锁定列表中，如果已经被锁定过，直接退出程序
          '''
            with open(lock_file, 'r') as pas:
                for line in pas.readlines():
                    if username in line:
                        print(color_red + "你已经连续三次输出，账号被锁定" + color_end)
                        text = "%s user login is locked at %s\n" % (username, today)
                        log_w(login_log, text)
                        flag = False
            '''
              判断账号及密码是否在password.txt文件中存在且正确，如果正确记录日志，输出登录信息
          '''
            with open(password_file, 'r') as pas:
                for line in pas.readlines():
                    user, passwd = line.strip('\n').split()	
                    # 去掉每行多余的\n并把这一行按空格分成两列，分别赋值为user,passwd两个变量
                    if username == user and password == passwd:
                        print(color_green + "欢迎登陆成功 %s !!!" % username + color_end) 	
                        # 输出欢迎信息，根据信息类型添加输入文字的颜色
                        text = "%s user login successfully at %s\n" % (username, today)
                        log_w(login_log, text)
                        flag = False        			# 如果账号及密码信息正确，则记录日志，跳出循环
                        break
                    else:
                        continue
            count += 1
        # 如果同一个账号连续输错三次，则将账号记录到锁定文件列表，并退出程序
        else:
            print(color_red + "你已经连续三次输出，账号被锁定" + color_end)
            text = "%s user login is locked at %s\n" % (username, today)
            log_w(login_log, text)
            text = "%s\n" % username
            log_w(lock_file, text)
            flag = False


def main():
    """
    主函数
    :return:
    """
    msg = '''欢迎登录本系统
1. 注册
2. 登录
3. 退出
'''
    while True:
        os.system('cls')                        # windows清屏
#       os.system('clear')                      # linux清屏
        print(msg)
        input_num = input("请选择:")
        if input_num.strip().isdigit():			# 过滤用户输入内容中的空格，然后判断内容是否是数字 
            input_num = int(input_num)
        if input_num == 1:
            print("账号注册".center(50, "-"))
            username = input("请输入用户名:")
            #   password = getpass.getpass("请输入密码:")           # 隐藏输入的密码信息
            password = input("请输入密码:")
            register(username, password)
        elif input_num == 2:
            username = input("请输入用户名:")
            #   password = getpass.getpass("请输入密码:")           # 隐藏输入的密码信息
            password = input("请输入密码:")
            login(username, password)
        elif input_num == 3:
            break
        else:
            os.system('cls')
            print("输入错误")
            continue

if __name__ == "__main__":
    main()
