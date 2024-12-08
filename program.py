import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk  # Library untuk menangani gambar

# Nama file default
file_siswa = "D:\projectc\data_siswa.xlsx"

# Data login admin
admin_username = "admin"
admin_password = "1"

# Fungsi untuk membaca file Excel
def baca_data(file_path, columns):
    if os.path.exists(file_path):
        data = pd.read_excel(file_path, engine='openpyxl')
        if set(columns).issubset(data.columns):
            return data
        else:
            return pd.DataFrame(columns=columns)
    else:
        return pd.DataFrame(columns=columns)

# Fungsi untuk menyimpan data ke Excel
def simpan_data(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
        data.to_excel(writer, index=False)

# Membaca data siswa
def baca_data_siswa():
    data = baca_data(file_siswa, ['ID', 'Nama', 'Kelas', 'Tanggal Lahir', 'Alamat'])
    
    # Pastikan kolom 'Tanggal Lahir' hanya menyimpan tanggal
    if not data.empty and 'Tanggal Lahir' in data.columns:
        data['Tanggal Lahir'] = pd.to_datetime(data['Tanggal Lahir'], errors='coerce').dt.date
    
    return data

# Aplikasi Tkinter
class AplikasiSiswa:
    def __init__(self, root):
        self.root = root
        self.root.title("Manajemen Data Siswa")
        self.root.geometry("1920x1080")

        # Muat gambar latar belakang untuk masing-masing frame
        try:
            self.bg_image_login = ImageTk.PhotoImage(Image.open("D:/projecta/paket a/Kelas-A---Kelompok-11/background login.jpg").resize((1400, 700)))
            self.bg_image_input_id = ImageTk.PhotoImage(Image.open("D:/projecta/paket a/Kelas-A---Kelompok-11/background id.jpg").resize((1400, 700)))
            self.bg_image_input_data = ImageTk.PhotoImage(Image.open("D:/projecta/paket a/Kelas-A---Kelompok-11/background data siswa.jpg").resize((1400, 700)))
            self.bg_image_tabel_data = ImageTk.PhotoImage(Image.open("D:/projecta/paket a/Kelas-A---Kelompok-11/background tabel.jpg").resize((1400, 700)))
        except Exception as e:
            messagebox.showerror("Error", f"Error loading image: {e}")
            return
 
        # Frame Login
        self.frame_login = self.buat_frame_dengan_bg(self.root, self.bg_image_login)
        tk.Label(self.frame_login, text="LOG IN ADMIN", font=("times new roman bold", 22), bg="white").place(relx=0.5, rely=0.2, anchor="center")
        tk.Label(self.frame_login, text="Username", font=("times new roman", 16), bg="pink").place(relx=0.5, rely=0.35, anchor="center")
        self.entry_username = tk.Entry(self.frame_login, font=("times new roman", 14))
        self.entry_username.place(relx=0.5, rely=0.4, anchor="center")
        tk.Label(self.frame_login, text="Password", font=("times new roman", 16), bg="pink").place(relx=0.5, rely=0.45, anchor="center")
        self.entry_password = tk.Entry(self.frame_login, show="*", font=("times new roman", 14))
        self.entry_password.place(relx=0.5, rely=0.5, anchor="center")
        tk.Button(self.frame_login, text="LOG IN", font=("times new roman", 18), bg="white", command=self.login).place(relx=0.5, rely=0.6, anchor="center")

        # Frame Input ID
        self.frame_input_id = self.buat_frame_dengan_bg(self.root, self.bg_image_input_id)
        tk.Label(self.frame_input_id, text="NOMOR IDENTITAS DIRI", font=("times new roman bold", 22), bg="pink").place(relx=0.5, rely=0.25, anchor="center")
        tk.Label(self.frame_input_id, text="Masukkan No. ID", font=("times new roman", 16), bg="beige").place(relx=0.5, rely=0.35, anchor="center")
        self.entry_id_input = tk.Entry(self.frame_input_id, font=("times new roman", 16))
        self.entry_id_input.place(relx=0.5, rely=0.4, anchor="center")
        tk.Button(self.frame_input_id, text="Cek ID", font=("times new roman", 16), bg="beige", command=self.cek_id).place(relx=0.5, rely=0.48, anchor="center")
        tk.Button(self.frame_input_id, text="Kembali", font=("times new roman", 16), bg="beige", command=self.kembali_ke_login).place(relx=0.5, rely=0.55, anchor="center")

        # Frame Input Data Siswa
        self.frame_input_data = self.buat_frame_dengan_bg(self.root, self.bg_image_input_data)
        tk.Label(self.frame_input_data, text="MASUKKAN DATA SISWA", font=("times new roman bold", 22), bg="beige").place(relx=0.5, rely=0.1, anchor="center")

        tk.Label(self.frame_input_data, text="Nama", font=("times new roman", 14), bg="pink").place(relx=0.5, rely=0.2, anchor="center")
        self.entry_nama = tk.Entry(self.frame_input_data, font=("times new roman", 14))
        self.entry_nama.place(relx=0.5, rely=0.25, anchor="center")

        tk.Label(self.frame_input_data, text="Kelas", font=("times new roman", 14), bg="pink").place(relx=0.5, rely=0.3, anchor="center")
        self.entry_kelas = tk.Entry(self.frame_input_data, font=("times new roman", 14))
        self.entry_kelas.place(relx=0.5, rely=0.35, anchor="center")

        tk.Label(self.frame_input_data, text="Tanggal Lahir (dd-mm-yyyy)", font=("times new roman", 14), bg="pink").place(relx=0.5, rely=0.4, anchor="center")
        self.entry_tanggal_lahir = tk.Entry(self.frame_input_data, font=("times new roman", 14))
        self.entry_tanggal_lahir.place(relx=0.5, rely=0.45, anchor="center")

        tk.Label(self.frame_input_data, text="Alamat", font=("times new roman", 14), bg="pink").place(relx=0.5, rely=0.5, anchor="center")
        self.entry_alamat = tk.Entry(self.frame_input_data, font=("times new roman", 14))
        self.entry_alamat.place(relx=0.5, rely=0.55, anchor="center")

        tk.Button(self.frame_input_data, text="Simpan Data", font=("times new roman", 16), bg="beige", command=self.tambah_data_siswa).place(relx=0.5, rely=0.65, anchor="center")
        tk.Button(self.frame_input_data, text="Kembali", font=("times new roman", 16), bg="beige", command=self.kembali_ke_input_id).place(relx=0.5, rely=0.75, anchor="center")

        # Frame Tabel Data Siswa
        self.frame_tabel_siswa = self.buat_frame_dengan_bg(self.root, self.bg_image_tabel_data)
        tk.Label(self.frame_tabel_siswa, text="DATA SISWA", font=("times new roman bold", 22), bg="pink").place(relx=0.5, rely=0.1, anchor="center")

        self.tree = ttk.Treeview(self.frame_tabel_siswa, columns=("ID", "Nama", "Kelas", "Tanggal Lahir", "Alamat"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nama", text="Nama")
        self.tree.heading("Kelas", text="Kelas")
        self.tree.heading("Tanggal Lahir", text="Tanggal Lahir")
        self.tree.heading("Alamat", text="Alamat")
        self.tree.place(relx=0.5, rely=0.45, anchor="center", width=1000, height=350)
        tk.Button(self.frame_tabel_siswa, text="Masukkan ID Lagi", font=("times new roman", 16), bg="pink", command=self.kembali_ke_input_id).place(relx=0.5, rely=0.75, anchor="center")
        tk.Button(self.frame_tabel_siswa, text="Log Out", font=("times new roman", 16), bg="pink", command=self.logout).place(relx=0.5, rely=0.85, anchor="center")

    def buat_frame_dengan_bg(self, parent, bg_image):
        frame = tk.Frame(parent)
        canvas = tk.Canvas(frame, width=1920, height=1080)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg_image, anchor="nw")
        frame.canvas = canvas  # Simpan referensi
        return frame

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if username == admin_username and password == admin_password:
            messagebox.showinfo("Sukses", "Login berhasil!")
            self.frame_login.pack_forget()
            self.frame_input_id.pack(fill="both", expand=True)
        else:
            messagebox.showerror("Error", "Username atau password salah.")

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

    def tampilkan_data_siswa(self, data_siswa):
        self.frame_input_id.pack_forget()
        self.frame_tabel_siswa.pack(fill="both", expand=True)

        for i in self.tree.get_children():
            self.tree.delete(i)

        for _, row in data_siswa.iterrows():
            self.tree.insert("", "end", values=(row["ID"], row["Nama"], row["Kelas"], row["Tanggal Lahir"], row["Alamat"]))

    def tambah_data_siswa(self):
        id_input = self.entry_id_input.get()
        nama = self.entry_nama.get()
        kelas = self.entry_kelas.get()
        tanggal_lahir = self.entry_tanggal_lahir.get()
        alamat = self.entry_alamat.get()

        if not all([id_input, nama, kelas, tanggal_lahir, alamat]):
            messagebox.showerror("Error", "Semua kolom harus diisi.")
            return

        try:
            id_input = int(id_input)
        except ValueError:
            messagebox.showerror("Error", "ID harus berupa angka.")
            return

        data_siswa = baca_data_siswa()
        if id_input in data_siswa["ID"].values:
            messagebox.showerror("Error", f"ID {id_input} sudah ada.")
            return

        data_baru = pd.DataFrame({
            "ID": [id_input],
            "Nama": [nama],
            "Kelas": [kelas],
            "Tanggal Lahir": [tanggal_lahir],
            "Alamat": [alamat]
        })

        data_siswa = pd.concat([data_siswa, data_baru], ignore_index=True)
        simpan_data(file_siswa, data_siswa)

        messagebox.showinfo("Sukses", "Data berhasil disimpan.")
        self.entry_nama.delete(0, "end")
        self.entry_kelas.delete(0, "end")
        self.entry_tanggal_lahir.delete(0, "end")
        self.entry_alamat.delete(0, "end")
        self.frame_input_data.pack_forget()
        self.frame_input_id.pack(fill="both", expand=True)

    def kembali_ke_login(self):
        self.frame_input_id.pack_forget()
        self.frame_login.pack(fill="both", expand=True)

    def kembali_ke_input_id(self):
        self.frame_input_data.pack_forget()
        self.frame_tabel_siswa.pack_forget()
        self.frame_input_id.pack(fill="both", expand=True)

    def logout(self):
        self.frame_tabel_siswa.pack_forget()
        self.frame_login.pack(fill="both", expand=True)


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiSiswa(root)
    app.frame_login.pack(fill="both", expand=True)
    root.mainloop()
