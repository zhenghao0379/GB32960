from public_fun import *

# 效验码
class fun_08():
    def __init__(self, data):
        self.o = data[-1]
        self.bcc = False
    def BCC(self, data):
        if bcc(data):
            return self.bcc = True
        else :
            return self.bcc = False