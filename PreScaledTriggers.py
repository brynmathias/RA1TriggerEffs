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
  c1 = Print("./DEBUG_RUNREMOVAL.pdf")
  c1.open()
  # c1.Print()
  settings = {

"DEBUG_DEBUG_HLT_HT450_v5_HLT_HT250_v5":("HLT_HT450_v5Pre_25_HLT_HT250_v5Pre_200","HLT_HT450_v5Pre_25_HLT_HT250_v5Pre_400","HLT_HT450_v5Pre_10_HLT_HT250_v5Pre_200"),
# "DEBUG_HLT_HT500_v5_HLT_HT250_v5":("HLT_HT500_v5Pre_10_HLT_HT250_v5Pre_290","HLT_HT500_v5Pre_1_HLT_HT250_v5Pre_180"),
# "DEBUG_HLT_HT550_v5_HLT_HT250_v5":("HLT_HT550_v5Pre_1_HLT_HT250_v5Pre_200","HLT_HT550_v5Pre_1_HLT_HT250_v5Pre_180","HLT_HT550_v5Pre_1_HLT_HT250_v5Pre_290","HLT_HT550_v5Pre_1_HLT_HT250_v5Pre_400"),
  # "DEBUG_HLT_HT450_v5_HLT_Mu15_HT200_v3":("HLT_HT450_v5Pre_25_HLT_Mu15_HT200_v3Pre_1","HLT_HT450_v5Pre_14_HLT_Mu15_HT200_v3Pre_1",)



  }

  print settings.iteritems()
  for key,histList in sorted(settings.iteritems()):
    for pair in histList:
      print key,pair
      mg = None
      c1.cd()
      c1.Clear()
      print pair.split("_")[3]
      Nom   = GetSumHist(File = ["HTRun2011AB.root"], Directories = [key], Hist = "Nom_"+pair, Col = r.kBlack, Norm = [1.0,float(pair.split("_")[3])], LegendText = "")
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["HTRun2011AB.root"], Directories = [key], Hist = "Denom_"+pair, Col = r.kRed,  Norm = None, LegendText = "")
      Denom.HideOverFlow()
      Nom.Rebin(25,None)
      Denom.Rebin(25,None)
      Denom.Draw("h")
      Denom.hObj.GetXaxis().SetTitle("H_{T} (GeV)")
      Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %d GeV"%(Denom.hObj.GetBinWidth(1)))
      Denom.hObj.GetYaxis().SetTitleOffset(1.15)

      Nom.hObj.SetMarkerStyle(20)
      Nom.Draw("psame")
      c1.Print()
      # c1.toFile("Standard_"+pair)
      turnon = TurnOn(Nom,Denom)
      # c1.Clear()
      turnon.setRange(0.,3000.)
      c1.cd()
      turnon.DifferentialTurnOn().Draw("ap")
      c1.toFile(turnon.DifferentialTurnOn(),"Diff_"+pair)
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
      cumuTurnOn.GetXaxis().SetTitle("H_{T}^{cut} (GeV)")
      cumuTurnOn.GetXaxis().SetTitleSize(0.05)
      cumuTurnOn.GetYaxis().SetTitle("Cumulative efficiency")
      cumuTurnOn.GetYaxis().SetTitleOffset(1.5)
      c1.toFile(cumNom,"CumuNom_"+pair)
      c1.toFile(cumDenom,"CumuDenom_"+pair)
      cumuTurnOn.Draw("ap")
      c1.toFile(cumuTurnOn,"CUMULATIVETURNON_%s_(pre_=_%s)_from_ %s_(pre_=_%s) "%((pair.split("_")[1]),(pair.split("_")[3]),(pair.split("_")[5]),(pair.split("_")[-1])))
        # c1.Clear()
        #
        # for a in turnon.logEffs():
        #   a.SetNDC()
        #   a.Draw("same")
      c1.Print()
  c1.close()
  pass




if __name__ == '__main__':
  main()

