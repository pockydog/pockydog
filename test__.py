b = [22, 22, 33, 44, 55, 66, 77, 88, 99, 100]
# b = 33
t = ('apple', 'banana', 'orange', 'grap')
p = ('apple', 'banana', 'orange', 'grap')
# for i in a:
#     try:
#         if a == '100':
#             print(n)
#     except:
#         print("except")
#
#     print('g')
# a = ['x', '100'], ['y', '200'], ['z', '300']
# c =  (apple)

# print(t[2])
# v = t+p
# print(v)
# c = t*4
# print(c)
# g = dict(a)
# print(g)
# print(c & d)

# a = []
# for i in range(1, 10):
#   a.append(i*i)
# print(a)


# a = [i*2 for i in b]
# print(a)


# 生成式
# a = [[100, 200, 300, 400, 500], [100, 200, 500, 2, 1]]
# print(min([min(i) for i in a]))
# print([min(i) for i in a])

# b = [i*i for i in range(1, 10)]
# print(b)

# a = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# b = [max(a)-i for i in a]
# c = [min(a)-i for i in a]
# print(c)
# print(b)
#
# a = [i + str(j) for i in 'abc' for j in range(1, 3)]
# print(a)
#
# a = [i for i in range(1, 10) if i % 2==0]
# print(a)

# a = [ i for i in range(1, 10) if i % 2 == 0]
# print(a)
#
# a = {i:i*i for i in range(1, 10)}
# print(a)

# a = [j + str(i) for j in 'abc' for i in range(1, 10)]
# print(a)
# print([' '.join(["%sx%s=%-2s"%(j,i,i*j) for j in range(1,i+1)]) for i in range(1,10)])
#
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f'{i}*{j}')

# import time
# n = 10
# for i in range(n+1):
#   print(f'\r倒數 {n-i} 秒', end='')
#   time.sleep(1)
# print('\r時間到', end='')

# a = float('inf')
# print(a)
#
# print(round(2.5))
#
# a = complex(1, 2)
# print(a)

# while True:
#     try:
#         a = int(input('輸入 0～9：'))
#         if a > 9:  # 如果輸入的 a 大於 9
#             except  # 強制中斷，拋出錯誤資訊席
#         print(a)
    # except:
    #     print('有錯誤喔～')

class Aoo():
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3
        self.d = 4
        self.e = 5

    def soo(self, name):
        print('apple', name)

a = Aoo()
a.soo('vicky')


class Aoo():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    @classmethod
    def soo(cls, name):
        print('apple', name)

Aoo.soo('vicky')



class Aoo:
    def __init__(self, name):
        self.a = 'Apple2-page=1'
        self.n = {}
        self.name = name

    def soo(self):
        f = dict()
        for i in range(1, 10):
            aa = {'url': f'http://Apple2-page={i}'}
            f.update(aa)
            print('ngu')
        return f

    def poo(self):
        self.soo()
        # url = {'name': self.name}
        # for i in url:
        #     self.n.update(dict(i))
        # return self.n

# a = Aoo(name='vicky')
# print(a.soo())
# print(a.poo())


# from datetime import date
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def fromFathersAge(name, fatherBirthYear, fatherPersonAgeDiff):
#         return Person(name, date.today().year - fatherBirthYear -fatherPersonAgeDiff)
#
#     @classmethod
#     def fromBirthYear(cls, name, birthYear):
#         return cls(name, date.today().year - birthYear)
#
#     def display(self):
#         print(self.name + "'s age is: " + str(self.age))
#
# class Man(Person):
#     sex = 'Male'
#
# man = Man.fromBirthYear('John', 1985)
# print(isinstance(man, Man))
#
# man1 = Man.fromFathersAge('John', 1965, 20)
# print(isinstance(man1, Man))

class Test():
    a = {'r': 20, 'b': 40, 'y': 40}

    def __init__(self, type, size, name):
        self.type = type
        self.size = size
        self.name = name

    def get_info(self):
        return f'{self.type}dogs, {self.size} kg, name is {self.name}'

    @classmethod
    def count_num(cls):
        count = 0
        for i in cls.a.values():
            count += i
        return f'{count}個'

    @classmethod
    def count_s(cls):
        print(cls().get_info())


#
a = Test(type='dogs', size=2, name='pocky')
# print(Test.rrr())


class A():
    count = 12
    def foo(self):
        print('defffff')

    @classmethod
    def ff(cls):
        print(cls.count)
        cls().foo()  #foo沒有值的時候可以用

    @staticmethod
    def tryu():
        A().foo()


A.ff()
A.tryu()
#
# a = {'vicky': 'eat', 'pocky': 'roo'}
# b = {**a, 'mandy': 'uuu'}
# print(b)



