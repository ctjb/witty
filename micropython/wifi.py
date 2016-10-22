import network
import socket

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('SSID', 'password')

addr = socket.getaddrinfo('ctjb.net', 80)[0][-1]
sock = socket.socket()
sock.connect(addr)
sock.send(b'GET /kontakt?do=export_raw HTTP/1.1\r\nHost: ctjb.net\r\nConnection: close\r\n\r\n')

while True:
    data = sock.recv(1024)
    print(data)
    if not data:
        break

sock.close()
