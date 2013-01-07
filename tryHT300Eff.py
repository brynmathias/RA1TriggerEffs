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
from sys import argv

jMulti = "le3j"
if len(argv)>1:
  jMulti = argv[1]


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

  if jMulti == "le3j":
    #le3j
    dirList = ['DEBUG_le3j_HLT_HT300_v3_HLT_IsoMu24_v15', 'DEBUG_le3j_HLT_HT300_v3_HLT_IsoMu24_v15', 'DEBUG_le3j_HLT_HT300_v2_HLT_IsoMu24_eta2p1_v12', 'DEBUG_le3j_HLT_HT300_v1_HLT_IsoMu24_eta2p1_v11', 'DEBUG_le3j_HLT_HT300_v7_HLT_IsoMu24_v17', 'DEBUG_le3j_HLT_HT300_v7_HLT_IsoMu24_v17', 'DEBUG_le3j_HLT_HT300_v5_HLT_IsoMu24_v16', 'DEBUG_le3j_HLT_HT300_v5_HLT_IsoMu24_v16', 'DEBUG_le3j_HLT_HT300_v4_HLT_IsoMu24_v15', 'DEBUG_le3j_HLT_HT300_v4_HLT_IsoMu24_v15']
    histList = ['Nom_HLT_HT300_v3Pre_1000_HLT_IsoMu24_v15Pre_1', 'Nom_HLT_HT300_v3Pre_1200_HLT_IsoMu24_v15Pre_1', 'Nom_HLT_HT300_v2Pre_1000_HLT_IsoMu24_eta2p1_v12Pre_1', 'Nom_HLT_HT300_v1Pre_1000_HLT_IsoMu24_eta2p1_v11Pre_1', 'Nom_HLT_HT300_v7Pre_1000_HLT_IsoMu24_v17Pre_1', 'Nom_HLT_HT300_v7Pre_1200_HLT_IsoMu24_v17Pre_1', 'Nom_HLT_HT300_v5Pre_1200_HLT_IsoMu24_v16Pre_1', 'Nom_HLT_HT300_v5Pre_1000_HLT_IsoMu24_v16Pre_1', 'Nom_HLT_HT300_v4Pre_1000_HLT_IsoMu24_v15Pre_1', 'Nom_HLT_HT300_v4Pre_1200_HLT_IsoMu24_v15Pre_1']
    histList2 = ['Denom_HLT_HT300_v3Pre_1000_HLT_IsoMu24_v15Pre_1', 'Denom_HLT_HT300_v3Pre_1200_HLT_IsoMu24_v15Pre_1', 'Denom_HLT_HT300_v2Pre_1000_HLT_IsoMu24_eta2p1_v12Pre_1', 'Denom_HLT_HT300_v1Pre_1000_HLT_IsoMu24_eta2p1_v11Pre_1', 'Denom_HLT_HT300_v7Pre_1000_HLT_IsoMu24_v17Pre_1', 'Denom_HLT_HT300_v7Pre_1200_HLT_IsoMu24_v17Pre_1', 'Denom_HLT_HT300_v5Pre_1200_HLT_IsoMu24_v16Pre_1', 'Denom_HLT_HT300_v5Pre_1000_HLT_IsoMu24_v16Pre_1', 'Denom_HLT_HT300_v4Pre_1000_HLT_IsoMu24_v15Pre_1', 'Denom_HLT_HT300_v4Pre_1200_HLT_IsoMu24_v15Pre_1']
    weightList = [1000.0, 1200.0, 1000.0, 1000.0, 1000.0, 1200.0, 1200.0, 1000.0, 1000.0, 1200.0]
    c1 = Print("plotDump/HT300_le3j.pdf")
    textFileName = "textDump/eff_HT300_le3j.txt"
  elif jMulti == "ge4j":
    #ge4j
    dirList = ['DEBUG_ge4j_HLT_HT300_v3_HLT_IsoMu24_v15', 'DEBUG_ge4j_HLT_HT300_v3_HLT_IsoMu24_v15', 'DEBUG_ge4j_HLT_HT300_v2_HLT_IsoMu24_eta2p1_v12', 'DEBUG_ge4j_HLT_HT300_v1_HLT_IsoMu24_eta2p1_v11', 'DEBUG_ge4j_HLT_HT300_v7_HLT_IsoMu24_v17', 'DEBUG_ge4j_HLT_HT300_v7_HLT_IsoMu24_v17', 'DEBUG_ge4j_HLT_HT300_v5_HLT_IsoMu24_v16', 'DEBUG_ge4j_HLT_HT300_v5_HLT_IsoMu24_v16', 'DEBUG_ge4j_HLT_HT300_v4_HLT_IsoMu24_v15', 'DEBUG_ge4j_HLT_HT300_v4_HLT_IsoMu24_v15']
    histList = ['Nom_HLT_HT300_v3Pre_1000_HLT_IsoMu24_v15Pre_1', 'Nom_HLT_HT300_v3Pre_1200_HLT_IsoMu24_v15Pre_1', 'Nom_HLT_HT300_v2Pre_1000_HLT_IsoMu24_eta2p1_v12Pre_1', 'Nom_HLT_HT300_v1Pre_1000_HLT_IsoMu24_eta2p1_v11Pre_1', 'Nom_HLT_HT300_v7Pre_1000_HLT_IsoMu24_v17Pre_1', 'Nom_HLT_HT300_v7Pre_1200_HLT_IsoMu24_v17Pre_1', 'Nom_HLT_HT300_v5Pre_1200_HLT_IsoMu24_v16Pre_1', 'Nom_HLT_HT300_v5Pre_1000_HLT_IsoMu24_v16Pre_1', 'Nom_HLT_HT300_v4Pre_1200_HLT_IsoMu24_v15Pre_1', 'Nom_HLT_HT300_v4Pre_1000_HLT_IsoMu24_v15Pre_1']
    histList2 = ['Denom_HLT_HT300_v3Pre_1000_HLT_IsoMu24_v15Pre_1', 'Denom_HLT_HT300_v3Pre_1200_HLT_IsoMu24_v15Pre_1', 'Denom_HLT_HT300_v2Pre_1000_HLT_IsoMu24_eta2p1_v12Pre_1', 'Denom_HLT_HT300_v1Pre_1000_HLT_IsoMu24_eta2p1_v11Pre_1', 'Denom_HLT_HT300_v7Pre_1000_HLT_IsoMu24_v17Pre_1', 'Denom_HLT_HT300_v7Pre_1200_HLT_IsoMu24_v17Pre_1', 'Denom_HLT_HT300_v5Pre_1200_HLT_IsoMu24_v16Pre_1', 'Denom_HLT_HT300_v5Pre_1000_HLT_IsoMu24_v16Pre_1', 'Denom_HLT_HT300_v4Pre_1200_HLT_IsoMu24_v15Pre_1', 'Denom_HLT_HT300_v4Pre_1000_HLT_IsoMu24_v15Pre_1']
    weightList = [1000.0, 1200.0, 1000.0, 1000.0, 1000.0, 1200.0, 1200.0, 1000.0, 1200.0, 1000.0]
    c1 = Print("plotDump/HT300_ge4j.pdf")
    textFileName = "textDump/eff_HT300_ge4j.txt"


  c1.DoPageNum = False
  c1.SetGrid(True)
  
  c1.open()
  rFile = r.TFile().Open("../14Dec_ABCD/rootfiles/outSinMu_ABCD_HT_trigEffs.root")
  nomHist = None
  denomHist = None
  eh =  [1.15, 1.36, 1.53, 1.73, 1.98, 2.21, 2.42, 2.61, 2.80, 3.00 ]
  el =  [0.00, 1.00, 2.00, 2.14, 2.30, 2.49, 2.68, 2.86, 3.03, 3.19 ]
  for dir,hist,weight in zip(dirList,histList,weightList):
    curFile = rFile.Get(dir)
    currentHist = curFile.Get(hist)
    print currentHist.GetName()
    print type(currentHist)
    #currentHist.Rebin(25)
    for bin in range(currentHist.GetNbinsX()):
      if not currentHist.GetBinContent(bin) == 0:
        error = math.sqrt(currentHist.GetBinContent(bin))*weight
      else:
        error = 0
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
    #currentDenom.Rebin(25)
    for bin in range(currentDenom.GetNbinsX()):
      if currentDenom.GetBinContent(bin) < 10.:
        n = int(currentDenom.GetBinContent(bin))
        currentDenom.SetBinError(bin,max(eh[n],el[n]))
    if denomHist is None:
      denomHist = currentDenom.Clone()
    else:
      denomHist.Add(currentDenom)
  #force 25GeV binning
  nomHist.Rebin(25)
  denomHist.Rebin(25)
  
  nomHist.SetMarkerStyle(20)
  denomHist.SetLineColor(2)
  nomHist.Draw("p")

  nomHist.SetTitle("")
  denomHist.SetTitle("")
  
  denomHist.Draw("sameh")
  c1.Print()
  bins = [i*25. for i in range(int(275./25.)) ]+[325.,1000.]
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
      #text = "HT = %f, eff = %f + %f - %f"%(b.GetBinLowEdge(bin), b.GetBinContent(bin), b.GetBinErrorUp(bin), b.GetBinErrorLow(bin))
      text = "HT = %f, eff = %f \pm %f"%(b.GetBinLowEdge(bin), b.GetBinContent(bin), b.GetBinError(bin))
  
  textFile = open(textFileName, 'w')
  textFile.write(text)

  b.GetYaxis().SetRangeUser(0.,1.2)
  b.Draw("p")
  c1.Print()
  c1.close()

if __name__ == '__main__':
  main()

