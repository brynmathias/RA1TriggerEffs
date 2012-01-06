#!/usr/bin/env python
# encoding: utf-8
"""
FinalHTSum.py

Created by Bryn Mathias on 2011-11-25.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *
from finalDict import *



def main():
  outfile = open("./EffsTotal.txt",'w')
  c1 = Print("FinalPlotsFromHTTotals.pdf")
  text = ""
  histList = ("HT_Nom","HT_Denom")
  sums = {
  "HT375":(["HLT_HT350_v11_HLT_HT250_v11","HLT_HT350_v2_HLT_HT250_v2","HLT_HT350_v3_HLT_HT250_v3","HLT_HT350_v4_HLT_HT250_v4","HLT_HT350_v5_HLT_HT250_v5","HLT_HT350_v6_HLT_HT250_v6","HLT_HT350_v7_HLT_HT250_v7","HLT_HT350_v8_HLT_HT250_v8"],[710.363/3929.549,38.307/3929.549,160.689/3929.549,135.443/3929.549,465.518/3929.549,4.291/3929.549,194.938/3929.549,2220./3929.549]),
  "HT475":(["HLT_HT450_v11_HLT_HT250_v11","HLT_HT450_v2_HLT_HT250_v2","HLT_HT450_v3_HLT_HT250_v3","HLT_HT450_v4_HLT_HT250_v4","HLT_HT450_v5_HLT_HT250_v5","HLT_HT450_v6_HLT_HT250_v6","HLT_HT450_v7_HLT_HT250_v7","HLT_HT450_v8_HLT_HT250_v8",],[710.363/3929.549,38.307/3929.549,160.689/3929.549,135.443/3929.549,465.518/3929.549,4.291/3929.549,194.938/3929.549,2220./3929.549]),
  "HT575":(["HLT_HT550_v11_HLT_HT250_v11","HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT550_v8_HLT_HT250_v8",],[710.363/3929.549,38.307/3929.549,160.689/3929.549,135.443/3929.549,465.518/3929.549,4.291/3929.549,194.938/3929.549,2220./3929.549]),
  "HT675":(["HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT600_v1_HLT_HT250_v8","HLT_HT600_v4_HLT_HT250_v11",],[38.307/3929.549,160.689/3929.549,135.443/3929.549,465.518/3929.549,4.291/3929.549,2220./2930.363,710.363/2930.363]),
  "HT775":(["HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT600_v1_HLT_HT250_v8","HLT_HT700_v2_HLT_HT250_v11",],[38.307/3929.549,160.689/3929.549,135.443/3929.549,465.518/3929.549,4.291/3929.549,2220./2930.363,710.363/2930.363]),
  "HT875":(["HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT600_v1_HLT_HT250_v8","HLT_HT750_v3_HLT_HT250_v11",],[38.307/3929.549,160.689/3929.549,135.443/3929.549,465.518/3929.549,4.291/3929.549,2220./2930.363,710.363/2930.363]),

"AllFromHT400":(["HLT_HT400_v2_HLT_HT250_v2","HLT_HT400_v3_HLT_HT250_v3","HLT_HT400_v4_HLT_HT250_v4","HLT_HT400_v5_HLT_HT250_v5","HLT_HT400_v6_HLT_HT250_v6","HLT_HT400_v7_HLT_HT250_v7","HLT_HT400_v8_HLT_HT250_v8","HLT_HT400_v11_HLT_HT250_v11"],[38.307/3929.549,160.689/3929.549,135.443/3929.549,465.518/3929.549,4.291/3929.549,2220./2930.363,710.363/2930.363]),
  # "HT750":(["HLT_HT750_v3_HLT_HT250_v11",],[1.0]),
  }
  c1.open()
  for key,pairs in sorted(sums.iteritems()):
   Nom   = GetSumHist(File = ["./HTRun2011AB.root"], Directories = pairs[0], Hist = histList[0], Col = r.kBlack, Norm = pairs[1], LegendText = "")
   Nom.HideOverFlow()
   Denom = GetSumHist(File = ["./HTRun2011AB.root"], Directories = pairs[0], Hist = histList[1], Col = r.kRed,   Norm = pairs[1], LegendText = "")
   Denom.HideOverFlow()
   if "AlphaT" in histList[0]:
     Denom.hObj.SetTitle("%s"%(key))
     Denom.hObj.GetXaxis().SetTitle("#alpha_{T} (GeV)")
     Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %d "%(Denom.hObj.GetBinWidth(1)))
     Denom.hObj.GetYaxis().SetTitleOffset(1.15)
     Nom.hObj.SetMarkerStyle(20)
   else:
     Nom.Rebin(25,None)
     Denom.Rebin(25,None)
     if "DEBUG" in key:
       Denom.hObj.SetTitle("%s"%(key))
     else:
       Denom.hObj.SetTitle("%s"%(key))
     Denom.hObj.GetXaxis().SetTitle("H_{T} (GeV)")
     Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %d GeV"%(Denom.hObj.GetBinWidth(1)))
     Denom.hObj.GetYaxis().SetTitleOffset(1.15)
     Nom.hObj.SetMarkerStyle(20)
   Denom.Draw("h")
   Nom.Draw("psame")
   c1.Print()
   turnon = TurnOn(Nom,Denom)
   # c1.Clear()
   turnon.setRange(0.,3000.)
   c1.cd()
   turnon.DifferentialTurnOn().SetTitle("%s"%(key))
   turnon.DifferentialTurnOn().Draw("ap")
   c1.Print()
   cumNom   = Nom.CumulativeHist()
   cumDenom = Denom.CumulativeHist()
   cumuTurnOn = r.TGraphAsymmErrors()
   cumuTurnOn.Divide(cumNom,cumDenom)
   cumuTurnOn.GetXaxis().SetTitle("H_{T}^{cut} (GeV)")
   cumuTurnOn.GetXaxis().SetTitleSize(0.05)
   cumuTurnOn.GetYaxis().SetTitle("Cumulative efficiency")
   cumuTurnOn.GetYaxis().SetTitleOffset(1.5)
   xval = r.Double(0)
   yval = r.Double(0)
   # assume that point is bin center.
   # HT bins are 25 GeV wide. so take point == Val/25 + 1
   # Get val from the text name of the key.
   if key != "AllFromHT400":
    HT = int(key[2:])
    point = (HT/25)
    cumuTurnOn.GetPoint(point,xval,yval)

    if "DEBUG" in key:
      cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),HT))
      text += "%s is %f + %f - %f Efficient at %f \n"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),HT)
    else:
      cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),HT))
      text += "%s is %f + %f - %f Efficient at %f \n"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),HT)
   cumuTurnOn.Draw("ap")
   c1.Print()
   c1.Clear()
   if key == "AllFromHT400":
      textLines = []
      for i,HT in enumerate([475,575,675,775,875]):
        point = HT/25
        cumuTurnOn.GetPoint(point,xval,yval)

        textLines.append(r.TLatex(0.1,1.-i/10.," %f + %f - %f Efficient at %f \n"%(yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),HT)))
      for line in textLines:
        line.Draw()
      c1.Print()
  outfile.write(text)
  c1.close()


if __name__ == '__main__':
  main()

