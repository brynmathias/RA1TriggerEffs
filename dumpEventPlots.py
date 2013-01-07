#!/usr/bin/env python
# encoding: utf-8

import os
import ROOT as r
from plottingUtils import *

fileName = "../14Dec_ABCD/rootfiles/outSinMu_ABCD_HT_trigEffs.root"

rFile = r.TFile.Open(fileName)

trigger = "HLT_HT400"

dirList = []
denomHistList = []
nomHistList = []
weightList = []

for k in rFile.GetListOfKeys():
    if "DEBUG" in k.GetName():
        dir = rFile.Get(k.GetName())
        
        for k2 in dir.GetListOfKeys():
            if "Denom" in k2.GetName() and "Pre_0" not in k2.GetName() and trigger in k2.GetName():
                h = rFile.Get(k.GetName()+"/"+k2.GetName())
		print k.GetName()+"/"+k2.GetName()
                if h.Integral() > 0:
                    #print h.Integral(), k2.GetName()
                    #print k.GetName()+"/"+k2.GetName()
                    if "le3j" in k.GetName():
                        dirList.append(k.GetName())
                        denomHistList.append(k2.GetName())
                        nomHistList.append(k2.GetName().replace("Denom", "Nom"))
                        weightList.append(float(k2.GetName().split("Pre")[1].split("_")[1]))    

print "dirList =", dirList
print "histList =", nomHistList
print "histList2 =", denomHistList
print "weightList =", weightList
