class C1:
    def __init__(self,m,n):
          self.m=m
          self.n=n
    def __iter__(self):
          return self
    def __next__(self):
        while self.m > 20:
         raise StopAsyncIteration("停止")
         temp=self.n
         self.m+=temp
         print(self.m)
         self.n+=self.m
         print(self.n)
         # return self.n,self.m
         # self._m,self._n=self._n,self._m+self._n
         # return self._m
c1=C1(1,1)
for i in c1:
    print(i)
# 1 1 2    3
# m n m+n  n+ m+n

