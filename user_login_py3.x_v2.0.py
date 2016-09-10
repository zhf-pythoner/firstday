#!/usr/bin/env python
#-*-coding:utf-8-*-

import sys
import os
import datetime
import getpass

#user = "alex"
#passwd = "alex3714"
login_log = "login.log"
passwd_file = "passwd.txt"
lock_file = "lock_account.txt"
color_end = "\033[0m"
color_red = "\033[31;1m"
color_green = "\033[32;1m"
today = datetime.datetime.today().strftime("%Y:%m:%d %H:%M:%S")

os.system('clear')                              # linux清屏
#os.system('cls')                               # windows清屏

'''该函数功能打印指定内容的到登陆的日志文件'''
def log_w(result_name,text):
    f_name = "%s" % result_name
    f_log = open(f_name,"a+")
    f_log.write(text)
    f_log.close()

count = 0
flag = True
while flag:
    if count<3: 										# 只要重试不超过三次就不断循环  
       username = input("请输入用户名:")
       password = getpass.getpass("请输入密码:")    	# 隐藏输入的密码信息
       '''
         判断账号是否在锁定列表中，如果已经被锁定过，直接退出程序

       '''
       with open(lock_file,'r') as pas:				
           for line in pas.readlines():
               if username in line:
                  #print("get")
                  print(color_red + "你已经连续三次输出，账号被锁定" + color_end)
                  text = "%s user login is locked at %s\n" % (username,today) 
                  log_w(login_log,text)
                  flag = False

       '''
          判断账号及密码是否在passwd.txt文件中存在且正确，如果正确记录日志，输出登录信息

       '''
       with open(passwd_file,'r') as pas:
           for line in pas.readlines():
               user,passwd = line.strip('\n').split()									# 去掉每行多余的\n并把这一行按空格分成两列，分别赋值为user,passwd两个变量 
               #print(user,passwd)
               if username == user and password == passwd:
                  print(color_green + "欢迎登陆成功 %s !!!" % username + color_end) 	# 输出欢迎信息，根据信息类型添加输入文字的颜色
                  text = "%s user login successfully at %s\n" % (username,today) 
                  log_w(login_log,text)
                  flag = False        													# 如果账号及密码信息正确，则记录日志，跳出循环
               else:
                  count += 1
                  #print(count)
                  print(color_red +"用户名或者密码错误，请检查！！！" + color_end)
                  text = "%s user login failed at %s\n" % (username,today) 
                  log_w(login_log,text)

    # 如果同一个账号连续输错三次，则将账号记录到锁定文件列表，并退出程序
    else:
        print(color_red + "你已经连续三次输出，账号被锁定" + color_end)
        text = "%s user login is locked at %s\n" % (username,today) 
        log_w(login_log,text)
        text = "%s\n" % username
        log_w(lock_file,text)
        flag = False
