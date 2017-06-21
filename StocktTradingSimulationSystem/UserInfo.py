
import pickle,time


class userinfo(object):
    def __init__(self, username, userpw, money):
        self.username = username
        self.userpw = userpw
        self.money = money
        self.history=['在 '+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+' 注册账号，初始资本共 '+str(money)+'元']

        self.stocks={}

    def addstock(user,stockcode,num):
        user.stocks[stockcode]=num

    def butstock(user,stockcode,num,nowprice):
        if nowprice*num<=user.money:
            if user.stocks.get(stockcode) == None:
                user.stocks[stockcode]=num
            else:
                user.stocks[stockcode] += num
            user.money-=nowprice*num
            user.history.append('在 '+str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+' 以'+str(nowprice)+'价格' +' 购入股票 '+str(stockcode)+' '+str(num)+'股')
            user.history.append(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+' 余额 '+str(user.money)+'元')
            return 1
        else:
            return 0

    def sellstock(user,stockcode,num,nowprice):
        if user.stocks.get(stockcode) != None:
            if user.stocks[stockcode]>=num:
                user.stocks[stockcode] -= num
                user.money += nowprice * num
                user.history.append('在 ' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) +' 以'+str(nowprice)+'价格' +' 售出股票 ' + str(
                    stockcode) + ' ' + str(num) + '股')
                user.history.append(
                    str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + ' 余额 ' + str(user.money) + '元')
                return 1
            else:
                return 0
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
        users.append(userinfo(name,pw,100000))
        return users

    def save(users):
        pickle.dump(users, open("user.data", "wb"))

