# Analisis Kebutuhan Bisnis dan Teknis Data Warehouse di Industri Penerbangan

## Kelompok: 19 (Penerbangan)

**Anggota:**

* Feryadi Yulius (122450087)
* Jeremia Susanto (122450022)
* Dede Masita (121450007)
* Diana Syafithri (122450141)
* Nisrina Nur Afifah (122450052)
* Dwi Sulistiani (121450079)

---

## 1. Profil Industri Penerbangan & Masalah Bisnis

Industri penerbangan merupakan elemen vital dalam perekonomian global karena menghubungkan manusia dan barang antarnegara. Sektor ini memerlukan investasi besar, tunduk pada regulasi ketat, serta sangat dipengaruhi oleh dinamika ekonomi dan politik. Tantangan utama yang dihadapi maskapai penerbangan meliputi fluktuasi harga bahan bakar, persaingan tarif rendah, serta peraturan keselamatan dan emisi yang semakin ketat. Pandemi COVID-19 menunjukkan kerentanannya terhadap gangguan besar, sehingga mendorong pemanfaatan teknologi seperti sistem pemesanan cerdas dan pemeliharaan berbasis data untuk meningkatkan efisiensi dan kepuasan pelanggan.

---

## 2. Daftar Stakeholder Utama & Tujuan Bisnis

### Stakeholder

| Jabatan                         | Peran                                                                       |
| ------------------------------- | --------------------------------------------------------------------------- |
| CEO (Chief Executive Officer)   | Sponsor utama transformasi digital dan pengawas nilai strategis DW.         |
| COO (Chief Operating Officer)   | Menentukan kebutuhan data operasional, optimasi kru dan ground handling.    |
| CIO (Chief Information Officer) | Mengelola tata kelola data, memilih platform DW, mengawasi arsitektur data. |
| CTO (Chief Technology Officer)  | Menetapkan arsitektur teknis, mendorong inovasi teknologi BI dan ML.        |
| CMO (Chief Marketing Officer)   | Gunakan insight DW untuk promosi, segmentasi pasar, dan evaluasi kampanye.  |

### 2.1 Tujuan Utama Bisnis

1. Menjamin penerbangan aman sesuai standar dan prosedur.
2. Menghasilkan pendapatan yang menutup biaya operasional dan memberi keuntungan.
3. Mengoptimalkan pesawat, kru, dan fasilitas untuk menekan biaya.
4. Memberikan layanan nyaman, tepat waktu, dan responsif.
5. Mengurangi emisi lewat bahan bakar efisien dan teknologi hijau.

### 2.2 Interview Simulasi

Contoh pertanyaan interview:

* Apa saja sumber data utama yang digunakan untuk memantau potensi keterlambatan?
* Bagaimana proses integrasi data real‑time dari berbagai departemen?
* Seberapa cepat tim mengidentifikasi penyebab utama delay?
* Hambatan utama dalam memprediksi ritme check‑in dan boarding?
* Fitur analytics atau alert apa yang diharapkan ditambahkan ke DW?

### 2.3 Studi Kasus: Penanganan Masalah Delay Penerbangan

**Latar Belakang:**
18% penerbangan mengalami delay >30 menit/bulan, disebabkan faktor internal (ground handling lambat) dan eksternal (cuaca, slot bandara).

**Identifikasi Masalah:**

* Data penting tersebar dalam silo.
* Penanganan baru dilakukan setelah delay terjadi.
* Tidak ada model prediktif terpadu.

**Solusi:**

* Rancang skema fact-delays dan dimensi terkait (cuaca, kru, bandara, pesawat).
* Gunakan ML (misal: gradient boosting) untuk prediksi delay.
* Tampilkan heatmap risiko delay dan dashboard notifikasi otomatis.
* Atur ulang shift dan alokasi kru berdasarkan insight.

---

## 3. Fakta & Dimensi

### 3.1 Tabel Fakta

* **Jumlah Penumpang**
* **Pendapatan**
* **Biaya Operasional**
* **Waktu Keberangkatan & Kedatangan**
* **Keterlambatan**

### 3.2 Tabel Dimensi

* **Waktu**: tanggal, bulan, tahun, jam keberangkatan/kedatangan
* **Lokasi**: bandara asal/tujuan, kota, wilayah
* **Penerbangan**: nomor, rute, jenis
* **Pesawat**: registrasi, jenis, usia, konfigurasi kursi
* **Kelas Layanan**: ekonomi, bisnis, dll.
* **Status Penerbangan**: dijadwalkan, aktual, ditunda, dibatalkan

### 3.3 Contoh Star Schema

Diagram Star Schema:

![Diagram Star](sains-data/Kelompok-19-DW-RC/gambar/diagram_star.png)

---

## 4. Sumber Data & Metadata

### 4.1 Sistem Reservasi Tiket

* **Contoh Data:** nomor pemesanan, nama penumpang, rute, harga tiket
* **Metadata:** format (CSV/XML), frekuensi (real-time), kualitas (validitas)

### 4.2 Sistem Manajemen Keberangkatan

* **Contoh Data:** check-in, boarding, bagasi, manifes
* **Metadata:** format (EDIFACT), frekuensi (event-driven), kualitas (konsistensi)

### 4.3 Sistem Kontrol Lalu Lintas Udara

* **Contoh Data:** posisi, kecepatan, nomor penerbangan
* **Metadata:** format (ASTERIX), frekuensi (real-time), kualitas (presisi)

### 4.4 Data Cuaca

* **Contoh Data:** suhu, visibilitas, kondisi awan
* **Metadata:** format (BUFR, GRIB), frekuensi (per jam), kualitas (cakupan)

### 4.5 Data Operasional Bandara

* **Contoh Data:** jadwal, status gerbang, informasi bagasi
* **Metadata:** format (XML/API), frekuensi (real-time), kualitas (ketersediaan)

---

## 5. Kesimpulan

Rancangan Data Warehouse (DW) sangat potensial dalam meningkatkan efisiensi operasional dan mendukung pengambilan keputusan dalam industri penerbangan. Dengan wawasan lebih dalam terhadap performa operasional, perilaku pelanggan, dan tren pasar, DW dapat membantu mengurangi biaya, meningkatkan pendapatan, dan memperbaiki pengalaman pelanggan. DW harus dirancang dengan mempertimbangkan volume dan kecepatan data tinggi, format data yang bervariasi, serta kebutuhan integrasi data real-time. Infrastruktur yang tepat, alat ETL, dan platform analitik diperlukan, didukung oleh tata kelola data yang baik, keamanan, dan kepatuhan.
