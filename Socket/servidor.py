import socket

# Cria um objeto socket TCP 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtem o nome da máquina local
host = socket.gethostname()

port = 9999

# Associa a porta
serversocket.bind((host, port))

# Espera por conexões
serversocket.listen(5)

while True:
    # Estabelece a conexão
    clientsocket,addr = serversocket.accept()
    print("Got a connection from %s" % str(addr))
    msg = 'Obrigado por se conectar' + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
    
# Para testar o servidor, execute o código acima e depois execute o código abaixo
# Path: Socket/cliente.py   