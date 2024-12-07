def tampilkan_data_siswa(self, data_siswa):
        self.frame_input_id.pack_forget()
        self.frame_tabel_siswa.pack(fill="both", expand=True)

        for i in self.tree.get_children():
            self.tree.delete(i)

        for _, row in data_siswa.iterrows():
            self.tree.insert("", "end", values=(row["ID"], row["Nama"], row["Kelas"], row["Tanggal Lahir"], row["Alamat"]))

def kembali_ke_input_id(self):
        self.frame_input_data.pack_forget()
        self.frame_tabel_siswa.pack_forget()
        self.frame_input_id.pack(fill="both", expand=True)

def logout(self):
        self.frame_tabel_siswa.pack_forget()
        self.frame_login.pack(fill="both", expand=True)
