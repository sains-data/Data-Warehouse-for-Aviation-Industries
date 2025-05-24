# main_etl.py (Contoh skrip utama)

from etl_scripts.python.extract import extract_data_from_csv
from etl_scripts.python.transform import transform_flight_data
from etl_scripts.python.load import load_data_to_dwh

def run_etl_pipeline():
    print("Memulai pipeline ETL Penerbangan...")

    # 1. Extract
    print("\n--- Tahap Ekstraksi ---")
    raw_data_df = extract_data_from_csv()
    if raw_data_df is None:
        print("Ekstraksi gagal. Menghentikan pipeline.")
        return

    # 2. Transform
    print("\n--- Tahap Transformasi ---")
    transformed_data_df = transform_flight_data(raw_data_df)
    if transformed_data_df is None:
        print("Transformasi gagal. Menghentikan pipeline.")
        return

    # 3. Load
    print("\n--- Tahap Pemuatan ---")
    # Ganti 'Fakta_Penerbangan' jika nama tabel target Anda berbeda
    success = load_data_to_dwh(transformed_data_df, target_table='Fakta_Penerbangan')
    if success:
        print("Pipeline ETL Penerbangan selesai dengan sukses.")
    else:
        print("Pemuatan data gagal. Pipeline ETL dihentikan dengan error.")

if __name__ == '__main__':
    run_etl_pipeline()