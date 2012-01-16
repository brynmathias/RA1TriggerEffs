#!/usr/bin/env python
# encoding: utf-8
"""
HTEffCombinErrorsUseTurnOnClass.py

Created by Bryn Mathias on 2011-12-12.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *
from TurnOn import *
import array
r.gROOT.SetBatch(True) # suppress the creation of canvases on the screen.. much much faster if over a remote connection

def main():
  text = ""

  sums ={

#
"HT375":(["HLT_HT350_v11_HLT_HT250_v11","HLT_HT350_v2_HLT_HT250_v2","HLT_HT350_v3_HLT_HT250_v3","HLT_HT350_v4_HLT_HT250_v4","HLT_HT350_v5_HLT_HT250_v5","HLT_HT350_v6_HLT_HT250_v6","HLT_HT350_v7_HLT_HT250_v7","HLT_HT350_v8_HLT_HT250_v8"],"./noOddMuonVeto/ht375HadNoOddMuon.root"),
#   "HT475":(["HLT_HT450_v11_HLT_HT250_v11","HLT_HT450_v2_HLT_HT250_v2","HLT_HT450_v3_HLT_HT250_v3","HLT_HT450_v4_HLT_HT250_v4","HLT_HT450_v5_HLT_HT250_v5","HLT_HT450_v6_HLT_HT250_v6","HLT_HT450_v7_HLT_HT250_v7","HLT_HT450_v8_HLT_HT250_v8",],"./noOddMuonVeto/ht375HadNoOddMuon.root"),
#   "HT575":(["HLT_HT550_v11_HLT_HT250_v11","HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT550_v8_HLT_HT250_v8",],"./noOddMuonVeto/ht375HadNoOddMuon.root"),
#   "HT675":(["HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT600_v1_HLT_HT250_v8","HLT_HT600_v4_HLT_HT250_v11",],"./noOddMuonVeto/ht375HadNoOddMuon.root"),
#   "HT775":(["HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT600_v1_HLT_HT250_v8","HLT_HT700_v2_HLT_HT250_v11",],"./noOddMuonVeto/ht375HadNoOddMuon.root"),
#   "HT875":(["HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT600_v1_HLT_HT250_v8","HLT_HT750_v3_HLT_HT250_v11",],"./noOddMuonVeto/ht375HadNoOddMuon.root"),
#
"AllFromHT400":(["HLT_HT400_v2_HLT_HT250_v2","HLT_HT400_v3_HLT_HT250_v3","HLT_HT400_v4_HLT_HT250_v4","HLT_HT400_v5_HLT_HT250_v5","HLT_HT400_v6_HLT_HT250_v6","HLT_HT400_v7_HLT_HT250_v7","HLT_HT400_v8_HLT_HT250_v8","HLT_HT400_v11_HLT_HT250_v11"],"./noOddMuonVeto/ht375HadNoOddMuon.root"),

"HT275AlphaT":([
"HT275_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4","HT275_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4","HT275_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2","HT275_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3","HT275_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4","HT275_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1","DiMu_HT275_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4","DiMu_HT275_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5","DiMu_HT275_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4","DiMu_HT275_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
],"./noOddMuonVeto/ht275MuHadNoOddMuon.root"),
"HT325AlphaT":([
"HT325_HLT_HT300_AlphaT0p52_v1_HLT_Mu5_HT200_v4","HT325_HLT_HT300_AlphaT0p52_v2_HLT_Mu8_HT200_v4","HT325_HLT_HT300_AlphaT0p52_v3_HLT_Mu15_HT200_v2","HT325_HLT_HT300_AlphaT0p53_v3_HLT_Mu15_HT200_v3","HT325_HLT_HT300_AlphaT0p53_v4_HLT_Mu15_HT200_v4","HT325_HLT_HT300_AlphaT0p53_v5_HLT_Mu30_HT200_v1","HT325_HLT_HT300_AlphaT0p53_v6_HLT_Mu40_HT200_v3","HT325_HLT_HT300_AlphaT0p53_v6_HLT_Mu40_HT200_v4","HT325_HLT_HT300_AlphaT0p54_v5_HLT_Mu40_HT300_v4","HT325_HLT_HT300_AlphaT0p54_v5_HLT_Mu40_HT300_v5","DiMu_HT325_HLT_HT300_AlphaT0p55_v3_HLT_DoubleMu8_Mass8_HT200_v4","DiMu_HT325_HLT_HT300_AlphaT0p55_v3_HLT_DoubleMu8_Mass8_HT200_v5",
],"./useHadAlphaT/ht325MuHadNoOddMuon.root"),

"HT375AlphaT":([
"HT375_HLT_HT350_AlphaT0p51_v1_HLT_Mu5_HT200_v4","HT375_HLT_HT350_AlphaT0p51_v2_HLT_Mu8_HT200_v4","HT375_HLT_HT350_AlphaT0p51_v3_HLT_Mu15_HT200_v2","HT375_HLT_HT350_AlphaT0p51_v4_HLT_Mu15_HT200_v3","HT375_HLT_HT350_AlphaT0p51_v5_HLT_Mu15_HT200_v4","HT375_HLT_HT350_AlphaT0p52_v1_HLT_Mu30_HT200_v1","HT375_HLT_HT350_AlphaT0p52_v2_HLT_Mu40_HT200_v3","HT375_HLT_HT350_AlphaT0p52_v2_HLT_Mu40_HT200_v4","HT375_HLT_HT350_AlphaT0p53_v10_HLT_Mu40_HT300_v4","HT375_HLT_HT350_AlphaT0p53_v10_HLT_Mu40_HT300_v5",
],"./useHadAlphaT/ht375MuHadNoOddMuon.root"),

"HT475AlphaT":([
"HT475_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4","HT475_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4","HT475_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2","HT475_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3","HT475_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4","HT475_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1","HT475_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3","HT475_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4","HT475_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4","HT475_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5","HT475_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4","HT475_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
],"./useHadAlphaT/ht375MuHadNoOddMuon.root"),

"HT575AlphaT":([
"HT575_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4","HT575_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4","HT575_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2","HT575_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3","HT575_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4","HT575_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1","HT575_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3","HT575_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4","HT575_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4","HT575_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5","HT575_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4","HT575_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
],"./useHadAlphaT/ht375MuHadNoOddMuon.root"),
"HT675AlphaT":([
"HT675_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4","HT675_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4","HT675_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2","HT675_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3","HT675_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4","HT675_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1","HT675_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3","HT675_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4","HT675_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4","HT675_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5","HT675_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4","HT675_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
],"./useHadAlphaT/ht375MuHadNoOddMuon.root"),
"HT775AlphaT":([
"HT775_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4","HT775_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4","HT775_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2","HT775_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3","HT775_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4","HT775_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1","HT775_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3","HT775_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4","HT775_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4","HT775_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5","HT775_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4","HT775_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
],"./useHadAlphaT/ht375MuHadNoOddMuon.root"),
"HT875AlphaT":([
"HT875_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4","HT875_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4","HT875_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2","HT875_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3","HT875_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4","HT875_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1","HT875_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3","HT875_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4","HT875_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4","HT875_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5","HT875_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4","HT875_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
],"./useHadAlphaT/ht375MuHadNoOddMuon.root"),



}



  NumsForFinalPlot = []
  for key,Dirs in sorted(sums.iteritems()):
    if"AlphaT" not in key: histList = ("HT_Nom","HT_Denom")
    if"AlphaT" in key: histList = ("AlphaT_Nom","AlphaT_Denom")

    if "AlphaT" in key:axisTitle = "#alpha_{T}"
    else:axisTitle="H_{T}"
    numeratorList = []
    denominatorList = []

    BinEdges = [0.5,0.51,0.52,0.53,0.55,0.60,2.00]
    for Dir in Dirs[0]:
      # print Dir
      aNom = GetSumHist(File = [Dirs[1]], Directories = [Dir], Hist = histList[0], Col = r.kBlack, Norm = None, LegendText = "")
      # aNom.HideOverFlow()
      if "AlphaT" not in key:aNom.Rebin(25,None)
      # if "AlphaT" in key: aNom.Rebin(len(BinEdges)-1,BinEdges)
      # print aNom.hObj.Integral()

      numeratorList.append(aNom)
      aDenom =  GetSumHist(File = [Dirs[1]], Directories = [Dir], Hist = histList[1], Col = r.kRed, Norm = None, LegendText = "")
      # aDenom.HideOverFlow()
      if "AlphaT" not in key:aDenom.Rebin(25,None)
      # if "AlphaT" in key: aDenom.Rebin(len(BinEdges)-1,BinEdges)
      # print aDenom.hObj.Integral() , "DENOM INT"
      # if aNom.hObj.Integral() > aDenom.hObj.Integral(): print "ERROR !!!!!!!!!"

      denominatorList.append(aDenom)
    c1 = Print("./useHadAlphaT/HTNewErrors%s.pdf"%(key))
    c1.open()
    DiffNomList = []
    DiffDenomList = []
    CumuNomList = []
    CumuDenomList = []
    for nom,denom in zip(numeratorList,denominatorList):
      nom.hObj.SetTitle(key)
      # print nom.hObj.Integral() , "IN LOOP"
      denom.hObj.SetTitle(Dir)
      nom.hObj.SetName(key)
      # print nom.hObj.Integral() , "IN LOOP"
      denom.hObj.SetName(Dir)
      if denom.hObj.Integral() > 0.:
        DiffNomList.append(nom.hObj)
        DiffDenomList.append(denom.hObj)
        CumuNomList.append(MakeCumu(nom.hObj))
        CumuDenomList.append(MakeCumu(denom.hObj))

    DiffTurnOn = TurnOn(DiffNomList,DiffDenomList)
    for nom,denom in zip(DiffTurnOn.numerator,DiffTurnOn.denominator):
      if "alpha" in axisTitle:
        denom.GetYaxis().SetTitle("Events / %1.4f"%(denom.GetBinWidth(1)))
        denom.GetXaxis().SetRangeUser(0.,3.)
      if "H_" in axisTitle:
        denom.GetYaxis().SetTitle("Events / %1.f GeV"%(denom.GetBinWidth(1)))
        denom.GetXaxis().SetRangeUser(0.,1000.)

      denom.GetYaxis().SetLabelSize(0.035)
      denom.GetYaxis().SetTitleOffset(1.3)
      denom.Draw("h")
      nom.Draw("psame")
      c1.SetLog('y',True)
      c1.Print()
      c1.SetLog('y',False)
    DiffTurnOn.TotDenominator.SetTitle("Total Differential Hists for %s"%(key))
    if "alpha" in axisTitle:
      DiffTurnOn.TotDenominator.GetYaxis().SetTitle("Events / %1.4f"%(DiffTurnOn.TotDenominator.GetBinWidth(1)))
      DiffTurnOn.TotDenominator.GetXaxis().SetRangeUser(0.,3.)
    if "H_" in axisTitle:
      DiffTurnOn.TotDenominator.GetYaxis().SetTitle("Events / %1.f GeV"%(DiffTurnOn.TotDenominator.GetBinWidth(1)))
      DiffTurnOn.TotDenominator.GetXaxis().SetRangeUser(0.,1000.)
    DiffTurnOn.TotDenominator.GetYaxis().SetLabelSize(0.035)
    DiffTurnOn.TotDenominator.GetYaxis().SetTitleOffset(1.3)
    c1.SetLog('y',True)
    DiffTurnOn.TotDenominator.Draw("h")
    DiffTurnOn.TotNumerator.Draw("psame")
    c1.Print()
    c1.SetLog('y',False)
    for curve in DiffTurnOn.listOfTurnOns:
      if"AlphaT" in key: curve.GetXaxis().SetRangeUser(0.,3.)
      else: curve.GetXaxis().SetRangeUser(0.,1000.)
      print "="*25
      print "Differential Turn on for %s"%(Dir)
      print "="*25
      # curve.SetTitle("Differential Turn on for %s"%(Dir))
      curve.GetXaxis().SetTitle(axisTitle)
      curve.GetYaxis().SetTitle("Efficiency")
      curve.GetXaxis().SetTitleSize(0.045)
      curve.GetYaxis().SetTitleOffset(1.15)
      curve.Draw("ap")
      c1.Print()
    FinalDiff = DiffTurnOn.SumOfTurnOns()
    FinalDiff.SetTitle("Total Differential Turn on for %s"%(key))
    FinalDiff.GetXaxis().SetTitle(axisTitle)
    if"AlphaT" in key: FinalDiff.GetXaxis().SetRangeUser(0.,3.)
    else: FinalDiff.GetXaxis().SetRangeUser(0.,1000.)
    FinalDiff.GetYaxis().SetTitle("Efficiency")
    FinalDiff.GetYaxis().SetTitleOffset(1.15)
    FinalDiff.GetXaxis().SetTitleSize(0.045)
    FinalDiff.Draw("ap")
    c1.Print()
    xVal = r.Double(0)
    yVal = r.Double(0)
    point = []
    for gPoint in range(FinalDiff.GetN()):
      FinalDiff.GetPoint(gPoint,xVal,yVal)
      if "AlphaT" in key:
        text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Differential \n"%(key,xVal,yVal,FinalDiff.GetErrorYhigh(gPoint),FinalDiff.GetErrorYlow(gPoint)))
      else:text +=("%s at %3.0f %1.3f + %1.3f - %1.3f efficient  Differential \n"%(key,xVal,yVal,FinalDiff.GetErrorYhigh(gPoint),FinalDiff.GetErrorYlow(gPoint)))

    CumuTurnOn = TurnOn(CumuNomList,CumuDenomList)
    for curve in CumuTurnOn.ListOfTurnOns():
      # curve.SetTitle("Cumulative Turn on for %s"%(Dir))
      curve.GetXaxis().SetTitle(axisTitle)
      curve.GetXaxis().SetTitleSize(0.045)
      curve.GetYaxis().SetTitle("Cumulative Efficiency")
      curve.GetYaxis().SetTitleOffset(1.15)
      if"AlphaT" in key: curve.GetXaxis().SetRangeUser(0.,3.)
      else: curve.GetXaxis().SetRangeUser(0.,1000.)
      curve.Draw("ap")
      c1.Print()
    CumuTurnOn.TotDenominator.SetTitle("Total Cumulative Hists for %s"%(key))
    if "alpha" in axisTitle:
      CumuTurnOn.TotDenominator.GetYaxis().SetTitle("Cumulative Events / %1.4f"%(CumuTurnOn.TotDenominator.GetBinWidth(1)))
      CumuTurnOn.TotDenominator.GetXaxis().SetRangeUser(0.,3.)
    if "H_" in axisTitle:
      CumuTurnOn.TotDenominator.GetYaxis().SetTitle("Cumulative Events / %1.f GeV"%(CumuTurnOn.TotDenominator.GetBinWidth(1)))
    CumuTurnOn.TotDenominator.GetYaxis().SetLabelSize(0.035)
    CumuTurnOn.TotDenominator.GetYaxis().SetTitleOffset(1.3)
    CumuTurnOn.TotDenominator.Draw("h")
    CumuTurnOn.TotNumerator.Draw("psame")
    c1.SetLog('y',True)
    c1.Print()
    c1.SetLog('y',False)
    FinalCumu = CumuTurnOn.SumOfTurnOns()
    FinalCumu.SetTitle("Total Cumulative Turn on for %s"%(key))
    FinalCumu.GetXaxis().SetTitle(axisTitle)
    if "AlphaT" in key: 
        FinalCumu.GetXaxis().SetRangeUser(0.,3.)
        FinalCumu.GetXaxis().SetTitle("#alpha_{T}^{cut}")
    if "AlphaT" not in key: 
        FinalCumu.GetXaxis().SetRangeUser(0.,1000.)
        FinalCumu.GetXaxis().SetTitle("H_{T}^{cut}")
    FinalCumu.GetYaxis().SetTitle("Cumulative Efficiency")
    FinalCumu.GetYaxis().SetTitleOffset(1.15)
    FinalCumu.GetXaxis().SetTitleSize(0.045)
    # c1.SetLog('y',True)
    FinalCumu.Draw("ap")
    c1.Print()
    # c1.SetLog('y',False)
    xVal = r.Double(0)
    yVal = r.Double(0)
    c1.close()

    point = []
    # for Point in range(FinalCumu.GetN()):
    #   FinalCumu.GetPoint(Point,xVal,yVal)
    #   print "XVAL =",xVal
    #   if "AlphaT" in key:
    #     if xVal > 0.60 and xVal < 0.61:
    #       text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Cumu \n"%(key,xVal-0.005,yVal,FinalCumu.GetErrorYhigh(Point),FinalCumu.GetErrorYlow(Point)))
    #   else:text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Cumu \n"%(key,xVal,yVal,FinalCumu.GetErrorYhigh(Point),FinalCumu.GetErrorYlow(Point)))


    # if "AlphaT" in key:
    #   for x in [0.6]: point.append(x)
    # else:
    #   for x in [875.]:
    #     point.append(x)
    # for p in point:
    #   val = FinalDiff.Eval(p+ 0.005)
    #   for gPoint in range(FinalDiff.GetN()):
    #     FinalDiff.GetPoint(gPoint,xVal,yVal)
    #     xValue = int("%d"%(p*1000))
    #     if xValue == int("%d"%((xVal-0.005)*1000)):
    #       # print xVal-(DiffTurnOn.TotDenominator.GetBinWidth(1)/2.) ,DiffTurnOn.TotDenominator.GetBinLowEdge(p+1)
    #       text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Cumu\n"%(key,xVal-(CumuTurnOn.TotDenominator.GetBinWidth(1)/2.),yVal,FinalCumu.GetErrorYhigh(gPoint),FinalCumu.GetErrorYlow(gPoint)))
    #       break

  outFile = open("./EfficienciesForAllDiffPlotFinalAlphaTPlotBinning.txt",'w')
  outFile.write(text)
  # print text

if __name__ == '__main__':
  main()

