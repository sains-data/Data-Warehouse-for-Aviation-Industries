import pandas as pd
import os

# Konfigurasi
# Ganti dengan path lengkap dan benar ke file CSV Anda
# Sebaiknya gunakan path absolut atau path relatif yang dikelola dengan baik
# Misalnya, jika dataset ada di ../../data/source/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # <project_root_dir>
# Ganti 'nama_file_dataset_anda.csv' dengan nama file CSV yang benar
# Ini mengasumsikan file CSV Anda ada di <project_root_dir>/data/source/
CSV_FILE_PATH = os.path.join(BASE_DIR, 'data', 'source', 'fakta_penerbangan.csv')

# Untuk contoh ini, kita akan gunakan path yang Anda sebutkan sebelumnya,
# tapi Anda perlu memastikan path ini valid saat skrip dijalankan.
# Menggunakan path absolut lebih aman jika struktur folder kompleks.
# CSV_FILE_PATH = r'D:\data sains-data\Kelompok-19-DW-RC\dataset\fakta_penerbangan.csv' # GANTI DENGAN PATH ANDA!
# atau jika file CSV ada di folder yang sama dengan skrip Python:
# CSV_FILE_PATH = 'fakta_penerbangan.csv'


def extract_data_from_csv(file_path=CSV_FILE_PATH):
    """
    Mengekstrak data dari file CSV yang diberikan.

    Args:
        file_path (str): Path ke file CSV.

    Returns:
        pandas.DataFrame: DataFrame yang berisi data dari CSV, atau None jika terjadi error.
    """
    try:
        print(f"Mencoba membaca data dari: {file_path}")
        df = pd.read_csv(file_path)
        print(f"Berhasil membaca {len(df)} baris dari {file_path}")
        return df
    except FileNotFoundError:
        print(f"Error: File CSV tidak ditemukan di {file_path}")
        return None
    except Exception as e:
        print(f"Error saat membaca file CSV di extract_data_from_csv: {e}")
        return None

if __name__ == '__main__':
    # Contoh penggunaan fungsi extract
    extracted_df = extract_data_from_csv()

    if extracted_df is not None:
        print("\nData berhasil diekstrak. Berikut 5 baris pertama:")
        print(extracted_df.head())
        print(f"\nInformasi DataFrame:")
        extracted_df.info()