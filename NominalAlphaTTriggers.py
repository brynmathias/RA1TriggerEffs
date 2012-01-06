#!/usr/bin/env python
# encoding: utf-8
"""
FinalHTSum.py

Created by Bryn Mathias on 2011-11-25.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *
from finalDict import *









def main():
  outfile = open("./5GeVMuonsVBTFIDWithOddMuonVeto/EffsTotalAlphaT375.txt",'w')
  c1 = Print("./5GeVMuonsVBTFIDWithOddMuonVeto/FinalPlotsFromAlphaTTotals375.pdf")
  text = ""
  histList = ("AlphaT_Nom","AlphaT_Denom")
  sums = {
# "HT275":([
# "HT275_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4",
# "HT275_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4",
# "HT275_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",
# "HT275_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
# "HT275_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",
# "HT275_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
# ## "DiMu_HT275_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4",
# "DiMu_HT275_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5",
# "DiMu_HT275_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4",
# "DiMu_HT275_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
# ],[40.352/6258.651,1941./6258.651,119.04 /6258.651,385.241/6258.651,3.756/6258.651,204.618/6258.651,1941.00/6258.651,694.178/6258.651,117.644/6258.651,694.178/6258.651,117.644/6258.651,],
# ),
# "HT325":([
# "HT325_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4",
# "HT325_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4",
# "HT325_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",
# "HT325_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
# "HT325_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",
# "HT325_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
# "DiMu_HT325_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4",
# "DiMu_HT325_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5",
# "DiMu_HT325_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4",
# "DiMu_HT325_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
# ],[40.352/6258.651,1941./6258.651,119.04 /6258.651,385.241/6258.651,3.756/6258.651,204.618/6258.651,1941.00/6258.651,694.178/6258.651,117.644/6258.651,694.178/6258.651,117.644/6258.651,],
# ),
"HT375":([
"HT375_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4",
"HT375_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4",
"HT375_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",
"HT375_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
"HT375_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",
"HT375_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
"DiMu_HT375_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT375_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5",
"DiMu_HT375_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT375_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
],[40.352/6258.651,1941./6258.651,119.04 /6258.651,385.241/6258.651,3.756/6258.651,204.618/6258.651,1941.00/6258.651,694.178/6258.651,117.644/6258.651,694.178/6258.651,117.644/6258.651,],
),
"HT475":([
"HT475_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4",
"HT475_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4",
"HT475_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",
"HT475_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
"HT475_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",
"HT475_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
"DiMu_HT475_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT475_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5",
"DiMu_HT475_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT475_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
],[40.352/6258.651,1941./6258.651,119.04 /6258.651,385.241/6258.651,3.756/6258.651,204.618/6258.651,1941.00/6258.651,694.178/6258.651,117.644/6258.651,694.178/6258.651,117.644/6258.651,],
),
"HT575":([
"HT575_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4",
"HT575_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4",
"HT575_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",
"HT575_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
"HT575_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",
"HT575_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
"DiMu_HT575_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT575_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5",
"DiMu_HT575_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT575_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
],[40.352/6258.651,1941./6258.651,119.04 /6258.651,385.241/6258.651,3.756/6258.651,204.618/6258.651,1941.00/6258.651,694.178/6258.651,117.644/6258.651,694.178/6258.651,117.644/6258.651,],
),
"HT675":([
"HT675_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4",
"HT675_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4",
"HT675_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",
"HT675_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
"HT675_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",
"HT675_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
"DiMu_HT675_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT675_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5",
"DiMu_HT675_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT675_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
],[40.352/6258.651,1941./6258.651,119.04 /6258.651,385.241/6258.651,3.756/6258.651,204.618/6258.651,1941.00/6258.651,694.178/6258.651,117.644/6258.651,694.178/6258.651,117.644/6258.651,],
),
"HT775":([
"HT775_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4",
"HT775_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4",
"HT775_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",
"HT775_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
"HT775_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",
"HT775_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
"DiMu_HT775_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT775_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5",
"DiMu_HT775_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT775_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
],[40.352/6258.651,1941./6258.651,119.04 /6258.651,385.241/6258.651,3.756/6258.651,204.618/6258.651,1941.00/6258.651,694.178/6258.651,117.644/6258.651,694.178/6258.651,117.644/6258.651,],
),
"HT875":([
"HT875_HLT_HT250_AlphaT0p55_v1_HLT_Mu5_HT200_v4",
"HT875_HLT_HT250_AlphaT0p55_v2_HLT_Mu40_HT200_v4",
"HT875_HLT_HT250_AlphaT0p53_v2_HLT_Mu15_HT200_v2",
"HT875_HLT_HT250_AlphaT0p53_v3_HLT_Mu15_HT200_v3",
"HT875_HLT_HT250_AlphaT0p53_v4_HLT_Mu15_HT200_v4",
"HT875_HLT_HT250_AlphaT0p53_v5_HLT_Mu30_HT200_v1",
"DiMu_HT875_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT875_HLT_HT250_AlphaT0p58_v3_HLT_DoubleMu8_Mass8_HT200_v5",
"DiMu_HT875_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v4",
"DiMu_HT875_HLT_HT250_AlphaT0p60_v3_HLT_DoubleMu8_Mass8_HT200_v5",
],[40.352/6258.651,1941./6258.651,119.04 /6258.651,385.241/6258.651,3.756/6258.651,204.618/6258.651,1941.00/6258.651,694.178/6258.651,117.644/6258.651,694.178/6258.651,117.644/6258.651,],
),
  }
  c1.open()
  for key,pairs in sorted(sums.iteritems()):
   Nom   = GetSumHist(File = ["./5GeVMuonsVBTFIDWithOddMuonVeto/5GeVMuonsOddVetoVBTFidHT375.root"], Directories = pairs[0], Hist = histList[0], Col = r.kBlack, Norm = pairs[1], LegendText = "")
   Nom.HideOverFlow()
   Denom = GetSumHist(File = ["./5GeVMuonsVBTFIDWithOddMuonVeto/5GeVMuonsOddVetoVBTFidHT375.root"], Directories = pairs[0], Hist = histList[1], Col = r.kRed,   Norm = pairs[1], LegendText = "")
   Denom.HideOverFlow()
   if "AlphaT" in histList[0]:
     Denom.hObj.SetTitle("%s"%(key))
     Denom.hObj.GetXaxis().SetTitle("#alpha_{T} (GeV)")
     Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %d "%(Denom.hObj.GetBinWidth(1)))
     Denom.hObj.GetYaxis().SetTitleOffset(1.15)
     Nom.hObj.SetMarkerStyle(20)
   else:
     Nom.Rebin(25,None)
     Denom.Rebin(25,None)
     if "DEBUG" in key:
       Denom.hObj.SetTitle("%s"%(key))
     else:
       Denom.hObj.SetTitle("%s"%(key))
     Denom.hObj.GetXaxis().SetTitle("H_{T} (GeV)")
     Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %d GeV"%(Denom.hObj.GetBinWidth(1)))
     Denom.hObj.GetYaxis().SetTitleOffset(1.15)
     Nom.hObj.SetMarkerStyle(20)
   c1.SetLog('y',True)
   Denom.hObj.GetXaxis().SetRangeUser(0.,1.)
   Denom.Draw("h")
   Nom.Draw("psame")
   c1.Print()
   c1.SetLog('y',False)
   turnon = TurnOn(Nom,Denom)
   # c1.Clear()
   turnon.setRange(0.,1.5)
   c1.cd()
   turnon.DifferentialTurnOn().SetTitle("%s"%(key))
   turnon.DifferentialTurnOn().Draw("ap")
   turnon.DifferentialTurnOn().GetXaxis().SetRangeUser(0.,1.5)
   c1.canvas.Update()

   c1.Print()
   cumNom   = Nom.CumulativeHist()
   cumDenom = Denom.CumulativeHist()
   cumuTurnOn = r.TGraphAsymmErrors()
   cumuTurnOn.Divide(cumNom,cumDenom)
   cumuTurnOn.GetXaxis().SetTitle("H_{T}^{cut} (GeV)")
   cumuTurnOn.GetXaxis().SetRangeUser(0.,1.5)

   cumuTurnOn.GetXaxis().SetTitleSize(0.05)
   cumuTurnOn.GetYaxis().SetTitle("Cumulative efficiency")
   cumuTurnOn.GetYaxis().SetTitleOffset(1.5)
   xval = r.Double(0)
   yval = r.Double(0)
   # assume that point is bin center.
   # HT bins are 25 GeV wide. so take point == Val/25 + 1
   # Get val from the text name of the key.


   point = int(0.55/Nom.hObj.GetBinWidth(1))
   cumuTurnOn.GetPoint(point,xval,yval)

   if "DEBUG" in key:
     cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(pair,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),0.55))
     if yval > 0.:
       text += "%s is %f + %f - %f Efficient at %f \n"%(pair,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),0.55)
   else:
     cumuTurnOn.SetTitle("%s is %f + %f - %f Efficient at %f"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),0.55))
     if yval > 0.:
       text += "%s is %f + %f - %f Efficient at %f \n"%(key,yval,cumuTurnOn.GetErrorYhigh(point),cumuTurnOn.GetErrorYlow(point),0.55)
   cumuTurnOn.Draw("ap")
   cumuTurnOn.GetXaxis().SetRangeUser(0.,1.5)
   c1.canvas.Update()
   c1.Print()
  outfile.write(text)
  c1.close()


if __name__ == '__main__':
  main()

