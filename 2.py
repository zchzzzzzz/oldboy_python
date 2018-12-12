user_list=[
    {"username":"a","login":False},
    {"username":"b","login":False},
    {"username": "zzz", "login": False}
]
username=input("用户名").strip()
passwd=input("密码").strip()
def decorate(fun):
    def dec(*a,**b):
        for i in range(user_list.__len__()):
            a = user_list[i]["username"]
            b = user_list[i]["login"]
            if user_list[i]["login"]==True:
                print("用户名 %s,已登录 " %a)
                print("--")
                return fun
            # else:
            if (username=="zzz") & (passwd=="123"):
                        user_list[i]["login"]=True
                        print("用户名 %s,登录状态 %s" % (a, b))
                        print("密码正确")
                        return fun
            else:
                print("ERROR")
    return dec()
@decorate
def index(name):
    print("index")
# @decorate
# def home(name,passwd):
#     print("home")

# home("zzz","123")