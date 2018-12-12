from socket import *
IP_AND_PORT=("127.0.0.1",8800)
Listen_Size=5
recv_Size=1024

s1=socket(AF_INET,SOCK_STREAM)
s1.connect(IP_AND_PORT)
while True:
 str1=input("请输入")
 # if not str1:
 #  continue
 s1.send(bytes(str1,"utf8"))
 print("客户端消息已发",str1)
#收到服务器端发来的消息msg
 MSG=s1.recv(recv_Size)
 print("服务端返回的消息是 ",MSG)

s1.close()
