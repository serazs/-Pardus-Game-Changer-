import webview
import engine
import os
import sys

class Api:
    # 1. Pop!_OS Çekirdek ve Oyun Modu (GameMode + i386)
    def pop_os_core_boost(self):
        engine.install_pop_core()
        return "Pop!_OS Core Boost Aktif!"

    # 2. Grafik Kartı ve Vulkan (NVIDIA/AMD)
    def install_gpu_drivers(self):
        engine.setup_gpu()
        return "GPU ve Vulkan Sürücüleri Kuruldu!"

    # 3. Oyun Platformları (Steam, Lutris, Wine)
    def install_gaming_suite(self):
        engine.install_gaming_suite()
        return "Gaming Suite Hazır!"

    # 4. Performans Kerneli (XanMod)
    def optimize_cpu_kernel(self):
        engine.optimize_cpu_kernel()
        return "XanMod Kernel ve CPU Performans Modu Aktif!"

    # 5. Sosyal ve Yayıncı Araçları (Discord, OBS)
    def install_social_obs(self):
        engine.install_social_obs()
        return "Sosyal Araçlar Kuruldu!"

    # 6. Pop!_OS Özel: Ses Gecikmesi Sıfırlama (Pipewire)
    def setup_audio(self):
        engine.setup_pro_audio()
        return "Pipewire Ses Motoru Aktif!"

    # 7. Pop!_OS Özel: ZRAM ve Disk Optimizasyonu (Tweaks)
    def apply_pro_tweaks(self):
        engine.final_warrior_tweak()
        return "ZRAM ve Disk Zamanlayıcıları Optimize Edildi!"

    # 8. Sistem Temizliği
    def cleanup_system(self):
        engine.system_cleanup()
        return "Sistem Gereksiz Dosyalardan Arındırıldı!"

if __name__ == '__main__':
    api = Api()
    window = webview.create_window(
        title='Pardus Hyperion OS - Ultimate Gaming Edition', 
        url='index.html', 
        js_api=api, 
        width=1150,
        height=750,
        background_color='#000000'
    )
    webview.start()