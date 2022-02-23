def add_1(*args):
    print(type(args), args)
    total = 0
    for number in args:
        total += number
    return f'{total} time'


def add_2(**kwargs):
    print(type(kwargs), kwargs)
    total = 0
    for key, value in kwargs.items():
        total += value
    return f'{total} around'


def add_3(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)


print(add_1(1, 2, 3, 4, 5))
# add_1(a=1, b=2, c=3, d=4, e=5)  # Error args一定不能帶key
# add_2(1, 2, 3, 4, 5)  # Error 因為kwarg一定要帶key 像下面的用法 好處是可以隨意給key
print(add_2(a=1, b=2, c=3, d=4, e=5))

add_3(1, 2, 3, a=4, b=5)  # 也可以把args跟kwargs合併使用