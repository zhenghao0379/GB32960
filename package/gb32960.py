# import Ipynb_importer
import pandas as pd

from .public_fun import * 

import globalVar as glv

## fun_01to06

class fun_01to06(object):
    def __init__(self, data):
        self.cf = [2, 1, 1, 17, 1, 2]
        self.cf_a = hexlist2(self.cf)
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            "起始符",
            "命令标识",
            "应答标志",
            "唯一识别码",
            "数据单元加密方式",
            "数据单元长度"
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            "起始符":hex2str(self.oj["起始符"]),
            "命令标识":dict_list_replace('02', self.oj['命令标识']),
            "应答标志":dict_list_replace('03', self.oj['应答标志']),
            "唯一识别码":hex2str(self.oj["唯一识别码"]),
            "数据单元加密方式":dict_list_replace('05', self.oj['数据单元加密方式']),
            "数据单元长度":hex2dec(self.oj["数据单元长度"]),
        }
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        self.mo = self.oj["命令标识"]
        
        glv.set_value('data_f', self.next)
        glv.set_value('data_mo', self.mo)
        
        glv.set_value('data_01to07', self.o)
        print('fun_01to06 done!')

## fun_07

class fun_07:
    def __init__(self, data):
        
        self.mo = glv.get_value("data_mo")
        if self.mo == '01':
            self.o = fun_07_01(glv.get_value('data_f'))
        elif self.mo == '02' or self.mo == '03':
            self.o = fun_07_02(glv.get_value('data_f'))
        elif self.mo == '04':
            self.o = fun_07_04(glv.get_value('data_f'))
        elif self.mo == '05':
            self.o = fun_07_05(glv.get_value('data_f'))
        elif self.mo == '06':
            self.o = fun_07_06(glv.get_value('data_f'))
        else :
            print('命令标识:',self.mo,'有误')
        
        self.c = fun_07_cursor(glv.get_value('data_f'))
        
        self.oj = dict(self.o.oj, **self.c.oj)
        self.oj2 = {'数据单元':self.oj}
        self.ol = pd.merge(self.o.ol, self.c.ol, left_index=True, right_index=True)
        self.pj = dict(self.o.pj, **self.c.pj)
        self.pj2 = {'数据单元':self.pj}
        self.pl = pd.merge(self.o.pl, self.c.pl, left_index=True, right_index=True)
        
        print('fun_07 done!')

## fun_07_01

class fun_07_01(object):
    def __init__(self, data):
        self.cf = [6, 2, 20, 1, 1]
        self.cf_a = hexlist2(self.cf)
        self.n = hex2dec(data[self.cf_a[3]:self.cf_a[4]])
        self.m = hex2dec(data[self.cf_a[4]:self.cf_a[5]])
        self.cf.append(self.n*self.m)
        self.cf_a = hexlist2(self.cf)
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            "数据采集时间",
            "登入流水号",
            "ICCID",
            "可充电储能子系统数",
            "可充电储能系统编码长度",
            "可充电储能系统编码",
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        self.oj2 = {'车辆登入': self.oj}
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            "数据采集时间":get_datetime(self.oj['数据采集时间']),
            "登入流水号":hex2dec(self.oj['登入流水号']),
            "ICCID":hex2str(self.oj['ICCID']),
            "可充电储能子系统数":hex2dec(self.oj['可充电储能子系统数']),
            "可充电储能系统编码长度":hex2dec(self.oj['可充电储能系统编码长度']),
            "可充电储能系统编码":fun_07_01.fun_07_01_06(self.oj['可充电储能系统编码'], self.oj['可充电储能子系统数'], self.oj['可充电储能系统编码长度']),
        }
        self.pj2 = {'车辆登入': self.pj}
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        
        glv.set_value('data_07_01', self.o)
        
        print('fun_07_01 done!')
        
    def fun_07_01_06(data, n, m):
        if m=='00':
            return "NA"
        else :
            n = hex2dec(n)
            m = hex2dec(m) * 2
            output = []
            for i in range(n):                
                output_unit = hex2str(data[i * m: i* m +m])
                output.append(output_unit)
            return output

## fun_07_04

class fun_07_04(object):
    def __init__(self, data):
        self.cf = [6, 2]
        self.cf_a = hexlist2(self.cf)
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            "登出时间",
            "登出流水号",
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            "登出时间":get_datetime(self.oj['登出时间']),
            "登出流水号":hex2dec(self.oj['登出流水号']),
        }
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        
        glv.set_value('data_07_04', self.o)
        
        print('fun_07_04 done!')

## fun_07_05

class fun_07_05(object):
    def __init__(self, data):
        self.cf = [6, 2, 12, 20, 1]
        self.cf_a = hexlist2(self.cf)
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            "平台登入时间",
            "登入流水号",
            "平台用户名",
            "平台密码",
            "加密规则",
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            "平台登入时间":get_datetime(self.oj['平台登入时间']),
            "登入流水号":hex2dec(self.oj['登入流水号']),
            "平台用户名":hex2str(self.oj['平台用户名']),
            "平台密码":hex2str(self.oj['平台密码']),
            "加密规则":dict_list_replace('07_05_05',self.oj['加密规则']),
        }
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('data_07_05', self.o)
        print('fun_07_05 done!')

## fun_07_06

class fun_07_06(object):
    def __init__(self, data):
        self.cf = [6, 2]
        self.cf_a = hexlist2(self.cf)
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            "登出时间",
            "登出流水号",
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        print(self.oj)
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            "登出时间":get_datetime(self.oj['登出时间']),
            "登出流水号":hex2dec(self.oj['登出流水号']),
        }
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('data_07_06', self.o)
        print('fun_07_06 done!')

## fun_07_02

class fun_07_02:
    def __init__(self, data):
        self.o = data
        
        self.oj = {'数据采集时间': self.o[:12]}
        self.ol = pd.DataFrame({'01':['01']})
        self.pj = {'数据采集时间': get_datetime(self.oj['数据采集时间'])}
        self.pl = pd.DataFrame({'01':['01']})
        
        glv.set_value('data_f', data[12:])
        glv.set_value('m_07_02', data[12:14])
        
        self.mo_list = ['01','02','03','04','05','06','07','08','09']
        self.do_list = []
        
        while(glv.get_value('m_07_02') in self.mo_list):
            
            # 记录已执行的
            self.do_list.append(glv.get_value('m_07_02'))
            # 删除已执行的
            self.mo_list.remove(glv.get_value('m_07_02'))
            
            if glv.get_value('m_07_02') == '01':
                self.f_01 = fun_07_02_01(glv.get_value('data_f'))
            elif glv.get_value('m_07_02') == '02':
                self.f_02 = fun_07_02_02(glv.get_value('data_f'))
            elif glv.get_value('m_07_02') == '03':
                self.f_03 = fun_07_02_03(glv.get_value('data_f'))
            elif glv.get_value('m_07_02') == '04':
                self.f_04 = fun_07_02_04(glv.get_value('data_f'))
            elif glv.get_value('m_07_02') == '05':
                self.f_05 = fun_07_02_05(glv.get_value('data_f'))
            elif glv.get_value('m_07_02') == '06':
                self.f_06 = fun_07_02_06(glv.get_value('data_f'))
            elif glv.get_value('m_07_02') == '07':
                self.f_07 = fun_07_02_07(glv.get_value('data_f'))
            elif glv.get_value('m_07_02') == '08':
                self.f_08 = fun_07_02_08(glv.get_value('data_f'))
            elif glv.get_value('m_07_02') == '09':
                self.f_09 = fun_07_02_09(glv.get_value('data_f'))
            else:
                print("fun_07_02 done")
                print(glv.get_value('data_f'))
                print(glv.get_value('m_07_02'))
            
        self.do_list.sort()
        for i in self.do_list:
            if i == '01':
                self.oj = dict(self.oj,**self.f_01.oj2)
                self.ol = pd.merge(self.ol, self.f_01.ol, left_index=True, right_index=True)
                self.pj = dict(self.pj,**self.f_01.pj2)
                self.pl = pd.merge(self.pl, self.f_01.pl, left_index=True, right_index=True)
            elif i == '02':
                self.oj = dict(self.oj,**self.f_02.oj2)
                self.ol = pd.merge(self.ol, self.f_02.ol, left_index=True, right_index=True)
                self.pj = dict(self.pj,**self.f_02.pj2)
                self.pl = pd.merge(self.pl, self.f_02.pl, left_index=True, right_index=True)
            elif i == '03':
                self.oj = dict(self.oj,**self.f_03.oj2)
                self.ol = pd.merge(self.ol, self.f_03.ol, left_index=True, right_index=True)
                self.pj = dict(self.pj,**self.f_03.pj2)
                self.pl = pd.merge(self.pl, self.f_03.pl, left_index=True, right_index=True)
            elif i == '04':
                self.oj = dict(self.oj,**self.f_04.oj2)
                self.ol = pd.merge(self.ol, self.f_04.ol, left_index=True, right_index=True)
                self.pj = dict(self.pj,**self.f_04.pj2)
                self.pl = pd.merge(self.pl, self.f_04.pl, left_index=True, right_index=True)
            elif i == '05':
                self.oj = dict(self.oj,**self.f_05.oj2)
                self.ol = pd.merge(self.ol, self.f_05.ol, left_index=True, right_index=True)
                self.pj = dict(self.pj,**self.f_05.pj2)
                self.pl = pd.merge(self.pl, self.f_05.pl, left_index=True, right_index=True)
            elif i == '06':
                self.oj = dict(self.oj,**self.f_06.oj2)
                self.ol = pd.merge(self.ol, self.f_06.ol, left_index=True, right_index=True)
                self.pj = dict(self.pj,**self.f_06.pj2)
                self.pl = pd.merge(self.pl, self.f_06.pl, left_index=True, right_index=True)
            elif i == '07':
                self.oj = dict(self.oj,**self.f_07.oj2)
                self.ol = pd.merge(self.ol, self.f_07.ol, left_index=True, right_index=True)
                self.pj = dict(self.pj,**self.f_07.pj2)
                self.pl = pd.merge(self.pl, self.f_07.pl, left_index=True, right_index=True)
            elif i == '08':
                self.oj = dict(self.oj,**self.f_08.oj2)
                self.ol = pd.merge(self.ol, self.f_08.ol, left_index=True, right_index=True)
                self.pj = dict(self.pj,**self.f_08.pj2)
                self.pl = pd.merge(self.pl, self.f_08.pl, left_index=True, right_index=True)
            elif i == '09':
                self.oj = dict(self.oj,**self.f_09.oj2)
                self.ol = pd.merge(self.ol, self.f_09.ol, left_index=True, right_index=True)
                self.pj = dict(self.pj,**self.f_09.pj2)
                self.pl = pd.merge(self.pl, self.f_09.pl, left_index=True, right_index=True)
                
                
                
        self.oj2 = {'信息上报': self.oj}
        self.pj2 = {'信息上报': self.pj}

        print('fun_07_02 done!')

## fun_07_02_01

class fun_07_02_01(object):
    def __init__(self, data):
        self.cf = [1, 1, 1, 2, 4, 2, 2, 1, 1, 1, 2, 1, 1]
        self.cf_a = hexlist2(self.cf)
        data = data[2:]
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            '车辆状态',
            '充电状态',
            '运行模式',
            '车速',
            '累计里程',
            '总电压',
            '总电流',
            'SOC',
            'DC-DC状态',
            '挡位',
            '绝缘电阻',
            '加速踏板行程值',
            '制动踏板状态',
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        self.oj2 = {'整车数据': self.oj}
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            '车辆状态' : dict_list_replace("07_02_01_01", self.oj['车辆状态']),
            '充电状态' : dict_list_replace("07_02_01_02", self.oj['充电状态']),
            '运行模式' : dict_list_replace("07_02_01_03", self.oj['运行模式']),
            '车速' : hex2dec(self.oj['车速'], k=0.1),
            '累计里程' : hex2dec(self.oj['累计里程'], k=0.1),
            '总电压' : hex2dec(self.oj['总电压'], k=0.1),
            '总电流' : hex2dec(self.oj['总电流'], n=-1000, k=0.1),
            'SOC' : hex2dec(self.oj['SOC']),
            'DC-DC状态' : dict_list_replace("07_02_01_06", self.oj['DC-DC状态']),
            '挡位' : fun_07_02_01.fun_10(self.oj['挡位']),
            '绝缘电阻' : hex2dec(self.oj['绝缘电阻']),
            '加速踏板行程值' : fun_07_02_01.fun_12(self.oj['加速踏板行程值']),
            '制动踏板状态' : fun_07_02_01.fun_13(self.oj['制动踏板状态']),
        }
        self.pj2 = {'整车数据': self.pj}
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('m_07_02', self.nextMark)
        glv.set_value('data_07_02_01', self.o)
        
        print('fun_07_02_01 done!')
        
    # 02_01_10 挡位
    def fun_10(data):
        n = '{:08b}'.format(int(data, 16))
        dangwei = n[-4:]
        zhidongli = n[-5]
        qudongli = n[-6]
        
        # 挡位
        if dangwei == '0000':
            dangwei_s = '空挡'
        elif dangwei == '1101':
            dangwei_s = '倒挡'
        elif dangwei == '1110':
            dangwei_s = '自动D挡'
        elif dangwei == '1111':
            dangwei_s = '停车P挡'
        else :
            dangwei_s = (str(int(dangwei, 2)) + "档" )
            
        # 制动力
        if zhidongli == "1":
            zhidongli_s = "有制动力"
        else :
            zhidongli_s = "无制动力" 
            
        # 驱动力
        if qudongli == "1":
            qudongli_s = "有驱动力"
        else :
            qudongli_s = "无驱动力"

        output = [n, dangwei_s, zhidongli_s, qudongli_s]
        return output

    # 02_01_12 加速踏板行程值
    def fun_12(data):
        data = data.upper()
        if data == 'FE':
            return "异常"
        elif data == "FF":
            return "无效"
        else :
            return hex2dec(data)

    # 02_01_13 制动踏板状态
    def fun_13(data):
        data = data.upper()
        if data == 'FE':
            return "异常"
        elif data == "FF":
            return "无效"
        elif data == "65":
            return "制动有效"
        else :
            return hex2dec(data)

## fun_07_02_02

class fun_07_02_02(object):
    def __init__(self, data):
        data = data[2:]
        self.dj_n_o = data[0:2]
        self.dj_n_j = hex2dec(self.dj_n_o) # 电机个数
        
        self.cf_u = [1, 1, 1, 2, 2, 1, 2, 2]
        self.cf = [1] + self.cf_u * self.dj_n_j
        self.cf_a = hexlist2(self.cf)
        
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            "驱动电机个数",
            "驱动电机序号",
            "驱动电机状态",
            "驱动电机控制器温度",
            "驱动电机转速",
            "驱动电机转矩",
            "驱动电机温度",
            "电机控制器输入电压",
            "电机控制器直流母线电流",
        ]
        
        self.oj = fun_07_02_02.fun_oj(self)
        self.oj2 = {'驱动电机数据':self.oj}
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            "驱动电机个数":self.dj_n_j,
            "驱动电机序号":[hex2dec(i) for i in self.oj['驱动电机序号']],
            "驱动电机状态":[dict_list_replace('07_02_02_02', i) for i in self.oj['驱动电机状态']],
            "驱动电机控制器温度":[hex2dec(i, n=-40) for i in self.oj['驱动电机控制器温度']],
            "驱动电机转速":[hex2dec(i, n=-20000) for i in self.oj['驱动电机转速']],
            "驱动电机转矩":[hex2dec(i, k=0.1, n=-2000) for i in self.oj['驱动电机转矩']],
            "驱动电机温度":[hex2dec(i, n=-40) for i in self.oj['驱动电机温度']],
            "电机控制器输入电压":[hex2dec(i, k=0.1) for i in self.oj['电机控制器输入电压']],
            "电机控制器直流母线电流":[hex2dec(i, k=0.1, n=-1000) for i in self.oj['电机控制器直流母线电流']],
        }
        self.pj2 = {'驱动电机数据':self.pj}
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('m_07_02', self.nextMark)
        
        glv.set_value('data_07_02_02', self.o)
        
        print("fun_07_02_02 done!")
        
    #  oj
    def fun_oj(self):
        data = self.o[2:]
        cf_a = hexlist2(self.cf[1:])
        dict_oj = {
            "驱动电机个数":self.dj_n_o,
        }
        
        list_o = [
            "驱动电机序号",
            "驱动电机状态",
            "驱动电机控制器温度",
            "驱动电机转速",
            "驱动电机转矩",
            "驱动电机温度",
            "电机控制器输入电压",
            "电机控制器直流母线电流",
        ]
        
        dict_oj_u = {
            "驱动电机序号":[],
            "驱动电机状态":[],
            "驱动电机控制器温度":[],
            "驱动电机转速":[],
            "驱动电机转矩":[],
            "驱动电机温度":[],
            "电机控制器输入电压":[],
            "电机控制器直流母线电流":[],
        }
        for i in range(self.dj_n_j):
            for j in range(len(dict_oj_u)):
                data_unit = data[cf_a[i * len(dict_oj_u) + j]:cf_a[i * len(dict_oj_u) + j +1]]
                dict_oj_u[list_o[j]].append(data_unit)
        
        dict_all = dict(dict_oj, **dict_oj_u)
        return dict_all
    

## fun_07_02_03

class fun_07_02_03(object):
    def __init__(self, data):
        
        self.cf = [2, 2, 2, 2, None, 2, 1, 2, 1, 2, 1, 1]
        data = data[2:]
        self.dc_no = data[12:16]
        self.dc_np = hex2dec(self.dc_no)
        self.cf[4] = self.dc_np
        self.cf_a = hexlist2(self.cf)

        self.o = data[0:self.cf_a[-1]]
        
        self.list_o = [
            "燃料电池电压",
            "燃料电池电流",
            "燃料消耗率",
            "燃料电池温度探针总数",
            "探针温度值",
            "氢系统中最高温度",
            "氢系统中最高温度探针代号",
            "氢气最高浓度",
            "氢气最高浓度传感器代号",
            "氢气最高压力",
            "氢气最高压力传感器代号",
            "高压DC/DC状态",
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        self.oj2 = {'燃料电池数据':self.oj}
        self.ol = pd.DataFrame.from_dict(self.oj,orient='index').T
        self.pj = {
            "燃料电池电压":hex2dec(self.oj['燃料电池电压'], k=0.1),
            "燃料电池电流":hex2dec(self.oj['燃料电池电流'], k=0.1),
            "燃料消耗率":hex2dec(self.oj['燃料消耗率'], k=0.01),
            "燃料电池温度探针总数":hex2dec(self.oj['燃料电池温度探针总数']),
            "探针温度值":[hex2dec(i, n=-40, k=0.1) for i in self.oj['燃料电池温度探针总数']],
            "氢系统中最高温度":hex2dec(self.oj['氢系统中最高温度'], n=-40, k=0.1),
            "氢系统中最高温度探针代号":hex2dec(self.oj['氢系统中最高温度探针代号']),
            "氢气最高浓度":hex2dec(self.oj['氢气最高浓度']),
            "氢气最高浓度传感器代号":hex2dec(self.oj['氢气最高浓度传感器代号']),
            "氢气最高压力":hex2dec(self.oj['氢气最高压力'], k=0.1),
            "氢气最高压力传感器代号":hex2dec(self.oj['氢气最高压力传感器代号']),
            "高压DC/DC状态":dict_list_replace('07_02_03_12', self.oj['高压DC/DC状态']),
        }
        self.pj2 = {'燃料电池数据':self.pj}
        self.pl = pd.DataFrame.from_dict(self.pj,orient='index').T
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('m_07_02', self.nextMark)
        
        glv.set_value('data_07_02_03', self.o)
        
        print('fun_07_02_03 done!')

## fun_07_02_04

class fun_07_02_04(object):
    def __init__(self, data):
        cf = [1, 2, 2]
        cf_a = hexlist2(cf)
        data = data[2:]
        self.o = data[0:cf_a[-1]]
        list_o = [
            "发动机状态",
            "曲轴转速",
            "燃料消耗率",
        ]
        self.oj = list2dict(self.o, list_o, cf_a)
        self.oj2 = {'发动机数据':self.oj}
        self.ol = pd.DataFrame.from_dict(self.oj,orient='index').T
        self.pj = {
            "发动机状态":dict_list_replace("07_02_01_01", self.oj['发动机状态']),
            "曲轴转速":fun_07_02_04.fun_2(self.oj['曲轴转速']),
            "燃料消耗率":fun_07_02_04.fun_3(self.oj['燃料消耗率']),
        }
        self.pj2 = {'发动机数据':self.pj}
        self.pl = pd.DataFrame.from_dict(self.pj,orient='index').T
        
        self.next = data[cf_a[-1]:]
        self.nextMark = data[cf_a[-1]:cf_a[-1]+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('m_07_02', self.nextMark)
        
        glv.set_value('data_07_02_04', self.o)
        
        print('fun_07_02_04 done!')
        
    # 02_04_02 曲轴转速
    def fun_2(data):
        data = data.upper()
        if data == 'FFFE':
            return "异常"
        elif data == "FFFF":
            return "无效"
        else :
            return hex2dec(data)

    # 02_04_03 燃料消耗率
    def fun_3(data):
        data = data.upper()
        if data == 'FFFE':
            return "异常"
        elif data == "FFFF":
            return "无效"
        else :
            return hex2dec(data, k=0.01)

## fun_07_02_05

class fun_07_02_05(object):
    def __init__(self, data):
        self.cf = [1, 4, 4]
        self.cf_a = hexlist2(self.cf)
        data = data[2:]
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            "定位状态",
            "经度",
            "纬度",
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        self.oj2 = {'车辆位置数据':self.oj}
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            '定位状态' : fun_07_02_05.fun_01(self.oj['定位状态']),
            '经度' : hex2dec(self.oj['经度'], k=0.000001),
            '纬度' : hex2dec(self.oj['纬度'], k=0.000001),
        }
        self.pj2 = {'车辆位置数据':self.pj}
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('m_07_02', self.nextMark)
        
        glv.set_value('data_07_02_05', self.o)
        
        print('fun_07_02_05 done!')
        
    def fun_01(data):
        n = '{:08b}'.format(int(data, 16))    
        state = n[-1]
        longitude = n[-2]
        latitude = n[-3]
        
        if state == '0':
            state_s = "定位有效"
        else :
            state_s = "定位无效"
        
        if longitude == '0':
            longitude_s = "北纬"
        else :
            longitude_s = "南纬"
        
        if latitude == '0':
            latitude_s = "东经"
        else :
            latitude_s = "西经"
        
        output = [n, state_s, longitude_s, latitude_s]
        return output

## fun_07_02_06

class fun_07_02_06(object):
    def __init__(self, data):
        self.cf = [1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1]
        self.cf_a = hexlist2(self.cf)
        data = data[2:]
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            "最高电压电池子系统号",
            "最高电压电池单体代号",
            "电池单体电压最高值",
            "最低电压电池子系统号",
            "最低电压电池单体代号",
            "电池单体电压最低值",
            "最高温度子系统号",
            "最高温度探针序号",
            "最高温度值",
            "最低温度子系统号",
            "最低温度探针序号",
            "最低温度值",
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        self.oj2 = {'极值数据':self.oj}
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            '最高电压电池子系统号' : hex2dec(self.oj['最高电压电池子系统号'], e=True),
            '最高电压电池单体代号' : hex2dec(self.oj['最高电压电池单体代号'], e=True),
            '电池单体电压最高值' : hex2dec(self.oj['电池单体电压最高值'], k=0.001, e=True),
            '最低电压电池子系统号' : hex2dec(self.oj['最低电压电池子系统号'], e=True),
            '最低电压电池单体代号' : hex2dec(self.oj['最低电压电池单体代号'], e=True),
            '电池单体电压最低值' : hex2dec(self.oj['电池单体电压最低值'], k=0.001, e=True),
            '最高温度子系统号' : hex2dec(self.oj['最高温度子系统号'], e=True),
            '最高温度探针序号' : hex2dec(self.oj['最高温度探针序号'], e=True),
            '最高温度值' : hex2dec(self.oj['最高温度值'], n=-40, e=True),
            '最低温度子系统号' : hex2dec(self.oj['最低温度子系统号'], e=True),
            '最低温度探针序号' : hex2dec(self.oj['最低温度探针序号'], e=True),
            '最低温度值' : hex2dec(self.oj['最低温度值'], n=-40, e=True),
        }
        self.pj2 = {'极值数据':self.pj}
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('m_07_02', self.nextMark)
        
        glv.set_value('data_07_02_06', self.o)
        
        print('fun_07_02_06 done!')

## fun_07_02_07

class fun_07_02_07(object):
    def __init__(self, data):
        self.cf = [1, 4, 1, 1, 1, 1]
        self.cf_a = hexlist2(self.cf)
        data = data[2:]
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [
            "最高报警等级",
            "通用报警标志",
            "可充电储能装置故障总数N1",
            "驱动电机故障总数N2",
            "发动机故障总数N3",
            "其他故障总数N4",
        ]
        self.oj = list2dict(self.o, self.list_o, self.cf_a)
        self.oj2 = {'极值数据':self.oj}
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            '最高报警等级' : hex2dec(self.oj['最高报警等级'], e=True),
            '通用报警标志' : fun_07_02_07.fun_02(self.oj['通用报警标志']),
            '可充电储能装置故障总数N1' : hex2dec(self.oj['可充电储能装置故障总数N1'], e=True),
            '驱动电机故障总数N2' : hex2dec(self.oj['驱动电机故障总数N2'], e=True),
            '发动机故障总数N3' : hex2dec(self.oj['发动机故障总数N3'], e=True),
            '其他故障总数N4' : hex2dec(self.oj['其他故障总数N4'], e=True),
        }
        self.pj2 = {'极值数据':self.pj}
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]

        glv.set_value('data_f', self.next)
        glv.set_value('m_07_02', self.nextMark)
        
        glv.set_value('data_07_02_07', self.o)
        
        print('fun_07_02_07 done!')
        
    def fun_02(data):
        n = '{:032b}'.format(int(data, 16))

        baojing_list = [
            "温度差异报警",
            "电池高温报警",
            "车载储能装置类型过压报警",
            "车载储能装置类型欠压报警",
            "SOC低报警",
            "单体电池过压报警",
            "单体电池欠压报警",
            "SOC过高报警",
            "SOC跳变报警",
            "可充电储能系统不匹配报警",
            "电池单体一致性差报警",
            "绝缘报警",
            "DC-DC温度报警",
            "制动系统报警",
            "DC-DC状态报警",
            "驱动电机控制器温度报警",
            "高压互锁状态报警",
            "驱动电机温度报警",
            "车载储能装置类型过充",
        ]

        baojing = [n]

        for i in range(0,19):
            if n[-i] == "1":
                baojing.append(baojing_list[i])

        return baojing

## fun_07_02_08

class fun_07_02_08(object):
    def __init__(self, data):
        data = data[2:]
        self.o = data
        self.dj_n_o = data[0:2]
        self.dj_n_j = hex2dec(self.dj_n_o) # 电池个数
        
        self.cf_u = [1, 1]
        self.cf = fun_07_02_08.fun_cf(self)
        self.cf_a = hexlist2(self.cf)
        self.o = data[0:self.cf_a[-1]]
        self.list_o = [            
            "可充电储能子系统个数",
            "可充电储能子系统号",
            "可充电储能装置电压",
            "可充电储能装置电流",
            "单体电池总数",
            "本帧起始电池序号",
            "本帧单体电池总数",
            "单体电池电压",
        ]
        
        self.oj = fun_07_02_08.fun_oj(self)
        self.oj2 = {'可充电储能装置电压数据':self.oj}  
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            "可充电储能子系统个数":self.dj_n_j,
            "可充电储能子系统号":[hex2dec(i) for i in self.oj['可充电储能子系统号']],
            "可充电储能装置电压":[hex2dec(i, k=0.1) for i in self.oj['可充电储能装置电压']],
            "可充电储能装置电流":[hex2dec(i, k=0.1, n=-1000) for i in self.oj['可充电储能装置电流']],
            "单体电池总数":[hex2dec(i) for i in self.oj['单体电池总数']],
            "本帧起始电池序号":[hex2dec(i) for i in self.oj['本帧起始电池序号']],
            "本帧单体电池总数":[hex2dec(i) for i in self.oj['本帧单体电池总数']],
            "单体电池电压":[hex2list(i, num=2, kk=0.01) for i in self.oj['单体电池电压']],    
        }
        self.pj2 = {'可充电储能装置电压数据':self.pj}
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('m_07_02', self.nextMark)
        
        glv.set_value('data_07_02_07', self.o)
        
        print('fun_07_02_08 done!')
        
    
    def fun_cf(self):
        cf_u=[1,2,2,2,2,1,None]
        self.c = [] 
        data = self.o
        for i in range(self.dj_n_j):
            cf_u[6] = hex2dec(data[20:22]) * 2
            self.c = self.c + cf_u
            
            cf_a = hexlist2(self.c)
            data = data[cf_a[-1]:]
            
        self.c = [1] + self.c
            
        return self.c
    
    
    def fun_oj(self):
        data = self.o[2:]
        cf_a = hexlist2(self.cf[1:])
        dict_oj = {
            "可充电储能子系统个数":self.dj_n_o,
        }
        
        list_o = [
            "可充电储能子系统号",
            "可充电储能装置电压",
            "可充电储能装置电流",
            "单体电池总数",
            "本帧起始电池序号",
            "本帧单体电池总数",
            "单体电池电压",
        ]
        
        dict_oj_u = {
            "可充电储能子系统号":[],
            "可充电储能装置电压":[],
            "可充电储能装置电流":[],
            "单体电池总数":[],
            "本帧起始电池序号":[],
            "本帧单体电池总数":[],
            "单体电池电压":[],
        }
        
        for i in range(self.dj_n_j):
            for j in range(len(dict_oj_u)):
                data_unit = data[cf_a[i * len(dict_oj_u) + j]:cf_a[i * len(dict_oj_u) + j +1]]
                dict_oj_u[list_o[j]].append(data_unit)
        
        dict_all = dict(dict_oj, **dict_oj_u)
        return dict_all
    

## fun_07_02_09

class fun_07_02_09(object):
    def __init__(self, data):
        data = data[2:]
        self.o = data
        self.dj_n_o = data[0:2]
        self.dj_n_j = hex2dec(self.dj_n_o) # 电池个数
        
        self.cf_u = [1, 1]
        self.cf = fun_07_02_09.fun_cf(self)
        self.cf_a = hexlist2(self.cf)
        
        self.o = data[0:self.cf_a[-1]]
        
        self.list_o = [
            "可充电储能子系统个数",
            "可充电储能子系统号",
            "可充电储能温度探针个数",
            "可充电储能子系统各温度探针检测到的温度值",
        ]
        
        self.oj = fun_07_02_09.fun_oj(self)
        self.oj2 = {'可充电储能装置温度数据':self.oj}  
        self.ol = pd.DataFrame([self.oj]).reindex(columns=self.list_o)
        self.pj = {
            "可充电储能子系统个数":self.dj_n_j,
            "可充电储能子系统号":[hex2dec(i) for i in self.oj['可充电储能子系统号']],
            "可充电储能温度探针个数":[hex2dec(i) for i in self.oj['可充电储能温度探针个数']],
            "可充电储能子系统各温度探针检测到的温度值":[hex2list(i, num=1, kn=-40) for i in self.oj['可充电储能子系统各温度探针检测到的温度值']],
        }
        self.pj2 = {'可充电储能装置温度数据':self.pj}
        self.pl = pd.DataFrame([self.pj]).reindex(columns=self.list_o)
        
        self.next = data[len(self.o):]
        self.nextMark = data[len(self.o):len(self.o)+2]
        
        glv.set_value('data_f', self.next)
        glv.set_value('m_07_02', self.nextMark)
        
        glv.set_value('data_07_02_07', self.o)
        
        print('fun_07_02_09 done!')
        
    
    def fun_cf(self):
        cf_u=[1,2, None]
        self.c = [] 
        data = self.o
        for i in range(self.dj_n_j):
            n_str = data[4:8]
            n = hex2dec(n_str)
            cf_u[2] = n
            self.c = self.c + cf_u
            
            cf_a = hexlist2(self.c)
            data = data[cf_a[-1]:]
            
        self.c = [1] + self.c
            
        return self.c
    
    
    def fun_oj(self):
        data = self.o[2:]
        cf_a = hexlist2(self.cf[1:])
        dict_oj = {
            "可充电储能子系统个数":self.dj_n_o,
        }
        
        list_o = [
            "可充电储能子系统号",
            "可充电储能温度探针个数",
            "可充电储能子系统各温度探针检测到的温度值",
        ]
        
        dict_oj_u = {
            "可充电储能子系统号":[],
            "可充电储能温度探针个数":[],
            "可充电储能子系统各温度探针检测到的温度值":[],
        }
        
        for i in range(self.dj_n_j):
            for j in range(len(dict_oj_u)):
                data_unit = data[cf_a[i * len(dict_oj_u) + j]:cf_a[i * len(dict_oj_u) + j +1]]
                dict_oj_u[list_o[j]].append(data_unit)
        
        dict_all = dict(dict_oj, **dict_oj_u)
        return dict_all
    

## fun_07_cursor

class fun_07_cursor:
    def __init__(self, data):
        
        if len(data) > 2:
            self.o = data[:-2]
        elif len(data) < 2:
            print("错误")
        else :
            self.o = None
            
        self.oj = self.pj = {'自定义': self.o}
        self.ol = self.pl = pd.DataFrame({'自定义': [self.o]})
        
        print('fun_07_curos done!')

## fun_08

class fun_08:
    def __init__(self, data):
        self.o = data[-2:]
        
        self.oj = self.pj = {'校验码':self.o}
        self.ol = self.pl = pd.DataFrame({'校验码':[self.o]})
        
        print('fun_08 done!')

## 主体

class gb32960:
    
    glv._init()
    
    def __init__(self, data):
        
        data = data.upper()
        glv.set_value('data_f', data)
        
        self.o = data
        self.f_01 = fun_01to06(glv.get_value('data_f'))
        self.f_07 = fun_07(glv.get_value('data_f'))
        self.f_08 = fun_08(glv.get_value('data_f'))     
        
        
        self.oj = dict(self.f_01.oj, **self.f_07.oj)
        self.oj = dict(self.oj, **self.f_08.oj)
        
        self.ol = pd.merge(self.f_01.ol, self.f_07.ol, left_index=True, right_index=True)
        self.ol = pd.merge(self.ol, self.f_08.ol, left_index=True, right_index=True)
        
        
        self.pj = dict(self.f_01.pj, **self.f_07.pj)
        self.pj = dict(self.pj, **self.f_08.pj)
        
        self.pl = pd.merge(self.f_01.pl, self.f_07.pl, left_index=True, right_index=True)
        self.pl = pd.merge(self.pl, self.f_08.pl, left_index=True, right_index=True)
        
        print("all done!")