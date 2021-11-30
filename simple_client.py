import socket
import time

SERVER_HOST = 'localhost'
SERVER_PORT = 8090


client_socket = socket.socket()
client_socket.connect((SERVER_HOST, SERVER_PORT))

print('Sending Ping...')
client_socket.send('Ping'.encode())
print('Receiving response...')
response = client_socket.recv(100)
print(f'{response} was received')
time.sleep(5)

print('Closing connection...')
client_socket.close()
