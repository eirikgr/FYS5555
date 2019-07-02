from infofile import infos
from tabulate import tabulate
import re

backgrounds = []
sample_name = []
infile = open('Background_samples.txt')
for line in infile: 
    sample_name.append(line.split()[0])
    name = line.split('.')[1]
    backgrounds.append(name)
    #print word
infile.close()   

Diboson = [105985, 105986, 105987];
Zjets = [147770, 147771, 147772];
ttbar = [117049, 117050];
singleTop =  [110090, 110091, 110119, 110140];
Wjets = [167740, 167741, 167742, 167743, 167744, 167745, 167746, 167747, 167748];
DY = [173041, 173042, 173043, 173044, 173045, 173046];
Higgs = [160155, 160205, 161005, 161055]; 


all_info = []
for name in backgrounds:
    sample_info = []
    info = infos[name]
    keys = ['DSID', 'events', 'red_eff', 'sumw', 'xsec']
    sample_info.append(name)
    if info['DSID'] in Diboson: 
        sample_info.append("Diboson")
    if info['DSID'] in Zjets: 
        sample_info.append("Zjets")
    if info['DSID'] in ttbar: 
        sample_info.append("ttbar")
    if info['DSID'] in singleTop: 
        sample_info.append("singleTop")
    if info['DSID'] in Wjets: 
        sample_info.append("Wjets")
    if info['DSID'] in DY: 
        sample_info.append("DY")
    if info['DSID'] in Higgs: 
        sample_info.append("Higgs")
    for key in keys: 
        sample_info.append(info[key])
    all_info.append(sample_info)   


headers = ['Process', 'Class', 'Dataset ID', 'Events', 'Red eff', 'Sum of weights', 'Cross section']
outfile = open("Infofile.txt", "w")
outfile.write(tabulate(all_info, tablefmt = "plain", numalign="left"))
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
