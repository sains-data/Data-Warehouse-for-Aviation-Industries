# LAPORAN TUGAS MISI KETIGA  
## PERGUDANGAN DATA RC

### Disusun oleh: Kelompok 19

- Jeremia Susanto (122450022)  
- Feryadi Yulius (122450087)  
- Dede Masita (121450007)  
- Nisrina Nur Afifah (122450052)  
- Dwi Sulistiani (121450079)  



---

## BAB 1: PENDAHULUAN

### Latar Belakang
Industri penerbangan merupakan hal penting dalam perekonomian global karena menghubungkan manusia dan barang antarnegara. [...] untuk meningkatkan efisiensi dan kepuasan pelanggan.

### Rumusan Masalah
1. Bagaimana merancang dan membangun gudang data untuk industri penerbangan menggunakan pendekatan skema bintang (star schema)?  
2. Bagaimana struktur data dalam tabel fakta dan tabel dimensi dapat mendukung proses analisis tren penerbangan?  
3. Bagaimana penerapan gudang data ini dapat membantu pengguna dalam menyajikan informasi yang relevan dan mendukung pengambilan keputusan strategis dalam industri penerbangan?

### Metode Pengembangan Gudang Data
Penjelasan mengenai pendekatan **waterfall** dan **iterative** dalam pengembangan gudang data.

---

## BAB 2: DESAIN KONSEPTUAL

### Identifikasi Proses Bisnis
Beberapa pertanyaan bisnis:
- Berapa rata-rata keterlambatan untuk rute Jakarta–Surabaya per bulan pada tahun 2024?
- Bandara mana yang memiliki total biaya operasional tertinggi dalam 3 bulan terakhir?
- [...] dan lainnya.

### Data
Dataset berisi 1.000 entri data penerbangan dari Jan 2024 - Mei 2025, mencakup waktu, penumpang, biaya, dll.

### Tabel Dimensi dan Fakta

#### Tabel Fakta: `Fakta_Penerbangan`
- **Kunci asing:** waktu, lokasi, penerbangan, pesawat, kelas layanan, status penerbangan
- **Atribut numerik:** jumlah penumpang, pendapatan, jumlah penerbangan

#### Tabel Dimensi:

| Nama Tabel            | Primary Key        | Atribut Deskriptif                                      | Tipe Data            |
|----------------------|--------------------|----------------------------------------------------------|----------------------|
| Dim_Waktu            | ID_Waktu           | Tanggal, Hari, Bulan, Tahun, Kuartal                     | DATE, VARCHAR, INT   |
| Dim_Lokasi           | ID_Lokasi          | Nama_Bandara, Kota, Negara                               | VARCHAR              |
| Dim_Penerbangan      | ID_Penerbangan     | Kode_Penerbangan, Maskapai, Waktu_Berangkat, Waktu_Tiba | VARCHAR, TIME        |
| Dim_Pesawat          | ID_Pesawat         | Nomor_Pesawat, Tipe_Pesawat, Kapasitas                  | VARCHAR, INT         |
| Dim_KelasLayanan     | ID_KelasLayanan    | Nama_Kelas, Deskripsi                                   | VARCHAR, TEXT        |
| Dim_StatusPenerbangan| ID_StatusPenerbangan| Status, Deskripsi                                      | VARCHAR, TEXT        |

---

## BAB 3: DESAIN LOGIKAL DAN FISIK GUDANG DATA

### Translasi ke SQL (Model Relasional)

```sql
CREATE TABLE Dim_Waktu (
    ID_Waktu INT PRIMARY KEY,
    Tanggal DATE,
    Hari VARCHAR(20),
    Bulan INT,
    Tahun INT,
    Kuartal INT
);

CREATE TABLE Dim_Lokasi (...);
CREATE TABLE Dim_Penerbangan (...);
CREATE TABLE Dim_Pesawat (...);
CREATE TABLE Dim_KelasLayanan (...);
CREATE TABLE Dim_StatusPenerbangan (...);

CREATE TABLE Fakta_Penerbangan (
    ID_FaktaPenerbangan INT PRIMARY KEY,
    ID_Waktu INT,
    ID_Lokasi INT,
    ID_Penerbangan INT,
    ID_Pesawat INT,
    ID_KelasLayanan INT,
    ID_StatusPenerbangan INT,
    Jumlah_Penumpang INT,
    Pendapatan BIGINT,
    Jumlah_Penerbangan INT,
    FOREIGN KEY (ID_Waktu) REFERENCES Dim_Waktu(ID_Waktu),
    [...]
);
