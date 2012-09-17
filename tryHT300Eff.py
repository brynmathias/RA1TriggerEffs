#!/usr/bin/env python
# encoding: utf-8
"""
tryHT250Eff.py

Created by Bryn Mathias on 2011-12-01.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
import ROOT as r
from plottingUtils import *




def MakeCumu(inHist):
    cumulativeHist = inHist.Clone()
    maxbin = inHist.GetNbinsX()
    for bin in range(0,maxbin):
      err = r.Double(0)
      val = inHist.IntegralAndError(bin, maxbin, err)
      cumulativeHist.SetBinContent(bin,val)
      cumulativeHist.SetBinError(bin,err)
    return cumulativeHist



"Denom_HLT_HT300_v12Pre_1000_HLT_DoubleMu8_Mass8_HT200_v4Pre_1",
"Denom_HLT_HT300_v3Pre_10_HLT_Mu5_HT200_v4Pre_1"                ,
"Denom_HLT_HT300_v3Pre_15_HLT_Mu5_HT200_v4Pre_1"                ,
"Denom_HLT_HT300_v3Pre_7_HLT_Mu5_HT200_v4Pre_1"                 ,
"Denom_HLT_HT300_v4Pre_100_HLT_Mu8_HT200_v4Pre_1"             ,
"Denom_HLT_HT300_v4Pre_150_HLT_Mu8_HT200_v4Pre_1"             ,
"Denom_HLT_HT300_v4Pre_200_HLT_Mu8_HT200_v4Pre_1"             ,
"Denom_HLT_HT300_v4Pre_60_HLT_Mu8_HT200_v4Pre_1"              ,
"Denom_HLT_HT300_v5Pre_120_HLT_Mu15_HT200_v2Pre_1"            ,
"Denom_HLT_HT300_v5Pre_200_HLT_Mu15_HT200_v2Pre_1"            ,
"Denom_HLT_HT300_v5Pre_240_HLT_Mu15_HT200_v2Pre_1"            ,
"Denom_HLT_HT300_v5Pre_60_HLT_Mu15_HT200_v2Pre_1"             ,
"Denom_HLT_HT300_v6Pre_120_HLT_Mu15_HT200_v3Pre_1"            ,
"Denom_HLT_HT300_v6Pre_80_HLT_Mu15_HT200_v3Pre_1"             ,
"Denom_HLT_HT300_v8Pre_100_HLT_Mu30_HT200_v1Pre_1"            ,
"Denom_HLT_HT300_v8Pre_150_HLT_Mu30_HT200_v1Pre_1"            ,
"Denom_HLT_HT300_v8Pre_40_HLT_Mu30_HT200_v1Pre_1"             ,
"Denom_HLT_HT300_v8Pre_70_HLT_Mu30_HT200_v1Pre_1"             ,





def main():
  dirList = ["DEBUG_DiMu_HT0_HLT_HT300_v12_HLT_DoubleMu8_Mass8_HT200_v4",
"DEBUG_DiMu_HT0_HLT_HT300_v3_HLT_Mu5_HT200_v4",
"DEBUG_DiMu_HT0_HLT_HT300_v3_HLT_Mu5_HT200_v4",
"DEBUG_DiMu_HT0_HLT_HT300_v3_HLT_Mu5_HT200_v4",
"DEBUG_DiMu_HT0_HLT_HT300_v4_HLT_Mu8_HT200_v4",
"DEBUG_DiMu_HT0_HLT_HT300_v4_HLT_Mu8_HT200_v4",
"DEBUG_DiMu_HT0_HLT_HT300_v4_HLT_Mu8_HT200_v4",
"DEBUG_DiMu_HT0_HLT_HT300_v4_HLT_Mu8_HT200_v4",
"DEBUG_DiMu_HT0_HLT_HT300_v5_HLT_Mu15_HT200_v2",
"DEBUG_DiMu_HT0_HLT_HT300_v5_HLT_Mu15_HT200_v2",
"DEBUG_DiMu_HT0_HLT_HT300_v5_HLT_Mu15_HT200_v2",
"DEBUG_DiMu_HT0_HLT_HT300_v5_HLT_Mu15_HT200_v2",
"DEBUG_DiMu_HT0_HLT_HT300_v6_HLT_Mu15_HT200_v3",
"DEBUG_DiMu_HT0_HLT_HT300_v6_HLT_Mu15_HT200_v3",
"DEBUG_DiMu_HT0_HLT_HT300_v8_HLT_Mu30_HT200_v1",
"DEBUG_DiMu_HT0_HLT_HT300_v8_HLT_Mu30_HT200_v1",
"DEBUG_DiMu_HT0_HLT_HT300_v8_HLT_Mu30_HT200_v1",
"DEBUG_DiMu_HT0_HLT_HT300_v8_HLT_Mu30_HT200_v1",]

  histList = ["Nom_HLT_HT300_v12Pre_1000_HLT_DoubleMu8_Mass8_HT200_v4Pre_1",
"Nom_HLT_HT300_v3Pre_10_HLT_Mu5_HT200_v4Pre_1"                ,
"Nom_HLT_HT300_v3Pre_15_HLT_Mu5_HT200_v4Pre_1"                ,
"Nom_HLT_HT300_v3Pre_7_HLT_Mu5_HT200_v4Pre_1"                 ,
"Nom_HLT_HT300_v4Pre_100_HLT_Mu8_HT200_v4Pre_1"             ,
"Nom_HLT_HT300_v4Pre_150_HLT_Mu8_HT200_v4Pre_1"             ,
"Nom_HLT_HT300_v4Pre_200_HLT_Mu8_HT200_v4Pre_1"             ,
"Nom_HLT_HT300_v4Pre_60_HLT_Mu8_HT200_v4Pre_1"              ,
"Nom_HLT_HT300_v5Pre_120_HLT_Mu15_HT200_v2Pre_1"            ,
"Nom_HLT_HT300_v5Pre_200_HLT_Mu15_HT200_v2Pre_1"            ,
"Nom_HLT_HT300_v5Pre_240_HLT_Mu15_HT200_v2Pre_1"            ,
"Nom_HLT_HT300_v5Pre_60_HLT_Mu15_HT200_v2Pre_1"             ,
"Nom_HLT_HT300_v6Pre_120_HLT_Mu15_HT200_v3Pre_1"            ,
"Nom_HLT_HT300_v6Pre_80_HLT_Mu15_HT200_v3Pre_1"             ,
"Nom_HLT_HT300_v8Pre_100_HLT_Mu30_HT200_v1Pre_1"            ,
"Nom_HLT_HT300_v8Pre_150_HLT_Mu30_HT200_v1Pre_1"            ,
"Nom_HLT_HT300_v8Pre_40_HLT_Mu30_HT200_v1Pre_1"             ,
"Nom_HLT_HT300_v8Pre_70_HLT_Mu30_HT200_v1Pre_1"             ,]

  histList2 = ["Denom_HLT_HT300_v12Pre_1000_HLT_DoubleMu8_Mass8_HT200_v4Pre_1",
"Denom_HLT_HT300_v3Pre_10_HLT_Mu5_HT200_v4Pre_1"                ,
"Denom_HLT_HT300_v3Pre_15_HLT_Mu5_HT200_v4Pre_1"                ,
"Denom_HLT_HT300_v3Pre_7_HLT_Mu5_HT200_v4Pre_1"                 ,
"Denom_HLT_HT300_v4Pre_100_HLT_Mu8_HT200_v4Pre_1"             ,
"Denom_HLT_HT300_v4Pre_150_HLT_Mu8_HT200_v4Pre_1"             ,
"Denom_HLT_HT300_v4Pre_200_HLT_Mu8_HT200_v4Pre_1"             ,
"Denom_HLT_HT300_v4Pre_60_HLT_Mu8_HT200_v4Pre_1"              ,
"Denom_HLT_HT300_v5Pre_120_HLT_Mu15_HT200_v2Pre_1"            ,
"Denom_HLT_HT300_v5Pre_200_HLT_Mu15_HT200_v2Pre_1"            ,
"Denom_HLT_HT300_v5Pre_240_HLT_Mu15_HT200_v2Pre_1"            ,
"Denom_HLT_HT300_v5Pre_60_HLT_Mu15_HT200_v2Pre_1"             ,
"Denom_HLT_HT300_v6Pre_120_HLT_Mu15_HT200_v3Pre_1"            ,
"Denom_HLT_HT300_v6Pre_80_HLT_Mu15_HT200_v3Pre_1"             ,
"Denom_HLT_HT300_v8Pre_100_HLT_Mu30_HT200_v1Pre_1"            ,
"Denom_HLT_HT300_v8Pre_150_HLT_Mu30_HT200_v1Pre_1"            ,
"Denom_HLT_HT300_v8Pre_40_HLT_Mu30_HT200_v1Pre_1"             ,
"Denom_HLT_HT300_v8Pre_70_HLT_Mu30_HT200_v1Pre_1"             ,]


  weightList =[  1000.,   10.,  15.,  7.,   100.,  150.,  200.,  60.,  120.,  200.,  240.,  60.,  120.,  80.,  100.,  150.,  40.,  70.,]
  c1 = Print("HT300Try.pdf")
  c1.DoPageNum = False
  
  c1.open()
  rFile = r.TFile().Open("./5GeVMuonsVBTFIDWithOddMuonVeto/5GeVMuonsOddVetoVBTFidHT325.root")
  nomHist = None
  denomHist = None
  eh =  [1.15, 1.36, 1.53, 1.73, 1.98, 2.21, 2.42, 2.61, 2.80, 3.00 ]
  el =  [0.00, 1.00, 2.00, 2.14, 2.30, 2.49, 2.68, 2.86, 3.03, 3.19 ]
  for dir,hist,weight in zip(dirList,histList,weightList):
    curFile = rFile.Get(dir)
    currentHist = curFile.Get(hist)
    print currentHist.GetName()
    print type(currentHist)
    currentHist.Rebin(25)
    for bin in range(currentHist.GetNbinsX()):
      error = math.sqrt(((currentHist.GetBinContent(bin)+1)*weight)-1)
      value = currentHist.GetBinContent(bin)*weight
      currentHist.SetBinContent(bin,value)
      currentHist.SetBinError(bin,error)
    if nomHist is None:
      nomHist = currentHist.Clone()
      # nomHist.Scale(weight)
    else:
      nomHist.Add(currentHist)
  for dir,hist in zip(dirList,histList2):
    curFile = rFile.Get(dir)
    currentDenom = curFile.Get(hist)
    currentDenom.Rebin(25)
    for bin in range(currentDenom.GetNbinsX()):
      if currentDenom.GetBinContent(bin) < 10.:
        n = int(currentDenom.GetBinContent(bin))
        currentDenom.SetBinError(bin,max(eh[n],el[n]))
    if denomHist is None:
      denomHist = currentDenom.Clone()
    else:
      denomHist.Add(currentDenom)
  # nomHist.Rebin(25)
  # denomHist.Rebin(25)
  nomHist.SetMarkerStyle(20)
  denomHist.SetLineColor(2)
  nomHist.Draw("p")
  denomHist.Draw("sameh")
  c1.Print()
  bins = [i*25. for i in range(int(325./25.)) ]+[325.,1000.]
  a = nomHist.Rebin(len(bins) -1 ,"a",array.array('d',  bins))
  b = denomHist.Rebin(len(bins) - 1,"b",array.array('d',bins))
  a.Divide(b)
  a.GetXaxis().SetTitle("H_{T} (GeV)")
  a.GetYaxis().SetTitle("Efficiency")
  a.SetTitle("")
  a.Draw("p")
  a.GetYaxis().SetRangeUser(0.,1.2)
  c1.Print()
  cumuNom = MakeCumu(nomHist)
  cumuDenom = MakeCumu(denomHist)
  cumuNom.Draw("p")
  cumuDenom.Draw("histsame")
  c1.Print()
  b = cumuNom.Clone()
  b.Divide(cumuDenom)
  for bin in range(b.GetNbinsX()):
    if int(b.GetBinLowEdge(bin)) == 325:
      print"X = %f, Red = %f pm %f"%(b.GetBinLowEdge(bin),b.GetBinContent(bin), b.GetBinError(bin))
  b.GetYaxis().SetRangeUser(0.,1.2)
  b.Draw("p")
  c1.Print()
  c1.close()
if __name__ == '__main__':
  main()

