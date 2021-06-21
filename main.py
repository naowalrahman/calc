#!/usr/bin/python

########## CALCULATOR IMPORTS (DO NOT CHANGE) ##########
from math import radians, degrees, sqrt, pi
import math
import os
import matplotlib.pyplot as plt
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
from sympy.solvers import solve
from sympy import Eq, Symbol
from math import sin as rsin
from math import cos as rcos
from math import tan as rtan
from math import asin as arsin
from math import acos as arcos
from math import atan as artan


print("Input something to get started with the calculator. For default functions and operations, type help. To exit, type exit or q.\n")

########## TRIGONOMETRY FUNCTIONS ##########

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


########### EXPRESSION EVALUATION ##########

parse_expr_dict = {"sin": sin, "cos": cos, "tan": tan, "asin": asin, "acos": acos, "atan": atan, "sqrt": sqrt, "pi": pi, "rsin": rsin, "rcos": rcos, "rtan": rtan, "arsin": arsin, "arcos": arcos, "artan": artan}

def calc(user_input):
    # use sympy parse_expr to safely evaluate math expression
    global parse_expr_dict
    if os.name == "nt":
        return "\n{0} = ( ".format(user_input) + str(float(parse_expr(user_input, local_dict=parse_expr_dict))) + " )\n\n"
    else: 
        return "\n{0} = ( \033[1m".format(user_input) + str(float(parse_expr(user_input, local_dict=parse_expr_dict))) + "\033[0m )\n\n"


def graph():
    # use matplotlib to grpah different types of equations
    graph_range = input("Range of graph: ")
    try:
        graph_range = int(graph_range)
        x = np.array(range(graph_range))
    except: 
        graph_range = graph_range.split()
        x = np.array(range(int(graph_range[0]), int(graph_range[1])))

    print("""Choose an equation type: 
    1) Linear (y = mx + b)
    2) Quadratic (y = ax^2 + bx + c)
    3) Exponential (y = a * b^x)
    """)
    eq_type = input()

    if eq_type == "1":
        print("equation y = mx + b")
        m = float(input('m = '))
        b = float(input('b = ')) 
        print("\n")
        plt.title("Linear Equation")
        y = m * x + b

    elif eq_type == "2": 
        print("equation type: y = ax^2 + bx + c")
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        print("\n")
        plt.title("Quadratic Equation")
        y = a*x**2 + b*x + c
    
    elif eq_type == "3":
        print("equation type: y = a * b^x")
        a = float(input("a = "))
        b = float(input("b = "))
        print("\n")
        plt.title("Exponential Equation")
        y = a * b**x

    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x, y)
    plt.show()


def algebra_solver(inp):
    x = Symbol("x")
    evaluation = inp.replace(" ", "").split("=")
    if os.name == "nt": 
        res = "\n{0} -> ( ".format(inp) + str(solve(Eq(eval(evaluation[0]), eval(evaluation[1])))) + " )\n\n"
    else:
        res = "\n{0} -> ( \033[1m".format(inp) + str(solve(Eq(eval(evaluation[0]), eval(evaluation[1])))) + "\033[0m )\n\n"
    return res
    

########## EXPRESSION DRIVERS ##########

while True:
    user_input = input()
    try:
        if user_input == "exit" or user_input == "q":
            print("Exited calculator.")
            break

        elif user_input == "graph":
            graph()

        elif "eq" in user_input: 
            user_input = user_input[3:]
            print(algebra_solver(user_input))

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
                         pi:   pi
             graph equation:   graph
     solve algebra equation:   eq""")

        elif user_input == "clear":
            os.system("cls" if os.name == "nt" else "clear")

        else:
            print(calc(user_input))
    except:
        print("invalid input\n\n")
