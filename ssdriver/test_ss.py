import socket
import sys

cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cli.sendto(b'ping', ('127.0.0.1',62000))
print(cli.recv(1506))
cli.sendto(b'add: {"server_port":10001, "password":"7cd308cc059"}', ('127.0.0.1',62000))
print(cli.recv(1506))
cli.sendto(b'remove: {"server_port": 8381}', ('127.0.0.1',62000))
print(cli.recv(1506))

