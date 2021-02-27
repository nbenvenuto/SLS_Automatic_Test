import socket
import time


# create socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
clientSocket.connect(("192.168.0.10", 20000))

# send data to server
data = "<ESC>GetWindowSerial<CR>"
clientSocket.send(data.encode())

# receive message from server
#dataFromServer = clientSocket.recv(1024)
#message_decoded = dataFromServer.decode()

# print to console
#print(message_decoded)
