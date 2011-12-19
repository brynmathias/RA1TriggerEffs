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
  c1 = Print("HT400Investigation.pdf")
  c1.open()
  # c1.Print()
  settings = {
# : ("HLT_HT350_v8Pre_280_HLT_HT250_v8Pre_1400","HLT_HT350_v8Pre_200_HLT_HT250_v8Pre_580","HLT_HT350_v8Pre_70_HLT_HT250_v8Pre_350",),
# : ("HLT_HT400_v8Pre_25_HLT_HT250_v8Pre_150","HLT_HT400_v8Pre_105_HLT_HT250_v8Pre_1050","HLT_HT400_v8Pre_140_HLT_HT250_v8Pre_1400"),

# "HLT_HT350_v11_HLT_HT250_v11":  ("HT_Nom","HT_Denom"),
# "HLT_HT350_v2_HLT_HT250_v2"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT350_v3_HLT_HT250_v3"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT350_v4_HLT_HT250_v4"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT350_v5_HLT_HT250_v5"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT350_v6_HLT_HT250_v6"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT350_v7_HLT_HT250_v7"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT350_v8_HLT_HT250_v8"  :  ("HT_Nom","HT_Denom"),
"HLT_HT400_v11_HLT_HT250_v11":  ("HT_Nom","HT_Denom"),
"HLT_HT400_v2_HLT_HT250_v2"  :  ("HT_Nom","HT_Denom"),
"HLT_HT400_v3_HLT_HT250_v3"  :  ("HT_Nom","HT_Denom"),
"HLT_HT400_v4_HLT_HT250_v4"  :  ("HT_Nom","HT_Denom"),
"HLT_HT400_v5_HLT_HT250_v5"  :  ("HT_Nom","HT_Denom"),
"HLT_HT400_v6_HLT_HT250_v6"  :  ("HT_Nom","HT_Denom"),
"HLT_HT400_v7_HLT_HT250_v7"  :  ("HT_Nom","HT_Denom"),
"HLT_HT400_v8_HLT_HT250_v8"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT450_v11_HLT_HT250_v11":  ("HT_Nom","HT_Denom"),
# "HLT_HT450_v2_HLT_HT250_v2"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT450_v3_HLT_HT250_v3"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT450_v4_HLT_HT250_v4"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT450_v5_HLT_HT250_v5"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT450_v6_HLT_HT250_v6"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT450_v7_HLT_HT250_v7"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT450_v8_HLT_HT250_v8"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT550_v11_HLT_HT250_v11":  ("HT_Nom","HT_Denom"),
# "HLT_HT550_v2_HLT_HT250_v2"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT550_v3_HLT_HT250_v3"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT550_v4_HLT_HT250_v4"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT550_v5_HLT_HT250_v5"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT550_v6_HLT_HT250_v6"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT550_v7_HLT_HT250_v7"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT550_v8_HLT_HT250_v8"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT600_v1_HLT_HT250_v8"  :  ("HT_Nom","HT_Denom"),
# "HLT_HT600_v4_HLT_HT250_v11" :  ("HT_Nom","HT_Denom"),
# "HLT_HT750_v3_HLT_HT250_v11" :  ("HT_Nom","HT_Denom"),

  # "HLT_HT300_v*_HLT_HT200_v*": ("HT_Nom","HT_Denom"),
  # "HLT_HT300_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"),
  # "HLT_HT300_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"),
  # "HLT_HT350_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"),
  # "HLT_HT400_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"),
  # "HLT_HT450_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger
  # "HLT_HT500_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"),
  # "HLT_HT550_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"),
  # "HLT_HT600_v*_HLT_HT250_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger
  # "HLT_HT300_v*_HLT_HT300_v*": ("HT_Nom","HT_Denom"),
  # "HLT_HT350_v*_HLT_HT300_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger
  # "HLT_HT400_v*_HLT_HT300_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger
  # "HLT_HT450_v*_HLT_HT300_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger
  # "HLT_HT500_v*_HLT_HT300_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger
  # "HLT_HT550_v*_HLT_HT300_v*": ("HT_Nom","HT_Denom"),
  # "HLT_HT600_v*_HLT_HT300_v*": ("HT_Nom","HT_Denom"), # soemthing strange happens with this trigger
  # "HLT_HT500_v8_HLT_HT250_v8": ("HLT_HT500_v8Pre_2_HLT_HT250_v8Pre_150","HLT_HT500_v8Pre_3_HLT_HT250_v8Pre_210","HLT_HT500_v8Pre_5_HLT_HT250_v8Pre_180","HLT_HT500_v8Pre_7_HLT_HT250_v8Pre_410",
                      # "HLT_HT500_v8Pre_10_HLT_HT250_v8Pre_580","HLT_HT500_v8Pre_15_HLT_HT250_v8Pre_490","HLT_HT500_v8Pre_30_HLT_HT250_v8Pre_1050","HLT_HT500_v8Pre_45_HLT_HT250_v8Pre_1680"),
  # "HLT_HT550_v8_HLT_HT300_v9": ("HLT_HT550_v8Pre_1_HLT_HT300_v9Pre_150","HLT_HT550_v8Pre_1_HLT_HT300_v9Pre_210","HLT_HT550_v8Pre_1_HLT_HT300_v9Pre_75"),

  # "HLT_HT600_v1_HLT_HT300_v9": ("HLT_HT600_v1Pre_1_HLT_HT300_v9Pre_450","HLT_HT600_v1Pre_1_HLT_HT300_v9Pre_590","HLT_HT600_v1Pre_1_HLT_HT300_v9Pre_150","HLT_HT600_v1Pre_1_HLT_HT300_v9Pre_300","HLT_HT600_v1Pre_1_HLT_HT300_v9Pre_450"),
  }
  diffList = []
  cumuList = []
  print settings.iteritems()
  for key,histList in sorted(settings.iteritems()):
      print histList
      mg = None
      c1.cd()
      c1.Clear()
      Nom   = GetSumHist(File = ["4fbHTTriggers.root"], Directories = [key], Hist = histList[0], Col = r.kBlack, Norm = None, LegendText = "")
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["4fbHTTriggers.root"], Directories = [key], Hist = histList[1], Col = r.kRed,  Norm = None, LegendText = "")
      Denom.HideOverFlow()
      Nom.Rebin(25,None)
      Denom.Rebin(25,None)
      Nom.hObj.GetXaxis().SetRangeUser(0.,1200.)
      Denom.hObj.GetXaxis().SetRangeUser(0.,1200.)
      Denom.hObj.SetTitle(key)
      Denom.Draw("h")
      Denom.hObj.GetXaxis().SetTitle("H_{T} (GeV)")
      Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %d GeV"%(Denom.hObj.GetBinWidth(1)))
      Denom.hObj.GetYaxis().SetTitleOffset(1.15)

      Nom.hObj.SetMarkerStyle(20)
      Nom.Draw("psame")
      c1.Print()
      c1.toFile(Nom.hObj,"Nom_Standard_"+key)
      c1.toFile(Denom.hObj,"Denom_Standard_"+key)
      turnon = TurnOn(Nom,Denom)
      # c1.Clear()
      turnon.setRange(0.,1200.)
      c1.cd()
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
      cumuTurnOn.GetXaxis().SetTitle("H_{T}^{cut} (GeV)")
      cumuTurnOn.GetXaxis().SetTitleSize(0.05)
      cumuTurnOn.GetYaxis().SetTitle("Cumulative efficiency")
      cumuTurnOn.GetYaxis().SetTitleOffset(1.5)
      cumuTurnOn.GetXaxis().SetRangeUser(0.,1200.)
      cumuTurnOn.SetMarkerStyle(20)
      cumuTurnOn.SetMarkerSize(0.5)
      cumuList.append(cumuTurnOn)
      c1.toFile(cumNom,"CumuNom_"+key)
      c1.toFile(cumDenom,"CumuDenom_"+key)
      cumuTurnOn.SetTitle("CumuTuronOn_"+key)
      cumuTurnOn.Draw("ap")
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
    # print g.GetName() , "Differential"
    # for point in range(1,Nom.hObj.GetNbinsX()):
    #     xval = r.Double(0)
    #     yval = r.Double(0)
    #     g.GetPoint(point,xval,yval)
    #  # print "approx %f efficient at a cut of %f"%(yval,newBinEdge)
    #     print "%s is approx 90%% efficient at a cut of %f"%(g.GetName(),Nom.hObj.GetBinLowEdge(point))
    #     if yval > 0.95:
    #       print "%s is approx 95%% efficient at a cut of %f"%(g.GetName(),Nom.hObj.GetBinLowEdge(point))
    #       if yval > 0.99:
    #         print "%s is >= 99%% efficient  at a cut of %f"%(g.GetName(),Nom.hObj.GetBinLowEdge(point))
    #         break
    if col1 == 5 or col1 == 10: col1+=1
    print col1 , g.GetName()
    g.SetLineColor(col1)
    g.SetMarkerColor(col1)
    col1 +=1
    mg.Add(g)
  mg.Draw("ap")
  mg.GetXaxis().SetRangeUser(0.,1200.)
  c1.Print()

  mg2 = r.TMultiGraph()
  col2 = 2
  c1.Clear()
  # c1.Print()
  for g in cumuList:
    # print g.GetName() , "Cumulative"
    if col2 == 5 or col2 == 10: col2+=1
    # for point in range(1,Nom.hObj.GetNbinsX()):
    #     xval = r.Double(0)
    #     yval = r.Double(0)
    #     g.GetPoint(point,xval,yval)
    #   # print "approx %f efficient at a cut of %f"%(yval,newBinEdge)
    #     print "%s is approx 90%% efficient at a cut of %f"%(g.GetName(),xval)
    #     if yval > 0.95:
    #       print "%s is approx 95%% efficient at a cut of %f"%(g.GetName(),xval)
    #       if yval > 0.99:
    #         print "%s is >= 99%% efficient  at a cut of %f"%(g.GetName(),xval)
    #         break

    g.SetLineColor(col2)
    g.SetMarkerColor(col2)
    col2 +=1
    mg2.Add(g)
  mg2.Draw("ap")
  mg2.GetXaxis().SetRangeUser(0.,1200.)
  c1.Print()
  c1.close()
  pass




if __name__ == '__main__':
  main()

