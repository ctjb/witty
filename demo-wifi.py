import network
import socket

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('SSID', 'password')

addr = socket.getaddrinfo('ctjb.net', 80)[0][-1]
sock = socket.socket()
sock.connect(addr)
sock.send(b'GET /2016 HTTP/1.1\r\nHost: ctjb.net\r\n\r\n')
data = sock.recv(1024)
sock.close()
data = data.decode('ascii')

print(data)
