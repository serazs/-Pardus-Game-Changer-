import webview
import engine
import os
import sys


# =========================
# API BRIDGE
# =========================

class Api:

    # =====================
    # MAIN BOOST
    # =====================

    def pop_os_core_boost(self):

        engine.install_pop_core()

        return "Hyperion Core Boost Aktif!"


    # =====================
    # GPU
    # =====================

    def install_gpu_drivers(self):

        engine.setup_gpu()

        return "GPU ve Vulkan sürücüleri kuruldu!"


    # =====================
    # GAMING SUITE
    # =====================

    def install_gaming_suite(self):

        engine.install_gaming_suite()

        return "Gaming Suite başarıyla kuruldu!"


    # =====================
    # KERNEL
    # =====================

    def optimize_cpu_kernel(self):

        engine.optimize_cpu_kernel()

        return "XanMod Kernel aktif!"


    # =====================
    # SOCIAL
    # =====================

    def install_social_obs(self):

        engine.install_social_obs()

        return "Discord & OBS Studio kuruldu!"


    # =====================
    # AUDIO
    # =====================

    def setup_audio(self):

        engine.setup_pro_audio()

        return "PipeWire düşük gecikme modu aktif!"


    # =====================
    # TWEAKS
    # =====================

    def apply_pro_tweaks(self):

        engine.final_warrior_tweak()

        return "ZRAM ve TCP optimizasyonları aktif!"


    # =====================
    # CLEANUP
    # =====================

    def cleanup_system(self):

        engine.system_cleanup()

        return "Sistem temizliği tamamlandı!"


    # =====================
    # FAST BOOT
    # =====================

    def fast_boot(self):

        engine.fast_boot()

        return "Fast Boot tweak uygulandı!"


    # =====================
    # RAM BOOST
    # =====================

    def ram_boost(self):

        engine.ram_boost()

        return "RAM cache temizlendi!"


    # =====================
    # SYSTEM INFO
    # =====================

    def get_system_info(self):

        return engine.get_system_info()



# =========================
# START WINDOW
# =========================

if __name__ == '__main__':

    api = Api()

    window = webview.create_window(

        title='Pardus Hyperion OS',

        url='index.html',

        js_api=api,

        width=1280,

        height=820,

        min_size=(1100, 700),

        background_color='#000000',

        text_select=True
    )

    webview.start(debug=False)
