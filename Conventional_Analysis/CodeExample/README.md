# FYS5555 Code Example for 13 TeV ATLAS Open Data

Prepared by Even Håland

This is a complete code example for use with the ATLAS 13 TeV Open Data. Use it to
get started quickly with your analysis. Try first to run the code as it is and check
that everything works, then you can move on to edit the relevant code files to
perform your analysis of interest.

## Running the code

Get hold of the 2-lepton skim of ATLAS Open Data from here: http://opendata.cern.ch/record/15003
(download the .zip file and extract it in your working directory). Your working directory should now look
like this:
```
$ ls
2lep  Histograms  infofile.py  MakePlots.py  MySelector.C  MySelector.h  Plots  README  README.md  runSelector.py
```
Run the code on data (note that the code is not compatible with python version 3, depending on what you have installed, you may need to explicitly specify "python2" in the command):
- `python runSelector.py Data`

Run the code on MC (there are many MC datasets, so this may take a bit longer):
- `python runSelector.py MC`

Run the plotting for the electron channel:
- `python MakePlots.py ee`

Run the plotting for the muon channel:
- `python MakePlots.py uu`

If all commands ran without errors and you have some nice-looking plots in the Plots/ directory, you are
ready to move on to modify the analysis according to your needs.
