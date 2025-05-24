# Analisis Kebutuhan Bisnis dan Teknis Data Warehouse di Industri Penerbangan

**Kelompok 19**  
Anggota:
- Jeremia Susanto 122450022  
- Feryadi Yulius 122450087  
- Dede Masita 121450007  
- Nisrina Nur Afifah 122450052  
- Dwi Sulistiani 121450079  

## Ringkasan Kebutuhan dari Misi

Berikut adalah ringkasan kebutuhan yang diidentifikasi untuk pengembangan Data Warehouse (DW) di industri penerbangan:

* **Meningkatan efisiensi operasional**  
    * DW mengintegrasikan data jadwal penerbangan, pelacakan pesawat, dan kru ke satu sistem terpusat.  
    * Dengan ETL harian/real-time, analisis performa dan rotasi kru jadi lebih cepat.  
    * Visualisasi dengan tools seperti Power BI memungkinkan pengurangan delay dan biaya operasional.

* **Meningkatkan pengalaman pelanggan**  
    * DW mengumpulkan data pemesanan, loyalty, media sosial, dan feedback.  
    * OLAP mendukung segmentasi pelanggan untuk layanan personal seperti rekomendasi rute dan notifikasi otomatis.  
    * DW juga mendukung integrasi ML untuk prediksi kebutuhan pelanggan.

* **Meningkatkan perencanaan dan pengelolaan rute penerbangan**  
    * DW menyimpan data load factor, harga, dan musim dari tahun ke tahun.  
    * Query multidimensi membantu evaluasi performa rute dan strategi pricing.  
    * Star schema dan analitik historis mendukung optimasi rute dan yield management.

* **Manajemen risiko yang lebih efektif**  
    * DW menggabungkan data insiden, sertifikasi kru, dan laporan teknis.  
    * Data mining digunakan untuk mendeteksi pola risiko.  
    * Laporan berbasis standar audit otomatis memudahkan kepatuhan, dan threshold analitik memberi notifikasi dini risiko keselamatan.

* **Perbaikan dalam pengelolaan sumber daya**  
    * DW menyediakan data tren armada dan permintaan rute.  
    * OLAP dan prediksi membantu perencanaan investasi armada, SDM, dan ekspansi.  
    * DW mendukung simulasi ROI dan evaluasi strategi berbasis data jangka panjang.

## 2. Skema Konseptual Multidimensi

### Pemilihan Skema:
Jenis Skema yang digunakan adalah **Star Schema**.  
Skema ini memiliki satu tabel fakta utama `Fakta_Penerbangan` yang langsung terhubung ke beberapa tabel dimensi. Tidak ada pemecahan pada tabel dimensi (misalnya, dimensi lokasi tidak dipisah menjadi Negara, Kota, dan sebagainya), dalam star schema semua informasi tersebut disimpan dalam satu tabel dimensi saja agar struktur tetap sederhana dan kueri tetap cepat, sesuai dengan kebutuhan analitik real-time di industri penerbangan, performa penerbangan, dan layanan pelanggan.

![Diagram Star](sains-data/Kelompok-19-DW-RC/gambar/diagram_star.png)

*Keterangan: Gambar di atas adalah skema konseptual multidimensi awal.*

### Identifikasi Fakta:
Pada tabel fakta penerbangan berisi ukuran (measures) yang bersifat kuantitatif dan dapat dianalisis untuk manajemen pendapatan, perencanaan kapasitas penerbangan, pemantauan performa layanan, dan sebagainya.  
Kolom-kolomnya meliputi:
* Jumlah penumpang
* Jumlah bagasi
* Pendapatan

### Identifikasi Dimensi
* **Dimensi Waktu:** Informasi tanggal, hari, bulan, kuartal, tahun.  
* **Dimensi Status Penerbangan:** Status seperti “Tepat Waktu”, “Tertunda”, dan “Dibatalkan”.  
* **Dimensi Kelas Layanan:** Kelas layanan seperti Ekonomi, Bisnis, First.  
* **Dimensi Pesawat:** Jenis, kapasitas, dan informasi lain dari pesawat (produsen, tahun pembuatan, serta spesifikasi teknis pesawat).  
* **Dimensi Penerbangan:** Informasi kode penerbangan, maskapai, dll.  
* **Dimensi Lokasi:** Lokasi asal dan tujuan penerbangan (bandara, kota, negara).  

## 3. Definisi Granularitas
Granularitas atau tingkat kedetailan data sangat tinggi. Data disimpan dalam satu waktu penerbangan dengan mencatat penerbangan secara lengkap.

* **Dimensi Waktu:** detail waktu sampai ke tanggal.  
* **Dimensi Lokasi:** asal & tujuan (kota & bandara).  
* **Dimensi Status Penerbangan:** status tunggal per penerbangan.  
* **Dimensi Kelas Layanan:** ekonomi/bisnis dsb.  
* **Dimensi Penerbangan:** kode dan maskapai.  
* **Dimensi Pesawat:** tipe dan kapasitas.

## 4. Hubungan Antar Tabel
Hubungan antar tabel dimensi dalam ERD ini terhubung ke tabel fakta penerbangan melalui relasi **one to many**.  
Artinya, satu entri di tabel dimensi dapat digunakan oleh banyak entri di tabel fakta. Sebaliknya, setiap baris dalam tabel fakta hanya satu nilai dari masing-masing dimensi.

![ERD](sains-data/Kelompok-19-DW-RC/gambar/diagram_star2.png)
*Keterangan: Gambar di atas adalah ERD yang menunjukkan hubungan antar tabel.*

## 4. Penjelasan Tiap Komponen (Lanjutan)

### Tabel Fakta
Tabel ini menyimpan data utama dari setiap penerbangan.  
Kolom-kolom:
* **Jumlah_Penumpang** (orang)  
* **Pendapatan** (Rp)  
* **Biaya_Operasional** (Rp)  
* **Waktu_Keberangkatan dan Waktu_Kedatangan**  
* **Keterlambatan** (menit)

### Tabel Dimensi
* **Dim_Waktu:** Tanggal, Bulan, dan Tahun.  
* **Dim_Lokasi:** Bandara_Asal dan Bandara_Tujuan.  
* **Dim_Penerbangan:** Nomor_Penerbangan dan Rute.  
* **Dim_Pesawat:** PesawatID, Nomor_Registrasi, dan Jenis pesawat.  
* **Dim_KelasLayanan:** Nama_Kelas dan Harga_Kelas.  
* **Dim_StatusPenerbangan:** Status dan Alasan_Keterlambatan.

### Query
Contoh query yang dapat dijawab:
- Rata-rata keterlambatan rute Jakarta–Surabaya per bulan 2024  
- Bandara dengan biaya operasional tertinggi dalam 3 bulan  
- Tren jumlah penumpang per kelas layanan kuartalan  
- Jenis pesawat paling sering delay > 30 menit  
- Apakah pesawat tua lebih sering delay?

## 5. Justifikasi Desain Konseptual

### Kesesuaian dengan Kebutuhan Bisnis
Star schema dengan fakta `Flight_Operations` dan dimensi seperti Waktu, Rute, Armada, dan Pelanggan mendukung analisis delay, pendapatan, dan segmen pelanggan.

### Optimalisasi Performa
Struktur star schema meminimalkan jumlah join dan mempercepat query. Fakta hanya menyimpan foreign key dan nilai numerik. Index dan partitioning mempercepat akses.

### Fleksibilitas dan Skalabilitas
Desain modular, mudah diperluas (misalnya menambah dimensi Cuaca), granularitas tinggi memungkinkan analisis multi-level.

### Trade-off dalam Desain
Ada redundansi seperti data kota berulang, tetapi ditebus oleh kecepatan query dan kemudahan pengguna bisnis.

## 6. Kesesuaian dengan Sumber Data

### Identifikasi Sumber Data:
* **Sistem Reservasi Penerbangan**  
* **Sistem Operasional Penerbangan**  
* **Sistem Manajemen Bandara/ATC**  
* **Sistem Manajemen Armada**  
* **Sistem Pelaporan Keuangan**  

### Mapping Data:
* Data operasional dan keuangan → `Fakta_Penerbangan`  
* Tanggal → `Dim_Waktu`  
* Lokasi asal & tujuan → `Dim_Lokasi`  
* Nomor penerbangan → `Dim_Penerbangan`  
* Detail pesawat → `Dim_Pesawat`  
* Kelas layanan → `Dim_KelasLayanan`  
* Status dan alasan keterlambatan → `Dim_StatusPenerbangan`

### Ketersediaan Data:
Sebagian besar data tersedia, tetapi ada kesenjangan seperti alasan keterlambatan tidak lengkap dan biaya operasional tidak real-time.

### Kualitas Data:
* **Akurasi** penting dalam keuangan dan performa  
* **Kelengkapan** diperlukan untuk analisis valid  
* **Konsistensi** dijaga dengan ETL dan validasi
