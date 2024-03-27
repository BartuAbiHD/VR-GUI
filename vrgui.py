import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog, messagebox, StringVar
import os
import subprocess

class App:
    def __init__(self, root):
        self.root = root
        self.input_file = ""
        self.output_dir = ""
        self.device = tk.StringVar(value="GPU")

        self.input_label = ctk.CTkLabel(root, text="Giriş Dosyası: ")
        self.input_label.pack(pady=10)

        self.input_button = ctk.CTkButton(root, text="Dosya Seç", command=self.select_input)
        self.input_button.pack(pady=5)

        self.output_label = ctk.CTkLabel(root, text="Çıkış Dizini: ")
        self.output_label.pack(pady=5)

        self.output_button = ctk.CTkButton(root, text="Dizin Seç", command=self.select_output)
        self.output_button.pack(pady=5)

        self.device_radio1 = ctk.CTkRadioButton(root, text="GPU", variable=self.device, value="GPU")
        self.device_radio1.pack(pady=5)

        self.device_radio2 = ctk.CTkRadioButton(root, text="CPU", variable=self.device, value="CPU")
        self.device_radio2.pack(pady=5)

        self.convert_button = ctk.CTkButton(root, fg_color="green", hover_color="darkgreen", text="Dönüştür", command=self.convert)
        self.convert_button.pack(pady=5)

        version_label = ctk.CTkLabel(root, text="v1.1  ", text_color="#FFB0B0")
        version_label.pack(side="bottom", anchor="se")

    def select_input(self):
        self.input_file = filedialog.askopenfilename(filetypes=(("wav files", "*.wav"), ("mp3 files", "*.mp3")))
        self.input_label['text'] = "Giriş Dosyası: " + self.input_file
        self.input_button['text'] = "Dosya Seçildi"  # Buton metnini değiştir

    def select_output(self):
        self.output_dir = filedialog.askdirectory()
        self.output_label['text'] = "Çıkış Dizini: " + self.output_dir
        self.output_button['text'] = "Dizin Seçildi"  # Buton metnini değiştir

    def convert(self):
        if not self.input_file:
            messagebox.showwarning("Uyarı", "Lütfen giriş kısmından dosya seçiniz.")
        elif not self.output_dir:
            messagebox.showwarning("Uyarı", "Lütfen çıkış kısmından bir dizin belirtiniz.")
        else:
            command = f"python inference.py --input \"{self.input_file}\" --output_dir \"{self.output_dir}\""
            if self.device.get() == "GPU":
                command += " --gpu 0"
            subprocess.run(command, shell=True)

root = ctk.CTk()
root.iconbitmap("icon.ico")
ctk.set_appearance_mode("dark")
root.title("Vocal Remover GUI [Trias AI] - [bartucivas.com.tr]")
root.geometry("502x285")  # Çözünürlüğü 502x285 olarak ayarla
root.resizable(0, 0)  # Pencerenin boyutunu değiştirmeyi devre dışı bırak

# Pencereyi ekranın ortasına yerleştir
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth()/2 - window_width/2)
position_down = int(root.winfo_screenheight()/2 - window_height/2)
root.geometry("+{}+{}".format(position_right, position_down))

app = App(root)
root.mainloop()