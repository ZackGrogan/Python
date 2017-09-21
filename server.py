import socket
import os

soc = socket.socket()
host = socket.gethostname()
port = 1000
soc.bind((host, port))
fts = open('File.txt','w')
soc.listen(5)
while True:
    c, ip=soc.accept()
print'Receiving connection from', ip
rec = c.recv(1000)
While(rec)
print"Receiving File from", ip
f.write(rec)
rec = c.recv(1000)
c.close()
