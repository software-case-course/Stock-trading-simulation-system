# -*- coding: gb2312 -*-
#用户名密码登录系统（MD5加密并存入文件）及对字符串进行凯撒密码加解密操作
#作者：凯鲁嘎吉 - 博客园 http://www.cnblogs.com/kailugaji/
import hashlib
def md5(arg):#这是加密函数，将传进来的函数加密
        md5_pwd = hashlib.md5(bytes('admin'))
        md5_pwd.update(bytes(arg))
        return md5_pwd.hexdigest()#返回加密的数据

def log(user,pwd):#登录时的函数，由于md5不能反解，因此登陆的时候用正解
        with open('pass.txt','r') as f:
            for line in f:
                u,p=line.strip().split('|')
                if u == user and p == md5(pwd):#登录的时候验证用户名以及加密的密码跟之前保存的是否一样
                     return True

def register(user,pwd):#注册的时候把用户名和加密的密码写进文件，保存起来
        with open('pass.txt','a') as f:
            temp = user+'|'+ md5(pwd)+'\n'
            f.write(temp)

def encryption(): #加解密界面
        offset=int(input('~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                         '请输入偏移量:\n'
                         '大于0小于26:偏移量\n'
                         '0：退出登录\n'
                         '~~~~~~~~~~~~~~~~~~~~~~~~~~\n'))
        if offset in range(1,25):
            variable=int(input('~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                               '请选择操作：\n'
                               '1：加密\n'
                               '2：解密\n'
                               '~~~~~~~~~~~~~~~~~~~~~~~~~~\n'))
            user1=Caesar(offset,variable)
            user1.choose()
        elif offset==0:
            print('谢谢使用，再见！')
            exit(0)
        else:
            print('偏移量超出范围,请重新输入！')

class Caesar: # 定义类，名叫Caesar
    def __init__(self, offset, variable):# 初始化
        self.passage = offset
        self.type = variable

    def encrypt(self,offset): # 加密
        move = (ord(offset)-97+self.passage) % 26+97  # 用ASCII码值来完成移动，ord()将字符转化为对应ASCII码的十进制数
        return chr(move)    #将ASCII码转化为对应的数值，chr()将一个整数转化为Unicode字符

    def decrypt(self,offset): # 解密
        move=(ord(offset)-97-self.passage)%26+97
        if move < 97:
            move = move + 26
        return chr(move)

    def choose(self):   # 选择
        str2=''
        if self.type==1: # 加密时进入
            str1=input("请输入要加密的字符串('xxx'):\n")
            org=str1
            for i in range (len(str1)): # str1为输入的字符串
                str1=str1[:i]+self.encrypt(str1[i])+str1[i+1:]
            for i in range (len(str1)):
                str2=str2+str1[i]
            print ('字符串'+org+'加密后为：'+str2)
        elif self.type==2:  # 解密时进入
            str1=input("请输入要解密的字符串('xxx'):\n")
            org=str1
            for i in range (len(str1)):
                str1=str1[:i]+self.decrypt(str1[i])+str1[i+1:]
            for i in range (len(str1)):
                str2=str2+str1[i]
            print ('字符串'+org+'解密后为：'+str2)
        else:
            print('选择错误，请重新输入！')

class Login:
    def __init__(self,i):
        self.i=i

    def showface(self):
        if self.i==2:
            user = input("用户名('xxx')：")
            pwd =input("密码('xxx')：")
            register(user,pwd)
        elif self.i==1:
            count=1
            while count<=3:
                user = user = input("用户名('xxx')：")
                pwd =input("密码('xxx')：")
                r=log(user,pwd)#验证用户名和密码
                if r==True:
                    print('登录成功')
                    while True:
                        encryption()
                else:
                    print('登录失败')
                count +=1
                if count == 4:
                    print("密码输入次数过多，账户将被锁定！")
                    exit(0)
                else:
                    print("还有%d次尝试机会！"%(4-count))
        elif self.i==0:
            print('谢谢使用，再见！')
            exit(0)
        else:
            print('输入错误，请重新输入！')

if __name__=='__main__':  # 测试程序
    while True:
        i=int(input('~~~~~~~~趣味密码学~~~~~~~\n'
                    '0.退出\n'
                    '1.登录\n'
                    '2.注册\n'
                    '~~~~~~~~~~~~~~~~~~~~~~~~\n'
                    '请输入您的选择：'))
        pass1=Login(i)
        pass1.showface()