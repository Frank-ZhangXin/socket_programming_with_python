"""
Project: CS 5523 Operating System Project 1
File name: server.py
Author: Xin Zhang
Email: zxuuzx@gmail.com
Date: 11-03-2014
UTSA CS Department

#########################################

Instruction:
This program is written with Python language. Before running please install python 2.7.x in your system.
1. In server.py direction, type "python server.py" executing server program
2. The server will keep listening request from client and stand by processing request, so you are supposed to execute client program with client.py file then.
3. When requests processed achieve 100, prompt will show currenty usage statistic. (Though requirement asked print out statistic after 1000 requests, this should more intuitional and straight forward)
4. About the print-out statistic, 'C' means counter, and 'T' means timer by second unit.
5. Server is implemented by Multi-threading, which means server will automatically create a new thread to response client request when it arrives.
6. For connection, server socket is setted to address 'localhost' and port 8000.
7. Please feel free to contact me if you met any problems with this program, good luck.

#########################################
"""

import SocketServer
import pickle
import time
# Auxiliary file
import global_var
import counter_timer_grow
from operation import Operation


# Server request handler
class ServerHandler(SocketServer.BaseRequestHandler):
	# Customized server handler (dealing with request)
	def handle(self):
		# Receive and unmarshal request
		self.data = pickle.loads(self.request.recv(2048))

		# Call job dispatcher
		self.dispatcher()
		# Marshal and send back result
		self.request.sendto(pickle.dumps(self.data), self.client_address)

		totalC = global_var.counter1 + global_var.counter2 + global_var.counter3 + global_var.counter4
		totalT = global_var.timer1 + global_var.timer2 + global_var.timer3 + global_var.timer4
		
		# Generate and print report every _ request invocations
		if totalC % 100 == 0:
			print "####### SEVER REPORT #########"
			print "Add	C: %d	T: %f" % (global_var.counter1, global_var.timer1)
			print "Sub	C: %d	T: %f" % (global_var.counter2, global_var.timer2)
			print "Mul	C: %d	T: %f" % (global_var.counter3, global_var.timer3)
			print "Sort	C: %d	T: %f" % (global_var.counter4, global_var.timer4)
			print "------------------------------"
			print "Total	C: %d	T: %f" % (totalC, totalT)
			print "##############################"
			print ""


	# Choose job
	def dispatcher(self):
		arg_list = self.data
		# Choose magicAdd
		if arg_list[0] == '1':
			# Starting time
			timeA = time.time()
			# Increment magicAdd counter
			counter_timer_grow.growAddC()
			#print "This is magicAdd"
			# Operation with args
			newOperation = Operation(arg_list[1], arg_list[2], arg_list[3])
			self.data = []
			self.data.append(newOperation.magicAdd())

			# Ending time
			timeB = time.time()
			# Increment magicSort timer
			counter_timer_grow.growAddT(timeB - timeA)

		# Choose magicSub
		elif arg_list[0] == '2':
			# Starting time
			timeA = time.time()
			# Increment magicSub counter
			counter_timer_grow.growSubC()
			#print "This is magicSub"
			#
			# Operation with args
			newOperation = Operation(arg_list[1], arg_list[2], arg_list[3])
			self.data = []
			self.data.append(newOperation.magicSub())

			# Ending time
			timeB = time.time()
			# Increment magicSort timer
			counter_timer_grow.growSubT(timeB - timeA)

		# Choose magicMul
		elif arg_list[0] == '3':
			# Starting time
			timeA = time.time()
			# Increment magicMul counter
			counter_timer_grow.growMulC()
			#print "This is magicMul"
			# Operation with args
			newOperation = Operation(arg_list[1], arg_list[2], arg_list[3])
			self.data = []
			self.data.append(newOperation.magicMul())

			# Ending time
			timeB = time.time()
			# Increment magicSort timer
			counter_timer_grow.growMulT(timeB - timeA)

		# Choose magicSort
		else:
			# Starting time
			timeA = time.time()
			# Increment magicSort counter
			counter_timer_grow.growSortC()
			#print "This is magicSort"
			#
			arg_list.pop(0)
			# Sorting
			arg_list.sort()
			self.data = arg_list
			# Ending time
			timeB = time.time()
			# Increment magicSort timer
			counter_timer_grow.growSortT(timeB - timeA)

# Multi-threading server
class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
	# Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True
    # Base class init
    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)
        print "Server address is: ", server_address[0], server_address[1]



# 'Main' method, program entrance
if __name__ == "__main__":
	# Init every global vars
	global_var.initVar()

	# Server host, server port
	HOST, PORT = 'localhost', 8000

	# Instantiate the server 
	myServer = ThreadedServer((HOST, PORT), ServerHandler)
	# Keep server running
	myServer.serve_forever()

