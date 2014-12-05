"""
Project: CS 5523 Operating System Project 1
File name: client.py
Author: Xin Zhang
Email: zxuuzx@gmail.com
Date: 11-03-2014
UTSA CS Department

#########################################

Instruction:
This program is written with Python language. Before running please install python 2.7.x in your system.
1. After starting server program, type command "python client.py" to execute client program.
2. Client will automatically send 1000 requests continously that are mixed with four kinds of computation randomly. And the mechanism is implemented by Thread Pool, which is defined in "threadpool.py".
3. For connection, client socket connects address 'localhost', and port 8000.
4. Please feel free to contact me if you met any problems with this program, good luck.

#########################################
"""


from socket import *
from random import *
import pickle
import time
from threadpool import ThreadPool, ThreadPoolTask


# Generate request type and args randomly
def genRequest():
	arg_list = []
	rType = randint(1, 4)
	# Test, set type of opertation to sorting
	# rType = 1  
	if rType != 4:
		# Assume float number generate range -1000 to 1000
		op1 = uniform(-1000000000, 1000000000)
		op2 = uniform(-1000000000, 1000000000)
		k = randint(500, 1000)
		arg_list.extend([str(rType), op1, op2, k])
	else:
		arg_list.append(str(rType))
		# EOF Error might happen when k goes up over 200
		k = randint(100, 200)
		for i in range(k):
			arg_list.append(randint(1, 1000000))
	
	# Marshal request
	serial_list = pickle.dumps(arg_list)
	return serial_list

# Client socket config, connect; send  request & receive result
def request():
	# Init client socket
	client_socket = socket(AF_INET, SOCK_STREAM)
	client_socket.connect(('localhost', 8000))
	# Send request
	client_socket.send(genRequest())
	print pickle.loads(client_socket.recv(2048))
	client_socket.close()

# 'Main' method, program entrance.
if __name__ == "__main__":

	# Task list
	tList = []
	# Generate __ requests
	for i in range(1000):
		tList.append(ThreadPoolTask(request))

	# Instantiate Thread Pool and pool size is 5
	# Five active threads are sending requests
	tp = ThreadPool(5)

	# Add all task into waiting queue
	for i in tList:
		tp.addTask(i)
	
	# Start Thread Pool thread
	tp.start()

	# Wait a little bit until each task is done (Each request is sent)
	time.sleep(3)
	tp.terminate()








