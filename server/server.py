import socket
import threading

HOST='**********'
PORT=9999
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))

server.listen()

clients=[]
nicknames=[]

#broadcast
def broadcast(message):
    for client in clients:
        client.send(message)
  
#handle
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            print(f"{nicknames[clients.index(client)]} says {message}")
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            nickname=nicknames[index]
            broadcast('{} left!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            with open(r'online.txt', 'w') as fp:
                for item in nicknames:
                    # write each item on a new line
                    fp.write("%s\n" % item)
            break

#receive
def receive():
    while True:
        client,address=server.accept()
        print(f"connected with {str(address)}!")
        
        client.send("NICK".encode('utf-8'))
        nickname=client.recv(1024).decode('utf-8')
        
        nicknames.append(nickname)
        with open(r'online.txt', 'w') as fp:
            for item in nicknames:
                # write each item on a new line
                fp.write("%s\n" % item)
        clients.append(client)
        
        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        thread1=threading.Thread(target=handle,args=(client,))

        thread1.start()
        
        
print("---Server running---")                                               
receive()