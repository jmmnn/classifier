#!/usr/bin/env python

'''
Setting up your new Ubuntu server (Ubuntu 16 preferred)
'''
import subprocess
import sys
import os
#get current directory
dir = os.getcwd()

#List commands to execute.

#Server setup
UPDATE ="sudo apt-get update"
GIT = "sudo apt-get install git"
CLONE_REPO = "git clone https://github.com/jmmnn/classifier.git"

#######  Python stuff
CONDA_ENV = "conda create --name classifier scikit-learn lxml"
CONDA_ACTIVATE = "source activate classifier"

#FIRST list of commands in sequence ## Uncomment these for 1st install
cmds = [
    CONDA_ENV
    ]

#SECOND list of commands in sequence ## Uncomment these for 1st install
cmds2 = [
    CONDA_ACTIVATE
    ]


###### Iterates over the FIRST list of commands
count=0
for cmd in cmds:
    count+=1
    print ("____Running Command Number : ",count , " $" , cmd)
    subprocess.call(cmd, shell=True)
    print ("____Finished Running Command: $" , cmd)

###### Iterates over the SECOND list of commands
count2=0
for cmd in cmds2:
    count2+=1
    print ("____Running Command Number : ",count2 , " $" , cmd)
    subprocess.call(cmd, shell=True)
    print ("____Finished Running Command: $" , cmd)
