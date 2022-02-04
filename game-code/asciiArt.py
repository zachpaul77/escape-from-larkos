#!/bin/python
## Prints ASCII art character-by-character

from __future__ import print_function
import os
import time

WHITE = '\033[97m' + unichr(0x2588)
white = '\033[97m'
BLACK = '\033[30m' + unichr(0x2588)
LIGHT_G = '\033[37m' + unichr(0x2588)
DARK_G = '\033[90m' + unichr(0x2588)
YELLOW = '\033[93m' + unichr(0x2588)
RED = '\033[31m' + unichr(0x2588)
ENDC = '\033[m'

def colorSpace(color, blocknum):
    for a in range(0, blocknum):
        if color == "black":
            print(" ", end='')
        elif color == "dark_g":
            print(DARK_G, end='')
        elif color == "light_g":
            print(LIGHT_G, end='')
        elif color == "white":
            print(WHITE, end='')
        elif color == "yellow":
            print(YELLOW, end='')
        elif color == "red":
            print(RED, end='')
        else:
            print(color, end='')

def tuxBody():
    print("")
    colorSpace("black", 52)
    colorSpace("dark_g", 3)
    colorSpace("white", 8)
    colorSpace("dark_g", 5)
    print("")
    colorSpace("black", 52)
    colorSpace("dark_g", 3)
    colorSpace("white", 9)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 51)
    colorSpace("dark_g", 4)
    colorSpace("white", 9)
    colorSpace("dark_g", 5)
    print("")
    colorSpace("black", 50)
    colorSpace("dark_g", 4)
    colorSpace("white", 3)
    colorSpace("light_g", 4)
    colorSpace("white", 4)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 50)
    colorSpace("dark_g", 4)
    colorSpace("white", 2)
    colorSpace("light_g", 6)
    colorSpace("white", 3)
    colorSpace("dark_g", 5)
    print("")
    colorSpace("black", 50)
    colorSpace("dark_g", 3)
    colorSpace("white", 2)
    colorSpace("light_g", 8)
    colorSpace("white", 2)
    colorSpace("dark_g", 5)
    print("")
    colorSpace("black", 49)
    colorSpace("dark_g", 4)
    colorSpace("white", 1)
    colorSpace("light_g", 10)
    colorSpace("white", 2)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 49)
    colorSpace("dark_g", 3)
    colorSpace("white", 2)
    colorSpace("light_g", 11)
    colorSpace("white", 1)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 49)
    colorSpace("dark_g", 4)
    colorSpace("light_g", 12)
    colorSpace("dark_g", 5)
    print("")
    colorSpace("black", 49)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 2)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 10)
    colorSpace("dark_g", 6)
    print("")
    colorSpace("black", 49)
    colorSpace("yellow", 4)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 9)
    colorSpace("yellow", 1)
    colorSpace("dark_g", 3)
    colorSpace("yellow", 2)
    print("")
    colorSpace("black", 48)
    colorSpace("yellow", 5)
    colorSpace("dark_g", 3)
    colorSpace("light_g", 8)
    colorSpace("yellow", 6)
    print("")
    colorSpace("black", 47)
    colorSpace("yellow", 7)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 8)
    colorSpace("yellow", 7)
    print("")
    colorSpace("black", 47)
    colorSpace("yellow", 7)
    colorSpace("dark_g", 1)
    colorSpace("light_g", 8)
    colorSpace("yellow", 8)
    print("")
    colorSpace("black", 47)
    colorSpace("yellow", 8)
    colorSpace("light_g", 8)
    colorSpace("yellow", 8)
    print("")
    colorSpace("black", 47)
    colorSpace("yellow", 9)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 3)
    colorSpace("dark_g", 2)
    colorSpace("yellow", 7)
    print("")
    colorSpace("black", 48)
    colorSpace("yellow", 8)
    colorSpace("dark_g", 7)
    colorSpace("yellow", 5)
    print("")
    colorSpace("black", 50)
    colorSpace("yellow", 6)
    colorSpace("dark_g", 1)
    colorSpace("black", 5)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 4)
    print("")
    colorSpace("black", 52)
    colorSpace("yellow", 3)
    colorSpace("black", 8)
    colorSpace("yellow", 3)
    print(white)
def tuxTopHead():
    os.system('cls' if os.name == 'nt' else 'clear')

    colorSpace("black", 56)
    colorSpace("dark_g", 7)
    print("")
    for a in range(0, 2):
        colorSpace("black", 55)
        colorSpace("dark_g", 9)
        print("")
    colorSpace("black", 55)
    colorSpace("dark_g", 10)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 11)
    print("")
def lookStraight():
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
def lookLeft():
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("black", 1)
    colorSpace("white", 2)
    colorSpace("dark_g", 1)
    colorSpace("black", 1)
    colorSpace("white", 2)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("black", 1)
    colorSpace("white", 2)
    colorSpace("yellow", 1)
    colorSpace("black", 1)
    colorSpace("white", 2)
    colorSpace("dark_g", 3)
    print("")
def lookLeftDown():
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 3)
    colorSpace("dark_g", 1)
    colorSpace("white", 3)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("black", 1)
    colorSpace("white", 2)
    colorSpace("yellow", 1)
    colorSpace("black", 1)
    colorSpace("white", 2)
    colorSpace("dark_g", 3)
    print("")
def lookRight():
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 2)
    colorSpace("black", 1)
    colorSpace("dark_g", 1)
    colorSpace("white", 2)
    colorSpace("black", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 2)
    colorSpace("black", 1)
    colorSpace("yellow", 1)
    colorSpace("white", 2)
    colorSpace("black", 1)
    colorSpace("dark_g", 3)
    print("")
def lookRightDown():
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 3)
    colorSpace("dark_g", 1)
    colorSpace("white", 3)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 2)
    colorSpace("black", 1)
    colorSpace("yellow", 1)
    colorSpace("white", 2)
    colorSpace("black", 1)
    colorSpace("dark_g", 3)
    print("")
def lookCheck(look):
    if look == "":
        lookStraight()
    elif look == "L":
        lookLeft()
    elif look == "LD":
        lookLeftDown()
    elif look == "R":
        lookRight()
    elif look == "RD":
        lookRightDown()

def tux(text, look):
    tuxTopHead()
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    colorSpace("white", 1)
    colorSpace("dark_g", 4)
    print("")

    lookCheck(look)

    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 7)
    colorSpace("dark_g", 3)
    
    # Text
    print('\033[97m' + "    " + text,end='')
    
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("white", 1)
    colorSpace("yellow", 3)
    colorSpace("white", 2)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 53)
    colorSpace("dark_g", 3)
    colorSpace("white", 7)
    colorSpace("dark_g", 4)
    tuxBody()
def tuxMouthOpen(text, look):
    tuxTopHead()
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    colorSpace("white", 1)
    colorSpace("dark_g", 4)
    print("")

    lookCheck(look)

    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 7)
    colorSpace("dark_g", 3)   
    # Text
    print('\033[97m' + "    " + text,end='')
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("yellow", 1)
    colorSpace("black", 3)
    colorSpace("yellow", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("yellow", 2)
    colorSpace("black", 1)
    colorSpace("yellow", 2)
    colorSpace("white", 1)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 53)
    colorSpace("dark_g", 3)
    colorSpace("white", 1)
    colorSpace("yellow", 3)
    colorSpace("white", 3)
    colorSpace("dark_g", 4)
    tuxBody()
def tuxAnnoyed1(text):
    os.system('cls' if os.name == 'nt' else 'clear')

    print("")
    colorSpace("black", 56)
    colorSpace("dark_g", 7)
    print("")
    for a in range(0, 2):
        colorSpace("black", 55)
        colorSpace("dark_g", 9)
        print("")
    colorSpace("black", 55)
    colorSpace("dark_g", 10)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 11)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 11)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 7)
    colorSpace("dark_g", 3)
    
    # Text
    print('\033[97m' + "    " + text,end='')
    
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("white", 1)
    colorSpace("yellow", 3)
    colorSpace("white", 2)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 53)
    colorSpace("dark_g", 3)
    colorSpace("white", 7)
    colorSpace("dark_g", 4)
    tuxBody()
def tuxAnnoyed2(text):
    os.system('cls' if os.name == 'nt' else 'clear')

    for a in range(0, 8):
        print("")
    colorSpace("black", 56)
    colorSpace("dark_g", 7)
    print("")
    colorSpace("black", 55)
    colorSpace("dark_g", 10)
    
    # Text
    print('\033[97m' + "    " + text,end='')
    
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 7)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 53)
    colorSpace("dark_g", 3)
    colorSpace("white", 7)
    colorSpace("dark_g", 4)
    tuxBody()
def tuxAngry1(text):
    tuxTopHead()
    colorSpace("black", 54)
    colorSpace("dark_g", 11)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("dark_g", 3)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 7)
    colorSpace("dark_g", 3)
    
    # Text
    print('\033[97m' + "    " + text,end='')
    
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("white", 1)
    colorSpace("yellow", 3)
    colorSpace("white", 2)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 53)
    colorSpace("dark_g", 3)
    colorSpace("white", 7)
    colorSpace("dark_g", 4)
    tuxBody()
def tuxAngry2(text):
    os.system('cls' if os.name == 'nt' else 'clear')

    colorSpace("black", 56)
    colorSpace("dark_g", 7)
    print("")
    for a in range(0, 2):
        colorSpace("black", 55)
        colorSpace("dark_g", 9)
        print("")
    colorSpace("black", 55)
    colorSpace("dark_g", 10)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("red", 2)
    colorSpace("dark_g", 3)
    colorSpace("red", 2)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("red", 2)
    colorSpace("dark_g", 1)
    colorSpace("red", 2)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("red", 3)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 1)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 7)
    colorSpace("dark_g", 3)
    
    # Text
    print('\033[97m' + "    " + text,end='')
    
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("white", 1)
    colorSpace("yellow", 3)
    colorSpace("white", 2)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 53)
    colorSpace("dark_g", 3)
    colorSpace("white", 7)
    colorSpace("dark_g", 4)
    tuxBody()
def tuxSpeechless(text):
    tuxTopHead()
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    colorSpace("white", 1)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 2)
    colorSpace("dark_g", 1)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("black", 2)
    colorSpace("yellow", 1)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 5)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 7)
    colorSpace("dark_g", 3)
    
    # Text
    print('\033[97m' + "    " + text,end='')
    
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    #colorSpace("yellow", 1)
    colorSpace("black", 5)
    #colorSpace("yellow", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 3)
    print("")
    colorSpace("black", 54)
    colorSpace("dark_g", 2)
    colorSpace("white", 1)
    colorSpace("yellow", 3)
    colorSpace("white", 2)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 53)
    colorSpace("dark_g", 3)
    colorSpace("white", 7)
    colorSpace("dark_g", 4)
    tuxBody()
def tuxClose(text):
    os.system('cls' if os.name == 'nt' else 'clear')

    colorSpace("black", 42)
    colorSpace("dark_g", 17)
    colorSpace("light_g", 2)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 41)
    colorSpace("dark_g", 17)
    colorSpace("light_g", 1)
    colorSpace("white", 1)
    colorSpace("light_g", 2)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 41)
    colorSpace("dark_g", 17)
    colorSpace("light_g", 3)
    colorSpace("dark_g", 6)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 27)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 28)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 28)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 28)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 29)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 30)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 5)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 11)
    colorSpace("light_g", 2)
    colorSpace("dark_g", 11)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 4)
    colorSpace("light_g", 3)
    colorSpace("dark_g", 9)
    colorSpace("light_g", 5)
    colorSpace("dark_g", 9)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 3)
    colorSpace("light_g", 5)
    colorSpace("dark_g", 7)
    colorSpace("light_g", 2)
    colorSpace("white", 3)
    colorSpace("light_g", 2)
    colorSpace("dark_g", 8)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 3)
    colorSpace("light_g", 1)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("white", 2)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 5)
    colorSpace("light_g", 1)
    colorSpace("white", 2)
    colorSpace("light_g", 3)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 8)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 1)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("black", 1)
    colorSpace("light_g", 1)
    colorSpace("white", 2)
    colorSpace("dark_g", 5)
    colorSpace("white", 2)
    colorSpace("light_g", 1)
    colorSpace("black", 3)
    colorSpace("light_g", 1)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 8)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 2)
    colorSpace("black", 3)
    colorSpace("light_g", 1)
    colorSpace("white", 1)
    colorSpace("dark_g", 5)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("black", 5)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 8)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 2)
    colorSpace("black", 4)
    colorSpace("white", 1)
    colorSpace("dark_g", 5)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("black", 5)
    colorSpace("white", 2)
    colorSpace("dark_g", 8)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 2)
    colorSpace("black", 4)
    colorSpace("light_g", 1)
    colorSpace("yellow", 4)
    colorSpace("dark_g", 1)
    colorSpace("light_g", 2)
    colorSpace("black", 5)
    colorSpace("white", 2)
    colorSpace("dark_g", 8)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 3)
    colorSpace("white", 1)
    colorSpace("black", 3)
    colorSpace("yellow", 8)
    colorSpace("light_g", 1)
    colorSpace("black", 5)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 8)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 3)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("light_g", 1)
    colorSpace("yellow", 12)
    colorSpace("black", 2)
    colorSpace("white", 2)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 8)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 3)
    colorSpace("light_g", 1)
    colorSpace("white", 1)
    colorSpace("yellow", 15)
    colorSpace("light_g", 2)
    colorSpace("dark_g", 9)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 4)
    colorSpace("yellow", 19)
    colorSpace("dark_g", 8)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 3)
    colorSpace("yellow", 21)
    colorSpace("dark_g", 7)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 17)
    colorSpace("black", 2)
    colorSpace("yellow", 3)
    colorSpace("dark_g", 8)

    # Text
    print('\033[97m' + "    " + text,end='')

    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 1)
    colorSpace("yellow", 16)
    colorSpace("black", 2)
    colorSpace("yellow", 3)
    colorSpace("dark_g", 9)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 2)
    colorSpace("yellow", 13)
    colorSpace("black", 3)
    colorSpace("yellow", 4)
    colorSpace("dark_g", 9)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 2)
    colorSpace("yellow", 12)
    colorSpace("black", 2)
    colorSpace("yellow", 5)
    colorSpace("dark_g", 4)
    colorSpace("light_g", 2)
    colorSpace("dark_g", 5)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 1)
    colorSpace("yellow", 2)
    colorSpace("black", 2)
    colorSpace("yellow", 4)
    colorSpace("black", 4)
    colorSpace("yellow", 5)
    colorSpace("light_g", 2)
    colorSpace("dark_g", 4)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 2)
    colorSpace("yellow", 3)
    colorSpace("black", 5)
    colorSpace("yellow", 6)
    colorSpace("light_g", 4)
    colorSpace("dark_g", 4)
    colorSpace("light_g", 1)
    colorSpace("white", 1)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 2)
    colorSpace("light_g", 3)
    colorSpace("yellow", 12)
    colorSpace("light_g", 6)
    colorSpace("dark_g", 4)
    colorSpace("light_g", 2)
    colorSpace("dark_g", 4)
    print("")
    colorSpace("black", 40)
    colorSpace("dark_g", 2)
    colorSpace("white", 1)
    colorSpace("light_g", 3)
    colorSpace("yellow", 9)
    colorSpace("light_g", 5)
    colorSpace("white", 2)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 11)
    print("")
    colorSpace("black", 39)
    colorSpace("dark_g", 3)
    colorSpace("white", 2)
    colorSpace("light_g", 4)
    colorSpace("yellow", 5)
    colorSpace("light_g", 5)
    colorSpace("white", 5)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 10)
    print("")
    colorSpace("black", 38)
    colorSpace("dark_g", 4)
    colorSpace("white", 3)
    colorSpace("light_g", 12)
    colorSpace("white", 6)
    colorSpace("light_g", 1)
    colorSpace("dark_g", 11)
    print(white)

def larkBoot():
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(.05)
    colorSpace("black", 54)
    colorSpace("white", 12)
    print("")
    time.sleep(.05)
    colorSpace("black", 52)
    colorSpace("white", 3)
    colorSpace("black", 10)
    colorSpace("white", 2)
    print("")
    time.sleep(.05)
    colorSpace("black", 50)
    colorSpace("white", 3)
    colorSpace("black", 13)
    colorSpace("white", 2)
    print("")
    time.sleep(.05)
    colorSpace("black", 49)
    colorSpace("white", 2)
    colorSpace("black", 16)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 2)
    colorSpace("black", 17)
    colorSpace("white", 2)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 2)
    colorSpace("white", 3)
    colorSpace("black", 9)
    colorSpace("white", 3)
    colorSpace("black", 2)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 5)
    colorSpace("black", 7)
    colorSpace("white", 5)
    colorSpace("black", 1)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 5)
    colorSpace("black", 7)
    colorSpace("white", 5)
    colorSpace("black", 1)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 2)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("black", 7)
    colorSpace("white", 2)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 2)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("black", 7)
    colorSpace("white", 2)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("black", 11)
    colorSpace("white", 1)
    colorSpace("black", 4)
    colorSpace("white", 1)
    print("")
    time.sleep(1)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 9)
    colorSpace("yellow", 2)
    colorSpace("black", 8)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 8)
    colorSpace("yellow", 4)
    colorSpace("black", 7)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 7)
    colorSpace("yellow", 6)
    colorSpace("black", 6)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 6)
    colorSpace("yellow", 8)
    colorSpace("black", 5)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 5)
    colorSpace("yellow", 8)
    colorSpace("black", 6)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 8)
    colorSpace("yellow", 3)
    colorSpace("black", 3)
    colorSpace("yellow", 1)
    colorSpace("black", 4)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 5)
    colorSpace("yellow", 2)
    colorSpace("black", 5)
    colorSpace("yellow", 2)
    colorSpace("black", 5)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 6)
    colorSpace("yellow", 7)
    colorSpace("black", 6)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 7)
    colorSpace("yellow", 5)
    colorSpace("black", 7)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 8)
    colorSpace("yellow", 2)
    colorSpace("black", 9)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 19)
    colorSpace("white", 1)
    print("")
    time.sleep(.05)
    colorSpace("black", 48)
    colorSpace("white", 1)
    colorSpace("black", 19)
    colorSpace("white", 1)
    print("")
    print("")
    time.sleep(2)
    colorSpace("black", 38)
    colorSpace("white", 1)
    colorSpace("black", 13)
    colorSpace("white", 3)
    colorSpace("black", 7)
    colorSpace("white", 1)
    colorSpace("black", 9)
    colorSpace("white", 1)
    colorSpace("black", 5)
    colorSpace("white", 1)
    print("")
    time.sleep(.2)
    colorSpace("black", 38)
    colorSpace("white", 1)
    colorSpace("black", 12)
    colorSpace("white", 2)
    colorSpace("black", 1)
    colorSpace("white", 1)
    colorSpace("black", 7)
    colorSpace("white", 7)
    colorSpace("black", 3)
    colorSpace("white", 1)
    colorSpace("black", 3)
    colorSpace("white", 2)
    print("")
    time.sleep(.2)
    colorSpace("black", 38)
    colorSpace("white", 1)
    colorSpace("black", 11)
    colorSpace("white", 2)
    colorSpace("black", 2)
    colorSpace("white", 2)
    colorSpace("black", 6)
    colorSpace("white", 2)
    colorSpace("black", 4)
    colorSpace("white", 2)
    colorSpace("black", 2)
    colorSpace("white", 4)
    print("")
    time.sleep(.2)
    colorSpace("black", 38)
    colorSpace("white", 1)
    colorSpace("black", 10)
    colorSpace("white", 2)
    colorSpace("black", 4)
    colorSpace("white", 2)
    colorSpace("black", 5)
    colorSpace("white", 8)
    colorSpace("black", 2)
    colorSpace("white", 2)
    print("")
    time.sleep(.2)
    colorSpace("black", 38)
    colorSpace("white", 1)
    colorSpace("black", 10)
    colorSpace("white", 1)
    colorSpace("black", 2)
    colorSpace("white", 6)
    colorSpace("black", 4)
    colorSpace("white", 2)
    colorSpace("black", 3)
    colorSpace("white", 2)
    colorSpace("black", 3)
    colorSpace("white", 2)
    print("")
    time.sleep(.2)
    colorSpace("black", 38)
    colorSpace("white", 1)
    colorSpace("black", 9)
    colorSpace("white", 7)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("black", 4)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 2)
    colorSpace("black", 6)
    colorSpace("white", 1)
    colorSpace("black", 1)
    colorSpace("white", 1)
    print("")
    time.sleep(.2)
    colorSpace("black", 38)
    colorSpace("white", 1)
    colorSpace("black", 8)
    colorSpace("white", 2)
    colorSpace("black", 8)
    colorSpace("white", 2)
    colorSpace("black", 3)
    colorSpace("white", 1)
    colorSpace("black", 2)
    colorSpace("white", 2)
    colorSpace("black", 5)
    colorSpace("white", 1)
    colorSpace("black", 2)
    colorSpace("white", 2)
    print("")
    time.sleep(.2)
    colorSpace("black", 38)
    colorSpace("white", 7)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("black", 10)
    colorSpace("white", 2)
    colorSpace("black", 2)
    colorSpace("white", 1)
    colorSpace("black", 3)
    colorSpace("white", 3)
    colorSpace("black", 3)
    colorSpace("white", 1)
    colorSpace("black", 3)
    colorSpace("white", 2)
    print(white)
    time.sleep(2)

