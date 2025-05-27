-- Tabel Dimensi Waktu
CREATE TABLE Dim_Waktu (
    ID_Waktu INT PRIMARY KEY,
    Tanggal DATE,
    Hari VARCHAR(20),
    Bulan INT,
    Tahun INT,
    Kuartal INT
);

-- Tabel Dimensi Lokasi
CREATE TABLE Dim_Lokasi (
    ID_Lokasi INT PRIMARY KEY,
    Nama_Bandara VARCHAR(100),
    Kota VARCHAR(100),
    Negara VARCHAR(100)
);

-- Tabel Dimensi Penerbangan
CREATE TABLE Dim_Penerbangan (
    ID_Penerbangan INT PRIMARY KEY,
    Kode_Penerbangan VARCHAR(20),
    Maskapai VARCHAR(100),
    Waktu_Berangkat TIME,
    Waktu_Tiba TIME
);

-- Tabel Dimensi Pesawat
CREATE TABLE Dim_Pesawat (
    ID_Pesawat INT PRIMARY KEY,
    Nomor_Pesawat VARCHAR(50),
    Tipe_Pesawat VARCHAR(100),
    Kapasitas INT
);

-- Tabel Dimensi Kelas Layanan
CREATE TABLE Dim_KelasLayanan (
    ID_KelasLayanan INT PRIMARY KEY,
    Nama_Kelas VARCHAR(50),
    Deskripsi TEXT
);

-- Tabel Dimensi Status Penerbangan
CREATE TABLE Dim_StatusPenerbangan (
    ID_StatusPenerbangan INT PRIMARY KEY,
    Status VARCHAR(50),
    Deskripsi TEXT
);

-- Tabel Fakta Penerbangan
CREATE TABLE Fakta_Penerbangan (
    ID_FaktaPenerbangan INT PRIMARY KEY,
    ID_Waktu INT,
    ID_Lokasi INT,
    ID_Penerbangan INT,
    ID_Pesawat INT,
    ID_KelasLayanan INT,
    ID_StatusPenerbangan INT,
    Jumlah_Penumpang INT,
    Pendapatan INTEGER,
    Jumlah_Penerbangan INT,
    Biaya_Operasional INTEGER,
    Waktu_Keberangkatan_Aktual DATETIME,
    Waktu_Kedatangan_Aktual DATETIME,
    Keterlambatan_Menit INT,
    FOREIGN KEY (ID_Waktu) REFERENCES Dim_Waktu(ID_Waktu),
    FOREIGN KEY (ID_Lokasi) REFERENCES Dim_Lokasi(ID_Lokasi),
    FOREIGN KEY (ID_Penerbangan) REFERENCES Dim_Penerbangan(ID_Penerbangan),
    FOREIGN KEY (ID_Pesawat) REFERENCES Dim_Pesawat(ID_Pesawat),
    FOREIGN KEY (ID_KelasLayanan) REFERENCES Dim_KelasLayanan(ID_KelasLayanan),
    FOREIGN KEY (ID_StatusPenerbangan) REFERENCES Dim_StatusPenerbangan(ID_StatusPenerbangan)
);