
## Installation (Windows host)

### step 0 ) Python 3.12
setup python installer (not embed!)
- from [python/download](https://www.python.org/downloads/) 
- customize installation path, ex : `$ /C/Tools/Python312/`

### step 1) Python winenv

```bash
# cd pyBird
/C/Tools/Python312/python.exe --version
Python 3.12.2
/C/Tools/Python312/python.exe -m venv ./winvenv
source ./winvenv/Scripts/activate
# verify version
python --version
## expect 3.12.2
python -m pip install --upgrade pip
```

### Step 2) Project dependencies
````bash
pip install -r ./requirements.txt
````
