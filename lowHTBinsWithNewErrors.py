#!/usr/bin/env python
# encoding: utf-8
"""
lowHTBinsWithNewErrors.py

Created by Bryn Mathias on 2011-12-14.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from TurnOn import *
from plottingUtils import *
import ROOT as r


settings = {
"HT275": {"File":"./noOddMuonVeto/ht275MuHadNoOddMuon.root",
          "Directories":["DEBUG_DiMu_HT0_HLT_HT250_v2_HLT_Mu5_HT200_v4"  ,"DEBUG_DiMu_HT0_HLT_HT250_v2_HLT_Mu5_HT200_v4"  ,"DEBUG_DiMu_HT0_HLT_HT250_v2_HLT_Mu5_HT200_v4"  ,"DEBUG_DiMu_HT0_HLT_HT250_v3_HLT_Mu8_HT200_v4"  ,"DEBUG_DiMu_HT0_HLT_HT250_v3_HLT_Mu8_HT200_v4"  ,"DEBUG_DiMu_HT0_HLT_HT250_v3_HLT_Mu8_HT200_v4"  ,"DEBUG_DiMu_HT0_HLT_HT250_v4_HLT_Mu15_HT200_v2","DEBUG_DiMu_HT0_HLT_HT250_v4_HLT_Mu15_HT200_v2","DEBUG_DiMu_HT0_HLT_HT250_v4_HLT_Mu15_HT200_v2","DEBUG_DiMu_HT0_HLT_HT250_v4_HLT_Mu15_HT200_v2","DEBUG_DiMu_HT0_HLT_HT250_v5_HLT_Mu15_HT200_v3","DEBUG_DiMu_HT0_HLT_HT250_v5_HLT_Mu15_HT200_v3","DEBUG_DiMu_HT0_HLT_HT250_v5_HLT_Mu15_HT200_v3","DEBUG_DiMu_HT0_HLT_HT250_v6_HLT_Mu15_HT200_v4","DEBUG_DiMu_HT0_HLT_HT250_v7_HLT_Mu30_HT200_v1","DEBUG_DiMu_HT0_HLT_HT250_v7_HLT_Mu30_HT200_v1","DEBUG_DiMu_HT0_HLT_HT250_v7_HLT_Mu30_HT200_v1","DEBUG_DiMu_HT0_HLT_HT250_v7_HLT_Mu30_HT200_v1",],
          "Numerators" : ["Nom_HLT_HT250_v2Pre_15_HLT_Mu5_HT200_v4Pre_1","Nom_HLT_HT250_v2Pre_25_HLT_Mu5_HT200_v4Pre_1","Nom_HLT_HT250_v2Pre_35_HLT_Mu5_HT200_v4Pre_1","Nom_HLT_HT250_v3Pre_150_HLT_Mu8_HT200_v4Pre_1","Nom_HLT_HT250_v3Pre_200_HLT_Mu8_HT200_v4Pre_1","Nom_HLT_HT250_v3Pre_90_HLT_Mu8_HT200_v4Pre_1","Nom_HLT_HT250_v4Pre_150_HLT_Mu15_HT200_v2Pre_1","Nom_HLT_HT250_v4Pre_200_HLT_Mu15_HT200_v2Pre_1","Nom_HLT_HT250_v4Pre_240_HLT_Mu15_HT200_v2Pre_1","Nom_HLT_HT250_v4Pre_60_HLT_Mu15_HT200_v2Pre_1","Nom_HLT_HT250_v5Pre_180_HLT_Mu15_HT200_v3Pre_1","Nom_HLT_HT250_v5Pre_200_HLT_Mu15_HT200_v3Pre_1","Nom_HLT_HT250_v5Pre_400_HLT_Mu15_HT200_v3Pre_1","Nom_HLT_HT250_v6Pre_200_HLT_Mu15_HT200_v4Pre_1","Nom_HLT_HT250_v7Pre_150_HLT_Mu30_HT200_v1Pre_1","Nom_HLT_HT250_v7Pre_200_HLT_Mu30_HT200_v1Pre_1","Nom_HLT_HT250_v7Pre_290_HLT_Mu30_HT200_v1Pre_1","Nom_HLT_HT250_v7Pre_85_HLT_Mu30_HT200_v1Pre_1",],
          "Denominators": ["Denom_HLT_HT250_v2Pre_15_HLT_Mu5_HT200_v4Pre_1","Denom_HLT_HT250_v2Pre_25_HLT_Mu5_HT200_v4Pre_1","Denom_HLT_HT250_v2Pre_35_HLT_Mu5_HT200_v4Pre_1","Denom_HLT_HT250_v3Pre_150_HLT_Mu8_HT200_v4Pre_1","Denom_HLT_HT250_v3Pre_200_HLT_Mu8_HT200_v4Pre_1","Denom_HLT_HT250_v3Pre_90_HLT_Mu8_HT200_v4Pre_1","Denom_HLT_HT250_v4Pre_150_HLT_Mu15_HT200_v2Pre_1","Denom_HLT_HT250_v4Pre_200_HLT_Mu15_HT200_v2Pre_1","Denom_HLT_HT250_v4Pre_240_HLT_Mu15_HT200_v2Pre_1","Denom_HLT_HT250_v4Pre_60_HLT_Mu15_HT200_v2Pre_1","Denom_HLT_HT250_v5Pre_180_HLT_Mu15_HT200_v3Pre_1","Denom_HLT_HT250_v5Pre_200_HLT_Mu15_HT200_v3Pre_1","Denom_HLT_HT250_v5Pre_400_HLT_Mu15_HT200_v3Pre_1","Denom_HLT_HT250_v6Pre_200_HLT_Mu15_HT200_v4Pre_1","Denom_HLT_HT250_v7Pre_150_HLT_Mu30_HT200_v1Pre_1","Denom_HLT_HT250_v7Pre_200_HLT_Mu30_HT200_v1Pre_1","Denom_HLT_HT250_v7Pre_290_HLT_Mu30_HT200_v1Pre_1","Denom_HLT_HT250_v7Pre_85_HLT_Mu30_HT200_v1Pre_1",],
          "Weights":[15.,25.,35.,150.,200.,90.,150.,200.,240.,60.,180.,200.,400.,200.,150.,200.,290.,85.]},

"HT325": {"File":"./noOddMuonVeto/ht325MuHadNoOddMuon.root",
          "Directories":["DEBUG_DiMu_HT0_HLT_HT300_v12_HLT_DoubleMu8_Mass8_HT200_v4",
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
"DEBUG_DiMu_HT0_HLT_HT300_v8_HLT_Mu30_HT200_v1",],
          "Numerators" : ["Nom_HLT_HT300_v12Pre_1000_HLT_DoubleMu8_Mass8_HT200_v4Pre_1",
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
"Nom_HLT_HT300_v8Pre_70_HLT_Mu30_HT200_v1Pre_1"             ,],
          "Denominators": ["Denom_HLT_HT300_v12Pre_1000_HLT_DoubleMu8_Mass8_HT200_v4Pre_1",
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
"Denom_HLT_HT300_v8Pre_70_HLT_Mu30_HT200_v1Pre_1"             ,],
          "Weights":[  1000.,   10.,  15.,  7.,   100.,  150.,  200.,  60.,  120.,  200.,  240.,  60.,  120.,  80.,  100.,  150.,  40.,  70.,]}
}





def main():
  for key,value in settings.iteritems():
    c1 = Print("./%s.pdf"%(key))
    c1.open()
    graphList = []
    rFile = r.TFile().Open(value["File"])
    TotNumerator = None
    TotDenominator = None
    denominatorList = []
    numeratorList = []
    cumulativeNumeratorList = []
    cumulativeDenominiatorList = []
    TotCumuNumerator   = None
    TotCumuDenominator = None
    cumuGraphList = []
    for dir,numerator,denominator,weight in zip(value["Directories"],value["Numerators"],value["Denominators"],value["Weights"]):
      currentFile = rFile.Get(dir)
      loopNumerator   = currentFile.Get(numerator)
      loopDenominator = currentFile.Get(denominator)
      loopDenominator.Sumw2()
      loopNumerator.Sumw2()
      loopNumerator.Rebin(25)
      loopDenominator.Rebin(25)
      loopDenominator.SetLineColor(r.kRed)
      loopNumerator.SetMarkerStyle(20)
      for bin in range( loopNumerator.GetNbinsX() ):
        error = math.sqrt((weight*(weight+1)*(2.*weight+1))/(6.*weight) - (weight/2.)**2)
        val = (loopNumerator.GetBinContent(bin))*weight


        print "Title = %s, Value = %.2f, BinContent = %f, Weight = %f, BinLowEdge = %f" %( loopNumerator.GetTitle(), val, loopNumerator.GetBinContent(bin), weight, loopNumerator.GetBinLowEdge(bin) )
        loopNumerator.SetBinContent(bin,val)
        loopNumerator.SetBinError(bin,error)
      a = loopNumerator.Clone()
      a.Divide(loopDenominator)
      graph = r.TGraphAsymmErrors(a)
      graphList.append(graph)
      loopDenominator.SetLineColor(r.kRed)
      loopDenominator.GetXaxis().SetRangeUser(0.,1000.)
      loopNumerator.SetMarkerStyle(20)
      numeratorList.append(loopNumerator)
      denominatorList.append(loopDenominator)

      # c1.Print()
      if TotNumerator is None:
        TotNumerator = loopNumerator.Clone()
      else: TotNumerator.Add(loopNumerator)
      if TotDenominator is None:
        TotDenominator = loopDenominator.Clone()
      else:TotDenominator.Add(loopDenominator)
      if TotCumuNumerator is None:
        TotCumuNumerator = MakeCumu(loopNumerator).Clone()
      else: TotCumuNumerator.Add(MakeCumu(loopNumerator))
      if TotCumuDenominator is None:
        TotCumuDenominator = MakeCumu(loopDenominator).Clone()
      else:TotCumuDenominator.Add(MakeCumu(loopDenominator))
      denominatorList.append(loopDenominator)
      cumulativeDenominiatorList.append(MakeCumu(loopDenominator))
      cumulativeNumeratorList.append(MakeCumu(loopNumerator))
      b = MakeCumu(loopNumerator).Clone()
      b.Divide(MakeCumu(loopDenominator))
      cumuGraph = r.TGraphAsymmErrors(b)
      cumuGraphList.append(cumuGraph)


    for loopNumerator,loopDenominator,graph,cumuNom,cumuDenom,cumuGraph in zip(numeratorList,denominatorList,graphList,cumulativeNumeratorList,cumulativeDenominiatorList,cumuGraphList):
      ymax  = max(loopNumerator.GetBinContent(loopNumerator.GetMaximumBin()),loopDenominator.GetBinContent(loopDenominator.GetMaximumBin()))+ 0.1*max(loopNumerator.GetBinContent(loopNumerator.GetMaximumBin()),loopDenominator.GetBinContent(loopDenominator.GetMaximumBin()))
      loopNumerator.GetXaxis().SetRangeUser(0.,1000.)
      loopNumerator.GetYaxis().SetRangeUser(0.,ymax)
      loopNumerator.SetMarkerStyle(20)
      loopNumerator.SetLineColor(1)
      loopDenominator.Draw("h")
      loopNumerator.Draw("psame")
      c1.Print()
      graph.GetYaxis().SetRangeUser(-0.2,4.)
      graph.GetXaxis().SetRangeUser(0.,1000.)
      graph.Draw("ap")
      #fermiFunction = r.TF1("#fermiFunction",errorFun,float(key[2:])-75.,float(key[2:])+75.,3)
      #fermiFunction.SetParameters(1.00,float(key[2:])+50.,1.)
      #fermiFunction.SetParNames("#epsilon","#mu","#sigma")
      # graph.Fit(#fermiFunction,"%f"%(float(key[2:])),"%f"%(float(key[2:])),float(key[2:])-75.,float(key[2:])+75.)
      #fermiFunction.Draw("same")



      c1.Print()
      ymax = max(cumuNom.GetBinContent(cumuNom.GetMaximumBin()),cumuDenom.GetBinContent(cumuDenom.GetMaximumBin()))+ 0.1*max(cumuNom.GetBinContent(cumuNom.GetMaximumBin()),cumuDenom.GetBinContent(cumuDenom.GetMaximumBin()))
      cumuNom.GetXaxis().SetRangeUser(0.,1000.)
      cumuNom.GetYaxis().SetRangeUser(0.,ymax)

      cumuNom.Draw("p")
      cumuDenom.Draw("hsame")
      c1.Print()
      cumuGraph.GetYaxis().SetRangeUser(-0.2,4.)
      cumuGraph.GetXaxis().SetRangeUser(0.,1000.)
      cumuGraph.Draw("ap")
      #fermiFunction = r.TF1("#fermiFunction",errorFun,float(key[2:])-75.,float(key[2:])+75.,3)
      #fermiFunction.SetParameters(1.00,float(key[2:])+50.,1.)
      #fermiFunction.SetParNames("#epsilon","#mu","#sigma")
      # cumuGraph.Fit(#fermiFunction,"%f"%(float(key[2:])),"%f"%(float(key[2:])),float(key[2:])-75.,float(key[2:])+75.)
      #fermiFunction.Draw("same")
      c1.Print()
    # Now make the sum of turn ons
    TotDenominator.SetTitle("Total plots")
    TotDenominator.GetXaxis().SetRangeUser(0.,1000.)
    TotDenominator.Draw("h")
    TotNumerator.Draw("psame")
    c1.Print()


    a = TotNumerator.Clone()
    a.Divide(TotDenominator)

    finalPlot = WeightedSumOfTurnOns(TotDenominator = TotDenominator, TurnOnHist = a, graphList = graphList, denominatorList = denominatorList )
    finalPlot.GetXaxis().SetRangeUser(0.,1000.)
    finalPlot.SetTitle("Final DiffPlot")
    finalPlot.GetYaxis().SetRangeUser(-0.2,4.)
    finalPlot.Draw("ap")
    #fermiFunction.SetParameters(1.00,float(key[2:])+100.,1.)
    #fermiFunction.SetParNames("#epsilon","#mu","#sigma")
    # finalPlot.Fit(#fermiFunction,"%f"%(float(key[2:])),"%f"%(float(key[2:])),float(key[2:])-100.,float(key[2:])+100.)
    #fermiFunction.Draw("same")
    c1.Print()

    b = TotCumuNumerator.Clone()
    b.Divide(TotCumuDenominator)



    finalPlotCumu= WeightedSumOfTurnOns(TotDenominator = TotCumuDenominator, TurnOnHist = b, graphList = cumuGraphList, denominatorList = cumulativeDenominiatorList )
    finalPlotCumu.GetXaxis().SetRangeUser(0.,1000.)
    finalPlotCumu.SetTitle("Final CumuPlot")
    finalPlotCumu.GetYaxis().SetRangeUser(-0.2,4.)
    finalPlotCumu.Draw("ap")
    #fermiFunction = r.TF1("#fermiFunction",errorFun,float(key[2:])-500.,float(key[2:])+200.,3)
    #fermiFunction.SetParameters(1.00,float(key[2:])+100.,1.)
    #fermiFunction.SetParNames("#epsilon","#mu","#sigma")
    # finalPlotCumu.Fit(#fermiFunction,"%f"%(float(key[2:])),"%f"%(float(key[2:])),float(key[2:])-500.,float(key[2:])+200.)
    #fermiFunction.Draw("same")
    c1.Print()
    c1.close()
  pass


if __name__ == '__main__':
  main()

