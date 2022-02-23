class Soo:

    @classmethod
    def c(cls):
        count = [1, 2, 3, 4, 55, 6, 9.9]
        return count

    @classmethod
    def ee(cls):
        count = cls.c()
        result = filter(lambda x: x !=1, count)
        return list(result)


    @classmethod
    def oo(cls):
        count= cls.c()
        result = map(lambda x: x*2, count)
        return list(result)

    @classmethod
    def show(cls):
        add = cls.oo()
        single = cls.ee()
        count = cls.c()
        a = list()
        # for i in add, single:
        #     result = {
        #         'add': add,
        #         'single': single
        #     }
        #     a.append(result)
        # print(a)
        for i in add:




if __name__ == '__main__':

    Soo.show()
