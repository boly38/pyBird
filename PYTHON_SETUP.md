
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

Note: around 2GB disk will be used

````bash
pip install -r ./requirements.txt
pip install git+https://github.com/Imageomics/pybioclip
````


### Tips to uninstall

````bash
df -kh

# docker : clean unused resources
docker image prune
docker volume prune

# pip : uninstall deps
pip info
du -khs ~/.cache/pip

pip uninstall -r requirements.txt -y
pip cache purge
pip info

# remove HF cache - https://huggingface.co/docs/huggingface_hub/guides/manage-cache#clean-cache-from-the-terminal
du -khs ~/.cache/huggingface
# rm ? :)

du -kh
````