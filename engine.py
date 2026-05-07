import subprocess
import os
import time

# =========================
# CORE EXECUTION ENGINE
# =========================

def run(command):
    try:
        print(f"\n[EXECUTING] {command}\n")

        subprocess.run(
            command,
            shell=True,
            check=True
        )

        print("[SUCCESS]\n")

    except subprocess.CalledProcessError as e:
        print(f"[ERROR] {e}")

    except Exception as e:
        print(f"[CRITICAL ERROR] {e}")


# =========================
# CORE GAMING BOOST
# =========================

def install_pop_core():

    run("sudo dpkg --add-architecture i386")

    run("sudo apt update")

    run(
        "sudo apt install -y "
        "gamemode "
        "libgamemode0:i386 "
        "libgamemodeauto0 "
        "mesa-utils "
        "vulkan-tools "
        "mangohud "
        "vkbasalt"
    )

    run("gamemoded -t")


# =========================
# GPU + VULKAN
# =========================

def setup_gpu():

    run(
        "sudo apt install -y "
        "nvidia-driver "
        "nvidia-settings "
        "nvidia-vulkan-icd "
        "mesa-vulkan-drivers "
        "mesa-vulkan-drivers:i386 "
        "libgl1-mesa-dri:i386 "
        "libgl1-mesa-glx:i386 "
        "vulkan-tools"
    )


# =========================
# GAMING SUITE
# =========================

def install_gaming_suite():

    run(
        "sudo apt install -y "
        "steam-installer "
        "steam-devices "
        "lutris "
        "wine "
        "wine32 "
        "wine64 "
        "winetricks "
        "mangohud "
        "goverlay "
        "gamemode"
    )


# =========================
# XANMOD KERNEL
# =========================

def optimize_cpu_kernel():

    run("sudo apt install -y curl wget gnupg")

    run("sudo apt install -y cpufrequtils")

    run("sudo cpufreq-set -r -g performance")

    run(
        "wget -qO - https://dl.xanmod.org/archive.key "
        "| sudo gpg --dearmor "
        "-o /usr/share/keyrings/xanmod-archive-keyring.gpg"
    )

    run(
        'echo "deb [signed-by=/usr/share/keyrings/xanmod-archive-keyring.gpg] '
        'http://deb.xanmod.org releases main" '
        '| sudo tee /etc/apt/sources.list.d/xanmod-release.list'
    )

    run("sudo apt update")

    run("sudo apt install -y linux-xanmod-x64v3")


# =========================
# AUDIO ENGINE
# =========================

def setup_pro_audio():

    run(
        "sudo apt install -y "
        "pipewire "
        "pipewire-pulse "
        "wireplumber "
        "pavucontrol"
    )

    run("systemctl --user enable --now pipewire")

    run("systemctl --user enable --now pipewire-pulse")

    run("systemctl --user restart pipewire")


# =========================
# PRO SYSTEM TWEAKS
# =========================

def final_warrior_tweak():

    run("sudo apt install -y zram-tools preload")

    run(
        "echo 'ALGO=zstd' "
        "| sudo tee /etc/default/zramswap"
    )

    run("sudo service zramswap restart")

    run(
        "echo 'net.ipv4.tcp_fastopen = 3' "
        "| sudo tee -a /etc/sysctl.conf"
    )

    run(
        "echo 'vm.swappiness=10' "
        "| sudo tee -a /etc/sysctl.conf"
    )

    run("sudo sysctl -p")


# =========================
# SOCIAL + STREAM
# =========================

def install_social_obs():

    run(
        "sudo apt install -y "
        "discord "
        "obs-studio"
    )


# =========================
# SYSTEM CLEANUP
# =========================

def system_cleanup():

    run("sudo apt autoremove --purge -y")

    run("sudo apt clean -y")

    run("sudo journalctl --vacuum-time=1d")


# =========================
# FAST BOOT TWEAK
# =========================

def fast_boot():

    run("sudo systemctl disable NetworkManager-wait-online.service")


# =========================
# RAM BOOST
# =========================

def ram_boost():

    run("sync")

    run("echo 3 | sudo tee /proc/sys/vm/drop_caches")


# =========================
# SYSTEM INFO
# =========================

def get_system_info():

    try:

        cpu = subprocess.check_output(
            "grep 'model name' /proc/cpuinfo | head -1",
            shell=True
        ).decode()

        return cpu.strip()

    except:
        return "Unknown CPU"
