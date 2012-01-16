#!/usr/bin/env python

from plottingUtils import *
import ROOT as r


settings = {
  "dirs":["275_325","325_375","375_475","475_575","575_675","675_775","775_875","875",],
  "plots":["AlphaT_all",],
  "AlphaTBins":[(int(0.51/0.01),int(0.52/0.01)),(int(0.52/0.01),int(0.53/0.01)),(int(0.53/0.01),int(0.55/0.01)),(int(0.55/0.01),int(10./0.01)+1),],
}

# mcGjets (None, None, 1290.0, 440.0, 178.0, 58.0, 20.0, 14.0)
# mcMuon (1541.28739072, 720.8726988799999, 520.3570512, 178.41035081, 66.33, 22.22, 7.67, 5.21)
# mcMuon2Jet (375.86688832, 225.52190848, 156.90827712, 38.949782029999994, 13.58, 5.0, 1.25, 1.0)
 # nPhot2Jet (None, None, 427, 127, 34, 10, 2, 1)
# mcPhot2Jet (None, None, 600.0, 150.0, 57.0, 16.0, 4.0, 3.0)
# mcTtw (1851.08014784, 717.12018944, 500.57183904000004, 171.11035361999998, 57.86, 23.08, 6.77, 5.48)
# mcZinv [1663.76, 702.96, 572.219944358578, 211.97037731287259, 79.05718701700152, 27.721351291675866, 10.267167145065134, 7.187017001545595]
# mcZinv01 (1663.76, 702.96, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
# mcZinv27 (0.0, 0.0, 572.219944358578, 211.97037731287259, 79.05718701700152, 27.721351291675866, 10.267167145065134, 7.187017001545595)
# mcZmumu (125.21, 76.95, 45.27, 16.12, 9.04, 3.02, 0.0, 1.21)




#HadSelectionDY.root
#HadSelectionData.root
#HadSelectionTTbar.root
#HadSelectionWJets250.root
#HadSelectionWJets300.root
#HadSelectionWJetsInclusive.root
#HadSelectionZinv100.root
#HadSelectionZinv200.root
#HadSelectionZinv50.root
#MuSelectionData.root
#MuSelectionTTbar.root
#MuSelectionWJets250.root
#MuSelectionWJets300.root
#MuSelectionWJetsInclusive.root
#MuSelectionZinv100.root
#MuSelectionZinv200.root
#MuSelectionZinv50.root
#MuonSelectionDY.root


samples = {

    "nHad":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionData","","Data","Had"),
    # "nHad_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionData","btag_","Data","Had"),

    # "nSingleMu_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionData","btag_OneMuon_","Data","Muon"),
    "nMuon":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionData","OneMuon_","Data","Muon"),
    "nMumu":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionData","DiMuon_","Data","DiMuon"),
    # "nDiMu_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionData","btag_DiMuon_","Data","DiMuon"),
    
    # "dict1":{"HT":"275","Yield":3500.,"SampleType":"Data","Category":"Muon"},
    # "dict1":{"HT":"275","Yield":3500.,"SampleType":"Data","Category":"Muon"},
    # "dict2":{"HT":"275","Yield":1049.,"SampleType":"Data","Category":"Had"},
    # "dict3":{"HT":"275","Yield":2011.,"SampleType":"Data","Category":"DiMuon"},
    # "dict4":{"HT":"275","Yield":1802.,"SampleType":"Data","Category":"Photon","Error":10},
    # "dict5":{"HT":"275","Yield":180.,"SampleType":"TTbar","Category":"Muon"},
    # "dict6":{"HT":"275","Yield":228.,"SampleType":"WJets250","Category":"Muon"},
    # "dict7":{"HT":"275","Yield":121.,"SampleType":"WJets300","Category":"Muon"},
    # "dict8":{"HT":"275","Yield":573.,"SampleType":"WJetsInc","Category":"Muon"},
    # "dict9":{"HT":"275","Yield":220.,"SampleType":"TTbar","Category":"Had"},
    # "dict10":{"HT":"275","Yield":220.,"SampleType":"WJets250","Category":"Had"},
    # "dict11":{"HT":"275","Yield":220.,"SampleType":"WJets300","Category":"Had"},
    # "dict12":{"HT":"275","Yield":220.,"SampleType":"WJetsInc","Category":"Had"},
    # "dict13":{"HT":"275","Yield":220.,"SampleType":"Zinv50","Category":"Had"},
    # "dict14":{"HT":"275","Yield":220.,"SampleType":"Zinv100","Category":"Had"},
    # "dict15":{"HT":"275","Yield":220.,"SampleType":"Zinv200","Category":"Had"},
    # "dict16":{"HT":"275","Yield":170.,"SampleType":"Zmumu","Category":"DiMuon"},
    # "dict17":{"HT":"275","Yield":2120.,"SampleType":"Photon","Category":"Photon"},
    
    
    
    
    # "HadZinv50":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionZinv50","","Zinv50","Had"),
    # "HadZinv100":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionZinv100","","Zinv100","Had"),
    # "HadZinv200":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionZinv200","","Zinv200","Had"),
    # "HadSelectionDY":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionDY","","Zmumu","Had"),
    # "mcMuon1":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionWJetsInclusive","","WJetsInc","Had"),
    # "mcMuon2":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionWJets250","","WJets250","Had"),
    # "mcMuon3":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionWJets300","","WJets300","Had"),
    # "mcTtw (add the mcMuonNumbers to me) ":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionTTbar","","TTbar","Had"),
    # "DiMuSelectionDY":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuonSelectionDY","DiMuon_","Zmumu","DiMuon"),
    # "DiMuZinv50" :("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv50","DiMuon_","Zinv50","DiMuon"),
    # "DiMuZinv100":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv100","DiMuon_","Zinv100","DiMuon"),
    # "DiMuZinv200":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv200","DiMuon_","Zinv200","DiMuon"),
    # "DiMuWJetsInc":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJetsInclusive","DiMuon_","WJetsInc","DiMuon"),
    # "DiMuWJets250":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJets250","DiMuon_","WJets250","DiMuon"),
    # "DiMuWJets300":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJets300","DiMuon_","WJets300","DiMuon"),
    # "DiMuTTbar":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionTTbar","DiMuon_","TTbar","DiMuon"),
    # "SingleMuSelectionDY":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuonSelectionDY","OneMuon_","Zmumu","Muon"),
    # "mcZinv01" :("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv50","OneMuon_","Zinv50","Muon"),
    # "mcZinv27":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv100","OneMuon_","Zinv100","Muon"),
    # "mcZinv27_2":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv200","OneMuon_","Zinv200","Muon"),
    # "mcMuon1":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJetsInclusive","OneMuon_","WJetsInc","Muon"),
    # "mcMuon2":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJets250","OneMuon_","WJets250","Muon"),
    # "mcMuon3":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJets300","OneMuon_","WJets300","Muon"),
    # "mcTtw (add the mcMuonNumbers to me) ":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionTTbar","OneMuon_","TTbar","Muon"),
    # "HadZinv50_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionZinv50","btag_"),
    # "HadZinv100_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionZinv100","btag_"),
    # "HadZinv200_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionZinv200","btag_"),
    # "HadSelectionDY_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionDY","btag_"),
    # "HadWJetsInc_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionWJetsInclusive","btag_"),
    # "HadWJets250_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionWJets250","btag_"),
    # "HadWJets300_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionWJets300","btag_"),
    # "HadTTbar_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/HadSelectionTTbar","btag_"),
    # "DiMuSelectionDY_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuonSelectionDY","btag_DiMuon_"),
    # "DiMuZinv50" :("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv50","btag_DiMuon_"),
    # "DiMuZinv100_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv100","btag_DiMuon_"),
    # "DiMuZinv200_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv200","btag_DiMuon_"),
    # "DiMuWJetsInc_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJetsInclusive","btag_DiMuon_"),
    # "DiMuWJets250_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJets250","btag_DiMuon_"),
    # "DiMuWJets300_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJets300","btag_DiMuon_"),
    # "DiMuTTbar_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionTTbar","btag_DiMuon_"), 
    # 
    # "SingleMuSelectionDY_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuonSelectionDY","btag_OneMuon_"),
    # "SingleMuZinv50_btag" :("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv50","btag_OneMuon_"),
    # "SingleMuZinv100_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv100","btag_OneMuon_"),
    # "SingleMuZinv200_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionZinv200","btag_OneMuon_"),
    # "SingleMuWJetsInc_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJetsInclusive","btag_OneMuon_"),
    # "SingleMuWJets250_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJets250","btag_OneMuon_"),
    # "SingleMuWJets300_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionWJets300","btag_OneMuon_"),
    # "SingleMuTTbar_btag":("./RA1_Muon_Analysis/MuonExcludedFromAlphaT/MuSelectionTTbar","btag_OneMuon_"),


}
# for key in sorted(samples):


# nHad = "sampleDict = {"
# 
# for key,fi in sorted(samples.iteritems()):
#     i = 0
#     # print fi
#     for dir in settings['dirs']:
#         nHad += "\t\"%s_%d\"  : "%(key,i)
#         i+=1
#         nHad += "{\"HT\":\"%s\","%(dir[0:3])
#         for histName in settings['plots']:
#             # print key,fi[0],fi[1]+dir,histName
#             dir = fi[1]+dir
#             normal =  GetSumHist(File = ["%s.root"%fi[0]], Directories = [dir], Hist = histName, Col = r.kBlack, Norm = None if "n" == key[0] else [4650./100.], LegendText = "nBtag")
#             normal.HideOverFlow()
#             nHad +=" \"Yield\": %.3e ,\"SampleType\":\"%s\",\"Category\":\"%s\"},\n"%(normal.hObj.Integral(),fi[2],fi[3])
# nHad +="}"
# print nHad

# 

alphaTbins = [0.51,0.52,0.53,0.55,0.56]#[0.5+0.01*i for i in range(12)]#
HTbins = [275.,325.,]+[375+100*i for i in range(7)]



nHad = ""
# 
c1 = Print("BinnedYeildPlots.pdf")
# c1.
c1.open()
for key,fi in sorted(samples.iteritems()):
    # print fi
    hist =  r.TH2D("finalPlot","%s"%(key),len(HTbins)-1,array.array('d',HTbins),len(alphaTbins)-1,array.array('d',alphaTbins))
    for dir in settings['dirs']:
        # print dir
        # nHad += "\t%s %s = (\n"%(key,dir)
        for histName in settings['plots']:
            binDir = dir
            dir = fi[1]+dir
            for aTbin in settings["AlphaTBins"]:
                print float(binDir.split("_")[0]),aTbin[0]
                HT = float(binDir.split("_")[0])

                bin = hist.FindBin(float((binDir.split("_")[0]))+10.,float(0.01*aTbin[0])+0.005)
                # print key,fi[0],fi[1]+dir,histName
# if "n" == key[0] else [4650./100.]    
                normal =  GetSumHist(File = ["%s.root"%fi[0]], Directories = [dir], Hist = histName, Col = r.kBlack, Norm = None , LegendText = "nBtag")
                aT = normal.hObj.GetBinLowEdge(aTbin[0]+1)
                print normal.hObj.GetBinLowEdge(aTbin[0]) + 0.005
                nHad +="%s_%s %.2f %.3e\n"%(key,dir,aTbin[0]*0.01,normal.hObj.Integral(aTbin[0]+1,aTbin[1]+1))
                if (aT+0.005 > 0.55 and HT+5. > 275.) or ( aT+0.005 >0.53 and HT+5. > 575) or ( aT+0.005 > 0.52 and HT+5. > 775 ):
                    hist.SetBinContent(bin,normal.hObj.Integral(aTbin[0]+1,aTbin[1]+1))
                else: hist.SetBinContent(bin,0.)
    hist.Draw("textCOLZ")
    c1.Print()        # nHad += ") \n"
c1.close()
# 
# 
# 
# 
# 
# 
# # nHad +="}"
print nHad



# 
# # function to give bin by bin translation from 4 input variables
# 
# MC_Weights = {"TTbar":0.00425452,"WJetsInc":0.0666131,"WJets250":0.000450549,"WJets300":0.00102329,"Zinv50":0.00485311,"Zinv100":0.00410382,"Zinv200":0.0013739,"Zmumu":0.00849073,"Photon":1.,"Data":1.}
# 600./157.66
# 

SingleMuWJets250 = (  0.000e+00 ,  0.000e+00 ,  3.365e-01 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
SingleMuWJets300 = (  0.000e+00 ,  0.000e+00 ,  1.491e+02 ,  3.741e+01 ,  1.317e+01 ,  5.004e+00 ,  1.254e+00 ,  1.004e+00 ,) 
SingleMuWJetsInc = (  3.748e+02 ,  2.176e+02 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
MuW = (a+b+c for a,b,c in zip(SingleMuWJets250,SingleMuWJets300,SingleMuWJetsInc))


MuonYeilds =  (  4.360e+02 ,  1.920e+02 ,  1.640e+02 ,  3.700e+01 ,  6.000e+00 ,  1.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
PhotonMC =  (None, None, 600.0, 150.0, 57.0, 16.0, 4.0, 3.0)
MuTT = (  3.308e+01 ,  1.318e+01 ,  8.242e+00 ,  2.018e+00 ,  4.086e-01 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
MuonMC = ( a+b for a,b in zip(MuTT,MuW))
PhotonYeilds = (None, None, 427, 127, 34, 10, 2, 1)

HTBins = (275,325,375,475,575,675,775,875)


# for gamma,mu in zip(PhotonMC,MuonMC):
#      if gamma is not None:
#          print mu/gamma, mu, gamma

        


# Collect eveything we need

NJetSingleMuTTbar    = (  4.646e+02 ,  2.183e+02 ,  1.533e+02 ,  5.526e+01 ,  2.250e+01 ,  5.970e+00 ,  1.030e+00 ,  9.533e-01 ,) 
NJetSingleMuWJets250 = (  0.000e+00 ,  0.000e+00 ,  1.963e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
NJetSingleMuWJets300 = (  0.000e+00 ,  0.000e+00 ,  3.416e+02 ,  1.182e+02 ,  4.333e+01 ,  1.534e+01 ,  6.280e+00 ,  4.042e+00 ,) 
NJetSingleMuWJetsInc = (  9.936e+02 ,  5.029e+02 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 

NJetDiMuSelectionDY = (  1.133e+02 ,  7.556e+01 ,  4.479e+01 ,  1.612e+01 ,  9.043e+00 ,  3.020e+00 ,  0.000e+00 ,  1.208e+00 ,) 
NJetDiMuTTbar = (  5.318e+00 ,  3.854e-01 ,  1.019e+00 ,  1.423e+00 ,  1.897e-01 ,  0.000e+00 ,  1.389e-01 ,  7.088e-01 ,) 
NJetDiMuWJets250 = (  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
NJetDiMuWJets300 = (  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
NJetDiMuWJetsInc = (  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 


DiJetSingleMuTTbar    = (  3.308e+01 ,  1.318e+01 ,  8.242e+00 ,  2.018e+00 ,  4.086e-01 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
DiJetSingleMuWJets250 = (  0.000e+00 ,  0.000e+00 ,  3.365e-01 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
DiJetSingleMuWJets300 = (  0.000e+00 ,  0.000e+00 ,  1.491e+02 ,  3.741e+01 ,  1.317e+01 ,  5.004e+00 ,  1.254e+00 ,  1.004e+00 ,) 
DiJetSingleMuWJetsInc = (  3.748e+02 ,  2.176e+02 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
DiJetMuSelectionDY    = (  5.905e+00 ,  1.853e+00 ,  2.516e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 

DiJetDiMuSelectionDY = (  4.776e+01 ,  3.285e+01 ,  2.337e+01 ,  5.088e+00 ,  8.923e-01 ,  1.555e+00 ,  0.000e+00 ,  1.496e-01 ,) 
DiJetDiMuTTbar = (  4.003e-01 ,  0.000e+00 ,  1.408e-02 ,  2.433e-01 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
DiJetDiMuWJets250 = (  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
DiJetDiMuWJets300 = (  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 
DiJetDiMuWJetsInc = (  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,  0.000e+00 ,) 



def BinErrors():
    """docstring for BinErrors"""
    pass



def predictBin(HT,n_x,n_y,n_x_MC,n_y_MC):
    """docstring for predictBin"""
    # print HT
    if n_x == None: return None
    factor = n_y_MC/n_x_MC
    prediction = factor * n_x
    # print HT
    return " %d|  %d * %.3f  = %.3f | %d "%(HT,n_x,factor, prediction,n_y)
    pass





NJetPhotonYeild = (None, None, 1046, 375, 130, 59, 18, 14)
NJetPhotonMC = []
for a,b in zip((None, None, 1290.0, 440.0, 178.0, 58.0, 20.0, 14.0), (None, None, 0.98, 0.99, 0.99, 0.99, 0.99, 0.99)):
    if a is None:
        NJetPhotonMC.append(a)
    else: NJetPhotonMC.append(a*b)



NJetMuonMc      = [(a+b+c+d)*e for a,b,c,d,e in zip(NJetSingleMuTTbar,NJetSingleMuWJets250,NJetSingleMuWJets300,NJetSingleMuWJetsInc,(0.89, 0.94, 0.97, 0.97, 0.97, 0.97, 0.97, 0.97))]
NJetMuonYeild   = (  1.421e+03 ,  6.440e+02 ,  5.170e+02 ,  1.690e+02 ,  5.200e+01 ,  1.800e+01 ,  8.000e+00 ,  1.000e+00 ,) 
NJetDiMuonMc    = [(a+b+c+d+e)*f for a,b,c,d,e,f in zip(NJetDiMuSelectionDY,NJetDiMuTTbar,NJetDiMuWJets250,NJetDiMuWJets300,NJetDiMuWJetsInc,(0.89, 0.94, 0.97, 0.97, 0.97, 0.97, 0.97, 0.97))]
NJetDiMuonYeild = (  1.140e+02 ,  6.500e+01 ,  4.200e+01 ,  1.500e+01 ,  7.000e+00 ,  1.000e+00 ,  0.000e+00 ,  2.000e+00 ,) 

DiJetPhotonYeild = (None, None, 427, 127, 34, 10, 2, 1)
DiJetPhotonMC = (None, None, 600.0, 150.0, 57.0, 16.0, 4.0, 3.0)

DiJetMuonMc  =  [(a+b+c+d)*e for a,b,c,d,e in zip(DiJetSingleMuTTbar,DiJetSingleMuWJets250,DiJetSingleMuWJets300,DiJetSingleMuWJetsInc,(0.89, 0.94, 0.97, 0.97, 0.97, 0.97, 0.97, 0.97))]
DiJetMuonYeild = (  4.360e+02 ,  1.920e+02 ,  1.640e+02 ,  3.700e+01 ,  6.000e+00 ,  1.000e+00 ,  0.000e+00 ,  0.000e+00 ,)
DiJetDiMuonMc  = [(a+b+c+d+e)*f for a,b,c,d,e,f in zip(DiJetDiMuSelectionDY,DiJetDiMuTTbar,DiJetDiMuWJets250,DiJetDiMuWJets300,DiJetDiMuWJetsInc,(0.89, 0.94, 0.97, 0.97, 0.97, 0.97, 0.97, 0.97))]
DiJetDiMuonYeild = (  4.900e+01 ,  3.100e+01 ,  1.800e+01 ,  5.000e+00 ,  1.000e+00 ,  1.000e+00 ,  0.000e+00 ,  0.000e+00 ,)


print "Predict for the DiJet case DiMuons from Muons"
print " HTBin |  SingleMuon * Factor  = Prediction | nDiMuon "
print "_"*50
for HT,n_x,n_y,n_x_MC,n_y_MC in zip(HTBins,DiJetMuonYeild,DiJetDiMuonYeild,DiJetMuonMc,DiJetDiMuonMc):
    if predictBin(HT,n_x,n_y,n_x_MC,n_y_MC) is not None:
        print  predictBin(HT,n_x,n_y,n_x_MC,n_y_MC)
print "_"*50


print "Predict for the NJet case DiMuons from Muons"
print " HTBin |  SingleMuon * Factor  = Prediction | nDiMuon "
print "_"*50
for HT,n_x,n_y,n_x_MC,n_y_MC in zip(HTBins,NJetMuonYeild,NJetDiMuonYeild,NJetMuonMc,NJetDiMuonMc):
    if predictBin(HT,n_x,n_y,n_x_MC,n_y_MC) is not None:
        print  predictBin(HT,n_x,n_y,n_x_MC,n_y_MC)
print "_"*50



print "Predict for the DiJet case DiMuons from Photons"
print " HTBin |  Photon * Factor  = Prediction | nDiMuon "
print "_"*50
# print HTBins,DiJetPhotonYeild,DiJetDiMuonYeild,DiJetPhotonMC,DiJetDiMuonMc
for HT,n_x,n_y,n_x_MC,n_y_MC in zip(HTBins,DiJetPhotonYeild,DiJetDiMuonYeild,DiJetPhotonMC,DiJetDiMuonMc):
    # print "HELLO NICK"
    if predictBin(HT,n_x,n_y,n_x_MC,n_y_MC) is not None:
        print  predictBin(HT,n_x,n_y,n_x_MC,n_y_MC)
print "_"*50



print "Predict for the NJet case DiMuons from Photons"
print " HTBin |  Photon * Factor  = Prediction | nDiMuon "
print "_"*50
for HT,n_x,n_y,n_x_MC,n_y_MC in zip(HTBins,NJetPhotonYeild,NJetDiMuonYeild,NJetPhotonMC,NJetDiMuonMc):
    if predictBin(HT,n_x,n_y,n_x_MC,n_y_MC) is not None:
        print  predictBin(HT,n_x,n_y,n_x_MC,n_y_MC)
print "_"*50



print "Predict for the DiJet case Muons from Photons"
print " HTBin |  Photon * Factor  = Prediction | nMuon "
print "_"*50
# print HTBins,DiJetPhotonYeild,DiJetDiMuonYeild,DiJetPhotonMC,DiJetDiMuonMc
for HT,n_x,n_y,n_x_MC,n_y_MC in zip(HTBins,DiJetPhotonYeild,DiJetMuonYeild,DiJetPhotonMC,DiJetMuonMc):
    if predictBin(HT,n_x,n_y,n_x_MC,n_y_MC) is not None:
        print  predictBin(HT,n_x,n_y,n_x_MC,n_y_MC)
print "_"*50



print "Predict for the NJet case Muons from Photons"
print " HTBin |  Photon * Factor  = Prediction | nMuon "
print "_"*50
for HT,n_x,n_y,n_x_MC,n_y_MC in zip(HTBins,NJetPhotonYeild,NJetMuonYeild,NJetPhotonMC,NJetMuonMc):
    if predictBin(HT,n_x,n_y,n_x_MC,n_y_MC) is not None:
        print  predictBin(HT,n_x,n_y,n_x_MC,n_y_MC)
print "_"*50










