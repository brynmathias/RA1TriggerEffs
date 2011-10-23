#!/usr/bin/env python
# encoding: utf-8
"""
TriggerTurnOn.py

Created by Bryn Mathias on 2011-10-04.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
import ROOT as r
from plottingUtils import *
outF = "HT_TriggerReview.pdf"
def main():
  a = GetSumHist()
  a.Help()
  PlotList = ["AlphaT_all"]#,"MHT_all"]
  c1.Print(outF+"[")
  for hist in PlotList:
    leg = Legend()
    TriggerOnly = GetSumHist(File = ["./HT_TriggerPurities.root"], Directories = ["TriggerOnly"], Hist = hist, Col = r.kBlack, Norm = None, LegendText = "HLT_Mu40_HT200_v*")
    HT275Trigger = GetSumHist(File = ["./HT_TriggerPurities.root"], Directories = ["Plots_HT275"], Hist = hist, Col = r.kBlack, Norm = None, LegendText = "HLT_Mu40_HT200_v*")
    HT270Trigger = GetSumHist(File = ["./HT_TriggerPurities.root"], Directories = ["Plots_HT270"], Hist = hist, Col = r.kBlack, Norm = None, LegendText = "HLT_Mu40_HT200_v*")
    HT275PreSelectionOnly = GetSumHist(File = ["./HT_TriggerPurities.root"], Directories = ["Plots_HT275_NoCleaning"], Hist = hist, Col = r.kBlack, Norm = None, LegendText = "HLT_Mu40_HT200_v*")
    HT270PreSelectionOnly = GetSumHist(File = ["./HT_TriggerPurities.root"], Directories = ["Plots_HT270_NoCleaning"], Hist = hist, Col = r.kBlack, Norm = None, LegendText = "HLT_Mu40_HT200_v*")
    HT260PreSelectionOnly = GetSumHist(File = ["./HT_TriggerPurities.root"], Directories = ["Plots_HT260_NoCleaning"], Hist = hist, Col = r.kBlack, Norm = None, LegendText = "HLT_Mu40_HT200_v*")
    print "Purity of HT270 AlphaT cut = 0.55 trigger with respect to full offline analysis is %f"%(HT270Trigger.Integral(0.55,5.)/TriggerOnly.Integral(0.,5.))
    print "Purity of HT275 AlphaT cut = 0.55 trigger with respect to full offline analysis is %f"%(HT275Trigger.Integral(0.55,5.)/TriggerOnly.Integral(0.,5.))
    print "Purity of HT270 AlphaT cut = 0.58 trigger with respect to full offline analysis is %f"%(HT270Trigger.Integral(0.58,5.)/TriggerOnly.Integral(0.,5.))
    print "Purity of HT275 AlphaT cut = 0.58 trigger with respect to full offline analysis is %f"%(HT275Trigger.Integral(0.58,5.)/TriggerOnly.Integral(0.,5.))
    print "Purity of HT275 AlphaT cut = 0.58 with respect to preselection = %f"%((HT275PreSelectionOnly.Integral(0.58,5.)/TriggerOnly.Integral(0.,5.)))
    print "Purity of HT270 AlphaT cut = 0.58 with respect to preselection = %f"%((HT270PreSelectionOnly.Integral(0.58,5.)/TriggerOnly.Integral(0.,5.)))
    print "Purity of HT260 AlphaT cut = 0.58 with respect to preselection = %f"%((HT260PreSelectionOnly.Integral(0.58,5.)/TriggerOnly.Integral(0.,5.)))
    print "Purity of HT275 AlphaT cut = 0.55 with respect to preselection = %f"%((HT275PreSelectionOnly.Integral(0.55,5.)/TriggerOnly.Integral(0.,5.)))
    print "Purity of HT270 AlphaT cut = 0.55 with respect to preselection = %f"%((HT270PreSelectionOnly.Integral(0.55,5.)/TriggerOnly.Integral(0.,5.)))
    print "Purity of HT260 AlphaT cut = 0.55 with respect to preselection = %f"%((HT260PreSelectionOnly.Integral(0.55,5.)/TriggerOnly.Integral(0.,5.)))
    Nominator = GetSumHist(File = ["./MuHad.root"], Directories = ["Cross_Trigger"], Hist = hist, Col = r.kRed, Norm = None, LegendText = "HLT_HT250_AlphaT0p55_v*")
    DeNominator = GetSumHist(File = ["./MuHad.root"], Directories = ["HT_Trigger"], Hist = hist, Col = r.kBlack, Norm = None, LegendText = "HLT_Mu40_HT200_v*")
    BinEdges = [0.0,.55,5.]
    Nominator.Rebin(2,BinEdges)
    DeNominator.Rebin(2,BinEdges)
    c1.cd()
    c1.SetLogy()
    leg.AddEntry(Nominator.hObj,Nominator.legendText,"P")
    leg.AddEntry(DeNominator.hObj,DeNominator.legendText,"l")
    Nominator.hObj.SetMarkerStyle(20)
    if Nominator.hist is "AlphaT_all":
      Nominator.SetRange('x',0.,2.)
      Nominator.hObj.SetTitle("AlphaT Comparison between Ref trigger and Sig trigger")
      Nominator.hObj.GetXaxis().SetTitle("#alpha_{T}")
    # Nominator.hObj.SetMarkerSize()
    Nominator.Draw("p")
    DeNominator.Draw("sameh")
    Nominator.Draw("samep")
    leg.Draw("SAME")
    # for bin in range( Nominator.hObj.GetNbinsX()):
      # print "Nom bin content = %d, DeNom bin content = %d"%(Nominator.hObj.GetBinContent(bin),DeNominator.hObj.GetBinContent(bin))
    c1.Print(outF)
    c1.SetLogy(r.kFALSE)
    graph = r.TGraphAsymmErrors()
    graph.SetLineWidth(3)
    graph.SetLineColor(r.kBlue)
    graph.SetMarkerColor(r.kBlue)
    graph.SetTitle("Efficiency in %s of AlphaT trigger w.r.t Muon Trigger"%(Nominator.hist[:-4]))
    graph.Divide(Nominator.hObj,DeNominator.hObj)
    graph.GetXaxis().SetTitle("#alpha_{T}")
    graph.Draw("AP")
    c1.Print(outF)
  c1.Print(outF+"]")
  pass


if __name__ == '__main__':
  main()

