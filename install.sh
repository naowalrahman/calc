#!/usr/bin/sh

cp main.py /usr/bin/calc
chmod +x /usr/bin/calc

cp calc-update.sh /usr/bin/calc-update
chmod +x /usr/bin/calc-update

echo "Installation finished with no error. Reopen your terminal and use the 'calc' command to start using the calculator!"
echo "To update the program, run 'calc-update,' and that's all!"
echo " " 
