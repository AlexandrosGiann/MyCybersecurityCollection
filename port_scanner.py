import socket

host = input("Enter url: ")
ports = [21, 22, 23, 25, 80, 110, 143, 443]

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    result = s.connect_ex((host, port))

    if result == 0:
        print(f"[OPEN] {port}")
    else:
        print(f"[CLOSED] {port}")

    s.close()