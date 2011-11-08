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
  c1 = printPDF("TestOutputHT600PreScaleMustEqual1.pdf")
  alphaT0p55 = TurnOnPrefs(File = "MuHadht375NoUpper",NomFile = ["HLT_HT250_AlphaT0p55_v*_From_HLT_Mu40_HT200_v*"],
                           DenomFile = ["HLT_Mu40_HT200_v*_For_HLT_HT250_AlphaT0p55_v*"],
                           Variables = ["AlphaT_all","AlphaT_all"],AxisRanges =[ (0.0,1.5),(0.0,1.5)], CumCut = ( [0.,0.55,5.],[0.,0.58,5.] ) )

  SingleMuht375NoUpperPreScaleMustEqual1 = TurnOnPrefs(File = "SingleMuht375NoUpper",NomFile = ["HLT_HT250_v7_From_HLT_Mu30_v5"],
                           DenomFile = ["HLT_Mu30_v5_For_HLT_HT250_v7"],
                           Variables = ["HT_all","preScaleHLT"],AxisRanges =[ (0.0,3000.)], CumCut = ( [0.,0.55,5.], ) )

  ht600 = TurnOnPrefs( File= "ht375NoUpperPreScaleMustEqual1",NomFile = ["HLT_HT600_v1_From_HLT_HT450_v8"],
                       DenomFile = ["HLT_HT450_v8_For_HLT_HT600_v1"],
                       Variables = ["HT_all","preScaleHLT"], AxisRanges = [(0.,2000.),(0.,100.)], CumCut = (None,None) )

  ht500 = TurnOnPrefs( File= "ht375NoUpperPreScaleMustEqual1",NomFile = ["HLT_HT500_v8_From_HLT_HT350_v8"],
                       DenomFile = ["HLT_HT350_v8_For_HLT_HT500_v8"],
                       Variables = ["HT_all","preScaleHLT"], AxisRanges = [(0.,2000.),(0.,100.)], CumCut = (None,None) )

  ht550 = TurnOnPrefs( File= "ht375NoUpperPreScaleMustEqual1",NomFile = ["HLT_HT550_v8_From_HLT_HT300_v9"],
                       DenomFile = ["HLT_HT300_v9_For_HLT_HT550_v8"],
                       Variables = ["HT_all","preScaleHLT"], AxisRanges = [(0.,2000.),(0.,100.)], CumCut = (None,None) )

  ht500from300 = TurnOnPrefs( File= "ht375NoUpperPreScaleMustEqual1",NomFile = ["HLT_HT500_v8_From_HLT_HT300_v9"],
                       DenomFile = ["HLT_HT300_v9_For_HLT_HT500_v8"],
                       Variables = ["HT_all","preScaleHLT"], AxisRanges = [(0.,2000.),(0.,100.)], CumCut = (None,None) )

  ht500from250 = TurnOnPrefs( File= "ht375NoUpperPreScaleMustEqual1",NomFile = ["HLT_HT500_v8_From_HLT_HT250_v8"],
                       DenomFile = ["HLT_HT250_v8_For_HLT_HT500_v8"],
                       Variables = ["HT_all","preScaleHLT"], AxisRanges = [(0.,2000.),(0.,100.)], CumCut = (None,None) )


  ht450from300 = TurnOnPrefs( File= "ht375NoUpperPreScaleMustEqual1",NomFile = ["HLT_HT450_v8_From_HLT_HT300_v9"],
                       DenomFile = ["HLT_HT300_v9_For_HLT_HT450_v8"],
                       Variables = ["HT_all","preScaleHLT"], AxisRanges = [(0.,2000.),(0.,100.)], CumCut = (None,None) )

  ht450from250 = TurnOnPrefs( File= "ht375NoUpperPreScaleMustEqual1",NomFile = ["HLT_HT450_v8_From_HLT_HT250_v8"],
                       DenomFile = ["HLT_HT250_v8_For_HLT_HT450_v8"],
                       Variables = ["HT_all","preScaleHLT"], AxisRanges = [(0.,2000.),(0.,100.)], CumCut = (None,None) )

  ht600From300 = TurnOnPrefs( File= "ht375NoUpperPreScaleMustEqual1",NomFile = ["HLT_HT600_v1_From_HLT_HT300_v9"],
                        DenomFile = ["HLT_HT300_v9_For_HLT_HT600_v1"],
                        Variables = ["HT_all","preScaleHLT"], AxisRanges = [(0.,2000.),(0.,100.)], CumCut = (None,None))



  cfgs = []
  # cfgs.append(alphaT0p55)
  # cfgs.append(SingleMuht375NoUpperPreScaleMustEqual1)
  cfgs.append(ht500)
  cfgs.append(ht550)
  cfgs.append(ht500from300)
  cfgs.append(ht450from300)
  cfgs.append(ht500from250)
  cfgs.append(ht450from250)
  cfgs.append(ht600)
  cfgs.append(ht600From300)
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
      Nom   = GetSumHist(File = ["./"+cfg.file+".root"], Directories = cfg.nomFile,  Hist = var, Col = r.kBlack, Norm = None, LegendText = cfg.nomFile[0])
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["./"+cfg.file+".root"], Directories = cfg.denomFile, Hist = var, Col = r.kRed,  Norm = None, LegendText = cfg.denomFile[0])
      Denom.HideOverFlow()
      c1.cd()
      Denom.hObj.SetTitle("Variable = %s, inputfile = %s"%(var,cfg.file))
      Nom.hObj.SetTitle("Variable = %s, inputfile = %s"%(var,cfg.file))
      Denom.SetRange('x',ranges[0],ranges[1])
      Nom.SetRange('x',ranges[0],ranges[1])
      Denom.hObj.Draw("h")
      Nom.hObj.SetMarkerStyle(20)
      Nom.hObj.Draw("psame")
      c1.SetLog('y',True)
      leg.AddEntry(Denom.hObj,Denom.legendText,"LP")
      leg.AddEntry(Nom.hObj,Nom.legendText,"LP")
      leg.Draw()
      c1.Print()
      leg.Clear()
      c1.SetLog('y',False)
      turnon = TurnOn(Nom,Denom)
      c1.Clear()
      # for a in turnon.logEffs():
        # a.SetNDC()
        # a.Draw("same")
      # c1.Print()
      # c1.Clear()
      turnon.setRange(ranges[0],ranges[1])
      turnon.DifferentialTurnOn().Draw("ap")
      c1.Print()
      c1.Clear()
      if cumulative != None :
        turnon.CumulativeTurnOn( array.array('d',cumulative) ).Draw("ap")
        c1.Print()
      c1.Clear()
  c1.close()
  pass


if __name__ == '__main__':
  main()