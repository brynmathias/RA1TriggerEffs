#!/usr/bin/env python
# encoding: utf-8
"""
FinalAlphaT.py

Created by Bryn Mathias on 2011-11-25.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *
from finalDict import *


def main():
  outfile = open("./EffsAlphaTDiMuon.txt",'w')
  c1 = Print("FinalPlotsFromAlphaTDiMuon.pdf")
  text = ""
  c1.open()
  for key,histList in sorted(finalDict.iteritems()):
    for pair in histList:
      if "AlphaT" not in pair or "AlphaT" not in key: continue
      print key,pair
      # Check they factorise
      if len(pair) > 8:
        if int(pair.split("_")[len(pair.split("_"))-1])%int(pair.split("_")[3]) != 0:
          continue

      Nom   = GetSumHist(File = ["./DiMuon.root"], Directories = [key], Hist = "Nom_"+pair if len(pair) > 8 else pair+"Nom", Col = r.kBlack, Norm = None, LegendText = "")
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["./DiMuon.root"], Directories = [key], Hist = "Denom_"+pair if len(pair) > 8 else pair+"Denom", Col = r.kRed,  Norm = None, LegendText = "")
      Denom.HideOverFlow()
      if "AlphaT" in pair:
        Denom.hObj.SetTitle("%s"%(key))
        Denom.hObj.GetXaxis().SetTitle("#alpha_{T} (GeV)")
        Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %d "%(Denom.hObj.GetBinWidth(1)))
        Denom.hObj.GetYaxis().SetTitleOffset(1.15)
        Nom.hObj.SetMarkerStyle(20)
        Denom.hObj.GetXaxis().SetRangeUser(0.,1.5)
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
      turnon.setRange(0.,1.5)
      c1.cd()
      turnon.DifferentialTurnOn().Draw("ap")
      c1.Print()
      cumNom   = Nom.CumulativeHist()
      cumDenom = Denom.CumulativeHist()
      cumuTurnOn = r.TGraphAsymmErrors()
      cumuTurnOn.Divide(cumNom,cumDenom,"n")
      cumuTurnOn.GetXaxis().SetTitle("H_{T}^{cut} (GeV)")
      cumuTurnOn.GetXaxis().SetTitleSize(0.05)
      cumuTurnOn.GetXaxis().SetRangeUser(0.,1.5)
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
        cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(pair,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),0.55))
        if yval > 0.:
          text += "%s is %f + %f - %f Efficient at %f \n"%(pair,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),0.55)
      else:
        cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),0.55))
        if yval > 0.:
          text += "%s is %f + %f - %f Efficient at %f \n"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),0.55)
      cumuTurnOn.Draw("ap")
      c1.Print()
  outfile.write(text)
  c1.close()


if __name__ == '__main__':
  main()

