import os

class GameChangerEngine:
    @staticmethod
    def run_in_terminal(command):
        # Pardus'ta terminal açıp komutu çalıştırır
        os.system(f"gnome-terminal -- bash -c '{command}; echo İŞLEM TAMAMLANDI; exec bash'")

    def install_nvidia(self):
        cmd = "sudo apt update && sudo apt install -y nvidia-driver firmware-misc-nonfree nvidia-settings"
        self.run_in_terminal(cmd)

    def install_xanmod_kernel(self):
        # Oyun performansı için en iyi kernel
        cmd = ("wget -qO - https://dl.xanmod.org/archive.key | sudo gpg --dearmor -o /usr/share/keyrings/xanmod-archive-keyring.gpg && "
               "echo 'deb [signed-by=/usr/share/keyrings/xanmod-archive-keyring.gpg] http://deb.xanmod.org nettle main' | sudo tee /etc/apt/sources.list.d/xanmod-kernel.list && "
               "sudo apt update && sudo apt install -y linux-xanmod-x64v3")
        self.run_in_terminal(cmd)

    def optimize_gaming(self):
        # Gamemode, Wine ve FPS göstergesi (MangoHud)
        cmd = "sudo apt install -y gamemode mangohud wine64-tools winetricks lutris steam"
        self.run_in_terminal(cmd)