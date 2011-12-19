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
  c1 = Print("HT875_NewData.pdf")
  c1.open()
  # c1.Print()
  settings = {
# "HT275_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
# "HT275_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
# "HT275_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT275_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
# "HT275_HLT_HT250_AlphaT0p53_v6_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT275_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT275_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT325_HLT_HT300_AlphaT0p52_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT325_HLT_HT300_AlphaT0p52_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT325_HLT_HT300_AlphaT0p52_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
# "HT325_HLT_HT300_AlphaT0p52_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
# "HT325_HLT_HT300_AlphaT0p52_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT325_HLT_HT300_AlphaT0p53_v5_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
# "HT325_HLT_HT300_AlphaT0p53_v6_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT375_HLT_HT350_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT375_HLT_HT350_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT375_HLT_HT350_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
# "HT375_HLT_HT350_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
# "HT375_HLT_HT350_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT375_HLT_HT350_AlphaT0p52_v1_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
# "HT375_HLT_HT350_AlphaT0p52_v2_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT375_HLT_HT350_AlphaT0p53_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
# "HT475_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
# "HT475_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT475_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT475_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
# "HT475_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
# "HT475_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT475_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
# "HT475_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT575_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
# "HT575_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT575_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT575_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
# "HT575_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
# "HT575_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT575_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
# "HT575_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT675_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
# "HT675_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT675_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT675_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
# "HT675_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
# "HT675_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT675_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
# "HT675_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT775_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
# "HT775_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT775_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
# "HT775_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
# "HT775_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
# "HT775_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
# "HT775_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
# "HT775_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
  }
  diffList = []
  cumuList = []
  print settings.iteritems()
  for key,histList in sorted(settings.iteritems()):
      print histList
      mg = None
      c1.cd()
      c1.Clear()
      Nom   = GetSumHist(File = ["MuHad_signal_ht375.root"], Directories = [key], Hist = histList[0], Col = r.kBlack, Norm = None, LegendText = "")
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["MuHad_signal_ht375.root"], Directories = [key], Hist = histList[1], Col = r.kRed,  Norm = None, LegendText = "")
      Denom.HideOverFlow()
      # Nom.Rebin(25,None)
      # Denom.Rebin(25,None)
      Nom.hObj.GetXaxis().SetRangeUser(0.,1.)
      Denom.hObj.GetXaxis().SetRangeUser(0.,1.)
      Denom.Draw("h")
      Denom.hObj.GetXaxis().SetTitle("#alpha_{T}")
      Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %f"%(Denom.hObj.GetBinWidth(1)))
      Denom.hObj.GetYaxis().SetTitleOffset(1.15)

      Nom.hObj.SetMarkerStyle(20)
      Nom.Draw("psame")
      c1.Print()
      c1.toFile(Nom.hObj,"Nom_Standard_"+key)
      c1.toFile(Denom.hObj,"Denom_Standard_"+key)
      turnon = TurnOn(Nom,Denom)
      # c1.Clear()
      turnon.setRange(0.,1.)
      c1.cd()
      turnon.DifferentialTurnOn().GetXaxis().SetRangeUser(0.,1.)
      turnon.DifferentialTurnOn().SetTitle(key)
      turnon.DifferentialTurnOn().Draw("ap")
      diffList.append(turnon.DifferentialTurnOn())
      c1.toFile(turnon.DifferentialTurnOn(),"Diff_"+key)
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
      cumuTurnOn.GetXaxis().SetTitle("#alphat_{T}^{cut} ")
      cumuTurnOn.GetXaxis().SetTitleSize(0.05)
      cumuTurnOn.GetYaxis().SetTitle("Cumulative efficiency")
      cumuTurnOn.GetYaxis().SetTitleOffset(1.5)
      cumuTurnOn.GetXaxis().SetRangeUser(0.,1.)
      cumuTurnOn.SetTitle(key)
      cumuTurnOn.SetMarkerStyle(20)
      cumuTurnOn.SetMarkerSize(0.5)
      cumuTurnOn.SetTitle(key)
      cumuList.append(cumuTurnOn)
      c1.toFile(cumNom,"CumuNom_"+key)
      c1.toFile(cumDenom,"CumuDenom_"+key)
      cumuTurnOn.Draw("ap")
      cumuTurnOn.GetXaxis().SetRangeUser(0.,1.)
      c1.canvas.Update()
      c1.Print()
      c1.toFile(cumuTurnOn,"Cumulative_%s"%(key))
      c1.Clear()
      # for a in cumuTurnOn.logEffs():
          # a.SetNDC()
          # a.Draw("same")
      # c1.Print()
  mg = r.TMultiGraph()
  c1.Clear()
  col1 = 2
  for g in diffList:
    if col1 == 5 or col1 == 10: col1+=1
    print col1 , g.GetName()
    g.SetLineColor(col1)
    g.SetMarkerColor(col1)
    col1 +=1
    mg.Add(g)
  mg.Draw("ap")
  mg.GetXaxis().SetRangeUser(0.,1.)
  c1.canvas.Update()
  c1.Print()

  mg2 = r.TMultiGraph()
  col2 = 2
  c1.Clear()
  # c1.Print()
  for g in cumuList:
    if col2 == 5 or col2 == 10: col2+=1
    g.SetLineColor(col2)
    g.SetMarkerColor(col2)
    col2 +=1
    mg2.Add(g)
  mg2.Draw("ap")
  mg2.GetXaxis().SetRangeUser(0.,1.)
  c1.canvas.Update()
  c1.Print()
  c1.close()
  pass




if __name__ == '__main__':
  main()

