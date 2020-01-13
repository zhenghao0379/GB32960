# oj 原始（json）
# ol 原始（dataframe）
# pj 解析（json）
# pl 解析（dataframe）

######################################################
import numpy as np
import pandas as pd
import binascii
import math
import datetime
import json

from abc import ABCMeta, abstractmethod

from public_fun import *

######################################################
# 主体
class gb32960(object):
    def __init__(self):
        self.oj = self.oj()
        self.ol = self.ol()
        self.pj = self.pj()
        self.pl = self.pl()
        self.custom = self.custom()
    def oj(self):
        return 
    def ol(self):
        return 
    def pj(self):
        return 
    def pl(self):
        return 
    def custom(self):
        return 
        
######################################################
# 数据采集时间
class bw_datetime():
    def __init__(self, datetime):
        self.datetime = bw_datetime(datetime)

# 起始部分
class fun_01to06(object):
    def __init__(self, data):
        cf = [2, 1, 1, 17, 1, 2]
        cf_a = hexlist2(cf)
        self.o = data[0:cf_a[-1]]
        self.oj = {
            "起始符":self.o[cf_a[0]:cf_a[1]],
            "命令标识":self.o[cf_a[1]:cf_a[2]],
            "应答标志":self.o[cf_a[2]:cf_a[3]],
            "唯一识别码":self.o[cf_a[3]:cf_a[4]],
            "数据单元加密方式":self.o[cf_a[4]:cf_a[5]],
            "数据单元长度":self.o[cf_a[5]:cf_a[6]],
        }
        self.ol = pd.DataFrame.from_dict(self.oj,orient='index').T
        self.pj = {
            "起始符":hex2str(self.oj["起始符"]),
            "命令标识":dict_list_replace('02', self.oj['命令标识']),
            "应答标志":dict_list_replace('03', self.oj['应答标志']),
            "唯一识别码":hex2str(self.oj["唯一识别码"]),
            "数据单元加密方式":dict_list_replace('05', self.oj['数据单元加密方式']),
            "数据单元长度":hex2dec(self.oj["数据单元长度"]),
        }
        self.pl = pd.DataFrame.from_dict(self.pj,orient='index').T
        self.next = data[cf_a[-1]:]
        self.nextMark = data[cf_a[-1]:cf_a[-1]+2]
        self.mo = self.oj["命令标识"]

# 效验码
class fun_08():
    def __init__(self, data):
        self.o = data[-1]
    
    def BCC(self):
        return 
# 数据单元
class fun_07():
    def __init__(self):
        return
    def o():
        return
    def p():
        return 

# 车辆登入
class fun_07_01():
    def __init__(self):
        return

# 信息上报(实时&补发)
class fun_07_02and03():

# 车辆登出
class fun_07_04():

# 平台登入
class fun_07_05():

# 平台登出
class fun_07_06():




######################################################
# 标识符
class fun_07_02_m():
    def __init__(self):
        self.__markList = []
    def __getMark(self, mark):
        self.__markList.append(mark)
    def returnMark(self):
        return self.__markList[-1]

# 剩余报文
class surplus():
    def __init__(self):
        pass
    def 


# 全局变量（剩余报文）

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
    def oj(self): 
        return 
    def ol(self):
        return 
    def pj(self):
        return 
    def pl(self):
        return 
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
# 自定义部分报文
class custom():
    def __init__(self):
        self.o = o()

