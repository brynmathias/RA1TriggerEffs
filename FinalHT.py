#!/usr/bin/env python
# encoding: utf-8
"""
FinalHT.py

Created by Bryn Mathias on 2011-11-25.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *
from finalDict import *


def main():
  outfile = open("./Effs.txt",'w')
  c1 = Print("FinalPlotsFromHT.pdf")
  text = ""
  c1.open()
  for key,histList in sorted(finalDict.iteritems()):
    for pair in histList:
      if "AlphaT" in pair or "AlphaT" in key or "Mu" in key or "DEBUG" in key: continue
      if int((key.split("_")[1])[2:]) > 400: continue
      print key,pair
      # Check they factorise
      if len(pair) > 8:
        if int(pair.split("_")[len(pair.split("_"))-1])%int(pair.split("_")[3]) != 0:
          continue

      Nom   = GetSumHist(File = ["./HTRun2011AB.root"], Directories = [key], Hist = "Nom_"+pair if len(pair) > 8 else pair+"Nom", Col = r.kBlack, Norm = None, LegendText = "")
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["./HTRun2011AB.root"], Directories = [key], Hist = "Denom_"+pair if len(pair) > 8 else pair+"Denom", Col = r.kRed,  Norm = None, LegendText = "")
      Denom.HideOverFlow()
      if int(Nom.hObj.Integral()) == 0: continue
      if "AlphaT" in pair:
        Denom.hObj.SetTitle("%s"%(key))
        Denom.hObj.GetXaxis().SetTitle("#alpha_{T} (GeV)")
        Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %d "%(Denom.hObj.GetBinWidth(1)))
        Denom.hObj.GetYaxis().SetTitleOffset(1.15)
        Nom.hObj.SetMarkerStyle(20)
      else:
        Nom.Rebin(25,None)
        Denom.Rebin(25,None)
        if "DEBUG" in key:
          Denom.hObj.SetTitle("%s"%(pair))
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
      if len(key) > 7:
        if "DEBUG" in key:
          HT = int((key.split("_")[3])[2:])
        else:
          HT = int((key.split("_")[1])[2:])
          point = (HT/25) + 1
          cumuTurnOn.GetPoint(point,xval,yval)
        if "DEBUG" in key:
          cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(pair,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),HT+25))
          text += "%s is %f + %f - %f Efficient at %f \n"%(pair,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),HT+25)
        else:
          cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),HT+25))
          text += "%s is %f + %f - %f Efficient at %f \n"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),HT+25)
      else:
        cumuTurnOn.SetTitle("%s"%(key))
      cumuTurnOn.Draw("ap")
      c1.Print()
      c1.Clear()
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

