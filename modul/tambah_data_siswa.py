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
        
def simpan_data(file_path, data):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
        data.to_excel(writer, index=False)
        
def baca_data(file_path, columns):
    if os.path.exists(file_path):
        data = pd.read_excel(file_path, engine='openpyxl')
        if set(columns).issubset(data.columns):
            return data
        else:
            return pd.DataFrame(columns=columns)
    else:
        return pd.DataFrame(columns=columns)

def baca_data_siswa():
    data = baca_data(file_siswa, ['ID', 'Nama', 'Kelas', 'Tanggal Lahir', 'Alamat'])
    
    # Pastikan kolom 'Tanggal Lahir' hanya menyimpan tanggal
    if not data.empty and 'Tanggal Lahir' in data.columns:
        data['Tanggal Lahir'] = pd.to_datetime(data['Tanggal Lahir'], errors='coerce').dt.date
    
    return data

def kembali_ke_input_id(self):
        self.frame_input_data.pack_forget()
        self.frame_tabel_siswa.pack_forget()
        self.frame_input_id.pack(fill="both", expand=True)
