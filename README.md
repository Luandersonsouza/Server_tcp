# Server_tcp
Aplicação que realiza a comunicação unilateral do cliente para o servidor.

Utilizando a biblioteca socket o programa envia mensagens do cliente ao servidor convertendo as strings para bytes e mandando via conexçao tcp, mas antes de seer possivel enviar qualquer mensagem é testada a conexão de porta e servidor para ai sim ser possivel enviar as mensagens, deixei "while True" para que sejam enviadas quantas mensagens quiser.
