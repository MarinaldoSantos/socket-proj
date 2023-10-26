import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))
s.listen(5)

connection, adress = s.accept()

namefile = connection.recv(1024).decode()
with open(namefile, 'rb') as file:
  for data in file.readlines():
    connection.send(data)

  print('Arquivo enviado')