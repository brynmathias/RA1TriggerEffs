#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Bryn Mathias on 2011-10-17.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *

def main():
  # c1.Clear()
  SetBatch()
  r.gROOT.SetBatch(True)
  c1 = printPDF("TestOutput.pdf")
  alphaT0p55 = TurnOnPrefs(File = "MuHadHT375NoUpper",NomFile = ["HLT_HT250_AlphaT0p55_v*_From_HLT_Mu40_HT200_v*"],DenomFile = ["HLT_Mu40_HT200_v*_For_HLT_HT250_AlphaT0p55_v*"],
                           Variables = ["AlphaT_all","AlphaT_all"],AxisRanges =[ (0.0,1.5),(0.0,1.5)], CumCut = ( [0.,0.55,5.],[0.,0.58,5.] ) )

  ht600 = TurnOnPrefs( File= "HT375NoUpper",NomFile = ["HLT_HT600_v1_From_HLT_HT450_v8"], DenomFile = ["HLT_HT450_v8_For_HLT_HT600_v1"],
                       Variables = ["HT_all","Meff_all"], AxisRanges = [(0.,2000.),(0.,1000.)], CumCut = ([0.,650.,2000.],None) )

  ht600From300 = TurnOnPrefs( File= "ht375NoUpperHT600From300",NomFile = ["HLT_HT600_v1_From_HLT_HT300_v9"], DenomFile = ["HLT_HT300_v9_For_HLT_HT600_v1"],
                       Variables = ["HT_all","Meff_all"], AxisRanges = [(0.,2000.),(0.,1000.)], CumCut = ([0.,650.,2000.],None) )
  L1PreScaleTest = TurnOnPrefs( File= "L1PreScaleTest",NomFile = ["HLT_HT300_v9_From_HLT_HT150_v8"], DenomFile = ["HLT_HT150_v8_For_HLT_HT300_v9"],
                       Variables = ["HT_all","PreScale_L1AndHT","preScaleHLT"], AxisRanges = [(0.,1000.),(0.,1000,),(0.,1000,)], CumCut = ([0.,350.,2000.],None,None) )
  cfgs = []
  cfgs.append(alphaT0p55)
  cfgs.append(ht600)
  cfgs.append(ht600From300)
  # cfgs.append(L1PreScaleTest)
  leg = Legend()
  c1.open()
  for cfg in cfgs:
    Text =  r.TLatex(0.01,0.9, "#scale[0.8]{input file = %s}"%(cfg.file))
    Text1 = r.TLatex(0.01,0.85,"#scale[0.8]{Variable for turn on curve = %s}"%(cfg.variables))
    Text2 = r.TLatex(0.01,0.8, "#scale[0.8]{Histogram files = %s}"%(cfg.nomFile))
    Text3 = r.TLatex(0.01,0.75,"#scale[0.8]{and %s}"%(cfg.denomFile))
    Text.SetNDC()
    Text1.SetNDC()
    Text2.SetNDC()
    Text3.SetNDC()
    Text.Draw()
    Text1.Draw()
    Text2.Draw()
    Text3.Draw()
    c1.Print()
    for var,ranges,cumulative in zip(cfg.variables,cfg.AxisRange,cfg.cutList):
      Nom   = GetSumHist(File = ["./"+cfg.file+".root"], Directories = cfg.nomFile, Hist = var, Col = r.kBlack, Norm = None, LegendText = cfg.nomFile[0])
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["./"+cfg.file+".root"], Directories = cfg.denomFile,   Hist = var, Col = r.kRed,   Norm = None, LegendText = cfg.denomFile[0])
      Denom.HideOverFlow()
      c1.cd()
      Denom.hObj.SetTitle("Variable = %s, inputfile = %s"%(var,cfg.file))
      Nom.hObj.SetTitle("Variable = %s, inputfile = %s"%(var,cfg.file))
      Denom.SetRange('x',ranges[0],ranges[1])
      Nom.SetRange('x',ranges[0],ranges[1])
      Denom.Draw("h")
      Nom.Draw("sameh")
      c1.SetLog('y',True)
      leg.AddEntry(Denom.hObj,Denom.legendText,"LP")
      leg.AddEntry(Nom.hObj,Nom.legendText,"LP")
      leg.Draw()
      c1.Print()
      leg.Clear()
      c1.SetLog('y',False)
      turnon = TurnOn(Nom,Denom)
      c1.Clear()
      for a in turnon.logEffs():
        # c1.Clear()
        a.SetNDC()
        a.Draw("same")
        # c1.Print()
      c1.Print()
      c1.Clear()
      turnon.setRange(ranges[0],ranges[1])
      turnon.DifferentialTurnOn().Draw("ap")
      c1.Print()
      c1.Clear()

      # c1.Print(outF+".pdf")
      if cumulative != None :
        turnon.CumulativeTurnOn( array.array('d',cumulative) ).Draw("ap")
        c1.Print()

      c1.Clear()

  c1.close()
  pass


if __name__ == '__main__':
  main()