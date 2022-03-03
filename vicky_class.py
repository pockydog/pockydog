class Test():
    a = {'red': 10, 'blue': 20}

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def print(self):
        #實例
        print(f'{self.name}, {self.type}') #1. 能讀取、修改範例屬性

        # 類
        print(Test.a) # 3. 能讀取、修改類屬性
        Test.a = {'red': 10, 'blue': 20, 'yellow': 7}
        print(Test.a)

    def print1(self):
        print(self.print())#2. 能呼叫實體方法


    @classmethod
    def print2(cls):
        print(cls.a)
        Test.a = {'red': 10, 'blue': 20, 'yellow': 10000}
        print(Test.a) #3. 能讀取、修改類屬性

    @classmethod
    def print3(cls):
        return cls.print2() #4. 能呼叫類方法

    @staticmethod
    def print4(a, b):
        Test.a = {'red': 10, 'blue': 20, 'yellow': 10000}
        print(Test.a) #3. 能讀取、修改類屬性

        print("{0}+{1}={2}".format(a, b, a + b))
        return a + b

    @staticmethod
    def print5():
        Test.print3() # 4. 能呼叫類方法



a = Test(name='pocky', type='dog')

# a.print()
# print(a.print1())
# Test.print2()
# a.print2()
# a.print3()
# Test.print4(2, 3)
# Test.print5()



