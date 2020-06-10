def add(x, y):
    return x+y

def multiply(x, y):
    return x*y

def division(x, y):
    return x//y

def subtract(x, y):
    return x-y
# __name__ 공통변수 
#__name__을 사용해 메인으로 코드가 실행됐을 때와 모듈을 임포트했을 때 다르게 실행된다
if(__name__ == '__main__'):
    print("모듈을 직접 실행하셨네요?")
else:
    print("임포트 하셨군요.")