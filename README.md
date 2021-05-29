# python-calculator
A basic terminal calculator in python that uses the `eval()` function with user input for its main usage. 

Though there are lots of GUI calculators for \*NIX systems, many of them are either so feature packed that they become annoying to use for basic use, or are just impractical to use. Thus, I wanted to create a calculator in python that could be used from the terminal but also make sure that it was hackable and not bloated. 

To add more functionality into the calculator, simply import more functions from the `math` module at the beginning of the `main.py` file. For example, the default functions available are imported as: 

```python 
from math import sin, cos, tan, asin, acos, atan, sqrt, pi
```

But, if you wanted to add, say, the `ceil` function, simply append it to the end of the first line with a comma, like so: 

```python
from math import sin, cos, tan, asin, acos, atan, sqrt, pi, ceil
```

This non-bloated and suckless approach to adding more functionality makes for more practicality of the calculator. 

## Basic Usage

The default functions included are sine, cosine, tangent, inverse sine, inverse cosine, inverse tangent, square root, and pi. They are referred to in the calculator with the following names: 

```
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
                         pi:   pi
```

At anytime, you can type `help` into the calculator to get a list of these function names. To exit the calculator, type `exit` or `q`. 

## Installation

There is an installation script provided that automatically adds the program to `$PATH` for all users, so it is a very easy installation. To install, use the following commands: 
```sh 
git clone https://github.com/naowalrahman/python-calculator.github
cd python-calculator 
sudo sh ./install.sh 
```

## Contributions 
Any contributions are welcome! If any issue arises, make an issue in the issues tab. If you want to contribute to this calculator, feel free to start a pull request! 
