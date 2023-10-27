'''
编写一个Python程序，
可以执行加法、减法、乘法和除法操作。
用户可以输入两个数字和运算符，然后计算并输出结果。
实现计算器的功能（+、-、*、/），并处理异常情况，比如：输入的不是数字、除数为0等。
'''


class MyException(Exception):
    def __init__(self, *args):
        print(f"请检查输入的数据{args}是否都正确")


def wai(*args):
    def wapper(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TypeError:
                return "请检查输入的是否是数字类型"
            except ZeroDivisionError:
                return "被除数不能为0"
            except Exception:
                raise MyException(*args)
        return inner
    return wapper

@wai("num1,num2,sign")
def cal(num1, num2, sign: str):
    sign_list = ["+", "-", "*", "/"]
    if sign == sign_list[0]:
        result = num1 + num2
    elif sign == sign_list[1]:
        result = num1 - num2
    elif sign == sign_list[2]:
        result = num1 * num2
    elif sign == sign_list[3]:
        result = num1 / num2
    return result


datas = [(1, 2, "+"), (5, 2, "-"), (3, 2, "*"), (4, 2, "/"),
         ("a", 2, "+"), (3, 0, "/"), (3, 6, "v")]
for i in datas:
    print(cal(*i))
