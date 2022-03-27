import os
import threading 



		
def enum1():
	for i in range(1,10000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum2():
	for i in range(10000,10000):
		oos.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum3():
	for i in range(10000,110000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
						

def enum4():
	for i in range(110000,20000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum5():
	for i in range(20000,210000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum6():
	for i in range(210000,30000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum7():
	for i in range(30000,310000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum8():
	for i in range(310000,40000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum9():
	for i in range(40000,410000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
		
def enum10():
	for i in range(410000,100000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum11():
	for i in range(100000,1010000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum12():
	for i in range(1010000,60000):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
def enum13():
	for i in range(60000,61010310):
		os.system(f"timeout 10 rdesktop  <target ip>:{i}  2>&1 | grep -v Autoselecting | tee success.txt")
	
		f = open("success.txt",'r')
		if "Valid From:" in f.read():
			print(f"found {i}")
			os.system(f"echo the port number is {i} > port.txt")
			break
		
		
		

		
t1 = threading.Thread(target=enum1)
t2 = threading.Thread(target=enum2)
t3 = threading.Thread(target=enum3)
t4 = threading.Thread(target=enum4)
t5 = threading.Thread(target=enum5)
t6 = threading.Thread(target=enum6)
t7 = threading.Thread(target=enum7)
t8 = threading.Thread(target=enum8)
t9 = threading.Thread(target=enum9)
t10 = threading.Thread(target=enum10)
t11 = threading.Thread(target=enum11)
t12 = threading.Thread(target=enum12)
t13 = threading.Thread(target=enum13)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()		
