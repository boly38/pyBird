
## Installation (Windows host)

### step 0 ) Python 3.11
# "pybioclip" requires Python compatible with PyTorch ==>  Python 3.8-3.11
setup python installer (not embed!)
- from [python/download](https://www.python.org/downloads/) 
- customize installation path, ex : `/C/Tools/Python3117/`

### step 1) Python winenv

```bash
# cd pyBird
/C/Tools/Python3117/python.exe --version
Python 3.11.7
/C/Tools/Python3117/python.exe -m venv ./venv
source ./venv/Scripts/activate
# verify version
python --version
## expect 3.11.7
python -m pip install --upgrade pip
```

### Step 2) Project dependencies
````bash
pip install -r ./requirements.txt
pip install git+https://github.com/Imageomics/pybioclip
````
