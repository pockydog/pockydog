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
    r =0
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
    count =int(input('enter:'))
    for i in range(count):
        a +=num
        b.append(a)
    print(sum(b))

# test7()

def test8():
    high = 100
    test = 0
    course = 100
    a = list()
    for i in range(1, 11):
        course, high = course+high, high/2
        print(f'第{i}次彈跳:{high}')
    print(f'總共彈跳:{course}')
test8()