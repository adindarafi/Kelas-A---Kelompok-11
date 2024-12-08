import os
import pandas as pd

# Nama file default untuk menyimpan data siswa
file_siswa = "D:/projectc/data_siswa.xlsx"

# Fungsi untuk membaca file Excel
def baca_data(file_path, columns):
    """
    Membaca data dari file Excel dengan kolom tertentu.

    :param file_path: Path file Excel.
    :param columns: List nama kolom yang diinginkan.
    :return: DataFrame dengan kolom yang diinginkan atau DataFrame kosong jika file tidak ada atau kolom tidak sesuai.
    """
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
    """
    Menyimpan data ke file Excel.

    :param file_path: Path file Excel.
    :param data: DataFrame yang akan disimpan.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with pd.ExcelWriter(file_path, engine='openpyxl', mode='w') as writer:
        data.to_excel(writer, index=False)

# Fungsi untuk membaca data siswa dengan validasi kolom
def baca_data_siswa():
    """
    Membaca data siswa dari file Excel default.

    :return: DataFrame dengan kolom ['ID', 'Nama', 'Kelas', 'Tanggal Lahir', 'Alamat'].
    """
    columns = ['ID', 'Nama', 'Kelas', 'Tanggal Lahir', 'Alamat']
    data = baca_data(file_siswa, columns)
    
    # Pastikan kolom 'Tanggal Lahir' hanya menyimpan tanggal
    if not data.empty and 'Tanggal Lahir' in data.columns:
        data['Tanggal Lahir'] = pd.to_datetime(data['Tanggal Lahir'], errors='coerce').dt.date
    
    return data
