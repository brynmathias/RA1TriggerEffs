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






"Denom_HLT_HT250_v2Pre_15_HLT_Mu5_HT200_v4Pre_1",
"Denom_HLT_HT250_v2Pre_25_HLT_Mu5_HT200_v4Pre_1",
"Denom_HLT_HT250_v2Pre_35_HLT_Mu5_HT200_v4Pre_1",
"Denom_HLT_HT250_v3Pre_150_HLT_Mu8_HT200_v4Pre_1",
"Denom_HLT_HT250_v3Pre_200_HLT_Mu8_HT200_v4Pre_1",
"Denom_HLT_HT250_v3Pre_90_HLT_Mu8_HT200_v4Pre_1",
"Denom_HLT_HT250_v4Pre_150_HLT_Mu15_HT200_v2Pre_1",
"Denom_HLT_HT250_v4Pre_200_HLT_Mu15_HT200_v2Pre_1",
"Denom_HLT_HT250_v4Pre_240_HLT_Mu15_HT200_v2Pre_1",
"Denom_HLT_HT250_v4Pre_60_HLT_Mu15_HT200_v2Pre_1",
"Denom_HLT_HT250_v5Pre_180_HLT_Mu15_HT200_v3Pre_1",
"Denom_HLT_HT250_v5Pre_200_HLT_Mu15_HT200_v3Pre_1",
"Denom_HLT_HT250_v5Pre_400_HLT_Mu15_HT200_v3Pre_1",
"Denom_HLT_HT250_v6Pre_200_HLT_Mu15_HT200_v4Pre_1",
"Denom_HLT_HT250_v7Pre_150_HLT_Mu30_HT200_v1Pre_1",
"Denom_HLT_HT250_v7Pre_200_HLT_Mu30_HT200_v1Pre_1",
"Denom_HLT_HT250_v7Pre_290_HLT_Mu30_HT200_v1Pre_1",
"Denom_HLT_HT250_v7Pre_85_HLT_Mu30_HT200_v1Pre_1",






def main():
  dirList = ["DEBUG_DiMu_HT0_HLT_HT250_v2_HLT_Mu5_HT200_v4"  ,
"DEBUG_DiMu_HT0_HLT_HT250_v2_HLT_Mu5_HT200_v4"  ,
"DEBUG_DiMu_HT0_HLT_HT250_v2_HLT_Mu5_HT200_v4"  ,
"DEBUG_DiMu_HT0_HLT_HT250_v3_HLT_Mu8_HT200_v4"  ,
"DEBUG_DiMu_HT0_HLT_HT250_v3_HLT_Mu8_HT200_v4"  ,
"DEBUG_DiMu_HT0_HLT_HT250_v3_HLT_Mu8_HT200_v4"  ,
"DEBUG_DiMu_HT0_HLT_HT250_v4_HLT_Mu15_HT200_v2",
"DEBUG_DiMu_HT0_HLT_HT250_v4_HLT_Mu15_HT200_v2",
"DEBUG_DiMu_HT0_HLT_HT250_v4_HLT_Mu15_HT200_v2",
"DEBUG_DiMu_HT0_HLT_HT250_v4_HLT_Mu15_HT200_v2",
"DEBUG_DiMu_HT0_HLT_HT250_v5_HLT_Mu15_HT200_v3",
"DEBUG_DiMu_HT0_HLT_HT250_v5_HLT_Mu15_HT200_v3",
"DEBUG_DiMu_HT0_HLT_HT250_v5_HLT_Mu15_HT200_v3",
"DEBUG_DiMu_HT0_HLT_HT250_v6_HLT_Mu15_HT200_v4",
"DEBUG_DiMu_HT0_HLT_HT250_v7_HLT_Mu30_HT200_v1",
"DEBUG_DiMu_HT0_HLT_HT250_v7_HLT_Mu30_HT200_v1",
"DEBUG_DiMu_HT0_HLT_HT250_v7_HLT_Mu30_HT200_v1",
"DEBUG_DiMu_HT0_HLT_HT250_v7_HLT_Mu30_HT200_v1",]

  histList = ["Nom_HLT_HT250_v2Pre_15_HLT_Mu5_HT200_v4Pre_1",
"Nom_HLT_HT250_v2Pre_25_HLT_Mu5_HT200_v4Pre_1",
"Nom_HLT_HT250_v2Pre_35_HLT_Mu5_HT200_v4Pre_1",
"Nom_HLT_HT250_v3Pre_150_HLT_Mu8_HT200_v4Pre_1",
"Nom_HLT_HT250_v3Pre_200_HLT_Mu8_HT200_v4Pre_1",
"Nom_HLT_HT250_v3Pre_90_HLT_Mu8_HT200_v4Pre_1",
"Nom_HLT_HT250_v4Pre_150_HLT_Mu15_HT200_v2Pre_1",
"Nom_HLT_HT250_v4Pre_200_HLT_Mu15_HT200_v2Pre_1",
"Nom_HLT_HT250_v4Pre_240_HLT_Mu15_HT200_v2Pre_1",
"Nom_HLT_HT250_v4Pre_60_HLT_Mu15_HT200_v2Pre_1",
"Nom_HLT_HT250_v5Pre_180_HLT_Mu15_HT200_v3Pre_1",
"Nom_HLT_HT250_v5Pre_200_HLT_Mu15_HT200_v3Pre_1",
"Nom_HLT_HT250_v5Pre_400_HLT_Mu15_HT200_v3Pre_1",
"Nom_HLT_HT250_v6Pre_200_HLT_Mu15_HT200_v4Pre_1",
"Nom_HLT_HT250_v7Pre_150_HLT_Mu30_HT200_v1Pre_1",
"Nom_HLT_HT250_v7Pre_200_HLT_Mu30_HT200_v1Pre_1",
"Nom_HLT_HT250_v7Pre_290_HLT_Mu30_HT200_v1Pre_1",
"Nom_HLT_HT250_v7Pre_85_HLT_Mu30_HT200_v1Pre_1", ]

  histList2 = ["Denom_HLT_HT250_v2Pre_15_HLT_Mu5_HT200_v4Pre_1",
"Denom_HLT_HT250_v2Pre_25_HLT_Mu5_HT200_v4Pre_1",
"Denom_HLT_HT250_v2Pre_35_HLT_Mu5_HT200_v4Pre_1",
"Denom_HLT_HT250_v3Pre_150_HLT_Mu8_HT200_v4Pre_1",
"Denom_HLT_HT250_v3Pre_200_HLT_Mu8_HT200_v4Pre_1",
"Denom_HLT_HT250_v3Pre_90_HLT_Mu8_HT200_v4Pre_1",
"Denom_HLT_HT250_v4Pre_150_HLT_Mu15_HT200_v2Pre_1",
"Denom_HLT_HT250_v4Pre_200_HLT_Mu15_HT200_v2Pre_1",
"Denom_HLT_HT250_v4Pre_240_HLT_Mu15_HT200_v2Pre_1",
"Denom_HLT_HT250_v4Pre_60_HLT_Mu15_HT200_v2Pre_1",
"Denom_HLT_HT250_v5Pre_180_HLT_Mu15_HT200_v3Pre_1",
"Denom_HLT_HT250_v5Pre_200_HLT_Mu15_HT200_v3Pre_1",
"Denom_HLT_HT250_v5Pre_400_HLT_Mu15_HT200_v3Pre_1",
"Denom_HLT_HT250_v6Pre_200_HLT_Mu15_HT200_v4Pre_1",
"Denom_HLT_HT250_v7Pre_150_HLT_Mu30_HT200_v1Pre_1",
"Denom_HLT_HT250_v7Pre_200_HLT_Mu30_HT200_v1Pre_1",
"Denom_HLT_HT250_v7Pre_290_HLT_Mu30_HT200_v1Pre_1",
"Denom_HLT_HT250_v7Pre_85_HLT_Mu30_HT200_v1Pre_1",]





  weightList =[15.,25.,35.,150.,200.,90.,150.,200.,240.,60.,180.,200.,400.,200.,150.,200.,290.,85.]
  c1 = Print("HT250Try.pdf")
  c1.open()
  rFile = r.TFile().Open("./5GeVMuonsVBTFIDWithOddMuonVeto/5GeVMuonsOddVetoVBTFidHT275.root")
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
  denomError = 0.
  Total = 0.
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
    currentCumu = MakeCumu(currentDenom)
    for bin in range(currentCumu.GetNbinsX()):
      if int(currentCumu.GetBinLowEdge(bin)) == 275:
        Total += currentCumu.GetBinContent(bin)
        print"Val = %f, Error = %f"%(currentCumu.GetBinContent(bin),currentCumu.GetBinError(bin))
        denomError += (currentCumu.GetBinError(bin))**2
  print"Error on HT275 bin is %f, Content is %f, sqrt Content = %f, diff = %f"%(math.sqrt(denomError),Total,math.sqrt(Total), math.sqrt(denomError)- math.sqrt(Total))
  # nomHist.Rebin(25)
  # denomHist.Rebin(25)
  nomHist.SetMarkerStyle(20)
  denomHist.SetLineColor(2)
  nomHist.Draw("p")
  nomHist.SetTitle("")
  denomHist.Draw("sameh")
  c1.Print()
  a = nomHist.Clone()
  a.Divide(denomHist)
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
    if int(b.GetBinLowEdge(bin)) == 275:
      print"X = %f, Red = %f pm %f"%(b.GetBinLowEdge(bin),b.GetBinContent(bin), b.GetBinError(bin))


  b.GetYaxis().SetRangeUser(0.,1.2)
  b.Draw("p")
  c1.Print()
  c1.close()

if __name__ == '__main__':
  main()

