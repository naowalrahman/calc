# Calc
A basic terminal calculator in python that uses the `eval()` function with user input for its main usage. 

Though there are lots of GUI calculators for \*NIX systems, many of them are either so feature packed that they become annoying to use for basic use, or are just impractical to use. Thus, I wanted to create a calculator in python that could be used from the terminal but also make sure that it was user-friendly and minimal.

For now, the ability to add your own math functions from the python `math` module has been removed because of the increasing complexity and adding of features to the program. However, in the future, I will add a very minimal calculator that can be added to and hack easily, and then a more current and actively developed featureful version that can't be as easily hacked up. 

The calculator depends on the matplotlib module for graphing, and the sympy module for solving algebraic equations. As of now, graphing is limited to 3 specific types of equations, and cannot yet dynamically recognize equations. However, I want to add this in the feature. As for algebra, calc can solve univariate algebraic equations, but cannot solve ones with trigonometric or logarithmic or any other function-based equations. Essentially, it works with an equation like `2*x + 1 = 11`, but doesn't work with something like `sin(x) = 25`. Again, this is all something that I would like to implement in the future. 

## Basic Usage

The default functions included are sine, cosine, tangent, inverse sine, inverse cosine, inverse tangent, square root, and pi. The default trigonometry functions are calculated in degrees. However, if you wish to use radians, there are trigonmetric functions available starting with r and then the function name that calculate values in radians (like `rsin` or `artan`). The inverse functions in radians start with ar and then the function name. As for graphing and univariate algebra, equations can be graphed with the prefix `graph` and solved with `eq`. This is the reference list for the names of the functions:

|**Function name**|**Function reference**|
|-----------------|----------------------|
|Add|+|
|Subtract|-|
|Multiply|*|
|Divide|/|
|Exponent|**|
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
|Graph an equation|graph|
|Solve algebraic equation|eq|

At anytime, you can type `help` into the calculator to get a list of these function names. To exit the calculator, type `exit` or `q`. To clear the screen, type `clear`. 

## Installation

### Unix/Linux/MacOS

There is an installation script provided that automatically adds the program to `$PATH` for all users, so it is a very easy installation. To install, use the following commands: 
```sh 
sudo pip install matplotlib && sudo pip install sympy
git clone https://github.com/naowalrahman/python-calculator.git
cd python-calculator 
sudo sh ./install.sh 
```

### Windows

There is a .exe binary file availability in the releases section that can be downloaded and run on Windows operating systems, but as of now there is no update functionality. However, if you run WSL on Windows 10, you can install calc on WSL just like you would on normal Linux system with the commands above. 

To update the calculator simply run `calc-update` in your  terminal. To uninstall the calculator, run the `uninstall.sh` file from the cloned git repository with the command `sudo sh ./uninstall.sh`. 

## Contributions 
Any contributions are welcome! If any issue arises, make an issue in the issues tab. If you want to contribute to this calculator, feel free to start a pull request! 

## To Do
- [X] Put algebra support into the calculator. 
- [X] Make the calculator ignore python-specific functions and expressions and only recognize math expressions. 
- [X] Make uninstall script. 
- [ ] Make two different versions of the calculator - one minimal edition and another feature edition. 
- [ ] Make the `eq` function solve algebraic equations with specific functions that are otherwise avaiable in the calculator. 
- [ ] Have dynamic graphing capability in the `graph` function. 