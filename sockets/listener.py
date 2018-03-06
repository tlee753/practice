import socket

serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a public host,
# and a well-known port
serversocket.bind(("127.0.0.1", 1200))
#become a server socket
serversocket.listen(5)
