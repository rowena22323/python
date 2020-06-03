class Employee:
    name = '강감찬'
    count = 0

    def __init__(self, name="없음"):
        # print(self.name, self.count)
        Employee.count += 1 # 전역변수 접근 class.variable
    def display(self, a=0):
        print(self.count, a)

class Employee2(Employee):
    def __init__(self):
        print("Employee2 생성자")
    
    def display2(self):
        print("Employee2 display2")

    def display(self, a = 0 , b = 1):
        print(a, b)

e4 = Employee2()
e4.display()
e4.display2()

print(isinstance(e4, Employee))