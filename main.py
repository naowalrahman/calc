#!/usr/bin/python 

########## USER IMPORTS ##########
from math import radians, degrees, sqrt, pi

########## CALCULATOR IMPORTS (DO NOT CHANGE) ##########
import math
import os
from math import sin as rsin 
from math import cos as rcos 
from math import tan as rtan
from math import asin as arsin
from math import acos as arcos
from math import atan as artan


print("Input something to get started with the calculator. For default functions and operations, type help. To exit, type exit or q.\n")

def sin(inp):
    return math.sin(radians(inp))

def cos(inp): 
    return math.cos(radians(inp))

def tan(inp): 
    return math.tan(radians(inp))

def asin(inp):
    return degrees(math.asin(inp))

def acos(inp): 
    return degrees(math.acos(inp))
    
def atan(inp): 
    return degrees(math.atan(inp))

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
             sine (degrees):   sin()
           cosine (degrees):   cos()
          tangent (degrees):   tan()
     inverse sine (degrees):   asin()
   inverse cosine (degrees):   acos()
  inverse tangent (degrees):   atan()
              sine (radian):   rsin()
            cosine (radian):   rcos()
           tangent (radian):   rtan()
      inverse sine (radian):   arsin()
    inverse cosine (radian):   arcos()
   inverse tangent (radian):   artan()
                square root:   sqrt() 
                         pi:   pi""") 
        elif user_input == "clear":
            os.system("cls" if os.name == "nt" else "clear")
        else: 
            print(calc(user_input))
    except: 
        print("invalid input\n")
