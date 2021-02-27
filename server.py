import socket

# create a stream socket IPv4
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind and listen
serverSocket.bind(("127.0.0.1", 9090))
serverSocket.listen()

# accept connections
while True:
    (clientConnected, clientAddress) = serverSocket.accept()

    print(f"Accepted connection request from {clientAddress}")

    dataFromClient = clientConnected.recv(1024)
    message_received = dataFromClient.decode()
    print(message_received)

    # send message to clinet
    message_to_client = f"clio client, come stai? - ho ricevuto il tuo messagio {message_received}"
    clientConnected.send(message_to_client.encode())