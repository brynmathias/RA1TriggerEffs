#!/usr/bin/env python
# encoding: utf-8
"""
makeDict.py

Created by Bryn Mathias on 2011-12-01.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
import ROOT as r
from optparse import OptionParser

def main():
  parser = OptionParser()
  parser.add_option('-i', action='store', dest='input_file')
  parser.add_option('--outFile', action='store', dest='output_file')
  parser.add_option('-d', action='store',dest="ignore_dir",default="\n")
  parser.add_option('--dict', action='store',dest="dictName",default="options")
  parser.add_option('--hist', action='store',dest="ignore_hist",default="\n")
  parser.add_option('-o', action='store', dest='output_file',default="outDict.py")
  (options,args) = parser.parse_args()
  outText = "%s = {\n"%(options.dictName)
  # print type(options.ignore_hist)
  # print options.input_file
  rFile = r.TFile().Open(options.input_file)
  for key in rFile.GetListOfKeys():
      appendD = True
      for igd in options.ignore_dir.split(","):
        if str(igd) in key.GetName(): appendD = False
      if appendD :
        outText += "\"%s\" :\t("%(key.GetName())
        for hist in rFile.Get(key.GetName()).GetListOfKeys():
          appendH = True
          for igh in options.ignore_hist.split(","):
            if str(igh) in hist.GetName(): appendH = False
          if appendH: outText += "\"%s\"," %(hist.GetName())
        outText+="),\n"
  outText+="}"
  out = open(options.output_file,'w')
  out.write(outText)
if __name__ == '__main__':
  main()

