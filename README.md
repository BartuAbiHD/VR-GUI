# VR-GUI
İstediğiniz bir şarkının, vokal kaydı ile alt yapısını ayırabilirsiniz.
## GUI
![GUI](https://github.com/BartuAbiHD/VR-GUI/raw/main/docs/GUI.png)
<br><br>
## Windows kullanıcıları için doğrudan kurulum
## [Windows-pkg](https://github.com/BartuAbiHD/VR-GUI/releases/tag/v1.2)
  
<br><br>
## Çevreyi Hazırlamak
* Bu adımları yalnızca kaynak kodları indirenler yapsın. Setup indirip programı kuranların yapmasına gerek yok.

* Yapmadıysanız Python 3.9 (Tercih edilen: 3.12) veya üstü bir sürümünü yükleyin:

* Bu komutları yürütün

Nvidia kartlı Windows'lar
```bash
python -m pip install -U pip setuptools wheel
pip install -U torch torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
```
Diğer
```
python -m pip install -U pip setuptools wheel
pip install -U torch torchaudio 
pip install -r requirements.txt
```

https://huggingface.co/datasets/TriasAI/VR-GUI/resolve/main/models/baseline.pth?download=true bu adrese gir ve inen dosyayı dizindeki models klasörünün içerisine at.

Apple silikon Mac'leri düzeltme
```
pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu

export PYTORCH_ENABLE_MPS_FALLBACK=1
```
### Sosyal Medya
* [ Trias AI](https://discord.gg/tpy6JbZhh8) Discord sunucusuna katılın.
