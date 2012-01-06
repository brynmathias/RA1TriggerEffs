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
  outfile = open("./AllFromHT400.txt",'w')
  c1 = Print("./AllFromHT400.pdf")
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
  for eff,weight in zip(TEffList,values[1]):
    # eff.SetWeight(weight)
    collection.Add(eff)


  for eff in collection:
   # eff.GetXaxis().SetRangeUser(0.,1.)
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


  for cumu in collectionCumu:
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
    binLumi = 0
    BinEff = 0.
    point = bin + 1
    errPlus = 0.
    errMinus = 0.
    yval = 0.
    xvalAtPoint = r.Double(0)
    yvalAtPoint = r.Double(0)
    pointEff = r.Double(0)
    xOfPoint = r.Double(0)
    asymErrorCumu.GetPoint(point,xOfPoint,r.Double(0))
    print "="*25
    print "Begin Bin" ,xOfPoint
    print "="*25
    for numerator,denominator,weight,TEff,name in zip(CumuNomList,CumuDenomList,values[1],collectionCumu,values[0]):
      if int(denominator.GetBinContent(bin)) is not 0:

        binLumi += weight
        TEff.GetPoint(point,xvalAtPoint,pointEff)
        BinEff += (pointEff*weight)
        # if TEff.GetErrorYhigh(point) > 0 and TEff.GetErrorYhigh(point) < 1e100:
        print "pointEff = %f, BinErrorHigh = %f, BinErrorLow = %f"%(pointEff,TEff.GetErrorYhigh(point),TEff.GetErrorYlow(point)  )
        errPlus += (TEff.GetErrorYhigh(point)**2 * weight**2)
        errMinus += (TEff.GetErrorYlow(point)**2 * weight**2)

        print "\t Itterativly we have for %s, Xval = %f, BinEff = %f +%f -%f, Weight = %f"%(name,xvalAtPoint,BinEff/binLumi,math.sqrt(errPlus/ (binLumi**2)),math.sqrt(errMinus/ (binLumi**2)),weight)
        if int((BinEff/binLumi)*100) == 0:
          print "BinEff = %f, pointEff = %f, weight = %f, binLumi = %f ErrorHigh = %f ErrorLow = %f"%(BinEff,pointEff,weight,binLumi,TEff.GetErrorYhigh(point),TEff.GetErrorYlow(point))
        # This is our efficiency for the bin.
    if int(binLumi) == 0: binLumi = 1.
    BinEff /= binLumi
    errPlus = math.sqrt(errPlus/ (binLumi**2))

    errMinus = math.sqrt(errMinus/ (binLumi**2))
    if int(xOfPoint*100) is not 0:
      print "Point = %f,%f, + %f, -%f"%(xOfPoint,BinEff,errPlus,errMinus)
    # Now we need to set the errors and points of our histogram!!!
    # if int(xvalAtPoint) is not 0:
    asymErrorCumu.SetPoint(point,xOfPoint,BinEff)
    if BinEff+errPlus > 1. :
      errPlus = 1.-BinEff
    asymErrorCumu.SetPointError(point, asymErrorCumu.GetErrorXlow(point),asymErrorCumu.GetErrorXhigh(point),errMinus,errPlus )
    if xOfPoint == 0.555:
      text = "Point = %f Eff =  %f +%f , -%f"%(xOfPoint,BinEff,errPlus,errMinus)
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

