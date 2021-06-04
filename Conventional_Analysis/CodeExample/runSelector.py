from ROOT import TChain, TFile
import sys, os, time
from optparse import OptionParser
import multiprocessing as mp

def worker(chain,arg):                                                                                                                                                                                                     
        chain.Process("MySelector.C+", arg)     

def parallel_exec(target, args_list, name=None, sleep = 30):
        tot_events = 0
        pids = []
        for a in args_list:
                #if len(pids) >= nproc:
                #        wait_completion(pids, sleep=sleep)
                p = mp.Process(target=target, args=(a,))        
                n = str(a) 
                print( ">>> Started: "+str(n) )
                p.name = n
                pids.append(p)
                p.start()
                if len(pids)==1:
                        time.sleep(10) 
        wait_all(pids)    
        return

def wait_all(pids):
    for p in pids:
        p.join()    
    print( "All jobs finished !" )
    return

def runJobs(idir):
        myChain = TChain('mini') 
        for filename in os.listdir(idir):
                if not '.root' in filename: continue 
                print("INFO \t Adding file %s"%filename)  
                myChain.Add(idir+filename) 
        nev = myChain.GetEntries()
        if "/Data/" in idir:
                print("INFO \t Running on real data with %i events"%(nev))
                arg =  "Data %s"%runcardfile
        else:
                print("INFO \t Running on MC with %i events"%(nev))
                arg =  "MC %s"%runcardfile
        myChain.Process("MySelector.C+", arg)                                                                                                                                                     

parser = OptionParser()
parser.add_option("--header", help="header file to use", default="")
parser.add_option("--source", help="source file to use", default="")
parser.add_option("--runcard", help="use runcard to specify cuts", default="")
parser.add_option("--doData", help = "run on data", default=0)
parser.add_option("--doMC", help="run on mc", default=0)
parser.add_option("--dataset", help="which data set to run on [1largeRjet1lep,1lep,1lep1tau,2lep,3lep,4lep,exactly2lep,GamGam]", default="3lep")
(options, args) = parser.parse_args()

h_file = str(options.header)
c_file = str(options.source)
runcard = str(options.runcard)
doData = int(options.doData)
doMC = int(options.doMC)
dataset = str(options.dataset)
input_dir = []
runcardfile = ""
rootpath = "/scratch/eirikgr/openData_13TeV/"
if h_file:
        print("INFO \t Using uploaded header file")
        os.system('cp ' + h_file + ' ./MySelector.h')
if c_file:
        print("INFO \t Using uploaded source file")
        os.system('cp ' + c_file + ' ./MySelector.C')
if doData:
        print("INFO \t Will run on data")
        input_dir.append('%s/%s/Data/'%(rootpath,dataset))
if doMC:
        print("INFO \t Will run on MC")
        input_dir.append('%s/%s/MC/'%(rootpath,dataset))
if runcard:
        print("INFO \t Will use cuts specified in %s"%runcard)
        runcardfile = "runcard.txt"
        os.system('cp ' + runcard + ' ./runcard.txt')

# Check that input exists
for idir in input_dir:
        if not os.path.isdir(idir):
                raise Exception("ERROR \t Could not find any data set for %s on %s"%(dataset,"MC" if "/MC/" in idir else "Data")) 


if not os.path.exists('./Histograms'):
    os.makedirs('./Histograms')
if not os.path.exists('./Histograms/MC/'):
    os.makedirs('./Histograms/MC')
if not os.path.exists('./Histograms/Data/'):
    os.makedirs('./Histograms/Data')


parallel_exec(runJobs,input_dir)

# for idir in input_dir:
#         myChain = TChain('mini') 
#         for filename in os.listdir(idir):
#                 if not '.root' in filename: continue 
#                 print("INFO \t Adding file %s"%filename)  
#                 myChain.Add(idir+filename) 
#         arg = ""
#         if "/Data/" in idir:
#                 print("INFO \t Running on real data!")
#                 arg =  "Data %s"%runcardfile
#         else:
#                 print("INFO \t Running on Monte Carlo!")
#                 arg =  "Data %s"%runcardfile
#         p = multiprocessing.Process(target=worker, args=(myChain,arg))
#         p.start()

        # entries = myChain.GetEntries() 
        # t0 = time.time() 
        # print("-------------------------------------------")
        # print("Number of events to process: %d" %entries)
        # if "/Data/" in idir:
        #         print("INFO \t Running on real data!")
        #         myChain.Process("MySelector.C+", "Data %s"%runcardfile)
        # else: 
        #         print("INFO \t Running on Monte Carlo!") 
        #         myChain.Process("MySelector.C+", "MC %s"%runcardfile) 
        # t = int( time.time()-t0 )/60  
        # print("INFO \t Time spent: %d min" %t) 
        # print("-------------------------------------------")



