#from infofile import infos
#from tabulate import tabulate
import re

backgrounds = []
sample_name = []
infile = open('Background_samples.txt')
for line in infile: 
    sample_name = line.split()[0]
    #name = line.split('.')[1]
    backgrounds.append(sample_name)
    #print word
infile.close()


Higgs = [341122,
         341155,
         341947,
         341964,
         344235,
         345060,
         345323,
         345324,
         345325,
         345327,
         345336,
         345337,
         345445]

Wjets = [364156,
         364157,
         364158,
         364159,
         364160,
         364161,
         364162,
         364163,
         364164,
         364165,
         364166,
         364167,
         364168,
         364169,
         364170,
         364171,
         364172,
         364173,
         364174,
         364175,
         364176,
         364177,
         364178,
         364179,
         364180,
         364181,
         364182,
         364183,
         364184,
         364185,
         364186,
         364187,
         364188,
         364189,
         364190,
         364191,
         364192,
         364193,
         364194,
         364195,
         364196,
         364197]

Zjets = [364100,
         364101,
         364102,
         364103,
         364104,
         364105,
         364106,
         364107,
         364108,
         364109,
         364110,
         364111,
         364112,
         364113,
         364114,
         364115,
         364116,
         364117,
         364118,
         364119,
         364120,
         364121,
         364122,
         364123,
         364124,
         364125,
         364126,
         364127,
         364128,
         364129,
         364130,
         364131,
         364132,
         364133,
         364134,
         364135,
         364136,
         364137,
         364138,
         364139,
         364140,
         364141]


Diboson = [363356,
           363358,
           363359,
           363360,
           363489,
           363490,
           363491,
           363492,
           363493]

ttbar = [410000]

singleTop = [410011,
             410012,
             410013,
             410014,
             410025,
             410026]


topX = [410155,
        410218,
        410219]

mc_categories = {"Diboson":Diboson,"Zjets":Zjets,"Wjets":Wjets,"singleTop":singleTop,"topX":topX,"Higgs":Higgs}
outfile = open("Infofile.txt", "w")
sample_info = {}
outfile.write("### %s|%s|%s\n"%("NAME","CATEGORY","DSID"))
for sample_name in backgrounds:
    dsid = int(sample_name.split(".")[0].split("_")[-1])
    name = sample_name.split('.')[1]
    for mc in mc_categories.keys():
        if dsid in mc_categories[mc]:
            outfile.write("%s|%s|%i\n"%(name,mc,dsid))
            break
                          
outfile.close()

"""
a = "mc_id.process"
b = re.split(';|\.|\_', a)
print b

name_and_id = []
for name in sample_name: 
    l = []
    l.append(name) 
    l.append(re.split(';|\.|\_',name)[1])
    name_and_id.append(l)


outfile1 = open("Name_and_ID.txt","w")
outfile1.write(tabulate(name_and_id, tablefmt="plain", numalign="left"))
outfile1.close()
"""
