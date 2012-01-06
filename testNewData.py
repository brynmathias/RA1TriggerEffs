#!/usr/bin/env python
# encoding: utf-8
"""
PreScaledTriggers.py

Created by Bryn Mathias on 2011-11-02.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *

# HLT_HT600_v1Pre_1_HLT_HT300_v9Pre_210
def main():
  c1 = Print("newDataTest.pdf")
  c1.open()
  # c1.Print()
  settings = {

"HT275_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
"HT275_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
"HT275_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT275_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
"HT275_HLT_HT250_AlphaT0p53_v6_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT275_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT275_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT325_HLT_HT300_AlphaT0p52_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT325_HLT_HT300_AlphaT0p52_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT325_HLT_HT300_AlphaT0p52_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
"HT325_HLT_HT300_AlphaT0p52_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
"HT325_HLT_HT300_AlphaT0p52_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT325_HLT_HT300_AlphaT0p53_v5_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
"HT325_HLT_HT300_AlphaT0p53_v6_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT375_HLT_HT350_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT375_HLT_HT350_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT375_HLT_HT350_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
"HT375_HLT_HT350_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
"HT375_HLT_HT350_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT375_HLT_HT350_AlphaT0p52_v1_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
"HT375_HLT_HT350_AlphaT0p52_v2_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT375_HLT_HT350_AlphaT0p53_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
"HT475_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
"HT475_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT475_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT475_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
"HT475_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
"HT475_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT475_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
"HT475_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT575_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
"HT575_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT575_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT575_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
"HT575_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
"HT575_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT575_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
"HT575_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT675_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
"HT675_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT675_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT675_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
"HT675_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
"HT675_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT675_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
"HT675_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT775_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
"HT775_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT775_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT775_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
"HT775_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
"HT775_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT775_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
"HT775_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v10_HLT_Mu40_HT300_v5":("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v1_HLT_Mu5_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v2_HLT_Mu8_HT200_v4"  :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v3_HLT_Mu15_HT200_v2" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v4_HLT_Mu15_HT200_v3" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v5_HLT_Mu15_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v6_HLT_Mu30_HT200_v1" :("AlphaT_Nom","AlphaT_Denom"),
"HT875_HLT_HT400_AlphaT0p51_v7_HLT_Mu40_HT200_v4" :("AlphaT_Nom","AlphaT_Denom"),

"HLT_HT350_v*_HLT_HT300_v*"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT550_v11_HLT_HT350_v11"                     :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT300_v*_HLT_HT300_v*"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT450_v*_HLT_HT300_v*"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT450_v11_HLT_HT300_v12"                     :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT450_v8_HLT_HT300_v9"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT450_v7_HLT_HT300_v8"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT350_v8_HLT_HT250_v8"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT750_v3_HLT_HT250_v11"                      :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT450_v6_HLT_HT300_v7"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT350_v2_HLT_HT250_v2"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT350_v3_HLT_HT250_v3"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT450_v5_HLT_HT300_v6"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT450_v4_HLT_HT300_v5"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT350_v6_HLT_HT250_v6"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT350_v7_HLT_HT250_v7"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT350_v4_HLT_HT250_v4"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT350_v5_HLT_HT250_v5"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT500_v*_HLT_HT300_v*"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT450_v3_HLT_HT300_v4"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT550_v*_HLT_HT300_v*"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT600_v*_HLT_HT300_v*"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT450_v2_HLT_HT300_v3"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT600_v4_HLT_HT250_v11"                      :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT550_v2_HLT_HT350_v2"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT550_v3_HLT_HT350_v3"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT550_v4_HLT_HT350_v4"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT550_v5_HLT_HT350_v5"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT550_v6_HLT_HT350_v6"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT550_v7_HLT_HT350_v7"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT550_v8_HLT_HT350_v8"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT350_v11_HLT_HT250_v11"                     :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT400_v*_HLT_HT300_v*"                       :("AlphaT_Nom","AlphaT_Denom"),
"HLT_HT600_v1_HLT_HT350_v8"                       :("AlphaT_Nom","AlphaT_Denom"),
  }
  diffList = []
  cumuList = []
  print settings.iteritems()
  for key,histList in sorted(settings.iteritems()):
      print histList
      mg = None
      c1.cd()
      c1.Clear()
      Nom   = GetSumHist(File = ["MuHad_signal_ht375.root"], Directories = [key], Hist = histList[0], Col = r.kBlack, Norm = None, LegendText = "")
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["MuHad_signal_ht375.root"], Directories = [key], Hist = histList[1], Col = r.kRed,  Norm = None, LegendText = "")
      Denom.HideOverFlow()
      # Nom.Rebin(25,None)
      # Denom.Rebin(25,None)
      Nom.hObj.GetXaxis().SetRangeUser(0.,1.)
      Denom.hObj.GetXaxis().SetRangeUser(0.,1.)
      Denom.hObj.SetTitle(key)
      Denom.Draw("h")
      Denom.hObj.GetXaxis().SetTitle("#alpha_{T}")
      Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %f"%(Denom.hObj.GetBinWidth(1)))
      Denom.hObj.GetYaxis().SetTitleOffset(1.15)

      Nom.hObj.SetMarkerStyle(20)
      Nom.Draw("psame")
      c1.Print()
      c1.toFile(Nom.hObj,"Nom_Standard_"+key)
      c1.toFile(Denom.hObj,"Denom_Standard_"+key)
  c1.close()
  pass




if __name__ == '__main__':
  main()

