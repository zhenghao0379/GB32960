import pandas as pd

from public_fun import *

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
        self.pl = pd.DataFrame.from_dict(self.pj,orient='index').T2
