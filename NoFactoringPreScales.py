#!/usr/bin/env python
# encoding: utf-8
"""
NoFactoringPreScales.py

Created by Bryn Mathias on 2011-11-13.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *
import ROOT as r
def gcd(num1, num2):
  # Take from:http://socialgeek.wordpress.com/2007/01/09/gcd-and-lcm-calculation-in-python/  as I am lazy
    if num1 > num2:
        for i in range(1,num2+1):
            if num2 % i == 0:
                if num1 % i == 0:
                    result = i
        return result

    elif num2 > num1:
        for i in range(1,num1+1):
            if num1 % i == 0:
                if num2 % i == 0:
                    result = i
        return result

    else:
        result = num1*num2/num1
        return result




def main():
  settings = {
  "HLT_HT350_v4_HLT_HT250_v4": ("HLT_HT350_v4Pre_70_HLT_HT250_v4Pre_200","HLT_HT350_v4Pre_50_HLT_HT250_v4Pre_150","HLT_HT350_v4Pre_20_HLT_HT250_v4Pre_60",
                                "HLT_HT350_v4Pre_14_HLT_HT250_v4Pre_40","HLT_HT350_v4Pre_120_HLT_HT250_v4Pre_240","HLT_HT350_v4Pre_10_HLT_HT250_v4Pre_30",
                                "HLT_HT350_v4Pre_240_HLT_HT250_v4Pre_480",),
  }
  c1 = Print("NonFactoringTest.pdf")
  c1.open()
  # print settings.iteritems()
  for key,histList in sorted(settings.iteritems()):
    for pair in histList:
      # print key,pair
      # Here we check if the prescales factor:
      # print pair.split("_")
      preSig = int(pair.split("_")[3])
      preRef = int(pair.split("_")[7])
      print preSig, preRef, preRef%preSig,gcd(preRef,preSig),float(gcd(preRef,preSig))/float(preSig)
      if preRef%preSig != 0:
        print "We should be maxing out at an efficiency of %f"%(float(gcd(preRef,preSig))/float(preSig))
      else: print"We should be maxing out at an efficiency of 1.0"
      c1.cd()
      c1.Clear()
      Nom   = GetSumHist(File = ["ROBREQUEST_DEBUG.root"], Directories = [key], Hist = "Nom_"+pair, Col = r.kBlack, Norm = None, LegendText = "")

      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["ROBREQUEST_DEBUG.root"], Directories = [key], Hist = "Denom_"+pair, Col = r.kRed,  Norm = None, LegendText = "")
      Denom.HideOverFlow()
      Nom.Rebin(25,None)
      Denom.Rebin(25,None)
      trigTurnOn = TurnOn(Nom,Denom)
      trigTurnOn.setRange(0.,3000.)

      c1.cd()
      trigTurnOn.DifferentialTurnOn().Draw("ap")
      c1.Print()
      cumNom   = Nom.CumulativeHist()
      cumDenom = Denom.CumulativeHist()
      cumuTurnOn = r.TGraphAsymmErrors()
      cumuTurnOn.Divide(cumNom,cumDenom)
      cumuTurnOn.GetXaxis().SetTitle("H_{T}^{cut} (GeV)")
      cumuTurnOn.GetXaxis().SetTitleSize(0.05)
      cumuTurnOn.GetYaxis().SetTitle("Cumulative efficiency")
      cumuTurnOn.GetYaxis().SetTitleOffset(1.5)
      if preRef%preSig != 0:
        cumuTurnOn.SetTitle("We should be maxing out at an efficiency of %f"%(float(gcd(preRef,preSig))/float(preSig)))
      else: cumuTurnOn.SetTitle("We should be maxing out at an efficiency of 1")



      c1.Clear()
      cumuTurnOn.Draw("ap")
      c1.Print()
  c1.close()
  pass


if __name__ == '__main__':
  main()

