import random

class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        return self.a + self.b +self.a

    def __sub__(self):
        return self.a - self.b

    def __mul__(self):
        return self.a * self.b

    def div(self):
        return  self.a / self.b


class MySort():
    '''
    随机生成100个10至1000之间的数，对生产的100个数进行排序
    '''
    def __init__(self, start, end, count):
        '''
        :param start: 限制随机数生产的范围
        :param end: 生成随机数生产的范围
        :param count: 生成的随机数个数
        '''
        self.start = start
        self.end = end
        self.count = count

        mycount = 0
        mylist = []
        while mycount <=self.count:
            value = random.uniform(self.start, self.end)
            mycount = mycount + 1
            mylist.append(value)


    def __mysort__(self):
        pass





if __name__ == "__main__":
    # calc = Calc(5, 4)
    # calc_result = calc.__add__()
    # # calc_result = calc.div()
    # print(calc_result)
    myso = MySort(10, 1000, 100)
    print(myso)

