#!/usr/bin/env python
import os
import sys

main_path = os.getcwd()

args_beta = sys.argv
args_real = [] 
i = 0

while i < len(args_beta):
    if i != 0:
        args_real.append(args_beta[i])
    i += 1

"""
    if args:
    0... - path to auto create
"""

if args_real:
    for item in range(len(args_real)):
        os.system("mkdir " + args_real[item])
    os.system("npm init -y")
    os.system("npm install --save")

else:
    os.system("npm init -y")
    os.system("npm install --save")