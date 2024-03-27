# VR-GUI
İstediğiniz bir şarkının, vokal kaydı ile alt yapısını ayırabilirsiniz.
  
## GUI

![GUI](https://github.com/BartuAbiHD/VR-GUI/raw/main/docs/GUI.png)
 <br><br>
  
## Windows kullanıcıları için doğrudan kurulum
## [Windows-pkg](https://github.com/BartuAbiHD/VR-GUI/releases/tag/Windows-pkg)
  
<br><br>
## Çevreyi Hazırlamak

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

Apple silikon Mac'leri düzeltme
```
pip install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu

export PYTORCH_ENABLE_MPS_FALLBACK=1
```
<br>
* Ardından VR-GUI'yi başlatmak için bu komutu kullanın:
```bash
python vrgui.py
```
Veya bu iki dosyadan birini Windows'ta çalıştırın
```
VR-GUI.bat
```
<br> 
### Sosyal Medya
* [ Trias AI](https://discord.gg/tpy6JbZhh8) Discord sunucusuna katılın.
