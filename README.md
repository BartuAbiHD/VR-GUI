# VR-GUI
You can separate the vocal recording from the background of a song you want.
## GUI
![GUI](https://github.com/BartuAbiHD/VR-GUI/raw/main/docs/GUI.png)
<br><br>
## Direct installation for Windows users
## [Windows-pkg](https://github.com/BartuAbiHD/VR-GUI/releases/tag/v1.2)
  
<br><br>
## Preparing the Environment
* Only those who download the source code should do these steps. Those who download the setup and install the program do not need to do it.

* Install Python version +3.9 if you have not:

* Execute these commands

Windows with Nvidia cards
```bash
python -m pip install -U pip setuptools wheel
pip install -U torch torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```
Other
```
python -m pip install -U pip setuptools wheel
pip install -U torch torchaudio 
pip install -r requirements.txt
```

Go to [baseline.pth](https://huggingface.co/datasets/TriasAI/VR-GUI/resolve/main/models/baseline.pth?download=true) and put the downloaded file into the "models" folder in the directory.

Apple silicon Macs fix
```
pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu

export PYTORCH_ENABLE_MPS_FALLBACK=1
```
### Social Media
* Join the [ Trias AI](https://discord.gg/tpy6JbZhh8) Discord.
