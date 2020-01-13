from public_fun import *

# 数据采集时间
class getTime(object):
    def __init__(self, data):
        cf = [6]
        cf_a = hexlist2(cf)
        self.o = data[0:cf_a[-1]]
        self.datetime = bw_datetime(self.o)

        self.next = data[cf_a[-1]:]
        self.nextMark = data[cf_a[-1]:cf_a[-1]+2]

# 数据单元
class fun_07():
    def __init__(self):
        if =="02" or =="03":
            self.o = 
            self.oj = 
            self.ol = 
            self.pj = 
            self.pl = 
        elif == "01":
            self = fun_07_01()
        elif == "03":
            self.o = 
            self.oj = 
            self.ol = 
            self.pj = 
            self.pl = 
        elif == "04":
            self.o = 
            self.oj = 
            self.ol = 
            self.pj = 
            self.pl = 
        elif == "05":
            self.o = 
            self.oj = 
            self.ol = 
            self.pj = 
            self.pl = 
        elif == "06":
            self.o = 
            self.oj = 
            self.ol = 
            self.pj = 
            self.pl = 

# 车辆登入
class fun_07_01():
    def __init__(self):
        self.

# 信息上报(实时&补发)
class fun_07_02():
    def __init__(self):
        self.oj = 
    def o(self):
        self.o = 

# 车辆登出
class fun_07_04():

# 平台登入
class fun_07_05():

# 平台登出
class fun_07_06():

######################################################
# 信息上报(实时&补发)
# 整车数据
class fun_07_02_01():
    def __init__(self):
        self.o = {}
        self.oj = self.oj()
        self.ol = self.ol()
        self.pj = self.pj()
        self.pl = self.pl()

# 驱动电机数据
class fun_07_02_02():


# 燃料电池数据
class fun_07_02_03():


# 发动机数据
class fun_07_02_04():


# 车辆位置数据
class fun_07_02_05():


# 极值数据
class fun_07_02_06():


# 报警数据
class fun_07_02_07():


# 可充电储能装置电压数据
class fun_07_02_08():


# 可充电储能装置温度数据
class fun_07_02_09():


######################################################
# 
class fun_07_02_m():
    def __init__(self, data):
        self.m = data[0:2]
        self.mList = []
    def addmliet(self):
        self.mList.append(self.m)
