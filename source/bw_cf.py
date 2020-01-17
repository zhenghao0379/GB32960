# 报文拆分


# 工具包
import numpy as np
import pandas as pd
import binascii
import datetime
import math

# 

cf_dict = {
    "00" : [2, 1, 1, 17, 1, 2],
    "01" : []
}

# 
def bw_cf(bw):
    global 



# 
def fun_cf_00(data, cf=cf_dict['00']):
    cf_a = hexlist2(cf)
    
    data_cf = {
        "起始符":data[cf_a[0]:cf_a[1]],
        "命令标识":data[cf_a[1]:cf_a[2]],
        "应答标志":data[cf_a[2]:cf_a[3]],
        "唯一识别码":data[cf_a[3]:cf_a[4]],
        "数据单元加密方式":data[cf_a[4]:cf_a[5]],
        "数据单元长度":data[cf_a[5]:cf_a[6]],
        "效验码":data[-2:]
    }
    str_split(data, cf_a[-1])
    return data_cf