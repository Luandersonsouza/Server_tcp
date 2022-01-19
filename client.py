import socket

ip_server = 'localhost'
porta_server = 8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

destino = (ip_server, porta_server)

tcp.connect (destino)

while True:
	msg = input( )
	tcp.send(bytes(msg, "utf-8"))

tcp.close()