# 字符串类 直接替换
# 列表类替换（报文解析）
def dict_list_replace(n, x):
    x = x.upper()
    index = jx_dict_o[n].index(x)
    output = jx_dict[n][index]
    return output

# 多值划拆为列表（报文解析）
def hex2list(x, n=1, hn=0, hk=1, he=False):
    x = x.upper()
    l = int(len(x)/(2*n))
    output = []
    for i in range(0,l):
        s_16 = x[2*n*i:2*n*i + 2*n]
        s_10 = hex2dec(s_16, n=hn, k=hk, e=he)
        output.append(s_10)
    return output