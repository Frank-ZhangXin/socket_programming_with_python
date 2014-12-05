"""
Project: CS 5523 Operating System Project 1
File name: counter_timer_grow.py
Author: Xin Zhang
Email: zxuuzx@gmail.com
Date: 11-03-2014
UTSA CS Department
##################
Instruction:
This is a auxiliary file for server.py which deals with global counter increment.
##################
"""

from threading import BoundedSemaphore
import global_var

# Counter change
def growAddC():
	semaphore = BoundedSemaphore()
	semaphore.acquire()
	global_var.counter1 += 1
	semaphore.release()

def growSubC():
	semaphore = BoundedSemaphore()
	semaphore.acquire()
	global_var.counter2 += 1
	semaphore.release()

def growMulC():
	semaphore = BoundedSemaphore()
	semaphore.acquire()
	global_var.counter3 += 1
	semaphore.release()

def growSortC():
	semaphore = BoundedSemaphore()
	semaphore.acquire()
	global_var.counter4 += 1
	semaphore.release()

# Timer Change

def growAddT(tSum):
	semaphore = BoundedSemaphore()
	semaphore.acquire()
	global_var.timer1 += tSum
	semaphore.release()

def growSubT(tSum):
	semaphore = BoundedSemaphore()
	semaphore.acquire()
	global_var.timer2 += tSum
	semaphore.release()

def growMulT(tSum):
	semaphore = BoundedSemaphore()
	semaphore.acquire()
	global_var.timer3 += tSum
	semaphore.release()

def growSortT(tSum):
	semaphore = BoundedSemaphore()
	semaphore.acquire()
	global_var.timer4 += tSum
	semaphore.release()
