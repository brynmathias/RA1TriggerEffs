#!/usr/bin/env python
# encoding: utf-8
"""
TEffiencyCombineTest.py

Created by Bryn Mathias on 2011-12-08.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *
import array

def MakeCumu(inHist):
    cumulativeHist = inHist.Clone()
    maxbin = inHist.GetNbinsX()
    for bin in range(0,maxbin):
      err = r.Double(0)
      val = inHist.IntegralAndError(bin, maxbin, err)
      cumulativeHist.SetBinContent(bin,val)
      cumulativeHist.SetBinError(bin,err)
    return cumulativeHist



def main():
  outfile = open("./275Bin.txt",'w')
  c1 = Print("./275Bin.pdf")
  text = ""
  histList = ("AlphaT_Nom","AlphaT_Denom")
  # histList = ("HT_Nom","HT_Denom")


  sums ={



# "HT375":(["HLT_HT350_v11_HLT_HT250_v11","HLT_HT350_v2_HLT_HT250_v2","HLT_HT350_v3_HLT_HT250_v3","HLT_HT350_v4_HLT_HT250_v4","HLT_HT350_v5_HLT_HT250_v5","HLT_HT350_v6_HLT_HT250_v6","HLT_HT350_v7_HLT_HT250_v7","HLT_HT350_v8_HLT_HT250_v8"],[710.363,38.307,160.689,135.443,465.518,4.291,194.938,2220.]),
#   # "HT475":(["HLT_HT450_v11_HLT_HT250_v11","HLT_HT450_v2_HLT_HT250_v2","HLT_HT450_v3_HLT_HT250_v3","HLT_HT450_v4_HLT_HT250_v4","HLT_HT450_v5_HLT_HT250_v5","HLT_HT450_v6_HLT_HT250_v6","HLT_HT450_v7_HLT_HT250_v7","HLT_HT450_v8_HLT_HT250_v8",],[710.363,38.307,160.689,135.443,465.518,4.291,194.938,2220.]),
#   "HT575":(["HLT_HT550_v11_HLT_HT250_v11","HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT550_v8_HLT_HT250_v8",],[710.363,38.307,160.689,135.443,465.518,4.291,194.938,2220.]),
#   "HT675":(["HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT600_v1_HLT_HT250_v8","HLT_HT600_v4_HLT_HT250_v11",],[38.307,160.689,135.443,465.518,4.291,2220.,710.363]),
#   "HT775":(["HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT600_v1_HLT_HT250_v8","HLT_HT700_v2_HLT_HT250_v11",],[38.307,160.689,135.443,465.518,4.291,2220.,710.363]),
#   "HT875":(["HLT_HT550_v2_HLT_HT250_v2","HLT_HT550_v3_HLT_HT250_v3","HLT_HT550_v4_HLT_HT250_v4","HLT_HT550_v5_HLT_HT250_v5","HLT_HT550_v6_HLT_HT250_v6","HLT_HT550_v7_HLT_HT250_v7","HLT_HT600_v1_HLT_HT250_v8","HLT_HT750_v3_HLT_HT250_v11",],[38.307,160.689,135.443,465.518,4.291,2220.,710.363]),

# "AllFromHT400":(["HLT_HT400_v2_HLT_HT250_v2","HLT_HT400_v3_HLT_HT250_v3","HLT_HT400_v4_HLT_HT250_v4","HLT_HT400_v5_HLT_HT250_v5","HLT_HT400_v6_HLT_HT250_v6","HLT_HT400_v7_HLT_HT250_v7","HLT_HT400_v8_HLT_HT250_v8","HLT_HT400_v11_HLT_HT250_v11"],[38.307,160.689,135.443,465.518,4.291,2220.,710.363]),

# 40.9 HT275_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4
        # HT275_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4
# 119.0  HT275_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2
# 403.9   HT275_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3
# 3.8   HT275_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4
# 186.0 HT275_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1
# 2880.0  HT275_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4
# 811.8 = 4445.4   DiMu_HT275_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4









"HT275":([
"HT275_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4",                                # 40.9
"HT275_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4",                               # 168.6
"HT275_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",                               # 119.0
"HT275_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",                               # 403.9
"HT275_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",                               # 3.8
"HT275_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",                               # 186.0
"DiMu_HT275_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4",               #
"DiMu_HT275_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5",               # 811.0
# "DiMu_HT275_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4",              4445.0
# "DiMu_HT275_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
],[40.352,2880.0,119.04,385.241,3.756,204.618,694.178,117.644],
),
# "HT325":([
# "HT325_HLT_HT300_AlphaT0p52_v1_HLT_Mu5_HT200_v4",
# "HT325_HLT_HT300_AlphaT0p52_v2_HLT_Mu8_HT200_v4",
# "HT325_HLT_HT300_AlphaT0p52_v3_HLT_Mu15_HT200_v2",
# "HT325_HLT_HT300_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
# "HT325_HLT_HT300_AlphaT0p53_v4_HLT_Mu15_HT200_v4",
# "HT325_HLT_HT300_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
# "HT325_HLT_HT300_AlphaT0p53_v6_HLT_Mu40_HT200_v3",
# "HT325_HLT_HT300_AlphaT0p53_v6_HLT_Mu40_HT200_v4",
# "HT325_HLT_HT300_AlphaT0p54_v5_HLT_Mu40_HT300_v4",
# "HT325_HLT_HT300_AlphaT0p54_v5_HLT_Mu40_HT300_v5",
# "DiMu_HT325_HLT_HT300_AlphaT0p55_v3_HLT_DoubleMu8_Mass8_HT200_v4",
# "DiMu_HT325_HLT_HT300_AlphaT0p55_v3_HLT_DoubleMu8_Mass8_HT200_v5",
# ],[40.352,158.567,119.04,385.241,
# 3.756,204.618,766.599,
# 694.178,117.644,694.178,117.644,]),


#   "HT375":([
# "HT375_HLT_HT350_AlphaT0p51_v1_HLT_Mu5_HT200_v4",
# "HT375_HLT_HT350_AlphaT0p51_v2_HLT_Mu8_HT200_v4",
# "HT375_HLT_HT350_AlphaT0p51_v3_HLT_Mu15_HT200_v2",
# "HT375_HLT_HT350_AlphaT0p51_v4_HLT_Mu15_HT200_v3",
# "HT375_HLT_HT350_AlphaT0p51_v5_HLT_Mu15_HT200_v4",
# "HT375_HLT_HT350_AlphaT0p52_v1_HLT_Mu30_HT200_v1",
# "HT375_HLT_HT350_AlphaT0p52_v2_HLT_Mu40_HT200_v3",
# "HT375_HLT_HT350_AlphaT0p52_v2_HLT_Mu40_HT200_v4",
# "HT375_HLT_HT350_AlphaT0p53_v10_HLT_Mu40_HT300_v4",
# "HT375_HLT_HT350_AlphaT0p53_v10_HLT_Mu40_HT300_v5",
# ],[40.352,158.567,119.04,385.241,3.756,204.618,766.599,1941.,694.178,117.644,]),
# "HT475":([
# "HT475_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4",
# "HT475_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4",
# "HT475_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2",
# "HT475_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3",
# "HT475_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4",
# "HT475_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1",
# "HT475_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3",
# "HT475_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4",
# "HT475_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4",
# "HT475_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5",
# "HT475_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4",
# "HT475_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
# ],[40.352,158.567,119.04,385.241,3.756,204.618,766.599,1941.,694.178,117.644,]),
#
# "HT575":([
# "HT575_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4",
# "HT575_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4",
# "HT575_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2",
# "HT575_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3",
# "HT575_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4",
# "HT575_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1",
# "HT575_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3",
# "HT575_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4",
# "HT575_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4",
# "HT575_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5",
# "HT575_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4",
# "HT575_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
# ],[40.352,158.567,119.04,385.241,3.756,204.618,766.599,1941.,694.178,117.644,]),
# "HT675":([
# "HT675_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4",
# "HT675_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4",
# "HT675_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2",
# "HT675_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3",
# "HT675_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4",
# "HT675_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1",
# "HT675_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3",
# "HT675_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4",
# "HT675_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4",
# "HT675_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5",
# "HT675_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4",
# "HT675_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
# ],[40.352,158.567,119.04,385.241,3.756,204.618,766.599,1941.,694.178,117.644,]),
# "HT775":([
# "HT775_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4",
# "HT775_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4",
# "HT775_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2",
# "HT775_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3",
# "HT775_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4",
# "HT775_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1",
# "HT775_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3",
# "HT775_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4",
# "HT775_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4",
# "HT775_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5",
# "HT775_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4",
# "HT775_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
# ],[40.352,158.567,119.04,385.241,3.756,204.618,766.599,1941.,694.178,117.644,]),
# "HT875":([
# "HT875_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4",
# "HT875_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4",
# "HT875_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2",
# "HT875_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3",
# "HT875_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4",
# "HT875_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1",
# "HT875_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v3",
# "HT875_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4",
# "HT875_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v4",
# "HT875_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5",
# "HT875_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v4",
# "HT875_HLT_HT400_AlphaT0p52_v5_HLT_Mu40_HT300_v5",
# ],[40.352,158.567,119.04,385.241,3.756,204.618,766.599,1941.,694.178,117.644,]),


  }
  c1.open()
  for key,values in sums.iteritems():
    nomList = []
    denomList = []
    TEffList = []
    TEffListCumu = []
    CumuNomList = []
    CumuDenomList = []
    for Dir in values[0]:
      print Dir
      nomList.append(GetSumHist(File = [".//5GeVMuonsVBTFIDWithOddMuonVeto/5GeVMuonsOddVetoVBTFidHT275.root"], Directories = [Dir], Hist = histList[0], Col = r.kBlack, Norm = None, LegendText = ""))
      denomList.append(GetSumHist(File = [".//5GeVMuonsVBTFIDWithOddMuonVeto/5GeVMuonsOddVetoVBTFidHT275.root"], Directories = [Dir], Hist = histList[1], Col = r.kRed,   Norm = None, LegendText = ""))
    for nom,denom in zip(nomList,denomList):
      c1.SetLog('y',True)
      # denom.Rebin(25,None)
      # nom.Rebin(25,None)
      denom.hObj.GetXaxis().SetRangeUser(0.,1.)
      denom.hObj.SetTitle(Dir)
      denom.Draw("hist")
      nom.Draw("psame")
      CumuNomList.append(MakeCumu(nom.hObj))
      CumuDenomList.append(MakeCumu(denom.hObj))
      a= r.TGraphAsymmErrors()
      b = r.TGraphAsymmErrors()
      a.Divide(nom.hObj,denom.hObj)
      b.Divide(MakeCumu(nom.hObj),MakeCumu(denom.hObj))
      TEffList.append(a)
      TEffListCumu.append(b)
      c1.Print()
      c1.Clear()
  c1.SetLog('y',False)
  collection = r.TList()
  totalDiff = None
  for eff in TEffList:
    # eff.SetWeight(weight)
    collection.Add(eff)


  for eff,name in zip(collection,values[0]):
   eff.GetXaxis().SetRangeUser(0.,1.)
   eff.SetTitle(name)
   eff.Draw("AP")
   c1.Print()


  collectionCumu = r.TList()
  for eff,weight in zip(TEffListCumu,values[1]):
    # eff.SetWeight(weight)
    collectionCumu.Add(eff)



  # CombinedDiff = r.TEfficiency()
  # asymError =  CombinedDiff.Combine(collection,"mode")
  # asymError.GetXaxis().SetRangeUser(0.,1.)
  # asymError.Draw("AP")
  # c1.Print()
  # CombinedDiff.GetTotalHistogram().Draw("h")
  # CombinedDiff.GetPassedHistogram().Draw("psame")
  # c1.SetLog('y',True)
  # c1.Print()


  for cumu,name in zip(collectionCumu,values[0]):
    cumu.GetXaxis().SetRangeUser(0.,1.)
    cumu.SetTitle(name)
    cumu.Draw("AP")
    c1.Print()
  cumuNomTotal = None
  cumuDenomTotal = None
  for nom,denom in zip(CumuNomList,CumuDenomList):
    if cumuNomTotal is None:
      cumuNomTotal = nom.Clone()
      cumuDenomTotal = denom.Clone()
    else:
      cumuNomTotal.Add(nom)
      cumuDenomTotal.Add(denom)

  asymErrorCumu = r.TGraphAsymmErrors()
  asymErrorCumu.Divide(cumuNomTotal,cumuDenomTotal)
  text = ""
  for bin in range(CumuNomList[0].GetNbinsX()):
    point = bin-1
    sum_w_i = 0.
    sum_eff_times_w_i = 0.
    xVal = r.Double(0)
    sum_w_i_plus = 0.
    sum_w_i_minus = 0.
    ran = r.Double(0)
    asymErrorCumu.GetPoint(point,xVal,ran)
    # print xVal
    if xVal > 1.0 or xVal < 0.001:continue
    print "="*25
    print "Start Bin %f,%f"%(xVal,CumuDenomList[0].GetBinLowEdge(bin))
    print "="*25
    for TEff,name,total,totalCumu in zip(collectionCumu,values[0],denomList,CumuDenomList):
      efficiency = r.Double(0)
      xvalAtPoint = r.Double(0)
      w_i = 0.
      ErrorYhigh = (TEff.GetErrorYhigh(point))
      ErrorYlow = (TEff.GetErrorYlow(point))
      if ErrorYlow < 1./1e10: ErrorYlow = 0.
      if ErrorYhigh < 1./1e10: ErrorYhigh = 0.
      TEff.GetPoint(point,xvalAtPoint,efficiency)
      if totalCumu.GetBinContent(bin) > 0.:
        # print ErrorYhigh
        if (ErrorYhigh**2) > 0. and ErrorYhigh < 1e5:
          w_i_plus = 1./(ErrorYhigh**2)
          if w_i_plus > 1e6:
            w_i_plus = 1e6
          sum_w_i_plus += w_i_plus
        # print ErrorYlow
        if (ErrorYlow**2) > 0 and ErrorYlow < 1e5:
          w_i_minus =1./(ErrorYlow**2)
          if w_i_minus > 1e6:
            w_i_minus = 1e6
          sum_w_i_minus += w_i_minus
          w_i = min(w_i_minus,w_i_plus)
        sum_w_i += w_i
        sum_eff_times_w_i += (efficiency*w_i)
        print "%s, w_i_plus = %f, w_i_minus = %f, sum_w_i %f, Efficiency = %f, efficiency*w_i = %f, at x = %f"%(name,w_i_plus,w_i_minus,sum_w_i, efficiency, efficiency*w_i, xvalAtPoint)
    if sum_w_i > 0:
      AvEff = sum_eff_times_w_i/sum_w_i
    else: AvEff = 0.
    # print "Erro Minus =  ",math.sqrt(1./sum_w_i_minus)
    if sum_w_i_minus > 0:
      error_minus = math.sqrt(1./sum_w_i_minus)
    else: error_minus = 0.
    if sum_w_i_plus > 0.:
      error_plus = math.sqrt(1./sum_w_i_plus)
    else: error_plus = 0.
    print "Totals for event:"
    print "\t AvEff = %f, + %f - %f"%(AvEff,error_plus,error_minus)
    asymErrorCumu.SetPoint(point,xVal,AvEff)
    if AvEff+error_plus > 1. :
      error_plus = 1.-AvEff
    asymErrorCumu.SetPointError(point, asymErrorCumu.GetErrorXlow(point),asymErrorCumu.GetErrorXhigh(point),error_minus,error_plus )



  # asymErrorCumu.SetMarkerStyle(20)
  asymErrorCumu.SetLineWidth(1)
  asymErrorCumu.SetLineColor(1)
  asymErrorCumu.SetTitle(key+text)
    # SetPointError(Double_t exl, Double_t exh, Double_t eyl, Double_t eyh)MENU
  c1.SetLog('y',False)
  asymErrorCumu.GetXaxis().SetRangeUser(0.,1.)
  asymErrorCumu.GetXaxis().SetTitle("#alpha_{T}")
  asymErrorCumu.GetYaxis().SetRangeUser(-0.2,1.2)
  asymErrorCumu.Draw("AP")
  c1.Print()

  c1.close()



if __name__ == '__main__':
  main()

