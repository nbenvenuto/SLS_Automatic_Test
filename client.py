import socket
import time


# create socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
clientSocket.connect(("127.0.0.1", 9090))

# send data to server
data = "bla bla bla "
clientSocket.send(data.encode())

model_number = "54744as"
ttt = "<CR>748785214</CR>"

time.sleep(2)
clientSocket.send(model_number.encode())

time.sleep(2)
clientSocket.send(ttt.encode())

# receive message from server
dataFromServer = clientSocket.recv(1024)
message_decoded = dataFromServer.decode()

# print to console
print(message_decoded)
