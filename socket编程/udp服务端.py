from socket import *
IP_AND_PORT=("127.0.0.1",8888)
Backlog_Num=3
Recv_Num=1024
udp_socket1=socket(AF_INET,SOCK_DGRAM)
udp_socket1.bind(IP_AND_PORT)
while True:
 print("UDP Socket")
 msg,Tuple_Client_IPANDPORT=udp_socket1.recvfrom(Recv_Num)
 print(type(msg))
 # print(type(Client_IPANDPORt))
 print("从客户端收到的消息是",msg)
 udp_socket1.sendto(msg.upper(),Tuple_Client_IPANDPORT)
 print("发送到客户端")
udp_socket1.close()