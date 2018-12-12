from socket import *
import time
IP_AND_PORT=("127.0.0.1",8899)
Recv_Num=1024
u1=socket(AF_INET,SOCK_DGRAM)
while True:
    a=input("请输入时间格式").strip()
    u1.sendto(bytes(a,"utf8"),IP_AND_PORT)
    data1,Server_IPANDPORT=u1.recvfrom(Recv_Num)
    print(type(data1))
    print("从服务端获得的时间",data1.decode("utf8"))

