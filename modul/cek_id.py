import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

def cek_id(self):
        id_input = self.entry_id_input.get()
        if not id_input:
            messagebox.showerror("Error", "ID tidak boleh kosong.")
            return

        try:
            id_input = int(id_input)
        except ValueError:
            messagebox.showerror("Error", "ID harus berupa angka.")
            return

        data_siswa = baca_data_siswa()
        if id_input in data_siswa["ID"].values:
            messagebox.showinfo("Info", f"ID {id_input} sudah ada. Menampilkan data siswa.")
            self.tampilkan_data_siswa(data_siswa)
        else:
            messagebox.showinfo("Info", f"ID {id_input} belum ada. Masukkan data baru.")
            self.frame_input_id.pack_forget()
            self.frame_input_data.pack(fill="both", expand=True)

def baca_data(file_path, columns):
    if os.path.exists(file_path):
        data = pd.read_excel(file_path, engine='openpyxl')
        if set(columns).issubset(data.columns):
            return data
        else:
            return pd.DataFrame(columns=columns)
    else:
        return pd.DataFrame(columns=columns)

def kembali_ke_login(self):
        self.frame_input_id.pack_forget()
        self.frame_login.pack(fill="both", expand=True)

def baca_data_siswa():
    data = baca_data( ['ID', 'Nama', 'Kelas', 'Tanggal Lahir', 'Alamat'])
    
    # Pastikan kolom 'Tanggal Lahir' hanya menyimpan tanggal
    if not data.empty and 'Tanggal Lahir' in data.columns:
        data['Tanggal Lahir'] = pd.to_datetime(data['Tanggal Lahir'], errors='coerce').dt.date
    
    return data