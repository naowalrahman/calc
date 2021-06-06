# Calc - Python Calculator

![Calculator showcase in terminal](/showcase.gif)

Calc is a basic terminal-based calculator in python that uses the `eval()` function with user input for its main usage. 

Though there are lots of GUI calculators for \*NIX systems, many of them are either so feature packed that they become annoying to use for basic use, or are just impractical to use. Thus, I wanted to create a calculator in python that could be used from the terminal but also make sure that it was hackable and not bloated. 

It is simple to use, easy to hack, and very fast. 

## Installation

There is an installation script provided that automatically adds the program to `$PATH` for all users, so it is a very easy installation. To install, use the following commands: 
```sh 
git clone https://github.com/naowalrahman/python-calculator.git
cd python-calculator 
sudo sh ./install.sh 
```

To update the calculator simply run `calc-update` in your  terminal. To uninstall the calculator, run the `uninstall.sh` file from the cloned git repository with the command `sudo sh ./uninstall.sh`. 

## Basic Usage

The default functions included are sine, cosine, tangent, inverse sine, inverse cosine, inverse tangent, square root, and pi. The default trigonometry functions are calculated in degrees. However, if you wish to use radians, there are trigonmetric functions available starting with r and then the function name that calculate values in radians (like `rsin` or `artan`). The inverse functions in radians start with ar and then the function name. This is the reference list for the names of the functions:

|**Function name**|**Function reference**|
|-----------------|----------------------|
|Add|+|
|Subtract|-|
|Multiply|*|
|Divide|/|
|Exponent|\**|
|Sine (degrees)|sin()|
|Cosine (degrees)|cos()|
|Tangent (degrees)|tan()|
|Inverse sine (degrees)|asin()|
|Inverse cosine (degrees)|acos()|
|Inverse tangent (degrees)|atan()|
|Sine (radians)|rsin()|
|Cosine (radians)|rcos()|
|Tangent (radians)|rtan()|
|Inverse sine (radians)|arsin()|
|Inverse cosine (radians)|arcos()|
|Inverse tangent (radians)|artan()|
|Square root|sqrt()|
|Pi|pi|

At anytime, you can type `help` into the calculator to get a list of these function names. To exit the calculator, type `exit` or `q`. To clear the screen, type `clear`. 

## Adding More Functionality

To add more functionality into the calculator, simply import more functions from the `math` module at the beginning of the `main.py` file. For example, the default functions available are imported as: 

```python 
########## USER IMPORTS ##########
from math import radians, degrees, sqrt, pi
```

But, if you wanted to add, say, the `ceil` function, simply append it to the end of the first line with a comma, like so: 

```python
########## USER IMPORTS ##########
from math import radians, degrees, sqrt, pi, ceil
```

This non-bloated and suckless approach to adding more functionality makes for more practicality of the calculator. However, the other import functions after the user imports should be modified as they are designed to be used for the custom functions defined later on, which are used for degree-based trigonometry. 

## To Do
This project is in active development, and these are some of the things I'd like and want to implement in the future:
- [X] Make an uninstall script.
- [ ] Make two different versions of the calculator - one minimal edition and another feature edition. 
- [ ] Put algebra support into the calculator. 
- [ ] Make the calculator ignore python-specific functions and expressions and only recognize math expressions. 

## Contributions 
Any contributions are welcome! If any issue arises, make an issue on this project's [GitHub page](https://github.com/naowalrahman/calc/issues). If you want to contribute to this calculator, feel free to start a pull request on GitHub! 
