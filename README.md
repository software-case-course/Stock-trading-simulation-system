# 股票交易模拟系统

股票交易模拟系统可以实现股价的实时更新查询，以及客户对股票的买卖。<br>客户除可买卖股票外，也可对账户余额进行更改，模拟股票交易流程。<br>系统的主要模块包括用户管理模块、股票查询模块、股票买卖模块三个部分。

##### 1.用户管理模块 

* 注册功能  

* 登陆功能  

##### 2.股票查询模块 

* 两个数据接口（新浪、腾讯接口）

* 输入股票代码（6位数字如：华宝油气————162411）  

* 显示股票名称、现价、开盘价、昨日收盘价、今日最低价、时间、日期  

##### 3.股票交易模块 


### 版本进度 v1

使用PyQt5完成股票信息查询模块的UI界面， 使用了[easyquotation](https://github.com/shidenggui/easyquotation)，输入股票代码即可获取实时或当天信息


程序基于python3编写，需要先布置python环境使用，请于[python官网](https://www.python.org/downloads/）或[备用](http://pan.baidu.com/s/1pLdkCIJ)下载。

可能需要用到的python模块：

pip install requests
pip install aiohttp
pip install easyutils
pip install pyQt5

