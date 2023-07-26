# 工具名
论文名XXXX
## Abstract
摘要
## Running environment
工具名 is an open-source Python-based toolkit, which operates in the Python environment (Python version 3.6 or above) and can run on multiple operating systems (such as Windows, Mac and Linux). Prior to installing and running 工具名, all the dependencies should be installed in the Python environment, including sys, os, re, PyQt5, qdarkstyle, numpy (1.24.3), pandas (1.5.3), threading, sip, scipy (1.9.3), Bio(1.5.9), tensorflow (2.10.0), random, multiprocessing and time. For convenience, we strongly recommended users to install the Anaconda Python environment in your local computer. The software can be freely downloaded from https://www.anaconda.com/.
## Installation
### Method 2
  - Download *工具名* by 
  ```sh
  git clone https://github.com/ChangXulinmessi/gongjum
  ```


  - Step 1. Download and install the anaconda platform.
  ```sh  
  Download from: https://www.anaconda.com/products/individual
  ```
  
  - Step 2. Install tensorflow:
  ```sh  
  Please refer to https://pytorch.org/get-started/locally/ for PyTorch installation.
  ```
  
  - Step 3. Install lightgbm, xgboost and qdarkstyle:
  ```sh
  pip3 install lightgbm
  pip3 install xgboost
  pip3 install qdarkstyle  
  ```
  
  - Step 4. run iLearnPlus:
  cd to the *iLearnPlus* folder which contains iLearnPlus.py and run the ‘iLearnPlus.py’ script as follows:
  ```sh
  python iLearnPlus.py
  ```
