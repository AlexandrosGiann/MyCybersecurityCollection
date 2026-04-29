import socket

host = input("Host: ")
port = int(input("Port: "))

s = socket.socket()
s.settimeout(5)

try:
    s.connect((host, port))
    banner = s.recv(1024)
    print("Banner:", banner.decode(errors="ignore"))
except:
    print("No banner or connection failed")

s.close()