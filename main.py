import tkinter as tk
from tkinter import ttk
from engine import GameChangerEngine

class App:
    def __init__(self, root):
        self.engine = GameChangerEngine()
        self.root = root
        self.root.title("Pardus Game-Changer v1.0")
        self.root.geometry("500x400")
        
        # Tema Ayarı
        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 10), padding=10)
        
        self.create_widgets()

    def create_widgets(self):
        header = tk.Label(self.root, text="Pardus Performans Merkezi", font=("Segoe UI", 16, "bold"), pady=20)
        header.pack()

        # Butonlar
        btn_kernel = ttk.Button(self.root, text="🚀 XanMod Kernel Kur (Düşük Gecikme)", 
                                command=self.engine.install_xanmod_kernel)
        btn_kernel.pack(fill='x', padx=50, pady=5)

        btn_nvidia = ttk.Button(self.root, text="🎮 NVIDIA Sürücülerini & Panelini Kur", 
                                command=self.engine.install_nvidia)
        btn_nvidia.pack(fill='x', padx=50, pady=5)

        btn_game = ttk.Button(self.root, text="📦 Oyun Araçlarını Yükle (Steam/Lutris)", 
                               command=self.engine.optimize_gaming)
        btn_game.pack(fill='x', padx=50, pady=5)

        footer = tk.Label(self.root, text="Sercan Edition - GitHub: @sercan", fg="gray")
        footer.pack(side="bottom", pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()