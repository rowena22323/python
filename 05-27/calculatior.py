def calf():
    return str(input("연산자를 입력해 주세요 : "))
def cal1():
    return int(input("첫번째 숫자를 입력해 주세요 : "))
def cal2():
    return int(input("두번째 숫자를 입력해 주세요 : "))

def add(a, b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a, b):
    return a//b

print("{0:#^37}".format("계 산 기"))
print("{0:#^40}".format("#"))
print("{0:<40}".format('# 1. 덧  셈'))
print("{0:<40}".format('# 2. 뺄  셈'))
print("{0:<40}".format('# 3. 나눗셈'))
print("{0:<40}".format('# 4. 곱  셈'))
print("{0:<40}".format('# 5. 종  료'))
print("{0:#^40}".format("#"))



while True:
    a= int(input("# 원하는 메뉴를 선택해 주세요 [1-5] : "))
    if (a==1) :
        b = cal1()
        calf()
        c = cal2()
        print("결과는",add(b, c),"입니다.")
    elif (a==2) :
        d = cal1()
        calf()
        e = cal2() 
        print("결과는",subtract(d, e),"입니다.")
    elif (a==3) :
        f= cal1()
        calf()
        g= cal2()
        print("결과는",multiply(f, g),"입니다.")
    elif (a==4) :
        h= cal1()
        calf()
        i= cal2()
        print("결과는",divide(h, i),"입니다.")
    elif (a==5) :
        print("연산 종료")
        break