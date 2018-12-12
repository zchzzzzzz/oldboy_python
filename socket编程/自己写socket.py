import socket
s1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.bind(("127.0.0.1",8080))
s1.listen(5)
s1.accept()
s1.recv()
s1.connect()
s1.close()