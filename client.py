import socket
import time

# Variables definitions
ip_working = "192.168.0.201"
port = 20000
SerialNumber = "B18P03933"

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
clientSocket.connect((ip_working, port))

# receive data to server
dataFromServer = clientSocket.recv(1024)
message_decoded = dataFromServer.decode(encoding="ascii")

# print to console the received message
print("Versione PTS" + " " + message_decoded)


# write the message to send the server (in this step it is important to convert the characters ESC, LF, CR in x1b,x0a,r)
Set_SerialNumber = '\x1b' + "SetSerialNumber" +'\x0a' + SerialNumber + '\r'
Get_SerialNumber = '\x1b' + "GetSerialNumber" + '\r'

# send Set_SerialNumber to server
clientSocket.send(Set_SerialNumber.encode())
time.sleep(2)
# receive message from server
dataFromServer = clientSocket.recv(1024)
message_decoded = dataFromServer.decode()
print("Stato operazione" + " " + message_decoded)

# send Get_SerialNumber to server
clientSocket.send(Get_SerialNumber.encode())
# receive message from server
dataFromServer = clientSocket.recv(1024)
message_decoded = dataFromServer.decode()
print("The New" + " " + message_decoded)

# close the socket connection
clientSocket.close()

