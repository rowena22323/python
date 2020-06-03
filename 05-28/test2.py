"""
class A : 
    def __init__(self, a):
        self.a = a
    def __add__(self, o):
        # 연산자 오버로딩
        return self.a + o.a

a = A(1)
b = A(2)
c = a.__add__(b)
c2 = a+b
print(c, c2)

# (1,2)+(3,4) -> (4, 6) ??

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, v):
        return self.a + v.a , self.b + v.b

t = Test(1,2)
t2 = Test(3,4)
t3 = t+t2 # t3 = t.__add__(t2)
print(t3)

try:
    a = int(input("a: "))
    b = int(input("b: "))
    c = a/b
    print(c)
except ZeroDivisionError:
    print("error")
else:
    print("ok")

def divide(a, b):
    return a/b

try:
    c = divide(5, "af")
except TypeError as e:
    print('error: ', e.args[0])
except Exception:
    print('음... 무슨에러인지 모르겠어요!?')
"""
class NegativeDivisionError(Exception):
    def __init__(self, value):
        self.value = value
    def PositiveDivide(a, b):
        if(b<0):
            raise NegativeDivisionError(b)
        return a/b

try :
    ret = PositiveDivide(10, -3)
    print('10/3')