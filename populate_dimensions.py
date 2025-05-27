#!/usr/bin/env python3
"""
Script untuk mengisi tabel dimensi dengan data referensi
"""

import sqlite3
import pandas as pd
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'aviation_warehouse.db')

def populate_dim_waktu():
    """Mengisi tabel Dim_Waktu dengan data tanggal dari 2024-2025"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Hapus data lama jika ada
    cursor.execute("DELETE FROM Dim_Waktu")
    
    # Generate data waktu untuk 2024-2025
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2025, 12, 31)
    current_date = start_date
    
    waktu_data = []
    while current_date <= end_date:
        waktu_id = int(current_date.strftime('%Y%m%d'))
        tanggal = current_date.strftime('%Y-%m-%d')
        hari = current_date.strftime('%A')
        bulan = current_date.month
        tahun = current_date.year
        kuartal = (current_date.month - 1) // 3 + 1
        
        waktu_data.append((waktu_id, tanggal, hari, bulan, tahun, kuartal))
        current_date += timedelta(days=1)
    
    cursor.executemany(
        "INSERT INTO Dim_Waktu (ID_Waktu, Tanggal, Hari, Bulan, Tahun, Kuartal) VALUES (?, ?, ?, ?, ?, ?)",
        waktu_data
    )
    
    conn.commit()
    print(f"Berhasil mengisi {len(waktu_data)} record ke Dim_Waktu")
    conn.close()

def populate_dim_lokasi():
    """Mengisi tabel Dim_Lokasi dengan data bandara"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Hapus data lama jika ada
    cursor.execute("DELETE FROM Dim_Lokasi")
    
    lokasi_data = [
        (1, 'Soekarno-Hatta International Airport', 'Jakarta', 'Indonesia'),
        (2, 'Ngurah Rai International Airport', 'Denpasar', 'Indonesia'),
        (3, 'Juanda International Airport', 'Surabaya', 'Indonesia'),
        (4, 'Sultan Hasanuddin Airport', 'Makassar', 'Indonesia'),
        (5, 'Adisutcipto Airport', 'Yogyakarta', 'Indonesia'),
        (6, 'Minangkabau International Airport', 'Padang', 'Indonesia'),
        (7, 'Ahmad Yani International Airport', 'Semarang', 'Indonesia'),
        (8, 'Sultan Syarif Kasim II Airport', 'Pekanbaru', 'Indonesia'),
        (9, 'Husein Sastranegara Airport', 'Bandung', 'Indonesia'),
        (10, 'El Tari Airport', 'Kupang', 'Indonesia')
    ]
    
    cursor.executemany(
        "INSERT INTO Dim_Lokasi (ID_Lokasi, Nama_Bandara, Kota, Negara) VALUES (?, ?, ?, ?)",
        lokasi_data
    )
    
    conn.commit()
    print(f"Berhasil mengisi {len(lokasi_data)} record ke Dim_Lokasi")
    conn.close()

def populate_dim_penerbangan():
    """Mengisi tabel Dim_Penerbangan dengan data penerbangan"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Hapus data lama jika ada
    cursor.execute("DELETE FROM Dim_Penerbangan")
    
    penerbangan_data = [
        (1, 'GA-101', 'Garuda Indonesia', '06:00:00', '08:30:00'),
        (2, 'JT-201', 'Lion Air', '07:15:00', '09:45:00'),
        (3, 'QZ-301', 'Indonesia AirAsia', '08:30:00', '11:00:00'),
        (4, 'SJ-401', 'Sriwijaya Air', '09:45:00', '12:15:00'),
        (5, 'GA-501', 'Garuda Indonesia', '10:00:00', '12:30:00'),
        (6, 'JT-601', 'Lion Air', '11:15:00', '13:45:00'),
        (7, 'QZ-701', 'Indonesia AirAsia', '12:30:00', '15:00:00'),
        (8, 'SJ-801', 'Sriwijaya Air', '13:45:00', '16:15:00'),
        (9, 'GA-901', 'Garuda Indonesia', '14:00:00', '16:30:00'),
        (10, 'JT-102', 'Lion Air', '15:15:00', '17:45:00'),
        (11, 'QZ-302', 'Indonesia AirAsia', '16:30:00', '19:00:00'),
        (12, 'SJ-402', 'Sriwijaya Air', '17:45:00', '20:15:00'),
        (13, 'GA-502', 'Garuda Indonesia', '18:00:00', '20:30:00'),
        (14, 'JT-602', 'Lion Air', '19:15:00', '21:45:00'),
        (15, 'QZ-702', 'Indonesia AirAsia', '20:30:00', '23:00:00'),
        (16, 'SJ-802', 'Sriwijaya Air', '21:45:00', '00:15:00'),
        (17, 'GA-902', 'Garuda Indonesia', '22:00:00', '00:30:00'),
        (18, 'JT-103', 'Lion Air', '05:30:00', '08:00:00'),
        (19, 'QZ-303', 'Indonesia AirAsia', '23:15:00', '01:45:00'),
        (20, 'SJ-403', 'Sriwijaya Air', '04:45:00', '07:15:00')
    ]
    
    cursor.executemany(
        "INSERT INTO Dim_Penerbangan (ID_Penerbangan, Kode_Penerbangan, Maskapai, Waktu_Berangkat, Waktu_Tiba) VALUES (?, ?, ?, ?, ?)",
        penerbangan_data
    )
    
    conn.commit()
    print(f"Berhasil mengisi {len(penerbangan_data)} record ke Dim_Penerbangan")
    conn.close()

def populate_dim_pesawat():
    """Mengisi tabel Dim_Pesawat dengan data pesawat"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Hapus data lama jika ada
    cursor.execute("DELETE FROM Dim_Pesawat")
    
    pesawat_data = [
        (1, 'PK-GIA', 'Boeing 737-800', 189),
        (2, 'PK-LKS', 'Airbus A320', 180),
        (3, 'PK-AXV', 'Airbus A320', 180),
        (4, 'PK-CMJ', 'Boeing 737-500', 132),
        (5, 'PK-GIB', 'Boeing 777-300ER', 314),
        (6, 'PK-LKT', 'Boeing 737-900ER', 215),
        (7, 'PK-AXW', 'Airbus A320', 180),
        (8, 'PK-CMK', 'Boeing 737-800', 189),
        (9, 'PK-GIC', 'Airbus A330-300', 335),
        (10, 'PK-LKU', 'Boeing 737-800', 189)
    ]
    
    cursor.executemany(
        "INSERT INTO Dim_Pesawat (ID_Pesawat, Nomor_Pesawat, Tipe_Pesawat, Kapasitas) VALUES (?, ?, ?, ?)",
        pesawat_data
    )
    
    conn.commit()
    print(f"Berhasil mengisi {len(pesawat_data)} record ke Dim_Pesawat")
    conn.close()

def populate_dim_kelas_layanan():
    """Mengisi tabel Dim_KelasLayanan dengan data kelas layanan"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Hapus data lama jika ada
    cursor.execute("DELETE FROM Dim_KelasLayanan")
    
    kelas_data = [
        (1, 'Ekonomi', 'Kelas ekonomi standar dengan layanan dasar'),
        (2, 'Bisnis', 'Kelas bisnis dengan layanan premium dan seat yang lebih luas'),
        (3, 'First Class', 'Kelas utama dengan layanan mewah dan fasilitas terbaik')
    ]
    
    cursor.executemany(
        "INSERT INTO Dim_KelasLayanan (ID_KelasLayanan, Nama_Kelas, Deskripsi) VALUES (?, ?, ?)",
        kelas_data
    )
    
    conn.commit()
    print(f"Berhasil mengisi {len(kelas_data)} record ke Dim_KelasLayanan")
    conn.close()

def populate_dim_status_penerbangan():
    """Mengisi tabel Dim_StatusPenerbangan dengan data status"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Hapus data lama jika ada
    cursor.execute("DELETE FROM Dim_StatusPenerbangan")
    
    status_data = [
        (1, 'On Time', 'Penerbangan tepat waktu'),
        (2, 'Delayed', 'Penerbangan mengalami keterlambatan'),
        (3, 'Cancelled', 'Penerbangan dibatalkan'),
        (4, 'Diverted', 'Penerbangan dialihkan ke bandara lain')
    ]
    
    cursor.executemany(
        "INSERT INTO Dim_StatusPenerbangan (ID_StatusPenerbangan, Status, Deskripsi) VALUES (?, ?, ?)",
        status_data
    )
    
    conn.commit()
    print(f"Berhasil mengisi {len(status_data)} record ke Dim_StatusPenerbangan")
    conn.close()

def main():
    """Fungsi utama untuk mengisi semua tabel dimensi"""
    print("Memulai pengisian tabel dimensi...")
    
    populate_dim_waktu()
    populate_dim_lokasi()
    populate_dim_penerbangan()
    populate_dim_pesawat()
    populate_dim_kelas_layanan()
    populate_dim_status_penerbangan()
    
    print("\nSemua tabel dimensi berhasil diisi!")
    
    # Verifikasi data
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    tables = ['Dim_Waktu', 'Dim_Lokasi', 'Dim_Penerbangan', 'Dim_Pesawat', 'Dim_KelasLayanan', 'Dim_StatusPenerbangan']
    
    print("\n=== RINGKASAN DATA DIMENSI ===")
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"{table}: {count} records")
    
    conn.close()

if __name__ == '__main__':
    main()
