class room:
    def __init__(self,name,length,width,height):
        self.name=name
        self.__length=length
        self.__width=width
        self.__height=height
    def mianji(self):
        print(self.__length*self.__width*self.__height)


room1=room("中南海",-1,-1,-1)
room1.mianji()
# print(room1.length)