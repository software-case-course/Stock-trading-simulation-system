import easyquotation

class userinfo(object):
    def __init__(self, username, userpw):
        self.username = username
        self.userpw = userpw
        self.money = 100000
        self.stocks=[]


a=userinfo("a","b")
b=userinfo("c","d")
user=[];
user.append(a)
user.append(b)
print(user[1].username)