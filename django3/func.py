# def 함수명(매개변수):
#     내용


def hi(name):
    print("Hello~", name, sep="^^")
    return 'ok'
# 다중return
# print(hi('김동현'))


# a = 3
# b = 5
# print(a, b)
def f1(x, y):
    r1 = x + y
    r2 = x - y
    r3 = x * y
    r4 = x / y
    return r1, r2, r3, r4
# a, b, c, d = f1(10, 3)
# print(a, b, c, d)
# e = f1(30, 20)
# print(e)


def f2(x, y):
    r1 = x + y
    r2 = x - y
    r3 = x * y
    r4 = x / y
    return {'add':r1,'sub': r2, 'mul': r3, 'div': r4}
# e=f2(50,30)
# print(e)

# *args, **kwargs --가변 * = tuple, ** = dictionary
def f3(*a):
    print(type(a))
    print(a)
    hap = 0
    for i in a:
        hap = hap + i
    print('총합:', hap)
    print('-'*30)
# f3(1, 2, 3)

# 값을 넘길때 딕셔너리로 들어오고 그냥쓰면 딕셔너리를 만듬
def f4(**b):
    print(b)

# f4(name1='둘리', name2='희동이')
# f4()

def f5(a, b, *c, **d):
    print(a, b, c, d)

# f5(1,2,3,4,5,6,7)
# f5(1,2)
# f5(1,2,apple='red',name='홍길동')

# 오류 갯수제한이 없는게 뒤로 가야한다.
# def f6(*a,**b, c, d):
#     print(a, b, c, d)

def f7(a=1, b=2, c=3, d=4):
    print(a, b, c, d)

# f7(10, 20, 30, 40)
# f7(100, 300, 300)
# f7(a=300, b=300)