#!/usr/bin/env python
# encoding: utf-8
"""
CheckLumiSections.py

Created by Bryn Mathias on 2011-11-28.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os


def main():
  pass
  inputFile = open("./NewLumisChecked.txt","r")
  text = inputFile.read()
  text = text.split("\n")
  inputFile.close()
  print len(text)
  Runs = []
  Lumis = []
  for i,line in enumerate(text):
    # print line.split(",")[1] , (text[i+1]).split(",")[1]
    if len(text) - (i) > 1:
      if len(line.split(",")) > 1 and int(line.split(",")[2]) != 4294967295:
        if  line.split(",")[0] == (text[i+1]).split(",")[0] and line.split(",")[1] == (text[i+1]).split(",")[1]:
          Runs.append(int(line.split(",")[0]))
          Lumis.append(int(line.split(",")[1]))
          print "GOTCAH  %s \t %s " , line.split(",")[0],line.split(",")[1]

  print Runs
  print Lumis

if __name__ == '__main__':
  main()

