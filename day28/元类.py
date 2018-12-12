# def __init__(self,name):
#     self.name=name
# def area(self):
#     print("area:--->")
# room1=type("room",(object,),{"name":"z","__init__":__init__,"area":area})
# r1=room1("abc")
# print(r1.name)
# r1.area()
class MyMetaclass(type):
    def __init__(self,a,b,c):
         pass
    def __call__(self, *args, **kwargs):
        print("call---->")
        isinstance1=object.__new__(self)
        self.__init__(isinstance1,*args, **kwargs)
        return  isinstance1
class car(metaclass=MyMetaclass):
    def __init__(self,name):
        self.name=name
        print("name=",name)
c1=car("abc")
print(c1.__dict__)

