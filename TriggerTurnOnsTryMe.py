#!/usr/bin/env python
# encoding: utf-8
"""
HTEffCombinErrorsUseTurnOnClass.py

Created by Bryn Mathias on 2011-12-12.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
from plottingUtils import *
from TurnOn import *
import array
r.gROOT.SetBatch(True) # suppress the creation of canvases on the screen.. much much faster if over a remote connection

# bin signal triggers in HT
doCrossHTbinning = False


def main():
  text = ""

  sums ={

### Run2012D
#"HT275AlphaT":([
#  'HT275_le3j_HLT_HT250_AlphaT0p55_v8_HLT_IsoMu24_v17',
#  'HT275_le3j_HLT_HT250_AlphaT0p57_v8_HLT_IsoMu24_v17',
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_trigEffs.root"),
#
#"HT325AlphaT":([
#  'HT325_le3j_HLT_HT300_AlphaT0p53_v8_HLT_IsoMu24_v17',
#  'HT325_le3j_HLT_HT300_AlphaT0p54_v14_HLT_IsoMu24_v17',
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_trigEffs.root"),
#
#"HT375AlphaT":([
#  'HT375_le3j_HLT_HT350_AlphaT0p52_v8_HLT_IsoMu24_v17',
#  'HT375_le3j_HLT_HT350_AlphaT0p53_v19_HLT_IsoMu24_v17',
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_trigEffs.root"),
#
#"HT475AlphaT":([
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_v17',
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_trigEffs.root"),
#
#"HT575AlphaT":([
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_v17',
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_trigEffs.root"),
#
#"HT675AlphaT":([
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_v17',
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_trigEffs.root"),
#
#"HT775AlphaT":([
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_v17',
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_trigEffs.root"),
#
#"HT875AlphaT":([
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17',
#  'HT475_le3j_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_v17',
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_trigEffs.root"),

### Run2012AB
#"HT275AlphaT":([
#"HT275_HLT_HT250_AlphaT0p55_v1_HLT_IsoMu24_eta2p1_v11",
#"HT275_HLT_HT250_AlphaT0p55_v2_HLT_IsoMu24_eta2p1_v12",
#"HT275_HLT_HT250_AlphaT0p55_v3_HLT_IsoMu24_eta2p1_v12",
#"HT275_HLT_HT250_AlphaT0p55_v4_HLT_IsoMu24_v15",
#],"../HCP_17Oct_SinMuAB/outSinMu_HCP_AB_275.root"),
#
#"HT325AlphaT":([
#"HT325_HLT_HT300_AlphaT0p53_v1_HLT_IsoMu24_eta2p1_v11",
#"HT325_HLT_HT300_AlphaT0p53_v2_HLT_IsoMu24_eta2p1_v12",
#"HT325_HLT_HT300_AlphaT0p53_v3_HLT_IsoMu24_eta2p1_v12",
#"HT325_HLT_HT300_AlphaT0p53_v4_HLT_IsoMu24_v15",
#"HT325_HLT_HT300_AlphaT0p53_v5_HLT_IsoMu24_v15",
#],"../HCP_17Oct_SinMuAB/outSinMu_HCP_AB_325.root"),
#
#"HT375AlphaT":([
#"HT375_HLT_HT350_AlphaT0p52_v1_HLT_IsoMu24_eta2p1_v11",
#"HT375_HLT_HT350_AlphaT0p52_v2_HLT_IsoMu24_eta2p1_v12",
#"HT375_HLT_HT350_AlphaT0p52_v3_HLT_IsoMu24_eta2p1_v12",
#"HT375_HLT_HT350_AlphaT0p52_v4_HLT_IsoMu24_v15",
#"HT375_HLT_HT350_AlphaT0p52_v5_HLT_IsoMu24_v15",
#],"../HCP_17Oct_SinMuAB/outSinMu_HCP_AB_375.root"),
#
#"HT475AlphaT":([
#"HT475_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT475_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
#],"../HCP_17Oct_SinMuAB/outSinMu_HCP_AB_375.root"),
#
#"HT575AlphaT":([
#"HT475_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT475_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
#],"../HCP_17Oct_SinMuAB/outSinMu_HCP_AB_375.root"),
#
#"HT675AlphaT":([
#"HT475_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT475_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
#],"../HCP_17Oct_SinMuAB/outSinMu_HCP_AB_375.root"),
#
#"HT775AlphaT":([
#"HT475_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT475_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
#],"../HCP_17Oct_SinMuAB/outSinMu_HCP_AB_375.root"),
#
#"HT875AlphaT":([
#"HT475_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT475_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT475_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
#],"../HCP_17Oct_SinMuAB/outSinMu_HCP_AB_375.root"),
#

##"HT225AlphaT":([
##"HT225_HLT_HT200_AlphaT0p57_v5_HLT_IsoMu24_v15",
##],"../out225_90jet.root"),
#

### Full Run2012ABC

#"HT275AlphaT":([
#"HT_275HLT_HT250_AlphaT0p55_v1_HLT_IsoMu24_eta2p1_v11",
#"HT_275HLT_HT250_AlphaT0p55_v2_HLT_IsoMu24_eta2p1_v12",
#"HT_275HLT_HT250_AlphaT0p55_v3_HLT_IsoMu24_eta2p1_v12",
#"HT_275HLT_HT250_AlphaT0p55_v4_HLT_IsoMu24_v15",
#"HT_275HLT_HT200_AlphaT0p57_v5_HLT_IsoMu24_v15",
#],"../HCP_09Oct_FitProbStudy/outSinMu_HCP_ge4j_275.root"),

#"HT325AlphaT":([
#"HT_325HLT_HT300_AlphaT0p53_v1_HLT_IsoMu24_eta2p1_v11",
#"HT_325HLT_HT300_AlphaT0p53_v2_HLT_IsoMu24_eta2p1_v12",
#"HT_325HLT_HT300_AlphaT0p53_v3_HLT_IsoMu24_eta2p1_v12",
#"HT_325HLT_HT300_AlphaT0p53_v4_HLT_IsoMu24_v15",
#"HT_325HLT_HT300_AlphaT0p53_v5_HLT_IsoMu24_v15",
#],"../HCP_09Oct_FitProbStudy/outSinMu_HCP_ge4j_325.root"),
#
#"HT375AlphaT":([
#"HT_375HLT_HT350_AlphaT0p52_v1_HLT_IsoMu24_eta2p1_v11",
#"HT_375HLT_HT350_AlphaT0p52_v2_HLT_IsoMu24_eta2p1_v12",
#"HT_375HLT_HT350_AlphaT0p52_v3_HLT_IsoMu24_eta2p1_v12",
#"HT_375HLT_HT350_AlphaT0p52_v4_HLT_IsoMu24_v15",
#"HT_375HLT_HT350_AlphaT0p52_v5_HLT_IsoMu24_v15"
#],"../HCP_09Oct_FitProbStudy/outSinMu_HCP_ge4j_375.root"),
#
#"HT475AlphaT":([
#"HT_475HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT_475HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT_475HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT_475HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#],"../HCP_09Oct_FitProbStudy/outSinMu_HCP_ge4j_375.root"),
#
#"HT575AlphaT":([
#"HT_575HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT_575HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT_575HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT_575HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#],"../HCP_09Oct_FitProbStudy/outSinMu_HCP_ge4j_375.root"),
#
#"HT675AlphaT":([
#"HT_675HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT_675HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT_675HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT_675HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#],"../HCP_09Oct_FitProbStudy/outSinMu_HCP_ge4j_375.root"),
#
#"HT775AlphaT":([
#"HT_775HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT_775HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT_775HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT_775HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#],"../HCP_09Oct_FitProbStudy/outSinMu_HCP_ge4j_375.root"),
#
#"HT875AlphaT":([
#"HT_875HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
#"HT_875HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
#"HT_875HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#"HT_875HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
#],"../HCP_09Oct_FitProbStudy/outSinMu_HCP_ge4j_375.root"),

### Run2012B
#"HT275AlphaT":([
#"HT275_HLT_HT250_AlphaT0p55_v4_HLT_IsoMu24_v15",
#"HT275_HLT_HT250_AlphaT0p55_v5_HLT_IsoMu24_v15",
#],"../HCP_30Sep_gctStudy/outSinMu_Run2012B_275.root"),

#"HT375AlphaT":([
#"HT375_HLT_HT350_AlphaT0p52_v4_HLT_IsoMu24_v15",
#"HT375_HLT_HT350_AlphaT0p52_v5_HLT_IsoMu24_v15",
#"HT375_HLT_HT350_AlphaT0p53_v15_HLT_IsoMu24_v15",
#"HT375_HLT_HT350_AlphaT0p53_v16_HLT_IsoMu24_v15",
#],"../HCP_30Sep_gctStudy/outSinMu_Run2012B_375.root"),
#
##"HT475AlphaT":([
##"HT475_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
##"HT475_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
##"HT475_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
##"HT475_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
##],"../HCP_30Sep_gctStudy/outSinMu_Run2012B_375.root"),
##
##"HT575AlphaT":([
##"HT575_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
##"HT575_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
##"HT575_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
##"HT575_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
##],"../HCP_30Sep_gctStudy/outSinMu_Run2012B_375.root"),
##
##"HT675AlphaT":([
##"HT675_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
##"HT675_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
##"HT675_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
##"HT675_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
##],"../HCP_30Sep_gctStudy/outSinMu_Run2012B_375.root"),
##
##"HT775AlphaT":([
##"HT775_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
##"HT775_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
##"HT775_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
##"HT775_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
##],"../HCP_30Sep_gctStudy/outSinMu_Run2012B_375.root"),
##
##"HT875AlphaT":([
##"HT875_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
##"HT875_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
##"HT875_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
##"HT875_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
##],"../HCP_30Sep_gctStudy/outSinMu_Run2012B_375.root"),


### Run2012C
#"HT275AlphaT":([
#"HT275_HLT_HT250_AlphaT0p55_v6_HLT_IsoMu24_v16",
#"HT275_HLT_HT250_AlphaT0p55_v8_HLT_IsoMu24_v17",
#],"../HCP_30Sep_gctStudy/outSinMu_Run2012C_275.root"),

#"HT375AlphaT":([
#"HT375_HLT_HT350_AlphaT0p52_v6_HLT_IsoMu24_v16",
#"HT375_HLT_HT350_AlphaT0p52_v8_HLT_IsoMu24_v17",
#"HT375_HLT_HT350_AlphaT0p53_v17_HLT_IsoMu24_v16",
#"HT375_HLT_HT350_AlphaT0p53_v17_HLT_IsoMu24_v17",
#],"../HCP_30Sep_gctStudy/outSinMu_Run2012C_375.root"),
#
#"HT475AlphaT":([
#"HT475_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
#"HT475_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
#"HT475_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
#"HT475_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
#],"../HCP_30Sep_gctStudy/outSinMu_Run2012C_375.root"),
#
#"HT575AlphaT":([
#"HT575_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
#"HT575_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
#"HT575_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
#"HT575_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
#],"../HCP_30Sep_gctStudy/outSinMu_Run2012C_375.root"),
#
#"HT675AlphaT":([
#"HT675_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
#"HT675_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
#"HT675_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
#"HT675_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
#],"../HCP_30Sep_gctStudy/outSinMu_Run2012C_375.root"),
#
#"HT775AlphaT":([
#"HT775_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
#"HT775_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
#"HT775_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
#"HT775_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
#],"../HCP_30Sep_gctStudy/outSinMu_Run2012C_375.root"),
#
#"HT875AlphaT":([
#"HT875_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
#"HT875_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
#"HT875_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
#"HT875_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
#],"../HCP_30Sep_gctStudy/outSinMu_Run2012C_375.root"),

#"HT275":([
#"HLT_HT250_v1_HLT_HT250_v1",
#"HLT_HT250_v2_HLT_HT250_v2",
#"HLT_HT250_v3_HLT_HT250_v3",
#"HLT_HT250_v4_HLT_HT250_v4",
#"HLT_HT250_v5_HLT_HT250_v5",
#"HLT_HT250_v7_HLT_HT250_v7",
#"HLT_HT250_v1_HLT_IsoMu24_eta2p1_v13",
#  ],"../HCP_11Oct_jMulti_HTtrigs/outSinMu_HCP_jM_HTtrig_275.root"),
#
#"HT325":([
#"HLT_HT300_v1_HLT_HT250_v1",
#"HLT_HT300_v2_HLT_HT250_v2",
#"HLT_HT300_v3_HLT_HT250_v3",
##"HT325_HLT_HT300_v4_HLT_HT250_v4",
##"HT325_HLT_HT300_v5_HLT_HT250_v5",
##"HT325_HLT_HT300_v7_HLT_HT250_v7",
#  ],"../HCP_26Sep_HT/outHT_325.root"),

#"HT375":([
#"HLT_HT350_v1_HLT_HT250_v1",
#"HLT_HT350_v2_HLT_HT250_v2",
#"HLT_HT350_v3_HLT_HT250_v3",
#"HLT_HT350_v4_HLT_HT250_v4",
#"HLT_HT350_v5_HLT_HT250_v5",
#"HLT_HT350_v7_HLT_HT250_v7",
#  ],"../HCP_26Sep_HT/outHT_375.root"),
#
#"HT475":([
#"HLT_HT450_v1_HLT_HT250_v1",
#"HLT_HT450_v2_HLT_HT250_v2",
#"HLT_HT450_v3_HLT_HT250_v3",
#"HLT_HT450_v4_HLT_HT250_v4",
#"HLT_HT450_v5_HLT_HT250_v5",
#"HLT_HT450_v7_HLT_HT250_v7",
#  ],"../HCP_26Sep_HT/outHT_375.root"),
#
#"HT575":([
#"HLT_HT450_v1_HLT_HT250_v1",
#"HLT_HT450_v2_HLT_HT250_v2",
#"HLT_HT450_v3_HLT_HT250_v3",
#"HLT_HT450_v4_HLT_HT250_v4",
#"HLT_HT450_v5_HLT_HT250_v5",
#"HLT_HT450_v7_HLT_HT250_v7",
#  ],"../HCP_26Sep_HT/outHT_375.root"),
#
#"HT675":([
#"HLT_HT450_v1_HLT_HT250_v1",
#"HLT_HT450_v2_HLT_HT250_v2",
#"HLT_HT450_v3_HLT_HT250_v3",
#"HLT_HT450_v4_HLT_HT250_v4",
#"HLT_HT450_v5_HLT_HT250_v5",
#"HLT_HT450_v7_HLT_HT250_v7",
#  ],"../HCP_26Sep_HT/outHT_375.root"),
#
#"HT775":([
#"HLT_HT450_v1_HLT_HT250_v1",
#"HLT_HT450_v2_HLT_HT250_v2",
#"HLT_HT450_v3_HLT_HT250_v3",
#"HLT_HT450_v4_HLT_HT250_v4",
#"HLT_HT450_v5_HLT_HT250_v5",
#"HLT_HT450_v7_HLT_HT250_v7",
#  ],"../HCP_26Sep_HT/outHT_375.root"),
#
#"HT875":([
#"HLT_HT450_v1_HLT_HT250_v1",
#"HLT_HT450_v2_HLT_HT250_v2",
#"HLT_HT450_v3_HLT_HT250_v3",
#"HLT_HT450_v4_HLT_HT250_v4",
#"HLT_HT450_v5_HLT_HT250_v5",
#"HLT_HT450_v7_HLT_HT250_v7",
#  ],"../HCP_26Sep_HT/outHT_375.root"),

#"HT375":([
#"HLT_HT350_v2_HLT_IsoMu24_eta2p1_v12",
#  ],"../HCP_26Sep_HT/outHT_375.root")

### Run2012D
#"HT275":([
#  "le3j_HLT_HT250_v7_HLT_IsoMu24_v17",
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_IsoMu24_HT_trigEffs.root"),
#"HT325":([
#  "le3j_HLT_HT300_v7_HLT_IsoMu24_v17",
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_IsoMu24_HT_trigEffs.root"),
#"HT375":([
#  "le3j_HLT_HT350_v7_HLT_IsoMu24_v17",
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_IsoMu24_HT_trigEffs.root"),
#"HT475":([
#  "le3j_HLT_HT450_v7_HLT_IsoMu24_v17",
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_IsoMu24_HT_trigEffs.root"),
#"HT575":([
#  "le3j_HLT_HT450_v7_HLT_IsoMu24_v17",
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_IsoMu24_HT_trigEffs.root"),
#"HT675":([
#  "le3j_HLT_HT450_v7_HLT_IsoMu24_v17",
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_IsoMu24_HT_trigEffs.root"),
#"HT775":([
#  "le3j_HLT_HT450_v7_HLT_IsoMu24_v17",
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_IsoMu24_HT_trigEffs.root"),
#"HT875":([
#  "le3j_HLT_HT450_v7_HLT_IsoMu24_v17",
#  ],"../12Dec_Run2012D/rootfiles/outSinMu_Run2012D_IsoMu24_HT_trigEffs.root"),
#

#### Run 2012 ABCD!!

#"HT225AlphaT":([
#  "HT225_ge4j_HLT_HT200_AlphaT0p57_v2_HLT_IsoMu24_eta2p1_v11",
#  "HT225_ge4j_HLT_HT200_AlphaT0p57_v3_HLT_IsoMu24_eta2p1_v12",
#  "HT225_ge4j_HLT_HT200_AlphaT0p57_v4_HLT_IsoMu24_eta2p1_v12",
#  "HT225_ge4j_HLT_HT200_AlphaT0p57_v5_HLT_IsoMu24_v15",
#  "HT225_ge4j_HLT_HT200_AlphaT0p57_v6_HLT_IsoMu24_v16",
#  "HT225_ge4j_HLT_HT200_AlphaT0p57_v8_HLT_IsoMu24_v17",
#],"../14Dec_ABCD/rootfiles/outSinMu_ABCD_trigEffs.root"),

"HT275AlphaT":([
  "HT275_HLT_HT250_AlphaT0p55_v1_HLT_IsoMu24_eta2p1_v11",
  "HT275_HLT_HT250_AlphaT0p55_v2_HLT_IsoMu24_eta2p1_v12",
  "HT275_HLT_HT250_AlphaT0p55_v3_HLT_IsoMu24_eta2p1_v12",
  "HT275_HLT_HT250_AlphaT0p55_v4_HLT_IsoMu24_v15",
  "HT275_HLT_HT250_AlphaT0p55_v5_HLT_IsoMu24_v15",
  "HT275_HLT_HT250_AlphaT0p55_v6_HLT_IsoMu24_v16",
  "HT275_HLT_HT250_AlphaT0p55_v8_HLT_IsoMu24_v17",
  #"HT275_le3j_HLT_HT250_AlphaT0p57_v1_HLT_IsoMu24_eta2p1_v11",
  #"HT275_le3j_HLT_HT250_AlphaT0p57_v2_HLT_IsoMu24_eta2p1_v12",
  #"HT275_le3j_HLT_HT250_AlphaT0p57_v3_HLT_IsoMu24_eta2p1_v12",
  #"HT275_le3j_HLT_HT250_AlphaT0p57_v4_HLT_IsoMu24_v15",
  #"HT275_le3j_HLT_HT250_AlphaT0p57_v5_HLT_IsoMu24_v15",
  #"HT275_le3j_HLT_HT250_AlphaT0p57_v6_HLT_IsoMu24_v16",
  #"HT275_le3j_HLT_HT250_AlphaT0p57_v8_HLT_IsoMu24_v17",
],"../14Dec_ABCD/rootfiles/outSinMu_ABCD_trigEffs.root"),

"HT325AlphaT":([
  "HT325_HLT_HT300_AlphaT0p53_v1_HLT_IsoMu24_eta2p1_v11",
  "HT325_HLT_HT300_AlphaT0p53_v2_HLT_IsoMu24_eta2p1_v12",
  "HT325_HLT_HT300_AlphaT0p53_v3_HLT_IsoMu24_eta2p1_v12",
  "HT325_HLT_HT300_AlphaT0p53_v4_HLT_IsoMu24_v15",
  "HT325_HLT_HT300_AlphaT0p53_v5_HLT_IsoMu24_v15",
  "HT325_HLT_HT300_AlphaT0p53_v6_HLT_IsoMu24_v16",
  "HT325_HLT_HT300_AlphaT0p53_v8_HLT_IsoMu24_v17",
  #"HT325_le3j_HLT_HT300_AlphaT0p54_v10_HLT_IsoMu24_v15",
  #"HT325_le3j_HLT_HT300_AlphaT0p54_v11_HLT_IsoMu24_v15",
  #"HT325_le3j_HLT_HT300_AlphaT0p54_v12_HLT_IsoMu24_v16",
  #"HT325_le3j_HLT_HT300_AlphaT0p54_v14_HLT_IsoMu24_v17",
  #"HT325_le3j_HLT_HT300_AlphaT0p54_v8_HLT_IsoMu24_eta2p1_v12",
  #"HT325_le3j_HLT_HT300_AlphaT0p54_v9_HLT_IsoMu24_eta2p1_v12",
],"../14Dec_ABCD/rootfiles/outSinMu_ABCD_trigEffs.root"),

"HT375AlphaT":([
  "HT375_HLT_HT350_AlphaT0p52_v1_HLT_IsoMu24_eta2p1_v11",
  "HT375_HLT_HT350_AlphaT0p52_v2_HLT_IsoMu24_eta2p1_v12",
  "HT375_HLT_HT350_AlphaT0p52_v3_HLT_IsoMu24_eta2p1_v12",
  "HT375_HLT_HT350_AlphaT0p52_v4_HLT_IsoMu24_v15",
  "HT375_HLT_HT350_AlphaT0p52_v5_HLT_IsoMu24_v15",
  "HT375_HLT_HT350_AlphaT0p52_v6_HLT_IsoMu24_v16",
  "HT375_HLT_HT350_AlphaT0p52_v8_HLT_IsoMu24_v17",
  #"HT375_le3j_HLT_HT350_AlphaT0p53_v12_HLT_IsoMu24_eta2p1_v11",
  #"HT375_le3j_HLT_HT350_AlphaT0p53_v13_HLT_IsoMu24_eta2p1_v12",
  #"HT375_le3j_HLT_HT350_AlphaT0p53_v14_HLT_IsoMu24_eta2p1_v12",
  #"HT375_le3j_HLT_HT350_AlphaT0p53_v15_HLT_IsoMu24_v15",
  #"HT375_le3j_HLT_HT350_AlphaT0p53_v16_HLT_IsoMu24_v15",
  #"HT375_le3j_HLT_HT350_AlphaT0p53_v17_HLT_IsoMu24_v16",
  #"HT375_le3j_HLT_HT350_AlphaT0p53_v19_HLT_IsoMu24_v17",
],"../14Dec_ABCD/rootfiles/outSinMu_ABCD_trigEffs.root"),

"HT475AlphaT":([
  "HT475_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
  "HT475_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
  "HT475_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
  "HT475_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
  "HT475_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
  "HT475_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
  #"HT475_le3j_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
  #"HT475_le3j_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
  #"HT475_le3j_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
  #"HT475_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
  #"HT475_le3j_HLT_HT400_AlphaT0p52_v7_HLT_IsoMu24_eta2p1_v11",
  #"HT475_le3j_HLT_HT400_AlphaT0p52_v8_HLT_IsoMu24_eta2p1_v12",
  #"HT475_le3j_HLT_HT400_AlphaT0p52_v9_HLT_IsoMu24_eta2p1_v12",
],"../14Dec_ABCD/rootfiles/outSinMu_ABCD_trigEffs.root"),

"HT575AlphaT":([
  "HT575_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
  "HT575_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
  "HT575_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
  "HT575_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
  "HT575_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
  "HT575_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
  #"HT575_le3j_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
  #"HT575_le3j_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
  #"HT575_le3j_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
  #"HT575_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
  #"HT575_le3j_HLT_HT400_AlphaT0p52_v7_HLT_IsoMu24_eta2p1_v11",
  #"HT575_le3j_HLT_HT400_AlphaT0p52_v8_HLT_IsoMu24_eta2p1_v12",
  #"HT575_le3j_HLT_HT400_AlphaT0p52_v9_HLT_IsoMu24_eta2p1_v12",
],"../14Dec_ABCD/rootfiles/outSinMu_ABCD_trigEffs.root"),

 "HT675AlphaT":([
   "HT675_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
   "HT675_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
   "HT675_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
   "HT675_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
   "HT675_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
   "HT675_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
   #"HT675_le3j_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
   #"HT675_le3j_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
   #"HT675_le3j_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
   #"HT675_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
   #"HT675_le3j_HLT_HT400_AlphaT0p52_v7_HLT_IsoMu24_eta2p1_v11",
   #"HT675_le3j_HLT_HT400_AlphaT0p52_v8_HLT_IsoMu24_eta2p1_v12",
   #"HT675_le3j_HLT_HT400_AlphaT0p52_v9_HLT_IsoMu24_eta2p1_v12",
 ],"../14Dec_ABCD/rootfiles/outSinMu_ABCD_trigEffs.root"),
 
 "HT775AlphaT":([
   "HT775_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
   "HT775_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
   "HT775_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
   "HT775_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
   "HT775_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
   "HT775_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
   #"HT775_le3j_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
   #"HT775_le3j_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
   #"HT775_le3j_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
   #"HT775_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
   #"HT775_le3j_HLT_HT400_AlphaT0p52_v7_HLT_IsoMu24_eta2p1_v11",
   #"HT775_le3j_HLT_HT400_AlphaT0p52_v8_HLT_IsoMu24_eta2p1_v12",
   #"HT775_le3j_HLT_HT400_AlphaT0p52_v9_HLT_IsoMu24_eta2p1_v12",
 ],"../14Dec_ABCD/rootfiles/outSinMu_ABCD_trigEffs.root"),

"HT875AlphaT":([
  "HT875_HLT_HT400_AlphaT0p51_v13_HLT_IsoMu24_eta2p1_v12",
  "HT875_HLT_HT400_AlphaT0p51_v14_HLT_IsoMu24_eta2p1_v12",
  "HT875_HLT_HT400_AlphaT0p51_v15_HLT_IsoMu24_v15",
  "HT875_HLT_HT400_AlphaT0p51_v16_HLT_IsoMu24_v15",
  "HT875_HLT_HT400_AlphaT0p51_v17_HLT_IsoMu24_v16",
  "HT875_HLT_HT400_AlphaT0p51_v19_HLT_IsoMu24_v17",
  #"HT875_le3j_HLT_HT400_AlphaT0p52_v10_HLT_IsoMu24_v15",
  #"HT875_le3j_HLT_HT400_AlphaT0p52_v11_HLT_IsoMu24_v15",
  #"HT875_le3j_HLT_HT400_AlphaT0p52_v12_HLT_IsoMu24_v16",
  #"HT875_le3j_HLT_HT400_AlphaT0p52_v14_HLT_IsoMu24_v17",
  #"HT875_le3j_HLT_HT400_AlphaT0p52_v7_HLT_IsoMu24_eta2p1_v11",
  #"HT875_le3j_HLT_HT400_AlphaT0p52_v8_HLT_IsoMu24_eta2p1_v12",
  #"HT875_le3j_HLT_HT400_AlphaT0p52_v9_HLT_IsoMu24_eta2p1_v12",
],"../14Dec_ABCD/rootfiles/outSinMu_ABCD_trigEffs.root"),

}

#HCP_30Sep_gctStudy/outSinMu_Run2012B_375.root
#HCP_30Sep_gctStudy/outSinMu_Run2012C_375.root



  jMulti = "ge4j"
  NumsForFinalPlot = []
  for key,Dirs in sorted(sums.iteritems()):
    if"AlphaT" not in key: histList = ("HT_Nom","HT_Denom")
    if"AlphaT" in key: histList = ("AlphaT_Nom","AlphaT_Denom")

    if "AlphaT" in key:axisTitle = "#alpha_{T}"
    else:axisTitle="H_{T}"
    
    if doCrossHTbinning:
      histList = ("HT_Nom","HT_Denom")
      axisTitle = "H_{T}"

    numeratorList = []
    denominatorList = []
    
    if doCrossHTbinning:
#      BinEdges = [100. + 25*i for i in range(175/25)]
#      for i in range(6):
#        newBin = 275.+i*100
#        if newBin == eval( key[2:5] ):
#          BinEdges += [newBin, 1000.]
#          break
#        else:
#          BinEdges += [float(newBin)]
        BinEdges = [100. + 25.*i for i in range(eval(key[2:5])/25)]+[1000.]
    else:
        BinEdges = [ 0.3 + 0.01*i for i in range(10)] + [0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.6]
    
    print BinEdges
    
    for Dir in Dirs[0]:
      
      tmp = Dir.split("_")
      tmp.insert(1, jMulti)
      Dir = "_".join(tmp)

      aNom = GetSumHist(File = [Dirs[1]], Directories = [Dir], Hist = histList[0], Col = r.kBlack, Norm = None, LegendText = "")
      aNom.hObj.SetTitle(Dir)
      if "AlphaT" not in key:aNom.Rebin(10,None)
      if "AlphaT" in key: aNom.Rebin(len(BinEdges)-1,BinEdges)
      # aNom.Rebin(5,None)
      aNom.HideOverFlow()

      print aNom.hObj.Integral()

      numeratorList.append(aNom)
      aDenom =  GetSumHist(File = [Dirs[1]], Directories = [Dir], Hist = histList[1], Col = r.kRed, Norm = None, LegendText = "")
      aDenom.hObj.SetTitle(Dir)

      if "AlphaT" not in key:aDenom.Rebin(10,None)
      if "AlphaT" in key: aDenom.Rebin(len(BinEdges)-1,BinEdges)
      # aDenom.Rebin(5,None)
      # , "DENOM INT"
      if aNom.hObj.Integral() > aDenom.hObj.Integral(): print "ERROR !!!!!!!!!"
      aDenom.HideOverFlow()
      denominatorList.append(aDenom)
    c1 = Print("./plotDump/%s_%s_RunAtFNAL.pdf"%(key, jMulti))
    #c1.SetGrid(True)
    c1.DoPageNum = False

    c1.open()
    DiffNomList = []
    DiffDenomList = []
    CumuNomList = []
    CumuDenomList = []
    for nom,denom in zip(numeratorList,denominatorList):
      # nom.hObj.SetTitle(key)
      # print nom.hObj.Integral() , "IN LOOP", "Above alphaT 0.55 =",nom.hObj.GetBinContent(nom.hObj.GetNbinsX())
      # denom.hObj.SetTitle(Dir)
      # nom.hObj.SetName(key)
      # print nom.hObj.Integral() , "IN LOOP"
      # denom.hObj.SetName(Dir)
      print "STUFF", nom.hObj, denom.hObj
      if denom.hObj.Integral() > 0.:
        DiffNomList.append(nom.hObj)
        DiffDenomList.append(denom.hObj)
        CumuNomList.append(MakeCumu(nom.hObj))
        CumuDenomList.append(MakeCumu(denom.hObj))
      else:
        print "ERROR: denom histo is empty!"
    for a in DiffNomList:
      print "PRINT NAMES!!!", a.GetName()
    DiffTurnOn = TurnOn(DiffNomList,DiffDenomList)
    for nom,denom in zip(DiffTurnOn.numerator,DiffTurnOn.denominator):
      if "alpha" in axisTitle:
        denom.GetYaxis().SetTitle("Events / %1.4f"%(denom.GetBinWidth(1)))
        denom.GetXaxis().SetRangeUser(0.,5.)
      if "H_" in axisTitle:
        denom.GetYaxis().SetTitle("Events / %1.f GeV"%(denom.GetBinWidth(1)))
        denom.GetXaxis().SetRangeUser(0.,1000.)

      denom.GetYaxis().SetLabelSize(0.035)
      denom.GetYaxis().SetTitleOffset(1.3)
      denom.Draw("h")
      nom.Draw("psame")
      c1.SetLog('y',True)
      c1.Print()
      c1.SetLog('y',False)
    #DiffTurnOn.TotDenominator.SetTitle("Total Differential Hists for %s"%(key))
    DiffTurnOn.TotDenominator.SetTitle("")

    if "alpha" in axisTitle:
      DiffTurnOn.TotDenominator.GetYaxis().SetTitle("Events / %1.4f"%(DiffTurnOn.TotDenominator.GetBinWidth(1)))
      DiffTurnOn.TotDenominator.GetXaxis().SetRangeUser(0.,5.)
    if "H_" in axisTitle:
      DiffTurnOn.TotDenominator.GetYaxis().SetTitle("Events / %1.f GeV"%(DiffTurnOn.TotDenominator.GetBinWidth(1)))
      DiffTurnOn.TotDenominator.GetXaxis().SetRangeUser(0.,1000.)
    DiffTurnOn.TotDenominator.GetYaxis().SetLabelSize(0.035)
    DiffTurnOn.TotDenominator.GetYaxis().SetTitleOffset(1.3)
    c1.SetLog('y',True)
    DiffTurnOn.TotDenominator.Draw("h")
    DiffTurnOn.TotNumerator.Draw("psame")
    c1.Print()
    c1.SetLog('y',False)
    for curve in DiffTurnOn.listOfTurnOns:
      if"AlphaT" in key: curve.GetXaxis().SetRangeUser(0.,5.)
      else: curve.GetXaxis().SetRangeUser(0.,1000.)
      print "="*25
      print "Differential Turn on for %s"%(Dir)
      print "="*25
      # curve.SetTitle("Differential Turn on for %s"%(Dir))
      curve.SetTitle()
      curve.GetXaxis().SetTitle(axisTitle)
      curve.GetYaxis().SetTitle("Efficiency")
      curve.GetXaxis().SetTitleSize(0.045)
      curve.GetYaxis().SetTitleOffset(1.15)
      curve.Draw("ap")
      c1.Print()
    FinalDiff = DiffTurnOn.SumOfTurnOns()
    #FinalDiff.SetTitle("Total Differential Turn on for %s"%(key))
    FinalDiff.SetTitle("")

    FinalDiff.GetXaxis().SetTitle(axisTitle)
    #if"AlphaT" in key: FinalDiff.GetXaxis().SetRangeUser(0.0,2.0)
    if"AlphaT" in key: FinalDiff.GetXaxis().SetRangeUser(0.35,0.6)
    else: FinalDiff.GetXaxis().SetRangeUser(0.,1000.)
    FinalDiff.GetYaxis().SetTitle("Efficiency")
#    FinalDiff.GetYaxis().SetTitleOffset(1.15)
#    FinalDiff.GetXaxis().SetTitleSize(0.045)
    FinalDiff.GetYaxis().SetTitleOffset(0.9)
    FinalDiff.GetYaxis().SetTitleSize(0.05)
    FinalDiff.GetXaxis().SetTitleOffset(0.7)
    FinalDiff.GetXaxis().SetTitleSize(0.08)
    FinalDiff.Draw("ap")

    # add CMS Lumi stamp
    t = r.TLatex(0.15,0.86,"CMS, L_{int} = 11.7 fb^{-1}, #sqrt{s} = 8 TeV")
    t.SetNDC()
    t.SetTextSize(0.04)
    #t.Draw()

    if jMulti=="le3j":    tText = "2 \leq n_{jet} \leq 3"
    elif jMulti=="ge4j":  tText = "n_{jet} \geq 4"
    t1 = r.TLatex(0.15, 0.8, tText)
    t1.SetNDC()
    t1.SetTextSize(0.04)
    t1.Draw()

    c1.Print()
    xVal = r.Double(0)
    yVal = r.Double(0)
    point = []
    # for gPoint in range(FinalDiff.GetN()):
    #   FinalDiff.GetPoint(gPoint,xVal,yVal)
    #   if "AlphaT" in key:
    #     text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Differential \n"%(key,xVal,yVal,FinalDiff.GetErrorYhigh(gPoint),FinalDiff.GetErrorYlow(gPoint)))
    #   else:text +=("%s at %3.0f %1.3f + %1.3f - %1.3f efficient  Differential \n"%(key,xVal,yVal,FinalDiff.GetErrorYhigh(gPoint),FinalDiff.GetErrorYlow(gPoint)))

    CumuTurnOn = TurnOn(CumuNomList,CumuDenomList)
    for curve in CumuTurnOn.ListOfTurnOns():
      # curve.SetTitle("Cumulative Turn on for %s"%(Dir))
      curve.GetXaxis().SetTitle(axisTitle)
      curve.GetXaxis().SetTitleSize(0.045)
      curve.GetYaxis().SetTitle("Cumulative Efficiency")
      curve.GetYaxis().SetTitleOffset(1.15)
      if"AlphaT" in key: curve.GetXaxis().SetRangeUser(0.,5.)
      else: curve.GetXaxis().SetRangeUser(0.,1000.)
      curve.Draw("ap")
      c1.Print()
    CumuTurnOn.TotDenominator.SetTitle("Total Cumulative Hists for %s"%(key))
    if "alpha" in axisTitle:
      CumuTurnOn.TotDenominator.GetYaxis().SetTitle("Cumulative Events / %1.4f"%(CumuTurnOn.TotDenominator.GetBinWidth(1)))
      CumuTurnOn.TotDenominator.GetXaxis().SetRangeUser(0.,5.)
    if "H_" in axisTitle:
      CumuTurnOn.TotDenominator.GetYaxis().SetTitle("Cumulative Events / %1.f GeV"%(CumuTurnOn.TotDenominator.GetBinWidth(1)))
    CumuTurnOn.TotDenominator.GetYaxis().SetLabelSize(0.035)
    CumuTurnOn.TotDenominator.GetYaxis().SetTitleOffset(1.3)
    CumuTurnOn.TotDenominator.Draw("h")
    CumuTurnOn.TotNumerator.Draw("psame")
    c1.SetLog('y',True)
    c1.Print()
    c1.SetLog('y',False)
    FinalCumu = CumuTurnOn.SumOfTurnOns()
    FinalCumu.SetTitle("Total Cumulative Turn on for %s"%(key))
    FinalCumu.GetXaxis().SetTitle(axisTitle)
    if "AlphaT" in key: 
        FinalCumu.GetXaxis().SetRangeUser(0.4,1.)
        FinalCumu.GetXaxis().SetTitle("#alpha_{T}^{cut}")
    if "AlphaT" not in key: 
        FinalCumu.GetXaxis().SetRangeUser(0.,1000.)
        FinalCumu.GetXaxis().SetTitle("H_{T}^{cut}")
    FinalCumu.GetYaxis().SetTitle("Cumulative Efficiency")
    FinalCumu.GetYaxis().SetTitleOffset(1.15)
    FinalCumu.GetXaxis().SetTitleSize(0.045)
    # c1.SetLog('y',True)
    FinalCumu.Draw("ap")
    c1.Print()
    # c1.SetLog('y',False)
    xVal = r.Double(0)
    yVal = r.Double(0)
    c1.close()


    point = []
    for Point in range(FinalCumu.GetN()):
      #print text, Point
      FinalCumu.GetPoint(Point,xVal,yVal)
      #print "XVAL =",xVal
      if "AlphaT" in key:
        if xVal > 0.55:# and xVal < 0.61:
          text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Cumu \n"%(key,xVal-0.005,yVal,FinalCumu.GetErrorYhigh(Point),FinalCumu.GetErrorYlow(Point)))
          if xVal == 0.55: text = text + " ***"
      else:text +=("%s at %f %1.3f + %1.3f - %1.3f efficient  Cumu \n"%(key,xVal,yVal,FinalCumu.GetErrorYhigh(Point),FinalCumu.GetErrorYlow(Point)))
  textFile = open("textDump/text_%s.txt"%jMulti,'w')
  textFile.write(text)

if __name__ == '__main__':
  main()
