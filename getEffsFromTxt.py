#!/usr/bin/env python
# encoding: utf-8
"""
getEffsFromTxt.py

Created by Chris Lucas on 2012-10-10.
Copyright (c) 2012 University of Bristol. All rights reserved.
"""

from sys import argv

def getNumbers(inFile):
    HTbins = ["275-325",
        "325-375",
        "375-475",
        "475-575",
        "575-675",
        "675-775",
        "775-875",
        "875-$\inf$"]

    counter=0
    
    for line in inFile:
        if "at 0.550000" in line:
            splLine = line.split(" ")
            print "%s & %s & +%s/-%s \\%s"%(HTbins[counter], splLine[3], splLine[5], splLine[7], "\\")
            counter+=1

f1 = open(argv[1], 'r')
print "le3j"
getNumbers(f1)

if len(argv)>2:
    f2 = open(argv[2], 'r')
    print "\nge4j"
    getNumbers(f2)
