# -*- coding: gb2312 -*-
#�û��������¼ϵͳ��MD5���ܲ������ļ��������ַ������п�������ӽ��ܲ���
#���ߣ���³�¼� - ����԰ http://www.cnblogs.com/kailugaji/
import hashlib
def md5(arg):#���Ǽ��ܺ��������������ĺ�������
        md5_pwd = hashlib.md5(bytes('admin'))
        md5_pwd.update(bytes(arg))
        return md5_pwd.hexdigest()#���ؼ��ܵ�����

def log(user,pwd):#��¼ʱ�ĺ���������md5���ܷ��⣬��˵�½��ʱ��������
        with open('pass.txt','r') as f:
            for line in f:
                u,p=line.strip().split('|')
                if u == user and p == md5(pwd):#��¼��ʱ����֤�û����Լ����ܵ������֮ǰ������Ƿ�һ��
                     return True

def register(user,pwd):#ע���ʱ����û����ͼ��ܵ�����д���ļ�����������
        with open('pass.txt','a') as f:
            temp = user+'|'+ md5(pwd)+'\n'
            f.write(temp)

def encryption(): #�ӽ��ܽ���
        offset=int(input('~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                         '������ƫ����:\n'
                         '����0С��26:ƫ����\n'
                         '0���˳���¼\n'
                         '~~~~~~~~~~~~~~~~~~~~~~~~~~\n'))
        if offset in range(1,25):
            variable=int(input('~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                               '��ѡ�������\n'
                               '1������\n'
                               '2������\n'
                               '~~~~~~~~~~~~~~~~~~~~~~~~~~\n'))
            user1=Caesar(offset,variable)
            user1.choose()
        elif offset==0:
            print('ллʹ�ã��ټ���')
            exit(0)
        else:
            print('ƫ����������Χ,���������룡')

class Caesar: # �����࣬����Caesar
    def __init__(self, offset, variable):# ��ʼ��
        self.passage = offset
        self.type = variable

    def encrypt(self,offset): # ����
        move = (ord(offset)-97+self.passage) % 26+97  # ��ASCII��ֵ������ƶ���ord()���ַ�ת��Ϊ��ӦASCII���ʮ������
        return chr(move)    #��ASCII��ת��Ϊ��Ӧ����ֵ��chr()��һ������ת��ΪUnicode�ַ�

    def decrypt(self,offset): # ����
        move=(ord(offset)-97-self.passage)%26+97
        if move < 97:
            move = move + 26
        return chr(move)

    def choose(self):   # ѡ��
        str2=''
        if self.type==1: # ����ʱ����
            str1=input("������Ҫ���ܵ��ַ���('xxx'):\n")
            org=str1
            for i in range (len(str1)): # str1Ϊ������ַ���
                str1=str1[:i]+self.encrypt(str1[i])+str1[i+1:]
            for i in range (len(str1)):
                str2=str2+str1[i]
            print ('�ַ���'+org+'���ܺ�Ϊ��'+str2)
        elif self.type==2:  # ����ʱ����
            str1=input("������Ҫ���ܵ��ַ���('xxx'):\n")
            org=str1
            for i in range (len(str1)):
                str1=str1[:i]+self.decrypt(str1[i])+str1[i+1:]
            for i in range (len(str1)):
                str2=str2+str1[i]
            print ('�ַ���'+org+'���ܺ�Ϊ��'+str2)
        else:
            print('ѡ��������������룡')

class Login:
    def __init__(self,i):
        self.i=i

    def showface(self):
        if self.i==2:
            user = input("�û���('xxx')��")
            pwd =input("����('xxx')��")
            register(user,pwd)
        elif self.i==1:
            count=1
            while count<=3:
                user = user = input("�û���('xxx')��")
                pwd =input("����('xxx')��")
                r=log(user,pwd)#��֤�û���������
                if r==True:
                    print('��¼�ɹ�')
                    while True:
                        encryption()
                else:
                    print('��¼ʧ��')
                count +=1
                if count == 4:
                    print("��������������࣬�˻�����������")
                    exit(0)
                else:
                    print("����%d�γ��Ի��ᣡ"%(4-count))
        elif self.i==0:
            print('ллʹ�ã��ټ���')
            exit(0)
        else:
            print('����������������룡')

if __name__=='__main__':  # ���Գ���
    while True:
        i=int(input('~~~~~~~~Ȥζ����ѧ~~~~~~~\n'
                    '0.�˳�\n'
                    '1.��¼\n'
                    '2.ע��\n'
                    '~~~~~~~~~~~~~~~~~~~~~~~~\n'
                    '����������ѡ��'))
        pass1=Login(i)
        pass1.showface()