#!/usr/bin/python 

from math import sin, cos, tan, asin, acos, atan, sqrt, pi
import sys

print("Input something to get started with the calculator. For default functions and operations, type help. To exit, type exit or q.\n")

def calc(user_input):
    return str(eval(user_input)) + "\n"

while True: 
    user_input = input()
    try:
        if user_input == "exit" or user_input == "q":
            print("Exited calculator.")
            break
        elif user_input == "help": 
            print("""Default functions and operations:
                        add:   + 
                   subtract:   - 
                   multiply:   *
                     divide:   /
                   exponent:   **
                       sine:   sin()
                     cosine:   cos()
                    tangent:   tan()
               inverse sine:   asin()
             inverse cosine:   acos()
            inverse tangent:   atan()
                square root:   sqrt() 
                         pi:   pi""") 

        else: 
            print(calc(user_input))
    except: 
        print("invalid input\n")
