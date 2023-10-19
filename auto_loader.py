'''
This code allows you to automatically download the necessary libraries 
through the Python programming language's PIP package manager. 
The list of required libraries is given in the file "requirements.txt". 
This code is intended for fast and automatic deployment of already existing 
program code on a new device, automating the process of downloading 
the necessary libraries through the PIP package manager. 
'''

import os

def install(package, i):
    print(f'{i}. Install {package}')
    #os.system(f"pip install {package}")

def loader_start():
    with open('requirements.txt', 'r') as f:
        print('The automatic installer will install now the following packages:')
        
        i = 1 # This variable is used as a counter to count the number of installed libraries, ignore it
        
        for line in f:
            install(line, i)
            i += 1
        
        print(f'\n{i - 1} libraries were installed')
