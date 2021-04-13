import socket
import threading


def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    try:
        connect = sock.connect((ip, port))
        print('Port :', port, ' открыт')
        connect.close()
    except:
        print('Port :', port, ' закрыт')


ip = input()
if (ip == ""):
    ip = "8.8.8.8"
    print(ip)
for i in range(1, 100):
    potoc = threading.Thread(target=scan_port, args=(ip, i))
    potoc.start()
input()
print("Конец")