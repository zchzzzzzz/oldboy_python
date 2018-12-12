def outerdecorate(**kwargs):
    def mydecorate(obj):
        print("装饰器已运行")
        obj.a=1
        obj.b=2
        obj.c=3
        return obj
    return mydecorate
@outerdecorate
class room:
    def __init__(self,name):
        self.name=name
        print(self.name)
r1=room("z")
print(r1.a)
print(room.a)
