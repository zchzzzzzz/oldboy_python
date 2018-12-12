from socket import *
IP_AND_PORT=("127.0.0.1",8888)
Backlog_NUM=3
Recv_NUM=1024
udp_socket2=socket(AF_INET,SOCK_DGRAM)
udp_socket2.connect(IP_AND_PORT)
while True:
 str1=input("请输入")
# udp_socket2.send(bytes(str1,"utf8"))
 udp_socket2.sendto(bytes(str1.encode("utf8")),IP_AND_PORT)
 Msg_recvfrom_Server,Server_IPANDPORT= udp_socket2.recvfrom(Recv_NUM)
# =udp_socket2.accept()
 print("收到的服务端返回消息",str(Msg_recvfrom_Server))

udp_socket2.close()
