import time
def decorate(fun):
   def dec(*a,**b):
       starttime = time.time()
       x=fun(*a,**b)
       endtime=time.time()
       print(endtime-starttime)
       return x
   return dec
# @decorate
# def f1(name,age):
#     time.sleep(1)
#     print("name %s, age %d" %(name,age))
@decorate
def f2(*m,**n):
    time.sleep(0.5)
    print(m,n)
# f1("abc",22)
f2(name="zzz",age=23,gender="men")
