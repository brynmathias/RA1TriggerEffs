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
  c1 = Print("HenningLook.pdf")
  c1.open()
  # c1.Print()
  settings = {

  # "HLT_HT350_v8_HLT_HT250_v8": ("HLT_HT350_v8Pre_280_HLT_HT250_v8Pre_1400",
                                # "HLT_HT350_v8Pre_200_HLT_HT250_v8Pre_580",
                                # "HLT_HT350_v8Pre_70_HLT_HT250_v8Pre_350",),
  # "HLT_HT350_v7_HLT_HT250_v7": ("HLT_HT350_v7Pre_50_HLT_HT250_v7Pre_150",),
  # "HLT_HT450_v5_HLT_HT300_v6": ("HLT_HT450_v5Pre_25_HLT_HT300_v6Pre_200","HLT_HT450_v5Pre_15_HLT_HT300_v6Pre_150","HLT_HT450_v5Pre_10_HLT_HT300_v6Pre_100"),
  # "HLT_HT450_v8_HLT_HT300_v9": ("HLT_HT450_v8Pre_30_HLT_HT300_v9Pre_300","HLT_HT450_v8Pre_10_HLT_HT300_v9Pre_110","HLT_HT450_v8Pre_15_HLT_HT300_v9Pre_150"),
  # "HLT_HT550_v*_HLT_HT300_v*": ("HLT_HT550_v*Pre_1_HLT_HT300_v*Pre_150","HLT_HT550_v*Pre_15_HLT_HT300_v*Pre_300","HLT_HT550_v*Pre_10_HLT_HT300_v*Pre_210","HLT_HT550_v*Pre_1_HLT_HT300_v*Pre_7",
  # "HLT_HT550_v*Pre_1_HLT_HT300_v*Pre_200","HLT_HT550_v*Pre_1_HLT_HT300_v*Pre_40","HLT_HT550_v*Pre_1_HLT_HT300_v*Pre_70"),
  # "HLT_HT450_v8_HLT_HT300_v9": ("HLT_HT450_v8Pre_30_HLT_HT300_v9Pre_300","HLT_HT450_v8Pre_10_HLT_HT300_v9Pre_110","HLT_HT450_v8Pre_15_HLT_HT300_v9Pre_150"),
  "HLT_HT450_v*_HLT_HT250_v*": ("HLT_HT450_v*Pre_50_HLT_HT250_v*Pre_1050","HLT_HT450_v*Pre_80_HLT_HT250_v*Pre_1680","HLT_HT450_v*Pre_1_HLT_HT250_v*Pre_150","HLT_HT450_v*Pre_1_HLT_HT250_v*Pre_15","HLT_HT450_v*Pre_1_HLT_HT250_v*Pre_35","HLT_HT450_v*Pre_50_HLT_HT250_v*Pre_300","HLT_HT450_v*Pre_1_HLT_HT250_v*Pre_25","HLT_HT450_v*Pre_5_HLT_HT250_v*Pre_85",),



  # "HLT_HT600_v*_HLT_HT300_v*": ("HLT_HT600_v*Pre_1_HLT_HT300_v*Pre_210","HLT_HT600_v*Pre_1_HLT_HT300_v*Pre_300","HLT_HT600_v*Pre_1_HLT_HT300_v*Pre_150"), # soemthing strange happens with this trigger
  # "HLT_HT350_v*_HLT_HT300_v*": ("HLT_HT350_v*Pre_35_HLT_HT300_v*Pre_70",), # soemthing strange happens with this trigger
  # "HLT_HT400_v*_HLT_HT300_v*": ("HLT_HT400_v*Pre_1_HLT_HT300_v*Pre_7","HLT_HT400_v*Pre_15_HLT_HT300_v*Pre_60"), # soemthing strange happens with this trigger
  # "HLT_HT450_v*_HLT_HT300_v*": ("HLT_HT450_v*Pre_15_HLT_HT300_v*Pre_150","HLT_HT450_v*Pre_1_HLT_HT300_v*Pre_100"), # soemthing strange happens with this trigger
  # "HLT_HT500_v*_HLT_HT300_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger
  # "HLT_HT600_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger
  # "HLT_HT450_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger

  }

  print settings.iteritems()
  for key,histList in sorted(settings.iteritems()):
    for pair in histList:
      print key,pair
      mg = None
      c1.cd()
      c1.Clear()
      Nom   = GetSumHist(File = ["ROBREQUEST_DEBUG.root"], Directories = [key], Hist = "Nom_"+pair, Col = r.kBlack, Norm = None, LegendText = "")
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["ROBREQUEST_DEBUG.root"], Directories = [key], Hist = "Denom_"+pair, Col = r.kRed,  Norm = None, LegendText = "")
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
      if float(pair.split("_")[7])%float((pair.split("_")[3:4])[0]) == 0:
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
        print pair
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

