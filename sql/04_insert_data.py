import pandas as pd
import pyodbc # Pustaka untuk koneksi ke SQL Server

# 1. Konfigurasi Koneksi Database
# Ganti dengan detail koneksi SQL Server Anda
db_config = {
    'driver': '{SQL Server Native Client 11.0}', # Sesuaikan driver jika perlu (misalnya, '{ODBC Driver 17 for SQL Server}')
    'server': 'NAMA_SERVER_ANDA',                # Misalnya, 'localhost\SQLEXPRESS' atau nama server Anda
    'database': 'NAMA_DATABASE_ANDA',        # Nama database tempat tabel Anda berada
    'username': 'USER_SQL_ANDA',                 # Jika menggunakan SQL Server Authentication
    'password': 'PASSWORD_SQL_ANDA'              # Jika menggunakan SQL Server Authentication
    # Jika menggunakan Windows Authentication, Anda bisa mengganti username & password dengan:
    # 'trusted_connection': 'yes'
}

# Membuat string koneksi
if 'trusted_connection' in db_config:
    conn_str = f"DRIVER={db_config['driver']};SERVER={db_config['server']};DATABASE={db_config['database']};TRUSTED_CONNECTION={db_config['trusted_connection']}"
else:
    conn_str = f"DRIVER={db_config['driver']};SERVER={db_config['server']};DATABASE={db_config['database']};UID={db_config['username']};PWD={db_config['password']}"

# 2. Lokasi File CSV
csv_file_path = r'sains-data/Kelompok-19-DW-RC/dataset/fakta_penerbangan.csv' # Contoh path, sesuaikan!


# 3. Membaca data dari CSV menggunakan Pandas
try:
    df_facts = pd.read_csv(csv_file_path)
    print(f"Berhasil membaca {len(df_facts)} baris dari {csv_file_path}")
except FileNotFoundError:
    print(f"Error: File CSV tidak ditemukan di {csv_file_path}")
    exit()
except Exception as e:
    print(f"Error saat membaca file CSV: {e}")
    exit()

# 4. Proses Memasukkan Data ke SQL Server
cnxn = None # Inisialisasi koneksi
try:
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    print("Berhasil terhubung ke database SQL Server.")

    # Query SQL untuk INSERT
    # Pastikan nama kolom di query SQL dan di DataFrame (CSV header) sesuai
    sql_insert_query = """
    INSERT INTO Fakta_Penerbangan (
        ID_FaktaPenerbangan,
        ID_Waktu,
        ID_Lokasi,
        ID_Penerbangan,
        ID_Pesawat,
        ID_KelasLayanan,
        ID_StatusPenerbangan,
        Jumlah_Penumpang,
        Pendapatan,
        Jumlah_Penerbangan
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """

    # Iterasi per baris DataFrame dan masukkan ke database
    rows_inserted = 0
    for index, row in df_facts.iterrows():
        try:
            # Sesuaikan 'nama_kolom_di_csv' dengan header kolom aktual di file CSV Anda
            # Pastikan urutan nilai sesuai dengan urutan kolom di query INSERT
            cursor.execute(sql_insert_query,
                           row['ID_FaktaPenerbangan'], # Sesuaikan dengan nama kolom di CSV Anda
                           row['ID_Waktu'],
                           row['ID_Lokasi'],
                           row['ID_Penerbangan'],
                           row['ID_Pesawat'],
                           row['ID_KelasLayanan'],
                           row['ID_StatusPenerbangan'],
                           row['Jumlah_Penumpang'],
                           row['Pendapatan'],
                           row['Jumlah_Penerbangan']
                           )
            rows_inserted += 1
        except Exception as e_insert:
            print(f"Error saat memasukkan baris ke-{index + 1} ({row.get('ID_FaktaPenerangan', 'ID Tidak Tersedia')}): {e_insert}")
            # Anda bisa memilih untuk menghentikan proses jika ada error:
            # raise
            # Atau melanjutkan ke baris berikutnya:
            # continue

    cnxn.commit() # Commit transaksi jika semua berjalan lancar
    print(f"Berhasil memasukkan {rows_inserted} baris data ke tabel Fakta_Penerbangan.")

except pyodbc.Error as db_err:
    print(f"Error koneksi atau eksekusi database: {db_err}")
    if cnxn:
        cnxn.rollback() # Rollback jika terjadi error
except Exception as e:
    print(f"Terjadi error yang tidak terduga: {e}")
    if cnxn:
        cnxn.rollback()
finally:
    if cnxn:
        cnxn.close()
        print("Koneksi database ditutup.")