#!/usr/bin/env python
# encoding: utf-8
"""
FindFractionOfRemoved.py

Created by Bryn Mathias on 2011-11-24.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *

def main():
  key = "DEBUG_HLT_HT450_v5_HLT_HT250_v5"
  pair = "HLT_HT450_v5Pre_25_HLT_HT250_v5Pre_200"
  HistNoneRemoved = GetSumHist(File = ["./investigationsIntRemovingLumisAndEventsFor_v5HTTriggers/NoRemovals.root"], Directories = [key], Hist = "Nom_"+pair, Col = r.kBlack, Norm = None, LegendText = "")
  HistRunRemoved  = GetSumHist(File = ["./investigationsIntRemovingLumisAndEventsFor_v5HTTriggers/RmRun166033.root"], Directories = [key], Hist = "Nom_"+pair, Col = r.kBlack, Norm = None, LegendText = "")
  HistLumiRemoved = GetSumHist(File = ["./investigationsIntRemovingLumisAndEventsFor_v5HTTriggers/RmMidLumiPreChanges.root"], Directories = [key], Hist = "Nom_"+pair, Col = r.kBlack, Norm = None, LegendText = "")
  HistAllRemoved  = GetSumHist(File = ["./investigationsIntRemovingLumisAndEventsFor_v5HTTriggers/RmAllProblems.root"], Directories = [key], Hist = "Nom_"+pair, Col = r.kBlack, Norm = None, LegendText = "")
  print "Number of events removed by cutting out the Run 166033 = %f"%(HistNoneRemoved.hObj.Integral() - HistRunRemoved.hObj.Integral())
  print "Number of events removed by cutting out the lumi's with over lapping prescles = %f"%(HistNoneRemoved.hObj.Integral() - HistLumiRemoved.hObj.Integral())
  print "Number of events removed by cutting out both = %f"%(HistNoneRemoved.hObj.Integral() - HistAllRemoved.hObj.Integral())

  print "Fraction of events removed by cutting out the Run 166033 = %f"%(1.0 - HistRunRemoved.hObj.Integral()/HistNoneRemoved.hObj.Integral())
  print "Fraction of events removed by cutting out the lumi's with over lapping prescles = %f"%(1.0 - HistLumiRemoved.hObj.Integral()/HistNoneRemoved.hObj.Integral())
  print "Fraction of events removed by cutting out both = %f"%(1.0 - HistAllRemoved.hObj.Integral()/HistNoneRemoved.hObj.Integral())



  pass


if __name__ == '__main__':
  main()

