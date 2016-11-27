#!/usr/bin/env python

'''
Setting up your new Ubuntu server (Ubuntu 16 preferred)
'''
import subprocess
import sys
import os

#List commands to execute.

#Server setup
UPDATE ="sudo apt-get update"
GIT = "sudo apt-get install git"
CLONE_REPO = "git clone https://github.com/jmmnn/classifier.git"

#######  Python stuff
CONDA_GET = "wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh"
CONDA_INSTALL = "bash ~/miniconda.sh"
CONDA_ENV = "conda create --name classifier scikit-learn lxml"
CONDA_ACTIVATE = "source activate classifier"

#FIRST list of commands in sequence ## Uncomment these for 1st install
cmds = [
    UPDATE,
    GIT,
    CONDA_GET,
    CONDA_INSTALL,
    CONDA_ENV,    
    CLONE_REPO
    ]

dir = os.getcwd()


###### Iterates over the FIRST list of commands
count=0
for cmd in cmds:
    count+=1
    print ("____Running Command Number : ",count , " $" , cmd)
    subprocess.call(cmd, shell=True)
    print ("____Finished Running Command: $" , cmd)
