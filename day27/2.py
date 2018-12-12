class room:
    def __getitem__(self, item):
         print("getitem")
         return self.__dict__[item]
    def __setitem__(self, key, value):
        print("setitem")
        self.__dict__[key]=value
    def __delitem__(self, key):
        print("delitem")
        del self.__dict__[key]
room1=room()
room1["name"]="中南海"
print("------")
print(room1["name"])
print("------")
del room1["name"]