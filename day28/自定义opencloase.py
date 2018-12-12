class  room:
    def __init__(self,name):
      self.name=name
    def __enter__(self):
        print("enter")
    def __exit__(self, exc_type, exc_val, exc_tb):
         print("exit")
         return True

with room("1.txt") as f:
    print("111")
    print(a)
    print('222')
