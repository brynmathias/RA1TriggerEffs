#!/usr/bin/env python
# encoding: utf-8
"""
FinalAlphaTPlot.py

Created by Bryn Mathias on 2011-12-15.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
import ROOT as r
import array
from plottingUtils import *

def findHTEff(File = None, SearchString = None, Value = None):
  iFile = open(File)
  for line in iFile.readlines():
    print line
    if SearchString in line:
      if int(line.split(" ")[2]) == int(Value):
        return float(line.split(" ")[3])
  """docstring for findHTEff"""
  pass


def main():
  pass
    # Ok now we create the FINAL PLOT!!!(s)
    # This plot(s) is the two dimensional (HT/ALPHAT) plot showing our efficiency in each bin. Has to be taken from the Differential plots
  inFile = open("./EfficienciesForAllDiffPlotFinalAlphaTPlotBinning.txt")
  alphaTbins = [0.51,0.52,0.53,0.55,0.60,0.61]#[0.5+0.01*i for i in range(12)]#
  HTbins = [275.,325.,]+[375+100*i for i in range(7)]
  FinalPlot = r.TH2D("finalPlot","",len(HTbins)-1,array.array('d',HTbins),len(alphaTbins)-1,array.array('d',alphaTbins))
  FinalPlot.GetXaxis().SetTitle("H_{T} (GeV)")
  FinalPlot.GetYaxis().SetTitle("#alpha_{T}")
  FinalPlot.GetYaxis().SetTitleSize(0.055)
  FinalPlot.GetYaxis().SetTitleOffset(.85)
  FinalPlot.GetXaxis().SetTitleSize(0.06)
  FinalPlot.GetYaxis().SetTitleSize(0.06)
  FinalPlot.GetZaxis().SetTitleSize(0.06)
  ErrorUp = r.TH2D("ErrorUp","",len(HTbins)-1,array.array('d',HTbins),len(alphaTbins)-1,array.array('d',alphaTbins))
  ErrorUp.GetXaxis().SetTitle("H_{T} (GeV)")
  ErrorUp.GetYaxis().SetTitle("#alpha_{T}")

  ErrorUp.GetXaxis().SetTitleSize(0.06)
  ErrorUp.GetYaxis().SetTitleSize(0.06)
  ErrorUp.GetZaxis().SetTitleSize(0.06)
  ErrorUp.GetYaxis().SetTitleOffset(.85)
  ErrorDown = r.TH2D("ErrorDown","",len(HTbins)-1,array.array('d',HTbins),len(alphaTbins)-1,array.array('d',alphaTbins))
  ErrorDown.GetXaxis().SetTitle("H_{T} (GeV)")
  ErrorDown.GetYaxis().SetTitle("#alpha_{T}")
  ErrorDown.GetXaxis().SetTitleSize(0.06)
  ErrorDown.GetYaxis().SetTitleSize(0.06)
  ErrorDown.GetZaxis().SetTitleSize(0.06)
  ErrorDown.GetYaxis().SetTitleOffset(.85)
  for line in inFile.readlines():
    if "AlphaT" in line:
      print line.split(" ")

      linearray = line.split(" ")
      HT = float((line.split(" ")[0])[2:5])
      # print type(HT)
      scalefactor = 1.0# findHTEff(File = "./EfficienciesForAll.txt", SearchString = "AllFrom" if int(HT-25.) > 400 else "HT375", Value = HT-25.)
      AlphaT = float(linearray[2])
      # if AlphaT > 0.61: AlphaT = 0.605
      bin = FinalPlot.FindBin(float((line.split(" ")[0])[2:5]),AlphaT)
      # print "AlphaT = %f, HT = %f, Eff = %f, Bin = %d, %s"%(AlphaT,HT,float(linearray[3]),bin,linearray[:-1])
      FinalPlot.SetBinContent(bin,float(linearray[3])*100.*scalefactor)
      ErrorUp.SetBinContent(bin,float(linearray[5])*100.)
      ErrorDown.SetBinContent(bin,float(linearray[7])*100.)

  # for y in range(len(HTbins)):
      # for x in range (len(alphaTbins)):
      # FinalPlot.SetBinContent(x,y,)

  c2 = r.TCanvas("canvas","mycanvas")
  c2.cd()
  c2.SetMargin(0.1,0.17,0.15,0.05)
  FinalPlot.GetZaxis().SetTitle("Efficiency (%)")
  FinalPlot.GetZaxis().SetTitleOffset(1.07)
  FinalPlot.GetZaxis().SetRangeUser(0.0,100.)

  FinalPlot.Draw("COLZtext")

  # raw_input()
  c2.SaveAs("./useHadAlphaT/FINALPLOTREBINTestDiff5456.pdf")
  ErrorUp.Draw("COLZtext")
  ErrorUp.GetZaxis().SetTitle("Positive error (%)")
  ErrorUp.GetZaxis().SetTitleOffset(1.07)
  ErrorUp.GetZaxis().SetRangeUser(0.0,ErrorUp.GetMaximum()*1.01)
  c2.SaveAs("./useHadAlphaT/FinalPlotErrorUpREBINTestDiff5456.pdf")
  ErrorDown.Draw("COLZtext")
  ErrorDown.GetZaxis().SetTitle("Negitive error (%)")
  ErrorDown.GetZaxis().SetTitleOffset(1.07)
  c2.SaveAs("./useHadAlphaT/FinalPlotErrorDownREBINTestDiff5456.pdf")


if __name__ == '__main__':
  main()

