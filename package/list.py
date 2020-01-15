# 执行顺序

def todo(data):
    key = data[]
    if key=='01':
        data_unit = todo_07_01(data)
    elif key=='02' or key=='03':
        data_unit = todo_07_02(data)
    elif key=='04':
        data_unit = todo_07_04(data)
    elif key=='05':
        data_unit = todo_07_04(data)
    elif key=='06':
        data_unit = todo_07_04(data)
    else :
        print("Error, something worry in charge data.")
    
import abc from ABCMeta, abstractmethod

class todo_07_01(metaclass=ABCMeta):
    @abstractmethod
    def fun_01to06(self):
        pass
    @abstractmethod
    def fun_datetime(self):
        pass
    @abstractmethod
    def fun_07_01(self):
        pass
    @abstractmethod
    def cursor(self):
        pass
    @abstractmethod
    def fun_08(self):
        pass
