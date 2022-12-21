import socket

hostname = 'www.google.com'
hsna = socket.getfqdn(hostname)
print(hsna)

print(socket.getfqdn("8.8.8.8"))