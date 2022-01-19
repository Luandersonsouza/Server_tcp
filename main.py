import socket 

meu_ip='localhost'

minha_porta= 8000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

testa_msg =''
my_server= (meu_ip, minha_porta)
tcp.bind(my_server)

tcp.listen(1)

con, doclient = tcp.accept()
print("O cliente = ", doclient, "se conectou")

while True:
	msg_recebida = con.recv(1024)
	if testa_msg != msg_recebida:
		print("Recebi = ", msg_recebida, "Do cliente", doclient)

con.close()