file1=open("haproxy.conf","r",encoding="utf8")
a=file1.readline()
print(file1.__next__())