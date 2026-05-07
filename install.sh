#!/bin/bash

echo "Pardus Hyperion Kurulumu Başlıyor..."

# 1. Sistem Bağımlılıklarını Kur
sudo apt update
sudo apt install -y python3-pip libwebkit2gtk-4.0-dev python3-gi python3-gi-cairo gir1.2-gtk-3.0 git

# 2. Python Kütüphanelerini Kur
pip3 install pywebview[gtk] setuptools pycairo PyGObject --break-system-packages || pip3 install pywebview[gtk] setuptools pycairo PyGObject

# 3. Uygulamayı Başlatılabilir Yap
chmod +x main.py

echo "✅ Kurulum Tamamlandı! Uygulama Başlatılıyor..."
sudo python3 main.py