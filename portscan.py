import socket
import sys

ip =input("Digite o IP")
for porta in range (1,65535):

     meusock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     if meusock.connect_ex ((ip,porta)) ==0:
             print("Porta",porta, "[Aberta]")
             meusock.close()
