# OsloML

Machine learning tools to be used for educational purposes

The *ReadRootFiles* read the openData ntuples from file and produce h5 files. These files can be read later in *MakeTrainingAndTestingSamples* to create training and testing samples. The *OpenDataPandaFramework* containes the method for doing the root -> panda -> h5 files. Doing skimming, slimming and augmentation before preparing a flat panda data frame to be used in ML. 

# Installation
One additional packages (assuming you have followed instructions https://github.com/eirikgr/FYS5555/tree/master/Anaconda_setup) are needed:
(NOTE: Always work in the conda environment!)

```
pip install import-ipynb
```


Note that there is no need for ROOT!

# User Input

For basic use all what should be changed by the user is contained in the second block of *ReadRootFiles*. Here one specifies the input directory of the openData root files. The luminosity (which for the 13TeV openData release is *10.6* ifb). The program assumes a certain directory structure with 

- **SM backgrounds** in folder named **SM_Backgrounds**
- **Signals** in folder named **BSM_Signal_Samples**
- **Data** in folder named **Data**

Further one can specify the number of leptons (*nlep*) and the pt of the leptons (*lep_ptcut*) used to skim the samples. More advanced skimming can be applied, but then one would need to change the functions in *OpenDataPandaFramework* (see below). A tag to the file name should also be specified (in *skimtag*) indicating the applied skimming requirements. Note that the default skimming is currently

- Exactly nlep number of leptons with pt > lep_ptcut[i]
- MET > 50 GeV

# Skimming

Skimming remove events which do not pass certain requirements. These are implemented in the *skimming* function of *OpenDataPandaFramework*. One can easilly add additional constraints depending on the physics process one is interested in. The important is to append the output (in terms of 0 (false) and 1 (true) for each event) of the skimming to the *skim* vector.

# Augmentation

Augmentation adds new variables to the panda data frame (e.g. *mll*). There is one augmentation function implemented for each of the objects leptons and jets. Follow the same procedure to add more variables if needed. Code which makes variables like lept1_xx, lept2_xx, lept3_xx etc. (depending on the value of *nlep* is already included). 

# Slimming 

Slimming removes branches. One need to make sure that all non-flat variables are removed (because these can not be read in ScikitLearn). The branches to remove are specified in the *remove_branches* vector.
