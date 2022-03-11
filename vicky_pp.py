def test1():
    a = list()
    for i in range(1, 5):
        for j in range(1, 5):
            for u in range(1, 5):
                if i != j and j != u and u != i:
                    a.append(f'{i} {j} {u}')
    return a
# print(test1())

def test2():
    i = float(input('淨利率:'))
    money = [1000000, 600000, 400000, 200000, 100000, 0]
    bonus = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    r = 0
    for go in range(6):
        if i > money[go]:
            i = i - money[go]
            r += i * bonus[go]
    print(r)
# test2()


def test3():
    year = int(input('year'))
    month = int(input('month'))-1
    day = int(input('day'))
    months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        a = months[month]+day
        if a > int(59):
            print(a+1)
    else:
        print(months[month]+day)
# test3()


def test4():
    a = [input('enter:') for _ in range(3)]
    print(a)
# test4()


import time


def test5():
    a = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in a:
        print(i)
        time.sleep(1)
# test5()


import datetime
def test6():
    s = input('请输入一个字符串:\n')
    letters = 0
    space = 0
    digit = 0
    others = 0
    for c in s:
        if c.isalpha():
            letters += 1
        elif c.isspace():
            space += 1
        elif c.isdigit():
            digit += 1
        else:
            others += 1
    print('char = %d,space = %d,digit = %d,others = %d' % (letters, space, digit, others))
# test6()

def test7():
    a = 0
    b = list()
    num = int(input('enter:'))
    count = int(input('enter:'))
    for _ in range(count):
        a += num
        b.append(a)
    print(sum(b))
# test7()


def test8():
    high = 100
    course = 100
    for i in range(1, 11):
        course, high = course+high, high/2
        print(f'第{i}次彈跳:{high}')
    print(f'總共彈跳:{course}')
# test8()

def test9():
    a = 1
    for _ in range(9, 0, -1):
        a = (a + 1) * 2
    print(a)
# test9()


import random
def test10():
    a = ['x', 'y', 'z', 'u', 'i', 'o', 'l']
    b = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    while True:
        random.shuffle(a)
        if 'x' not in a[0] and 'z' not in a[2] and 'z' not in a[0]:
            break
    for x, y in zip(a, b):
        print(f'{y}:{x}')
# test10()

def test11():
    a = 1
    b = 2
    for _ in range(0, 21):
        ans = (a + b)
        b = ans
        a = (b - a)
        print(a)
# test11()

def test12():
    a = 2.0
    b = 1.0
    sum = 0
    for _ in range(1, 21):
        sum += a / b
        t = a
        a = a + b
        b = t
    print(sum)
# test12()

def test13():
    a = input('enter:')
    for i in a[::-1]:
        print(i)
# test13()

def test14(n):
    if n == 1: c = 10
    else: c = test14(n - 1)+2
    return c
# print(test14(5))

def test15():
    a = input('enter_int:\n')
    print(a[::-1])
    print(len(a))
# test15()

def test16():
    L = [1, 2, 3, 4, 5]
    s1 = ','.join(str(n) for n in L)
    print(s1)
# test16()

def test17():
    print('pocky')

def test18():
    for i in range(3):
        test17()

# test18()

def test19():
    info = list()
    for i in range(4):
        a = int(input('enter_num:'))
        print(f'你輸入的數字為{a}')
        info.append(a)
    for i in info:
        print(i)
    print('調整過後：')
    info.sort()
    print(info)


# test19()

def test20():
    a = [5, 4, 6, 9, 13, 16, 19, 28, 40, 100]
    print('原始列表:')
    for i in a:
        print(i)
    haha = int(input('enter_your_num:'))
    print(f'{haha}為你輸入的數字')
    a.append(haha)
    a.sort()
    for i in a:
        print(i)

# test20()


def test21():
    a = [9, 6, 5, 4, 1]
    a[0], a[-1] = a[-1], a[0]
    print(a)

# test21()

def test22():
    num = 0
    print(f'num {num}')
    num +=1
# if __name__ == '__main__':
#     for i in range(3):
#         test22()
# test22()


class Test1():
    num = 5

    def test23(self):
        self.num +=1
        return self.num

# a = Test1()
# for i in range(3):
    # print(a.test23())


def test24():
    x = [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
    y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]
    result = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    for i in range(len(x)):
        for u in range(len(x)):
            result[i][u] = x[i][u] + y[i][u]
    print(result)


# test24()

def test25():
    num = 0
    for i in range(1, 101):
        num += i
    print(num)
# test25()

def test26():
    while True:
        a = int(input('enter_tour_num:'))
        if a*a <=50:
            print(f'{a} no')
            break
        else:
            int(f'{a}yes')

# test26()

def test27():
    a = [int(input('enter_num:')) for _ in range(3)]
    a.sort()
    print(a)


# test27()

def test28():
    a = [int(input('enter_num:')) for _ in range(6)]
    b = a.index(max(a))
    c = a.index(min(a))
    a[0], a[b], a[-1], a[c] = a[b], a[0], a[c], a[-1]
    print(a)

# test28()

def test29():
    name = input('enter_your_name:')
    score_math = int(input('enter your math score:'))
    # score_english = int(input('enter your english score:'))
    # score_sport = int(input('enter your sport score:'))
    # no = int(input('enter your No:'))
    print(f'{name}, {score_math}')

test29()

# def test30():