
import pickle


class userinfo(object):
    def __init__(self, username, userpw, money):
        self.username = username
        self.userpw = userpw
        self.money = money
        self.stocks={}

    def addstock(user,stockcode,num):
        user.stocks[stockcode]=num

    def butstock(user,stockcode,num,nowprice):
        if nowprice*num<=user.money:
            if user.stocks.get(stockcode) == None:
                user.stocks[stockcode]=num
                print(user.stocks[stockcode])
            else:
                user.stocks[stockcode] += num
            user.money-=nowprice*num
            print(user.money)
            return 1
        else:
            return 0

    def sellstock(user,stockcode,num,nowprice):
        if user.stocks[stockcode]>=num:
            user.stocks[stockcode] -= num
            user.money += nowprice * num
            return 1
        else:
            return 0



    def login(users,name,pw):
        for a in users:
            if a.username==name and a.userpw==pw:
                return a
        return 0

    def register(users,name,pw):
        for n in users:
            if n.username==name:
                return 0
        users.append(userinfo(name,pw,1000))
        return users

    def save(users):
        pickle.dump(users, open("user.data", "wb"))





# a=userinfo('mjl','1234',1000)
# b=userinfo('asdasd','asdas',100)
# user=[];
# user.append(a)
# user.append(b)
#
# userinfo.register(user,'asdaassd','asasddas')
# userinfo.register(user,'mjl','asasddas')
#
# userinfo.save(user)
# user2=userinfo.load()
# for c in user2:
#     print(c.username)
# print(userinfo.login(user2,'mjl','1234').money)


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

# user=[]
# userinfo.register(user,'asdaassd','asasddas')
#
# for c in user:
#      print(c.username)