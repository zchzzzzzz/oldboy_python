class People:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        while(self.n<20):
         return self
    def __next__(self):
        self.n+=1
        return self.n

p1=People(10)
for i in p1:
    print(i)
