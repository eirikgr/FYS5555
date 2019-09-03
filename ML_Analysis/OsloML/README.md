# OsloML

Machine learning tools to be used for educational purposes

The *ReadRootFiles* read the openData ntuples from file and produce h5 files. These files can be read later in *MakeTrainingAndTestingSamples* to create training and testing samples. The *OpenDataPandaFramework* containes the method for doing the root -> panda -> h5 files. Doing skimming, slimming and augmentation before preparing a flat panda data frame to be used in ML. Two additional packages are needed for this to work:

```
pip install
```

and 

```
conda config --add channels conda-forge # if you haven't added conda-forge already
conda install awkward
conda install awkward-numba # optional: integration with and optimization by Numba
```

There is no need for ROOT!
