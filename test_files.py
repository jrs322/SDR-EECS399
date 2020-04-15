# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:13:35 2020

@author: Derek Clontz
"""

import os

#Prints a list of files and folders in a given directory
with os.scandir('Directory path goes here...') as entries:
    for entry in entries:
        print(entry.name)

    
#Checks to see if a given path leads to a file or a directory
path="Directory path goes here..."  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()