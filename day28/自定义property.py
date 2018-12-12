# class MyProperty:
#     pass
# class room:
#     def __init__(self,name,width,length):
#         self.width=width
#         self.length=length
#     @MyProperty
#     def area(self):
#         return self.length*self.width
#
# r1=room("z",2,3)
# print(r1.area)
# a=type()
# print(type(a))
class room:
    pass
a=type("room",(object,),{"x":1})
print(a.__dict__)
b=room()
print(b.a)


