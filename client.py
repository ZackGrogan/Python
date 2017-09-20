import socket
import os



def Connection
soc = socket.socket()
host = socket.gethostname()
port 1000
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


def Info
with with io.FileIO*(str(Ln), "w"):
        FN = input('Enter your first name:  ')
        LN = input('Enter your first name:  ')
        AD = input('Enter your first name:  ')
        UN = input('Enter your first name:  ')
        PS = input('Enter Your Password:    ')
    out.write('{}\n{}\n{}\n{}\n'.format(LN,AD,UN,PS))
