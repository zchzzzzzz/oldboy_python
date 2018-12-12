file1=open("haproxy.conf","r",encoding="utf8")
def add1():
    print("add1")
def delete1():
    pass
def modify1():
    pass
def search1(data1):
    real_data="backend %s" %data1.strip()
    tag=False
    for i in file1:
      if real_data==i.strip():
         tag=True
         continue
      if tag:
          print(i)
dict_select={
    "1":"add1",
    "2":"delete1",
    "3":"modify1",
    "4":"search1"
}
while True:
 usr_input=input("请选择:")
 data1 = input("请输入要查询的内容:")
 if len(usr_input)==0:
     break
 if usr_input =="1":
     add1()
 if usr_input =="4":
     search1(data1)

