# etl_scripts/python/transform.py

import pandas as pd

def transform_flight_data(df_raw):
    """
    Melakukan transformasi pada DataFrame data penerbangan mentah.

    Args:
        df_raw (pandas.DataFrame): DataFrame mentah dari hasil ekstraksi.

    Returns:
        pandas.DataFrame: DataFrame yang sudah ditransformasi dan siap dimuat.
                          Mengembalikan None jika input DataFrame kosong atau terjadi error.
    """
    if df_raw is None or df_raw.empty:
        print("DataFrame input kosong, tidak ada transformasi yang dilakukan.")
        return None

    try:
        print("Memulai proses transformasi data...")
        df_transformed = df_raw.copy()

        # 1. Mengganti nama kolom agar sesuai dengan skema DWH
        # Sesuaikan dengan nama kolom aktual di CSV dan target di DWH Anda
        column_renames = {
            'FaktaID': 'ID_FaktaPenerbangan',
            'WaktuID': 'ID_Waktu',
            'LokasiID': 'ID_Lokasi',
            'PenerbanganID': 'ID_Penerbangan',
            'PesawatID': 'ID_Pesawat',
            'KelasID': 'ID_KelasLayanan',
            'StatusID': 'ID_StatusPenerbangan',
            'Keterlambatan': 'Keterlambatan_Menit',
            'Waktu_Keberangkatan': 'Waktu_Keberangkatan_Aktual',
            'Waktu_Kedatangan': 'Waktu_Kedatangan_Aktual'
            # Kolom seperti 'Jumlah_Penumpang', 'Pendapatan', 'Biaya_Operasional'
            # mungkin sudah memiliki nama yang benar.
        }
        df_transformed.rename(columns=column_renames, inplace=True)
        print("Penggantian nama kolom selesai.")

        # 2. Konversi Tipe Data
        # Kolom tanggal/waktu
        if 'Waktu_Keberangkatan_Aktual' in df_transformed.columns:
            df_transformed['Waktu_Keberangkatan_Aktual'] = pd.to_datetime(
                df_transformed['Waktu_Keberangkatan_Aktual'], errors='coerce'
            )
        if 'Waktu_Kedatangan_Aktual' in df_transformed.columns:
            df_transformed['Waktu_Kedatangan_Aktual'] = pd.to_datetime(
                df_transformed['Waktu_Kedatangan_Aktual'], errors='coerce'
            )

        # Kolom numerik (contoh)
        numeric_cols = ['Jumlah_Penumpang', 'Pendapatan', 'Biaya_Operasional', 'Keterlambatan_Menit']
        for col in numeric_cols:
            if col in df_transformed.columns:
                df_transformed[col] = pd.to_numeric(df_transformed[col], errors='coerce')
        print("Konversi tipe data selesai.")

        # 3. Menangani Nilai Null (Contoh: mengisi dengan 0 untuk numerik atau nilai default lain)
        # Ini sangat tergantung pada kebutuhan bisnis Anda.
        if 'Keterlambatan_Menit' in df_transformed.columns:
            df_transformed['Keterlambatan_Menit'].fillna(0, inplace=True)
        if 'Biaya_Operasional' in df_transformed.columns:
            df_transformed['Biaya_Operasional'].fillna(0.0, inplace=True)
        # Untuk FK, nilai null mungkin berarti data tidak diketahui atau tidak relevan.
        # Pastikan kolom FK di database Anda memperbolehkan NULL jika ini kasusnya.

        # 4. Menambahkan Kolom yang Mungkin Hilang (Contoh: Jumlah_Penerbangan)
        # Sesuai DDL awal, Fakta_Penerbangan memiliki 'Jumlah_Penerbangan'
        if 'Jumlah_Penerbangan' not in df_transformed.columns:
            df_transformed['Jumlah_Penerbangan'] = 1 # Asumsi setiap baris adalah 1 penerbangan
        print("Penambahan kolom default selesai.")

        # 5. Validasi Data (Contoh sederhana)
        # Pastikan ID Kunci Asing tidak null jika kolom tersebut di DB adalah NOT NULL
        # dan tidak memiliki nilai default.
        # Contoh:
        # required_fk_ids = ['ID_Waktu', 'ID_Lokasi', 'ID_Penerbangan', 'ID_Pesawat', 'ID_KelasLayanan', 'ID_StatusPenerbangan']
        # for fk_col in required_fk_ids:
        #     if fk_col in df_transformed.columns and df_transformed[fk_col].isnull().any():
        #         print(f"Peringatan: Terdapat nilai NULL di kolom kunci asing '{fk_col}' yang mungkin wajib diisi.")
        #         # Anda mungkin ingin memfilter baris ini atau mengisinya dengan nilai default jika memungkinkan

        print("Transformasi data selesai.")
        return df_transformed

    except Exception as e:
        print(f"Error selama proses transformasi data: {e}")
        return None

if __name__ == '__main__':
    # Contoh penggunaan fungsi transform
    # Buat DataFrame sampel mentah (biasanya ini akan datang dari extract.py)
    sample_raw_data = {
        'FaktaID': [1, 2, 3],
        'WaktuID': [20240101, 20240101, 20240102],
        'LokasiID': [1, 2, 1],
        'PenerbanganID': [101, 102, 103],
        'PesawatID': [1, 2, 1],
        'KelasID': [1, 1, 2],
        'StatusID': [1, 2, 1],
        'Jumlah_Penumpang': [150, 175, 160],
        'Pendapatan': [15000000, 17500000, 32000000],
        'Biaya_Operasional': [10000000, 12000000, None], # Contoh ada NaN
        'Waktu_Keberangkatan': ['2024-01-01 08:00:00', '2024-01-01 10:00:00', '2024-01-02 14:00:00'],
        'Waktu_Kedatangan': ['2024-01-01 09:00:00', '2024-01-01 11:30:00', '2024-01-02 15:00:00'],
        'Keterlambatan': [0, 30, 'N/A'] # Contoh ada string 'N/A'
    }
    df_sample_raw = pd.DataFrame(sample_raw_data)

    print("DataFrame Mentah Sampel:")
    print(df_sample_raw)

    transformed_df = transform_flight_data(df_sample_raw)

    if transformed_df is not None:
        print("\nData berhasil ditransformasi. Berikut 5 baris pertama:")
        print(transformed_df.head())
        print(f"\nInformasi DataFrame Setelah Transformasi:")
        transformed_df.info()