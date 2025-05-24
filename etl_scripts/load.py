# etl_scripts/python/load.py

import pyodbc
import pandas as pd # Hanya untuk membuat DataFrame sampel jika __main__ dijalankan

# Konfigurasi Koneksi Database
# Ganti dengan detail koneksi SQL Server Anda
db_config = {
    'driver': '{SQL Server Native Client 11.0}', # Sesuaikan driver jika perlu
    'server': 'NAMA_SERVER_ANDA',
    'database': 'NAMA_DATABASE_ANDA',
    'username': 'USER_SQL_ANDA',
    'password': 'PASSWORD_SQL_ANDA'
    # atau 'trusted_connection': 'yes'
}

# Membuat string koneksi
if 'trusted_connection' in db_config:
    conn_str = f"DRIVER={db_config['driver']};SERVER={db_config['server']};DATABASE={db_config['database']};TRUSTED_CONNECTION={db_config['trusted_connection']}"
else:
    conn_str = f"DRIVER={db_config['driver']};SERVER={db_config['server']};DATABASE={db_config['database']};UID={db_config['username']};PWD={db_config['password']}"


def load_data_to_dwh(df_transformed, target_table='Fakta_Penerbangan'):
    """
    Memuat DataFrame yang sudah ditransformasi ke tabel target di SQL Server.

    Args:
        df_transformed (pandas.DataFrame): DataFrame yang siap dimuat.
        target_table (str): Nama tabel target di database.

    Returns:
        bool: True jika pemuatan berhasil, False jika gagal.
    """
    if df_transformed is None or df_transformed.empty:
        print("DataFrame input kosong, tidak ada data yang dimuat.")
        return False

    cnxn = None
    try:
        cnxn = pyodbc.connect(conn_str)
        cursor = cnxn.cursor()
        print(f"Berhasil terhubung ke database untuk memuat data ke tabel {target_table}.")

        # Membuat query INSERT berdasarkan kolom DataFrame
        # Pastikan urutan kolom di DataFrame sesuai dengan urutan parameter di query
        cols = df_transformed.columns.tolist()
        placeholders = ', '.join(['?'] * len(cols)) # ?, ?, ?, ...
        sql_insert_query = f"INSERT INTO {target_table} ({', '.join(cols)}) VALUES ({placeholders})"
        
        print(f"Query INSERT yang akan digunakan: {sql_insert_query}")
        print(f"Kolom yang akan dimasukkan: {cols}")

        # Konversi DataFrame ke list of tuples untuk dimasukkan
        data_to_insert = [tuple(row) for row in df_transformed.to_numpy()]

        # Menggunakan executemany untuk performa yang lebih baik pada multiple inserts
        cursor.fast_executemany = True # Coba aktifkan untuk pyodbc, bisa meningkatkan performa
        cursor.executemany(sql_insert_query, data_to_insert)
        
        cnxn.commit()
        print(f"Berhasil memuat {len(data_to_insert)} baris ke tabel {target_table}.")
        return True

    except pyodbc.Error as db_err:
        print(f"Error koneksi atau eksekusi database saat memuat data: {db_err}")
        if cnxn:
            cnxn.rollback()
        return False
    except Exception as e:
        print(f"Terjadi error yang tidak terduga saat memuat data: {e}")
        if cnxn:
            cnxn.rollback()
        return False
    finally:
        if cnxn:
            cnxn.close()
            print("Koneksi database ditutup setelah proses pemuatan.")

if __name__ == '__main__':
    # Contoh penggunaan fungsi load
    # Buat DataFrame sampel yang sudah ditransformasi
    # (biasanya ini akan datang dari transform.py)
    sample_transformed_data = {
        'ID_FaktaPenerbangan': [1, 2, 3],
        'ID_Waktu': [20240101, 20240101, 20240102],
        'ID_Lokasi': [1, 2, 1],
        'ID_Penerbangan': [101, 102, 103],
        'ID_Pesawat': [1, 2, 1],
        'ID_KelasLayanan': [1, 1, 2],
        'ID_StatusPenerbangan': [1, 2, 1],
        'Jumlah_Penumpang': [150, 175, 160],
        'Pendapatan': [15000000.0, 17500000.0, 32000000.0],
        'Jumlah_Penerbangan': [1, 1, 1],
        'Biaya_Operasional': [10000000.0, 12000000.0, 0.0], # NaN sudah diisi 0.0
        'Waktu_Keberangkatan_Aktual': [pd.Timestamp('2024-01-01 08:00:00'), pd.Timestamp('2024-01-01 10:00:00'), pd.Timestamp('2024-01-02 14:00:00')],
        'Waktu_Kedatangan_Aktual': [pd.Timestamp('2024-01-01 09:00:00'), pd.Timestamp('2024-01-01 11:30:00'), pd.Timestamp('2024-01-02 15:00:00')],
        'Keterlambatan_Menit': [0, 30, 0] # 'N/A' sudah diisi 0
    }
    df_sample_transformed = pd.DataFrame(sample_transformed_data)

    # Pastikan urutan kolom di DataFrame ini sama dengan yang diharapkan oleh tabel Fakta_Penerbangan
    # dan query INSERT yang digenerate secara dinamis.
    # Ini penting jika Anda tidak secara eksplisit menyebutkan nama kolom di VALUES (?,?,?)
    # Dengan membuat query INSERT dinamis ({', '.join(cols)}), urutan dari df_transformed.columns akan digunakan.

    print("DataFrame Sampel Siap Dimuat:")
    print(df_sample_transformed)
    df_sample_transformed.info()

    # PENTING: Sebelum menjalankan ini, pastikan tabel Fakta_Penerbangan Anda sudah siap
    # dan tabel dimensi sudah terisi agar FK tidak error.
    # Juga, pastikan tidak ada data dengan ID_FaktaPenerbangan yang sama jika kolom itu adalah PRIMARY KEY.
    # success = load_data_to_dwh(df_sample_transformed)
    # if success:
    #     print("Contoh pemuatan data selesai dengan sukses.")
    # else:
    #     print("Contoh pemuatan data gagal.")
    print("\nKomentari bagian pemanggilan load_data_to_dwh di __main__ jika hanya ingin melihat struktur file.")