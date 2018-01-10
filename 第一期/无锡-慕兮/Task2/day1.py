# -*- coding:utf-8 -*-

__author__ = 'liqi'

if __name__ == "__main__":
    # 读取键盘输入的任何值
    word = 1012
    data = input ("请输入任何一串字符串：")

    '''
    旧版格式化
    '''
    # 文本格式化显示 %s：字符串 %d: 十进制整数 %x：十六进制整数 %o：八进制整数
    # %f:十进制浮点数 %e: 以科学计数法表示的浮点数
    # %%：文本%本身 不能单独使用，要和其他搭配使用 "%s%%" %data
    # print("这是你输入的字符串： %s%%" %data  )
    # print("word等于：%d data等于%s" %(word, data))
    # print("这是你输入的字符串：", data)
    print("word等于：%10.4d data等于%10.4s" % (word, data))
    '''
    新版格式化
    '''
    print("{} {}".format(word, data))
    print("{1} {0}".format(word, data))
    dictA = {'word':13, 'data':"sd"}
    print("{word} {data}".format(word = 13, data = "asdas"))


    # intdata = int(input("请输入你的int类型数："))
    # print("这是你输入的int类型数：%d" %intdata)

    # 以空格切割输入的字符串
    list_data = data.split(' ')

    # 打印切割后的数据
    # print(list_data)

