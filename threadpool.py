"""
Project: CS 5523 Operating System Project 1
File name: threadpool.py
Author: Xin Zhang
Email: zxuuzx@gmail.com
Date: 11-03-2014
UTSA CS Department
##################
Instruction:
This is a auxiliary file for client.py which implements thread pool for work load distribution.
##################
"""

from threading import Thread
import time

# Thread pool
class ThreadPool(Thread):
	def __init__(self, pool_size):
		Thread.__init__(self, target = self.__run)
		# Init thread pool size
		self.__pool_size = pool_size
		# Check freq on running task and remove finished one from 'running' list
		self.__check_frequence = 0.5
		# Waiting task queue
		self.__task__queue = []
		# Running task queue
		self.__task__running = []
		# Terminate main thread pool thread
		self.__stop = False

	# No one's waiting and running?
	def __allEmpty(self):
		return len(self.__task__queue) + len(self.__task__running) == 0

	# No one's waiting?
	def __qEmpty(self):
		return len(self.__task__queue) == 0

	# No one's running?
	def __noRunning(self):
		return len(self.__task__running) == 0

	# How many task are running
	def tRunning(self):
		return len(self.__task__running)

	def __run(self):

		# Neither queue is empty and No terminated by main thread
		while not (self.__allEmpty() and self.__stop):
			# Check freq
			time.sleep(self.__check_frequence)

			# Check if any task finished, if so, removed from running queue
			for task in self.__task__running:
				if not task.isAlive():
					self.__task__running.remove(task)

			# Pool is not full and waiting queue not empty, take one task to pool from queue
			while self.tRunning() < self.__pool_size and not self.__qEmpty():
				task_to_run = self.__task__queue.pop(0)
				task_to_run.start()
				self.__task__running.append(task_to_run)

	# Add new task into waiting queue
	def addTask(self, task):
		self.__task__queue.append(task)

	# Terminate thread pool thread
	def terminate(self):
		self.__stop = True

# Thread pool task
class ThreadPoolTask(Thread):
	def __init__(self, task):
		self.task = task
		Thread.__init__(self, target = self.task)


# TEST Main, no reference with outside invocation
if __name__ == "__main__":
	def myMethod():
		print "This is a method."

	def myMethod2():
		print "This is another method."

	myTask = ThreadPoolTask(myMethod)
	myTask2 = ThreadPoolTask(myMethod2)
	
	tp = ThreadPool(1)
	tp.addTask(myTask)
	tp.addTask(myTask2)
	tp.start()

	time.sleep(3)
	tp.terminate()




