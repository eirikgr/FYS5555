Follow the instructions to set up Anaconda2 with the required packages. The default python version is 2.7 but when the packages are installed, it will automatically be updated to 3.7.

# Setting up the environment (linux)

1. Download Anaconda for linux from [https://repo.anaconda.com/archive/Anaconda2-2018.12-Linux-x86_64.sh](https://www.anaconda.com/download/)
2. Following the installation instructions at [http://docs.anaconda.com/anaconda/install/linux/](http://docs.anaconda.com/anaconda/install/linux/)
   - it should be done by simply doing `bash ~/Downloads/Anaconda2-2018.12-Linux-x86_64.sh` (assuming you downloaded anaconda to the Download directory of your Home folder) and follow the instructions
      - answer "YES" on the agreement
      - use the default location to install anaconda (or change the path to something else)
      - installation should then start
      - at the end you have to choose if you want the anaconda path to be put in your .bashrc file (YES: means that any new shell you open will have anaconda, NO: you will need to add the anaconda path to your PATH environment variable whenever you like to use anaconda)
3. First do some initialization of the setup
   - To use the conda binary packages from the NLeSC Anaconda Cloud repository, you need to add the appropriate NLeSC main channel: `conda config --add channels https://conda.anaconda.org/NLeSC`
4. Create an environment as follows: 
   - `conda create -n name_of_environment`
5. Activate the environment: `conda activate name_of_environment`
6. Install the following packages in your working environment:
   - `conda install -c conda-forge uproot`
   - `conda install -c conda-forge jupyterlab`
   - `conda install -c anaconda pandas`
   - `conda install -c anaconda h5py`
   - `conda install -c conda-forge matplotlib`
   - `conda install -c conda-forge anaconda scikit-learn`
7. OPTIONAL: if you want ROOT in your environment, install it (latest version 6.18) by doing
   - `conda install -c conda-forge root`
   - `conda install -c conda-forge/label/gcc7 root`
   NOTE: We have tried our best to remove all ROOT dependencies for the machine learning analysis and see how far we can get.
8. For the BDT algorithm, you will need the xgboost package:
   - `conda install -c conda-forge xgboost`

