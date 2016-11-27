# classifier
Basic generic text classifier using linear support vector machine (SVM) model.

Dependencies:
------------

- Ubuntu Server 16
- Miniconda (python)
- sklearn


Install:
------------

Get installer script:
`$ wget https://raw.githubusercontent.com/jmmnn/classifier/master/server_installer.py`  

Run installer script, say yes when necessary:  
`$ python3 server_installer.py`  

Set path for miniconda python  
`$ export PATH="$HOME/miniconda/bin:$PATH"`  

Crete new environment  
`$ conda create --name classifier scikit-learn`

Activate the environemnt  
`source activate classifier`

