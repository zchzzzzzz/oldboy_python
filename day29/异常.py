# def f1():
#     a=1
#     return a
# def f2():
#     a=2
#     return a
# m=f1()
# n=f2()
# assert m>n
# print("little")
class MyException(BaseException):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

try:
    raise MyException("自定义异常")
except MyException as e:
    print(e)


