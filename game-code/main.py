#!/bin/python
from __future__ import print_function
from gameFunction import *

maindir = os.path.dirname(os.path.abspath(__file__))
readme = os.path.join(maindir, 'notes.txt')
white = '\033[97m'
black = '\033[30m'
light_g = '\033[37m'
dark_g = '\033[90m'
yellow = '\033[93m'
red = '\033[31m'
ENDC = '\033[m'

# Start here:
startingScreen()
