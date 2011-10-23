#!/usr/bin/env python

'''Created by Bryn Mathias
bryn.mathias@cern.ch
'''
import errno

import ROOT as r
import math
from time import strftime
import os, commands
import array
def ensure_dir(path):
    try:
      os.makedirs(path)
    except OSError as exc: # Python >2.5
      if exc.errno == errno.EEXIST:
        pass
      else: raise

r.gROOT.SetStyle("Plain") #To set plain bkgds for slides
r.gStyle.SetTitleBorderSize(0)
r.gStyle.SetCanvasBorderMode(0)
r.gStyle.SetCanvasColor(0)#Sets canvas colour white
r.gStyle.SetOptStat(1110)#set no title on Stat box
r.gStyle.SetLabelOffset(0.001)
r.gStyle.SetLabelSize(0.003)
r.gStyle.SetLabelSize(0.005,"Y")#Y axis
r.gStyle.SetLabelSize(0.1,"X")#Y axis
r.gStyle.SetTitleSize(0.06)
r.gStyle.SetTitleW(0.7)
r.gStyle.SetTitleH(0.07)
r.gStyle.SetOptTitle(1)
r.gStyle.SetOptStat(0)
r.gStyle.SetOptFit(1)
r.gStyle.SetAxisColor(1, "XYZ");
r.gStyle.SetStripDecimals(r.kTRUE);
r.gStyle.SetTickLength(0.03, "XYZ");
r.gStyle.SetNdivisions(510, "XYZ");
r.gStyle.SetPadTickX(1);
r.gStyle.SetPadTickY(1);
r.gStyle.SetLabelColor(1, "XYZ");
r.gStyle.SetLabelFont(42, "XYZ");
r.gStyle.SetLabelOffset(0.01, "XYZ");
r.gStyle.SetLabelSize(0.05, "XYZ");
r.gStyle.SetHatchesLineWidth(2)
# from PlottingFunctions import *
# r.gROOT.SetBatch(True) # suppress the creation of canvases on the screen.. much much faster if over a remote connection
# r.gROOT.SetStyle("Plain") #To set plain bkgds for slides
# r.gROOT.ProcessLine(".L ./Jets30/tdrstyle.C+")
r.gStyle.SetPalette(1)
# r.gROOT.ProcessLine(".L ./errorFun.C+")
intlumi =35.0 #4.433 #inv pico barns

def GetHist(DataSetName,folder,hist,col,norm,Legend):
    a = r.TFile.Open(DataSetName) #open the file
    # closeList.append(a) # append the file to the close list
    b = a.Get(folder) #open the directory in the root file
    Hist = b.Get(hist) # get your histogram by name
    # if Hist == None : Hist = r.TH1D()
    if Legend != 0:
      leg.AddEntry(Hist,Legend,"LP") # add a legend entry
    Hist.SetLineWidth(3)
    Hist.SetLineColor(col) #set colour
    Hist.SetBinContent(Hist.GetNbinsX() ,Hist.GetBinContent(Hist.GetNbinsX())+Hist.GetBinContent(Hist.GetNbinsX()+1))
    Hist.SetBinError(Hist.GetNbinsX() ,math.sqrt((Hist.GetBinError(Hist.GetNbinsX()))**2 + (Hist.GetBinError(Hist.GetNbinsX()+1))**2))
    Hist.SetBinContent(Hist.GetNbinsX()+1,0)
    if norm != 0:
       Hist.Scale(1.) #if not data normilse to the data by lumi, MC is by default weighted to 100pb-1, if you have changed this change here!
    return Hist

leg = r.TLegend(0.1, 0.6, 0.8, 0.8)
leg.SetShadowColor(0)
leg.SetBorderSize(0)
leg.SetFillStyle(4100)
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.SetShadowColor(0)
leg.SetBorderSize(0)
leg.SetFillStyle(4100)
leg.SetFillColor(0)
leg.SetLineColor(0)
prelim = r.TLatex(0.15,0.92,"#scale[0.8]{CMS}")
prelim.SetNDC()
lumi = r.TLatex(0.45,.82,"#scale[0.8]{#int L dt = 35 pb^{-1}, #sqrt{s} = 7 TeV}")
lumi.SetNDC()
c1 = r.TCanvas("canvas","canname",1200,1400)

# mainPad = r.TPad("","",0.01,0.01,0.99,0.99);
# mainPad.SetNumber(1);
# mainPad.SetRightMargin(10.)
# mainPad.SetBottomMargin(0.5);
# mainPad.Draw();


BitList=["Bit15","Bit16","Bit17","Bit18","Bit19","Bit20","Bit21","RecoHTL1100","RecoHTL1150","RecoHTL175","RecoHTL150"]#,"RecoHTL150","RecoHTL1100","RecoHTL1150"]
RefList = ["RefJet","RefJet","RefJet","RefJet","RefJet","RefJet","RefJet","RecoHT","RecoHT","RecoHT","RecoHT"]
CorThresholds =   [16.,20.,36.,52.,68.,92.,128.,100.,150.,75.,50.]
UnCorThresholds = [16.,20.,36.,52.,68.,92.,128.,100.,150.,75.,50.]


# Conversion Table:
# L1 Uncorrected   L1 Corrected Threshold
# 6U                  16
# 8U                  16
# 10U                 20
# 14U                 28
# 18U                 32
# 20U                 36
# 30U                 52
# 40U                 68
# 50U                 80
# 60U                 92
# 90U                 128
def errorFun(x, par):
  return 0.5*par[0]*(1. + r.TMath.Erf( (x[0] - par[1]) / (math.sqrt(2.)*par[2]) ))
def reBiner(Hist,minimum):
  """docstring for reBiner"""
  upArray = []
  nBins = -1
  for bin in range(0,Hist.GetNbinsX()):
    binC = 0
    if Hist.GetBinContent(bin) > minimum:
      upArray.append(Hist.GetBinLowEdge(bin+1))
      nBins+=1
    else:
      binC += Hist.GetBinContent(bin)
      if binC > minimum:
        upArray.append(Hist.GetBinLowEdge(bin+1))
        nBins+=1
        binC = 0
  upArray.append(Hist.GetBinLowEdge(Hist.GetNbinsX()))
  nBins+=1
  rebinList = array.array('d',upArray)
  # print upArray
  # print nBins
  return (nBins,rebinList)


# First Make Turn on curves
def MakeTurnOn(CorrHist = None,):
  out = []
  Nom = GetHist(CorrHist,"noAlphaT","AlphaT_all",1,0,"PromprReco-v4 Threshold")
  DeNom = GetHist(CorrHist,"TriggerOnly","AlphaT_all",1,0,0)
  # (i,bins)= reBiner(Nom,0.)
  bins = array.array('d',[0.,0.55,10.])
  a = Nom.Rebin(2,"a",bins)
  # a =  Nom.Rebin(i,"a",bins)
  # a.Draw("hist")
  # raw_input()
  b = DeNom.Rebin(2,"b",bins)
  # b =  DeNom.Rebin(i,"b",bins)
  # b.Draw("hist")
  # raw_input()i
  mg = r.TMultiGraph()
  TurnOn = r.TGraphAsymmErrors()
  TurnOn.Divide(a,b)
  TurnOn.SetMarkerColor(4)
  TurnOn.SetMarkerStyle(20)
  TurnOn.SetLineWidth(5)
  TurnOn.SetLineColor(4)
  mg.Add(TurnOn)
  out.append(TurnOn)
  c1.Clear()
  leg.Clear()
  # leg.AddEntry(TurnOn,"AlphaT 0.55 with 45GeV Jet thesholds, RecoJet requirement is for 275Bin.", "LP")
  mg.Draw("ap")

  mg.GetXaxis().SetTitle("#alpha_{T}")
  mg.GetYaxis().SetTitle("% of events passing offline selection")
  mg.GetYaxis().SetLabelSize(0.02)
  c1.Update()
  leg.Draw("same")
  ensure_dir("./")
  c1.SaveAs("./TurnOnFor_alphat055_250HT_6Jets40GeV_HLT200.pdf")
  #c1.Clear()
  leg.Clear()
  return out
# File2 = "MinBias_ZeroBiasTrigger.root"
# File = "JET_eta3_AllJetTriggers.root"
File2 = None


File = "TriggerTest.root"
File = "Trigger45Threshold.root"
File = "Trigger6Jets.root"
File = "Trigger6Jets_HT200HLT.root"
File = "LowetPlot.root"
outDir = File[0:-5]
a = MakeTurnOn(CorrHist = File)


