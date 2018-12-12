def dog(name,type,age):
     def barking():
         print("%s 在汪汪叫" %name)
     def run():
         print("狗在跑")
     dog1={
         "name":name,
          "type":type,
         "age":age
     }
     return dog

dog1=dog("哈士奇","狗",11)
dog1["barking"](dog1)





