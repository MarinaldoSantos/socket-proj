import socket 

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

c.connect((socket.gethostname(),1234))
print('conectado \n')

namefile = str(input('Arquivo >>>'))

c.send(namefile.encode())

with open(namefile, 'wb') as file:
  while 1:
    data = c.recv(10000000)
    if not data:
      break
    file.write(data)

print(f'{namefile} recebido \n')