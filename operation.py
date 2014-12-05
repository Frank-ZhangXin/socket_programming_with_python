"""
Project: CS 5523 Operating System Project 1
File name: operation.py
Author: Xin Zhang
Email: zxuuzx@gmail.com
Date: 11-03-2014
UTSA CS Department
##################
Instruction:
This is a auxiliary file for server.py which implements server's math operations like magicAdd, magicSub, magicMul.
##################
"""

class Operation(object):
	
	def __init__(self, op1, op2, op3):
		self.op1 = op1
		self.op2 = op2
		self.op3 = op3

	def magicAdd(self):
		ret_val = 0.0
		for i in range(1, self.op3+1):
			ret_val += self.op1/i + self.op2/i
		return ret_val
          
	def magicSub(self):
		ret_val = 0.0
		for i in range(1, self.op3+1):
			ret_val += self.op1/i - self.op2/i
		return ret_val

	def magicMul(self):
		ret_val = 0.0
		for i in range(1, self.op3+1):
			ret_val += (self.op1/i) * (self.op2/i)
		return ret_val



