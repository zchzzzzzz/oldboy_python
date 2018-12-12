class MyTypeString:
  def __get__(self, instance, owner):
      print("get方法的Instance是",instance)
      print("get方法的Value是",owner)
  def __set__(self, instance, value):
      print("set")
      print("set方法的Instance是",instance)
      print("set方法的Value是",value)

class room:
    age = MyTypeString()
    def __init__(self,name,age,salary):
       self.name=name
       self.age=age
       self.salary=salary
       print(self.name,self.age,self.salary)
r1=room("z",22,11)
r1.age="33"
print(r1.age)
r1.set("age","44")
print(r1.age)
print(r1.age)


