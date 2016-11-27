#!/usr/bin/env python

'''
Setting up your new Ubuntu server (Ubuntu 16 preferred)
'''
import subprocess
import sys
import os

#List commands to execute.

#######  Python stuff
ENV_CREATE = "conda create --name classifier scikit-learn"

#FIRST list of commands in sequence ## Uncomment these for 1st install
cmds = [
    ENV_CREATE
    ]

dir = os.getcwd()


###### Iterates over the FIRST list of commands
count=0
for cmd in cmds:
    count+=1
    print ("____Running Command Number : ",count , " $" , cmd)
    subprocess.call(cmd, shell=True)
    print ("____Finished Running Command: $" , cmd)
