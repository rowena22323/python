import mypackage.mymodule as mm

def st1():
    return int(input("첫번째 숫자를 입력해 주세요 : "))
def st2():
    return int(input("두번째 숫자를 입력해 주세요 : "))

print("*덧셈")
a = st1()
b = st2()
print(a,"+",b,"의 결과는",mm.add(a,b),"입니다.")
print("*곱셈")
c = st1()
d = st2()
print(c,"*",d,"의 결과는",mm.multiply(c,d),"입니다.")
print("*뺄셈")
e = st1()
f = st2()
print(e,"-",f,"의 결과는",mm.substract(e,f),"입니다.")
print("*나눗셈")
g = st1()
h = st2()
print(g,"/",h,"의 결과는",mm.divide(g,h),"입니다.")
print("계산종료")
    


