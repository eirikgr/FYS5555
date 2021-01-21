# FYS5555

This git page has been created to gather all the "hands-on" material of the course Research-based particle physics (FYS5555). Se more details below.

To copy all the material on your PC, in the terminal do `git clone https://github.com/eirikgr/FYS5555.git`

## Installation instructions (FOR ALL EXCEPT SUSYPHENO - see [below](#installation-instructions-for-susypheno) for how to setup SUSYPheno software)

To get all the software needed to run the programs the easiest is to install anaconda as described below. 

### First time setup (LINUX)

For other OSs see: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation

The following only needs to be done once:

```
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh
```

Follow the instructions on the screen. 

**Recomandation**: When the installer asks `Do you wish the installer to initialize Anaconda3` answer `no` to avoid the conda environment to be enabled by default whenever you start a new shell. 

More details on installation can be found here:

**Linux**: https://docs.anaconda.com/anaconda/install/linux/

Activate anaconda in your terminal

`source <path-to-where-anaconda-is-installed>/etc/profile.d/conda.sh`

Build the environment (using the python3 yml file in the github repo) - this may take some time

`conda env create -f environment_fys5555_py3.yml`

Then load the environement, and your good to go!

`conda activate fys5555_py3`

### Whenever you start a new session

If you have installed conda as described above, when you start a new shell, all you have to do is 

```
source <path-to-where-anaconda-is-installed>/etc/profile.d/conda.sh
conda activate fys5555_py3
``` 

## Installation instructions (for SUSYPHENO)

The SUSYPheno package uses python2 and thus a slightly different setup is needed. It follows similar steps as above.

```
wget https://repo.anaconda.com/archive/Anaconda2-2018.12-Linux-x86_64.sh
bash Anaconda2-2018.12-Linux-x86_64.sh
```

Follow the instructions on the screen. 

**Recomandation**: When the installer asks `Do you wish the installer to initialize Anaconda2` answer `no` to avoid the conda environment to be enabled by default whenever you start a new shell. 

More details on installation can be found here:

**Linux**: https://docs.anaconda.com/anaconda/install/linux/

Build the environment (using the python2 yml file in the githug repo) 

`conda env create -f environment_fys5555_py2.yml`

Then load the environement, and your good to go!

`conda activate fys5555_py2`

### Whenever you start a new session

If you have installed conda as described above, when you start a new shell, all you have to do is 

```
source <path-to-where-anaconda-is-installed>/etc/profile.d/conda.sh
conda activate fys5555_py2
```

## More Information on the content of FYS5555

This git page has been created to gather all the "hands-on" material of the course Research-based particle physics (FYS5555).

To copy all the material on your PC, in the terminal do `git clone https://github.com/Etienne357/FYS5555.git`

- CompHEP is a software package and event generator used to compute cross-sections. Follow the instructions on the following readme file for its installation: https://github.com/Etienne357/FYS5555/blob/master/CompHEP/README.md.
- You will need ROOT to do any analysis so it's better to install it once and for all. The best and tested way to install ROOT (which works with C++ and Python3) is via Anaconda which also contains all the machine learning packages; forget about other complicated ways to install ROOT. Follow the instructions given here: https://github.com/Etienne357/FYS5555/blob/master/Anaconda_setup/README.md
- An example dilepton (cut-and-count) analysis on the open data has been provided in the folder "Conventional_Analysis". This can be used as a skeleton to plot histograms and for further analyses. Instructions are found in https://github.com/Etienne357/FYS5555/blob/master/Conventional_Analysis/README.md
- The statistical analysis on cross-section limits can be found in the "Statistics" folder. Instructions are found in https://github.com/Etienne357/FYS5555/blob/master/Statistics/README.md.
- The SUSYPheno folder contains all the materials for the Supersymmetry part of the course. The instructions can be found in https://github.com/Etienne357/FYS5555/blob/master/SUSYPheno/README.md. 
- The machine learning analysis is found in the folder "ML_analysis". This section is still work in progress and will be finalized soon.
