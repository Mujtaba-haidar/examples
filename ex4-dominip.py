import socket

domin = input('Enter the domain url :')
ip = socket.gethostbyname(domin)
print(ip)