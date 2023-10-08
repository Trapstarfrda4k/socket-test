

from socket import *
from threading import *
from random import *

serverPort = 12022


def handleClient(clientSocket, addr):
    sentence = clientSocket.recv(2048).decode()     

    splittetText = sentence.split()                 
    Text=''
    if (splittetText[0].lower() == 'add'):      
        talx = int (splittetText[1])
        taly = int (splittetText[2])
        Text = f'{talx} +  {taly} = {(talx+taly)}'
    elif(splittetText[0].lower() == 'sub'):      
        talx = int (splittetText[1])
        taly = int (splittetText[2])
        Text = f'{talx} -  {taly} = {(talx-taly)}'
    elif(splittetText[0].lower() == 'ran'):      
        talx = int (splittetText[1])
        taly = int (splittetText[2])
        Text = f'{randint(talx,taly)}'
    else:
        Text = f'metoden er ugyldig {splittetText[0]}'

    clientSocket.send(Text.encode())                
    clientSocket.close()                            



serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))              
serverSocket.listen(1)                          
print('serveren starter op', serverSocket)

while True:
    connectionSocket, addr = serverSocket.accept()
    print('forbindelse til client', addr)
    Thread(target=handleClient, args=(connectionSocket, addr)).start()