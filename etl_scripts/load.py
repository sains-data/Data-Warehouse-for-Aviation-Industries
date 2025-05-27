# etl_scripts/load.py

import sqlite3
import pandas as pd
import os

# Konfigurasi Database SQLite untuk demonstrasi
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, 'aviation_warehouse.db')

def init_database():
    """
    Inisialisasi database dan tabel jika belum ada.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Baca file SQL dan eksekusi
    sql_file_path = os.path.join(BASE_DIR, 'sql', '01_create_tables.sql')
    
    if os.path.exists(sql_file_path):
        with open(sql_file_path, 'r', encoding='utf-8') as f:
            sql_content = f.read()
            # SQLite adaptation - remove TEXT type for compatibility
            sql_content = sql_content.replace('TEXT', 'VARCHAR(500)')
            sql_content = sql_content.replace('BIGINT', 'INTEGER')
            
            # Split and execute each CREATE TABLE statement
            statements = sql_content.split(';')
            for statement in statements:
                if statement.strip():
                    try:
                        cursor.execute(statement)
                    except sqlite3.Error as e:
                        if "already exists" not in str(e):
                            print(f"Error creating table: {e}")
                            print(f"Statement: {statement[:100]}...")
    
    conn.commit()
    conn.close()
    print(f"Database initialized at: {DB_PATH}")

def load_data_to_dwh(df_transformed, target_table='Fakta_Penerbangan'):
    """
    Memuat DataFrame yang sudah ditransformasi ke tabel target di SQLite.

    Args:
        df_transformed (pandas.DataFrame): DataFrame yang siap dimuat.
        target_table (str): Nama tabel target di database.

    Returns:
        bool: True jika pemuatan berhasil, False jika gagal.
    """
    if df_transformed is None or df_transformed.empty:
        print("DataFrame input kosong, tidak ada data yang dimuat.")
        return False

    try:
        # Inisialisasi database terlebih dahulu
        init_database()
        
        conn = sqlite3.connect(DB_PATH)
        print(f"Berhasil terhubung ke database untuk memuat data ke tabel {target_table}.")

        # Menggunakan pandas to_sql untuk kemudahan
        df_transformed.to_sql(target_table, conn, if_exists='append', index=False)
        
        conn.commit()
        print(f"Berhasil memuat {len(df_transformed)} baris ke tabel {target_table}.")
        
        # Verifikasi data yang dimuat
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {target_table}")
        total_rows = cursor.fetchone()[0]
        print(f"Total baris sekarang di tabel {target_table}: {total_rows}")
        
        conn.close()
        return True

    except sqlite3.Error as db_err:
        print(f"Error database saat memuat data: {db_err}")
        return False
    except Exception as e:
        print(f"Terjadi error yang tidak terduga saat memuat data: {e}")
        return False

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
        'Pendapatan': [15000000, 17500000, 32000000],
        'Jumlah_Penerbangan': [1, 1, 1],
    }
    df_sample_transformed = pd.DataFrame(sample_transformed_data)

    print("DataFrame Sampel Siap Dimuat:")
    print(df_sample_transformed)
    df_sample_transformed.info()

    # Test database initialization
    init_database()
    
    print("\nMenjalankan contoh pemuatan data...")
    success = load_data_to_dwh(df_sample_transformed)
    if success:
        print("Contoh pemuatan data selesai dengan sukses.")
    else:
        print("Contoh pemuatan data gagal.")