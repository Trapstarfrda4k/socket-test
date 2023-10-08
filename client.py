from socket import *

servername = 'localhost'
serverport = 12022

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((servername,serverport))

sentence = input('her har du mugligheden for at vælge add,ran,sub?: ')
data = sentence.encode()
clientSocket.send(data)

datatilbage = clientSocket.recv(2048)
sentenceTilbage = datatilbage.decode()

print ('det givende resultat ', sentenceTilbage)
clientSocket.close()