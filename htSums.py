#!/usr/bin/env python
# encoding: utf-8
"""
PreScaledTriggers.py

Created by Bryn Mathias on 2011-11-02.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *

# HLT_HT600_v1Pre_1_HLT_HT300_v9Pre_210
def main():
  c1 = Print("HLT_HT550_HLT_HT250.pdf")
  c1.open()
  # c1.Print()

  diffList = []
  cumuList = []
  histList = ("HT_Nom","HT_Denom")
  dirs = [
"HLT_HT550_v11_HLT_HT250_v11",
"HLT_HT550_v2_HLT_HT250_v2",
"HLT_HT550_v3_HLT_HT250_v3",
"HLT_HT550_v4_HLT_HT250_v4",
"HLT_HT550_v5_HLT_HT250_v5",
"HLT_HT550_v6_HLT_HT250_v6",
"HLT_HT550_v7_HLT_HT250_v7",
"HLT_HT550_v8_HLT_HT250_v8"  ,



]


  # dirs = [ "HT275_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",  "HT275_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
           # "HT275_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",  "HT275_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
           # "HT275_HLT_HT250_AlphaT0p53_v6_HLT_Mu40_HT200_v4",  "HT275_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4" ,
           # "HT275_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4"]
  # weights = [138.018/2760.509,444.633/2760.509,4.291/2760.509,179.041/2760.509,1799.0/2760.509,233.808/2760.509,1799.0/2760.509]
  weights = [1.0,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,]

  mg = None
  c1.cd()
  c1.Clear()
  Nom   = GetSumHist(File = ["4fbHTTriggers.root"], Directories = dirs, Hist = histList[0], Col = r.kBlack, Norm = weights, LegendText = "")
  Nom.HideOverFlow()
  Denom = GetSumHist(File = ["4fbHTTriggers.root"], Directories = dirs, Hist = histList[1], Col = r.kRed,  Norm = weights, LegendText = "")
  Denom.HideOverFlow()
  Nom.Rebin(25,None)
  Denom.Rebin(25,None)
  Nom.hObj.GetXaxis().SetRangeUser(0.,1200.)
  Denom.hObj.GetXaxis().SetRangeUser(0.,1200.)
  Denom.hObj.SetTitle("HLT_HT550_HLT_HT250")
  Denom.Draw("h")
  Denom.hObj.GetXaxis().SetTitle("H_{T}")
  Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %f"%(Denom.hObj.GetBinWidth(1)))
  Denom.hObj.GetYaxis().SetTitleOffset(1.15)

  Nom.hObj.SetMarkerStyle(20)
  Nom.Draw("psame")
  c1.Print()
  c1.toFile(Nom.hObj,"Nom_Standard_All")
  c1.toFile(Denom.hObj,"Denom_Standard_All")
  turnon = TurnOn(Nom,Denom)
  # c1.Clear()
  turnon.setRange(0.,1200.)
  c1.cd()
  turnon.DifferentialTurnOn().GetXaxis().SetRangeUser(0.,1200.)
  turnon.DifferentialTurnOn().Draw("ap")
  diffList.append(turnon.DifferentialTurnOn())
  c1.toFile(turnon.DifferentialTurnOn(),"HLT_HT550_HLT_HT250")
  c1.Print()
  # leg = Legend()
  # print float(pair.split("_")[7])/float((pair.split("_")[3:4])[0])
  # if float(pair.split("_")[7])%float((pair.split("_")[3:4])[0]) == 0:
  cumNom   = Nom.CumulativeHist()
  cumDenom = Denom.CumulativeHist()
  cumDenom.GetYaxis().SetTitle("")
  cumDenom.Draw("h")
  cumNom.Draw("psame")
  c1.Print()
  cumuTurnOn = r.TGraphAsymmErrors()
  cumuTurnOn.Divide(cumNom,cumDenom)
  cumuTurnOn.GetXaxis().SetTitle("H_{T}^{cut} ")
  cumuTurnOn.GetXaxis().SetTitleSize(0.05)
  cumuTurnOn.GetYaxis().SetTitle("Cumulative efficiency")
  cumuTurnOn.GetYaxis().SetTitleOffset(1.5)
  cumuTurnOn.GetXaxis().SetRangeUser(0.,1200.)
  cumuTurnOn.SetMarkerStyle(20)
  cumuTurnOn.SetMarkerSize(0.5)
  cumuTurnOn.SetTitle("Cumulative HLT_HT550_HLT_HT250")
  cumuList.append(cumuTurnOn)
  c1.toFile(cumNom,"CumuNom_All")
  c1.toFile(cumDenom,"CumuDenom_All")
  cumuTurnOn.Draw("ap")
  cumuTurnOn.GetXaxis().SetRangeUser(0.,1200.)
  c1.canvas.Update()
  c1.Print()
  c1.toFile(cumuTurnOn,"Cumulative HLT_HT550_HLT_HT250")
  c1.Clear()

  c1.close()
  pass




if __name__ == '__main__':
  main()

