"""
Project: CS 5523 Operating System Project 1
File name: global_var.py
Author: Xin Zhang
Email: zxuuzx@gmail.com
Date: 11-03-2014
UTSA CS Department
##################
Instruction:
This is a auxiliary file for server.py which defines and initializes global variables.
##################
"""

# Global variables

# Init every vars
def initVar():
	# Init global counter
	global counter1 # magicAdd
	counter1 = 0
	global counter2 # magicSub
	counter2 = 0
	global counter3 # magicMul
	counter3 = 0
	global counter4 # magicSort
	counter4 = 0
	# Init global timer
	global timer1
	timer1 = 0.0
	global timer2
	timer2 = 0.0
	global timer3
	timer3 = 0.0
	global timer4
	timer4 = 0.0