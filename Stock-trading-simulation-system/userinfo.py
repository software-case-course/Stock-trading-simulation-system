
class userinfo(object):
    def __init__(self, username, userpw, money):
        self.username = username
        self.userpw = userpw
        self.money = money
        self.stocks={}

    def addstock(self,stockcode,num):
        self.stocks[stockcode]=num

    def login(self,name,pw):
        for a in self:
            if a.username==name and a.userpw==pw:
                return a
        return 0

    def register(self,name,pw):
        for n in self:
            if n.username==name:
                return 0
        self.append(userinfo(name,pw,1000))
        return self



a=userinfo('mjl','1234',1000)
b=userinfo('asdasd','asdas',100)
user=[];
user.append(a)
user.append(b)

userinfo.register(user,'asdaassd','asasddas')
userinfo.register(user,'mjl','asasddas')
for c in user:
    print(c.username)
print(userinfo.login(user,'mjl','1234').money)


# a=userinfo("a","b",100)
# b=userinfo("c","d",100)
# user=[];
# user.append(a)
# user.append(b)
#
# for c in user:
#     print(c.username)
#     userinfo.addstock(c,100001,12313)
#     userinfo.addstock(c, 10401, 12513)
#     userinfo.addstock(c, 104501, 14313)
#
#     print(len(c.stocks))
#     for d in c.stocks:
#         print(d)
#         print(c.stocks[d])