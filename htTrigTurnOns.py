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
  SetBatch()
  VARS = ["AlphaT_all"]#,"HT_all","Meff_all","PreScale"]
  alphaT0p55 = TurnOnPrefs(File = "HT375NoUpper",NomFile = ["HLT_HT250_AlphaT0p55_v*_From_HLT_Mu40_HT200_v*"],DenomFile = ["HLT_Mu40_HT200_v*_For_HLT_HT250_AlphaT0p55_v*"],Variables = ["AlphaT_all"],AxisRanges = (0.0,1.5), CumCut = [0.,0.55,5.])
  cfgs.append(alphaT0p55)
  leg = Legend()
  for cfg in cfgs
    c1.Print(cfg.file+".pdf[")
    for var in cfg.variables:
      print var
      Nom   = GetSumHist(File = ["./"+cfg.file+".root"], Directories = cfg.NomFile, Hist = var, Col = r.kBlack, Norm = None, LegendText = cfg.nomFile[0])
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["./"+cfg.file+".root"], Directories = cfg.Denom,   Hist = var, Col = r.kRed,   Norm = None, LegendText = cfg.denomFile[0])
      Denom.HideOverFlow()
      c1.cd()
      Denom.Draw("h")
      Nom.Draw("sameh")
      c1.Print(cfg.file+".pdf")
      turnon = TurnOn(Nom,Denom)
      turnon.setCanvas(c1)
      turnon.setRange(cfg.AxisRange[0],cfg.AxisRange[1])
      turnon.DifferentialTurnOn().Draw("ap")
      c1.Print(infile+".pdf")
      if cfg.cutList != None:
        turnon.CumulativeTurnOn(array.array('d',cfg.cutList).Draw("ap")
        c1.Print(cfg.file+".pdf")



    c1.Print(cfg.file+".pdf]")
    pass


if __name__ == '__main__':
  main()

