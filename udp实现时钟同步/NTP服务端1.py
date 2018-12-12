from socket import *
import time
IP_AND_PORT=("127.0.0.1",8899)
Recv_Num=1024
u1=socket(AF_INET,SOCK_DGRAM)
u1.bind(IP_AND_PORT)
while True:
    a,client_IPANDPORT=u1.recvfrom(Recv_Num)
    if not a:
        x=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    else:
        print(type(a))
        x=time.strftime(str(a),time.localtime())
    u1.sendto(bytes(x,"utf8"),client_IPANDPORT)
u1.close()