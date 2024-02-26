import threading
import socket
import time

def cliente():
    # Cria um objeto socket TCP
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Obtem o nome da máquina local
    host = socket.gethostname()
    
    port = 9999
    
    # Conecta ao servidor
    clientsocket.connect((host, port))
    
    # Recebe no máximo 1024 bytes
    msg = clientsocket.recv(1024)
    
    clientsocket.close()
    
    print(msg.decode('ascii'))

# Cria 10 threads
for i in range(10):
    t = threading.Thread(target=cliente)
    t.start()
    time.sleep(1)

# Para testar o servidor, execute o código acima e depois execute o código abaixo
# Path: Socket/cliente.py
# Path: Socket/servidor.py
# Execute o servidor e depois execute o cliente
# O servidor irá imprimir:
# Got a connection from ('