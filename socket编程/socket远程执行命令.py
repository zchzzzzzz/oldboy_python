import subprocess

from socket import *
IP_AND_PORT=("127.0.0.1",8800)
Listen_Size=5
recv_Size=1024
s1=socket(AF_INET,SOCK_STREAM)
s1.bind(IP_AND_PORT)
s1.listen(Listen_Size)
print("listen开始")
while True:
  connection1,addr1=s1.accept()
  msg=connection1.recv(recv_Size)
  print("客户端发来的消息是",msg)
 #把收到的客户端消息全部大写，再转发出去
  connection1.send(msg.upper())


connection1.close()
s1.close()