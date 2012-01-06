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
  outfile = open("./DiMuonAlphaT.txt",'w')
  c1 = Print("DimuonAlphaT.pdf")
  text = ""
  histList = ("AlphaT_Nom","AlphaT_Denom")
  sums = {
"DiMuon58":(["DiMu_0.300000_HT275_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4","DiMu_0.300000_HT275_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5"],None,None),



  }
  c1.open()
  for key,pairs in sorted(sums.iteritems()):
   Nom   = GetSumHist(File = ["./DiMuon.root"], Directories = pairs[0], Hist = histList[0], Col = r.kBlack, Norm = pairs[1], LegendText = "")
   Nom.HideOverFlow()
   Denom = GetSumHist(File = ["./DiMuon.root"], Directories = pairs[0], Hist = histList[1], Col = r.kRed,   Norm = pairs[1], LegendText = "")
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
   c1.SetLog('y',True)
   Denom.hObj.GetXaxis().SetRangeUser(0.,1.5)
   Denom.Draw("h")
   Nom.Draw("psame")
   c1.Print()
   c1.SetLog('y',False)
   turnon = TurnOn(Nom,Denom)
   # c1.Clear()
   turnon.setRange(0.,1.5)
   c1.cd()
   turnon.DifferentialTurnOn().GetXaxis().SetRangeUser(0.,1.5)
   turnon.DifferentialTurnOn().SetTitle("%s"%(key))
   turnon.DifferentialTurnOn().Draw("ap")
   c1.Print()
   cumNom   = Nom.CumulativeHist()
   cumDenom = Denom.CumulativeHist()
   cumuTurnOn = r.TGraphAsymmErrors()
   cumuTurnOn.Divide(cumNom,cumDenom)
   cumuTurnOn.GetXaxis().SetTitle("H_{T}^{cut} (GeV)")
   cumuTurnOn.GetXaxis().SetRangeUser(0.,1.5)
   cumuTurnOn.GetXaxis().SetTitleSize(0.05)
   cumuTurnOn.GetYaxis().SetTitle("Cumulative efficiency")
   cumuTurnOn.GetYaxis().SetTitleOffset(1.5)
   xval = r.Double(0)
   yval = r.Double(0)
   # assume that point is bin center.
   # HT bins are 25 GeV wide. so take point == Val/25 + 1
   # Get val from the text name of the key.


   point = int(0.55/Nom.hObj.GetBinWidth(1))
   cumuTurnOn.GetPoint(point,xval,yval)

   if "DEBUG" in key:
     cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(pair,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),xval))
     if yval > 0.:
       text += "%s is %f + %f - %f Efficient at %f \n"%(pair,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),xval)
   else:
     cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),xval))
     if yval > 0.:
       text += "%s is %f + %f - %f Efficient at %f \n"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),xval)
   cumuTurnOn.Draw("ap")
   c1.Print()
  outfile.write(text)
  c1.close()


if __name__ == '__main__':
  main()

