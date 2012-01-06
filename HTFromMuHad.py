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
# from HTFromMUHadDict import *
from MoreHTALphaTests import *
# HLT_HT600_v1Pre_1_HLT_HT300_v9Pre_210
def main():
  c1 = Print("MoreAlphaTHTTests275_out.pdf")
  c1.open()
  # c1.Print()


  outText = []

  print options.iteritems()
  for key,histList in sorted(options.iteritems()):
    for pair in histList:
      pair = pair.replace("Nom_","")
      pair = pair.replace("_Nom","")
      # if "_0" in pair: continue
      print key,pair
      mg = None
      c1.cd()
      c1.Clear()
      Nom   = GetSumHist(File = ["./5GeVMuonsVBTFIDWithOddMuonVeto/5GeVMuonsOddVetoVBTFidHT275.root"], Directories = [key], Hist = "Nom_"+pair if len(pair) >2 else pair+"_Nom", Col = r.kBlack, Norm = None, LegendText = "")
      Nom.HideOverFlow()
      Denom = GetSumHist(File = ["./5GeVMuonsVBTFIDWithOddMuonVeto/5GeVMuonsOddVetoVBTFidHT275.root"], Directories = [key], Hist = "Denom_"+pair if len(pair) >2 else pair+"_Denom", Col = r.kRed,  Norm = None, LegendText = "")
      print len(pair)
      if Nom.hObj.Integral() > 0: outText.append("%s, %s NomIntegral = %f DenomIntegral = %f"%(key,pair,Nom.hObj.Integral(),Denom.hObj.Integral()) if len(pair) == 2 else "%s, %s NomIntegral = %f, Weight will be %s DenomIntegral = %f"%(key,pair,Nom.hObj.Integral(),(pair.split("_"))[3],Denom.hObj.Integral()) )
      if Nom.hObj.Integral() == 0: continue
      Denom.HideOverFlow()
      Nom.Rebin(25,None)
      Denom.Rebin(25,None)
      Denom.Draw("h")
      Denom.hObj.GetXaxis().SetTitle("H_{T} (GeV)")
      Denom.hObj.GetYaxis().SetTitle("Number of Trigger events / %d GeV"%(Denom.hObj.GetBinWidth(1)))
      Denom.hObj.GetYaxis().SetTitleOffset(1.15)

      Nom.hObj.SetMarkerStyle(20)
      Nom.Draw("psame")
      c1.Print()
      # c1.toFile("Standard_"+pair)
      turnon = TurnOn(Nom,Denom)
      # turnon.setGraph(False)
      # c1.Clear()
      turnon.setRange(0.,3000.)
      c1.cd()
      turnon.DifferentialTurnOn().Draw("ap")
      Hist = r.TH1D()
      Hist= Nom.hObj.Clone()
      Hist.Divide(Denom.hObj)

      Hist.GetXaxis().SetTitleSize(0.05)
      Hist.GetYaxis().SetTitle("Efficiency")
      Hist.GetYaxis().SetRangeUser(-0.2,1.2)

      # c1.Print()
      c1.toFile(turnon.DifferentialTurnOn(),"Diff_"+pair)
      c1.Print()
      # leg = Legend()
      # print float(pair.split("_")[7])/float((pair.split("_")[3:4])[0])
      # if float(pair.split("_")[7])%float((pair.split("_")[3:4])[0]) == 0:
      cumNom   = Nom.CumulativeHist()
      cumDenom = Denom.CumulativeHist()
      cumDenom.GetYaxis().SetTitle("")
      cumDenom.Draw("h")
      cumNom.Draw("psame")
      c1.Print()
      # cumuTurnOn = r.TH1D()
      cumuTurnOn = r.TGraphAsymmErrors()
      # cumuTurnOn = cumNom.Clone()
      # cumuTurnOn.Divide(cumDenom)
      cumuTurnOn.Divide(cumNom,cumDenom)
      cumuTurnOn.GetXaxis().SetTitle("H_{T}^{cut} (GeV)")
      cumuTurnOn.GetXaxis().SetTitleSize(0.05)
      cumuTurnOn.GetYaxis().SetTitle("Cumulative efficiency")
      cumuTurnOn.GetYaxis().SetTitleOffset(1.5)
      print pair
      c1.toFile(cumNom,"CumuNom_"+pair)
      c1.toFile(cumDenom,"CumuDenom_"+pair)
      cumuTurnOn.Draw("ap")
      # c1.toFile(cumuTurnOn,"CUMULATIVETURNON_%s_(pre_=_%s)_from_ %s_(pre_=_%s) "%((pair.split("_")[1]),(pair.split("_")[3]),(pair.split("_")[5]),(pair.split("_")[-1])))
        # c1.Clear()
        #
        # for a in turnon.logEffs():
        #   a.SetNDC()
        #   a.Draw("same")
      c1.Print()
  c1.close()
  newOutText = ""
  for line in sorted(outText):
    newOutText += "%s\n"%(line)


  outF = open("./MoreAlphaTHTTests275.txt",'w')
  outF.write(newOutText)
  pass




if __name__ == '__main__':
  main()

