Follow the temporary instructions to set up Anaconda with the required packages. They will be updated soon and python3 will probably be used instead of python2.

# Setting up the environment (linux)

1. Download Anaconda from [https://repo.anaconda.com/archive/Anaconda2-2018.12-Linux-x86_64.sh](https://www.anaconda.com/download/)
2. Following the installation instructions at [http://docs.anaconda.com/anaconda/install/linux/](http://docs.anaconda.com/anaconda/install/linux/)
   - it should be done by simply doing `bash ~/Downloads/Anaconda2-2018.12-Linux-x86_64.sh` (assuming you downloaded anaconda to the Download directory of your Home folder) and follow the instructions
      - answer "YES" on the agreement
      - use the default location to install anaconda (or change the path to something else)
      - installation should then start
      - at the end you have to choose if you want the anaconda path to be put in your .bashrc file (YES: means that any new shell you open will have anaconda, NO: you will need to add the anaconda path to your PATH environment variable whenever you like to use anaconda)
3. First do some initialization of the setup
   - To use the conda binary packages from the NLeSC Anaconda Cloud repository, you need to add the appropriate NLeSC main channel: `conda config --add channels https://conda.anaconda.org/NLeSC`
4. Install ROOT (version 6, python 2) in a new envoronment (names rootenv below)
   - `conda create --name=testenv root=6 python=2`
   - `conda activate testenv`
   - ROOT is already installed in the envirinment. Try running it by doing `root -l`. If ROOT doesn't work (unlikely), install it manually by doing `conda install -c conda-forge root` 
   
6. Install root_numpy
   - `conda install -c conda-forge root_numpy`
7. Install matplotlib
   - `conda install -c conda-forge matplotlib`
8. Install scikit learn
   - `conda install -c conda-forge anaconda scikit-learn`
9. Install h5py
   - `conda install -c conda-forge anaconda h5py`
10. Getting pyROOT to work add the following to your LD_LIBRARY_PATH:
   - `export LD_LIBRARY_PATH=/opt/app-sync/matlab/bin/glnxa64/`

You should now be able to run the Logistic Regression tutorial by cloning the repository:

`git clone https://github.com/eirikgr/OsloML.git`

and then open `jupyter-notebook`session in the directory of the ipython files.

To be able to run the BDT tutorial you'd need some additional installations:

11. Install xgboost
   - `conda install -c conda-forge xgboost`
   - if it doesn't work (which is very likely), inside the environment, do `pip install xgboost==0.71`
