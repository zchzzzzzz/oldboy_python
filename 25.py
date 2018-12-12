class Room:
    info="abc"
    def __init__(self,name,width,length):
     self.width = width
     self.length = length
     self.name=name
    @staticmethod
    def static_fun(a,b):
     print(a+b)
    def Non_static_fun(a,b):
        print(a + b)
Room.static_fun(1,2)
a=Room(3,4,5)
a.static_fun(6,7)
Room.Non_static_fun(8,9)
a.Non_static_fun(10,11)
#这行出错，证明实例不能调用非静态方法,会首先传入self