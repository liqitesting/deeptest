#coding=utf-8

try:
    a=int(raw_input("please input a number:"))
except ValueError:
    print("第一个运算数字输入非数字")


try:
    b=int(raw_input("please input another number:"))
except ValueError:
    print("第二个运算数字输入非数字")

print("打印两个数的和为：%d"%(a+b))
print("打印第一个数减去第二个数的差为：%d"%(a-b))
try:
    print("打印第一个数除以第二个数的差商为：%d"%(a/b))
except ZeroDivisionError:
    print("除数为0,请正确输入！")

print("打印两个数的乘积为：%d"%(a*b))