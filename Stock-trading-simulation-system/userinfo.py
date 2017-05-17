import easyquotation

class userinfo(object):
    def __init__(self, username, userpw):
        self.username = username
        self.userpw = userpw


a=userinfo("a","b")
user=[];
user.append(a)
print(user[0].username)