#!/bin/sh

sudo rm /usr/bin/calc

cd /tmp 
git clone https://github.com/naowalrahman/python-calculator.git

cd /tmp/python-calculator

sudo cp main.py /usr/bin/calc
sudo chmod +x /usr/bin/calc

sudo rm -rf /tmp/python-calculator

echo "Done updating! No error reported."

exit