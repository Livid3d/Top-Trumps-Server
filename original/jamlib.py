'''
jamlib.py By James Robinson
Copyright James Robinson 2018 - 2019
All rights reserved

Libary not ment to be ran on its own
V1.1
'''
import random

def whoami():
    print ("The James Liabry V 1.1")

# Classes ====================================================

class ProgressBar():
    def __init__(self, width=50):
        self.pointer = 0
        self.width = width

    def __call__(self,percent):
         # x in percent
         self.pointer = int(self.width*(percent/100.0))
         return "|" + "#"*self.pointer + "-"*(self.width-self.pointer)+\
                "|\n %d percent done" % int(percent)

# Functions ==================================================

def integer_input(message="Enter a number: "):
    while True:
        try:
            usrInput = int(input(message))
        except:
            print("\nERROR: Provide an integer")

        else:
            break

    return usrInput


def string_input(message="Enter a string: "):
    while True:
        try:
            usrInput = str(input(message))
        except:
            print("\nERROR: Provide a string")

        else:
            break

    return usrInput


def float_input(message="Enter a number: "):
    while True:
        try:
            usrinput = float(input(message))
        except:
            print("\nERROR: Provide a float.")

        else:
            break

    return usrinput

def spacer():
    print("\n", "=" * 50, "\n")

def print_file(file_name):
    with open("Assets//{}.txt".format(file_name), mode="r", encoding='utf8') as file_text:
        print(file_text.read())

def rand_from_file(file_name):
    return (random.choice(list(open("Assets//{}".format(file_name)))))[:-1]

def reset():
    print("\n"*100, "="*20, "RESET", "="*20)

