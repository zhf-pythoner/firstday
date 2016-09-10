# firstday
用户注册登陆

登录接口程序说明：
1、实现功能
1）输入用户名密码（预定于账号密码存在passwd.txt文件中）
2）认证成功后显示欢迎信息
3）输错三次后锁定(是一个用户连续输入错误3次锁定)（用户锁定后记录到lock_account.txt）
4）每次登陆都会记录日志文件（日志文件login.log）
5）涉及知识点：函数、文件读写、用户输入、while、for语句使用、颜色输出
6）测试环境说明：
OS:Ubuntu 16.04 LTS
Python:Python 3.5.1+
需要将相关程序及文件都传到测试环境
程序运行：python3 user_login_py3.x_v2.0.py 

7）测试过程
mads@mads-virtual-machine:~/test1$ python3 user_login_py3.x_v2.0.py 
请输入用户名:ss
请输入密码:
用户名或者密码错误，请检查！！！
请输入用户名:ss
请输入密码:
用户名或者密码错误，请检查！！！
请输入用户名:ss
请输入密码:
用户名或者密码错误，请检查！！！
你已经连续三次输出，账号被锁定

mads@mads-virtual-machine:~/test1$ python3 user_login_py3.x_v2.0.py 
请输入用户名:ss
请输入密码:
你已经连续三次输出，账号被锁定
用户名或者密码错误，请检查！！！

mads@mads-virtual-machine:~/test1$ python3 user_login_py3.x_v2.0.py 
请输入用户名:alex
请输入密码:
欢迎登陆成功 alex !!!
