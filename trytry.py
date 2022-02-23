# def test(*args):
#     print(args)
#
#
# def test2(**kwargs):
#     print(kwargs)
#
#
# test(1, 2, 3, 4, 5, 6, 7, 8, 9, 99)
# test2(coo='c', eoo='f', too='i')
# print(test)
# print(test2)

# param_a = 1
#
# class test:
#     param_b = 1
#
# @classmethod
# def function_a(cls):
#     param_c = 1


# def function_b(a, b):
#     return a + b
#
# def function_c(c):
#     return c * 2
#
# if __name__ == '__main__':
#     result = function_b(a=1, b=2)
#     results = function_c(c=result)
#     print(results)

import os
os.getcwd()
# print(os.getcwd())
# print(os.listdir())
# # os.mkdir('416')
# print(os.listdir())
# # os.rmdir('416')
# print(os.listdir())
# # os. rename('pockydog', 'pockyoxox')
# print(os.listdir())

# a = enumerate(['b', 'c', 'd'])
# # print(a)
# # print(list(a))
# a = iter([1, 2, 3])
# c = [2, 2, 2]
# print(c)
# red_copy = list(c)
# print(c)

tinydict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print("字典值 : %s" % tinydict.items())

a = 1, 2, 3, 4
b = 'q2'
c = {
    'a': a,
    'habit': b
}
print(c)
