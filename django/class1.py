# class 클래스명:
# 함수
# 함수


# class User:
#     def __init__(self, name, age):
#         print('생성자 호출')
#         self.name = name
#         self.age = age
#
#     def __init__(self, name):
#         print('생성자 호출')
#         self.name = name
#
#     def getinfo(self):
#         print(self.name+','+str(self.age))
#
#
# u1 = User('김동현', 26)
# print(u1.name)
# u1.getinfo()
# u2 = User('이몽룡', 16)
# print(u2.age)
# u3 = User('성춘향')
# print(u3.name)
# ----------------
'''
class Car(object):
    def __init__(self, color, tp):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car 의 show 메서드가 호출됨'


class BmwCar(Car):
    def __init__(self, name, color, tp):
        super().__init__(color, tp)
        self.name = name

    def showname(self):
        return '내차는 ' + self.name


class BenzCar(Car):
    def __init__(self, name, color, tp):
        super().__init__(color, tp)
        self.name = name

    def showname(self):
        return '내차는 '+self.name

    def show(self):
        return 'BenzCar 의 show 메서드'


c1 = BmwCar('720d', 'blue', 'sport')
print(c1.showname())
print(c1.show())

c2 = BenzCar('s560', 'white', 'suv')
print(c2.showname())
print(c2.show())

# 상속관계를 나타내는 메서드
print(BmwCar.mro())
print(BenzCar.mro())
'''
# --------------------------------


class X(object):
    pass
class Y():
    pass
class Z:
    pass
class A(X, Y):
    pass
class B(Y, Z):
    pass
class C(A, B):
    pass

print(C.mro())

