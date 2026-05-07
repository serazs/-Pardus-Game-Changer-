import subprocess

def run(command):
    try:
        print(f"[EXECUTING] {command}")
        subprocess.run(command, shell=True, check=True)
    except Exception as e:
        print(f"[ERROR] Hata oluştu: {e}")

def install_pop_core():
    # 32-bit desteği ve GameMode kurulumu
    run("sudo dpkg --add-architecture i386")
    run("sudo apt update")
    run("sudo apt install -y gamemode libgamemode0:i386 libgamemodeauto0 mesa-utils vulkan-tools")

def setup_gpu():
    # NVIDIA ve Vulkan Katmanı
    run("sudo apt install -y nvidia-driver nvidia-settings nvidia-vulkan-icd libgl1-mesa-glx:i386 libgl1-mesa-dri:i386 mesa-vulkan-drivers mesa-vulkan-drivers:i386")

def install_gaming_suite():
    # Oyun kütüphanesi ve FPS göstergesi
    run("sudo apt install -y steam-installer steam-devices lutris wine wine32 wine64 winetricks mangohud")

def optimize_cpu_kernel():
    # XanMod Kernel ve CPU Performans ayarı
    run("sudo apt install -y cpufrequtils")
    run("sudo cpufreq-set -r -g performance")
    run("wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/xanmod-archive-keyring.gpg")
    run('echo "deb [signed-by=/usr/share/keyrings/xanmod-archive-keyring.gpg] http://deb.xanmod.org releases main" | sudo tee /etc/apt/sources.list.d/xanmod-release.list')
    run("sudo apt update && sudo apt install -y linux-xanmod-x64v3")

def setup_pro_audio():
    # Pop!_OS'un kullandığı modern Pipewire ses motoru (Gecikmesiz ses)
    run("sudo apt install -y pipewire pipewire-audio-client-libraries pipewire-pulse wireplumber")
    run("systemctl --user enable --now pipewire-pulse")

def final_warrior_tweak():
    # Pop!_OS'un en büyük sırrı: ZRAM ve Network optimizasyonu
    run("sudo apt install -y zram-tools")
    # ZRAM yapılandırması
    run("echo 'ALGO=zstd' | sudo tee -a /etc/default/zramswap")
    run("sudo service zramswap restart")
    # TCP Gecikme Ayarı
    run("echo 'net.ipv4.tcp_fastopen = 3' | sudo tee -a /etc/sysctl.conf")
    run("sudo sysctl -p")

def install_social_obs():
    # Discord ve OBS Studio
    run("sudo apt install -y discord obs-studio")

def system_cleanup():
    # Kalıntıları temizle
    run("sudo apt autoremove --purge -y && sudo apt clean -y")
    run("sudo journalctl --vacuum-time=1d")