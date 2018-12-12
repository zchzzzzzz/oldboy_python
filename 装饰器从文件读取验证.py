file1=open("file.db","r",encoding="utf8")

def decorate1(fun):
    list1=list(file1)
    def inner(*a,**b):
        for i in list1:
            x=eval(i)
            # print(x)
            uname=x["username"]
            upassword=x["password"]=="111"
            if(uname=="a" )and(upassword=="111" ):
                print("%s is right" %uname)
                print()
                return fun
    return inner()
@decorate1
def f1():
    print("f1 已执行")

f1()