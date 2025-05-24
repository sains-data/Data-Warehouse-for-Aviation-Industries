# ✈️ Data Warehouse untuk Industri Penerbangan - Kelompok 19 RC ✈️

Selamat datang di repositori Proyek Data Warehouse untuk Industri Penerbangan! 📂 Repositori ini dikembangkan oleh **Kelompok 19 RC** dan berisi dokumentasi lengkap serta implementasi proyek. Tujuan utama kami adalah merancang dan membangun sebuah data warehouse yang canggih 💡 untuk membantu maskapai penerbangan dalam melakukan analisis data mendalam, meningkatkan efisiensi operasional ⚙️, dan mendukung pengambilan keputusan strategis yang lebih baik 🎯.

Dokumentasi ini secara khusus disusun untuk memenuhi **Tugas Misi Keempat: Implementasi, Reporting, dan Produksi**.

---

## 👥 1. Tim Proyek

* **Kelompok:** 19 RC
* **Anggota:**
    * 👤 Jeremia Susanto (122450022)
    * 👤 Feryadi Yulius (122450087)
    * 👤 Dede Masita (121450007)
    * 👤 Nisrina Nur Afifah (122450052)
    * 👤 Dwi sulistiani (121450079)

---

## 🔎 2. Ringkasan Proyek dan Latar Belakang

Industri penerbangan adalah pilar vital dalam perekonomian global 🌍, menghubungkan manusia dan barang lintas negara. Sektor ini menghadapi berbagai tantangan kompleks seperti investasi besar 💰, regulasi ketat 📜, dinamika ekonomi dan politik, fluktuasi harga bahan bakar ⛽, persaingan tarif yang ketat, serta peraturan keselamatan dan emisi yang semakin meningkat. Pandemi COVID-19 telah menyoroti kerentanan industri ini dan sekaligus mendorong adopsi teknologi inovatif seperti sistem pemesanan cerdas 💻 dan pemeliharaan berbasis data untuk meningkatkan efisiensi dan kepuasan pelanggan 🌟.

Proyek ini berfokus pada perancangan dan pembangunan data warehouse untuk industri penerbangan ✈️ menggunakan pendekatan skema bintang (star schema) ⭐. Tujuannya adalah untuk menyediakan platform yang solid yang mendukung analisis tren penerbangan 📊 dan pengambilan keputusan strategis berdasarkan data yang akurat dan relevan.

---

## 🎯 3. Tujuan dan Ruang Lingkup Sistem

### Tujuan Utama 🏆:
* Merancang dan membangun gudang data untuk industri penerbangan menggunakan skema bintang ⭐.
* Menyusun struktur tabel fakta dan dimensi yang optimal untuk mendukung analisis tren penerbangan secara mendalam 📈.
* Menyajikan informasi yang relevan dan *actionable* untuk mendukung pengambilan keputusan strategis di industri penerbangan 🚀. 
* Meningkatkan efisiensi operasional maskapai ⚙️.
* Meningkatkan pengalaman pelanggan 😊.
* Memperbaiki perencanaan dan pengelolaan rute penerbangan 🗺️.
* Mendukung manajemen risiko yang lebih efektif dan proaktif 🛡️. 
* Memperbaiki pengelolaan sumber daya (armada, SDM) 🧑‍✈️✈️. 

### Ruang Lingkup  Scope 🔍:
* Fokus pada data penerbangan yang mencakup jumlah penumpang, pendapatan, biaya operasional (sebagai data sumber), waktu keberangkatan dan kedatangan aktual, serta data keterlambatan ⏱️. 
* Analisis tren kinerja operasional, aspek finansial 💸, dan kualitas layanan pelanggan.
* Dataset awal terdiri dari 1.000 entri data penerbangan dari Januari 2024 hingga Mei 2025 📅. (Catatan: Ukuran dataset ini kemungkinan untuk tujuan pengembangan awal).

---

## 🛠️ 4. Metodologi

* **Pendekatan Pengembangan:** Menggunakan pendekatan **iterative** 🔄 untuk pengembangan gudang data. Pendekatan ini memungkinkan pengembangan sistem secara bertahap (prototipe kecil) yang dievaluasi dan diperbaiki secara berkelanjutan, memberikan fleksibilitas dalam menyesuaikan sistem terhadap perubahan kebutuhan yang dinamis dan kompleks dalam proyek gudang data.
* **Tools yang Digunakan/Diusulkan:**
    * 🗄️ Database: SQL Server (sesuai Tugas Misi Keempat).
    * 🔄 ETL: Skrip SQL, Python dengan pustaka Pandas, atau tools ETL seperti Talend, Apache NiFi, SSIS.
    * 📊 BI & Reporting: Power BI atau Tableau untuk visualisasi dan dashboard interaktif.
* **Tahapan Proyek (Misi 1-4) 🗺️:**
    1.  📝 Analisis Kebutuhan Bisnis dan Teknis.
    2.  🧩 Desain Konseptual Data Warehouse.
    3.  🧱 Desain Logikal, Fisik Gudang Data, dan Perancangan ETL.
    4.  🚀 Implementasi, Reporting, dan Produksi (dokumentasi ini).

---

## 💡 5. Analisis Kebutuhan (diringkas dari Misi 1 & 2)

### Kebutuhan Bisnis Utama 🚀:
* **Peningkatan Efisiensi Operasional:** Integrasi data jadwal penerbangan, pelacakan pesawat, dan kru untuk analisis performa yang lebih cepat ⏱️, serta pengurangan delay dan biaya operasional 💰.
* **Peningkatan Pengalaman Pelanggan:** Pengumpulan data pemesanan, loyalitas, dan feedback untuk layanan personal dan prediksi kebutuhan pelanggan ❤️.
* **Optimalisasi Perencanaan Rute:** Penyimpanan data historis (load factor, harga, musim) untuk evaluasi performa rute dan strategi harga 🗺️.
* **Manajemen Risiko Efektif:** Penggabungan data insiden dan laporan teknis untuk deteksi pola risiko dan kepatuhan 🛡️. 
* **Pengelolaan Sumber Daya yang Lebih Baik:** Penyediaan data tren armada dan permintaan rute untuk perencanaan investasi dan ekspansi ✈️🧑‍✈️.

### Stakeholder Utama 🤝:
CEO, COO, CIO, CTO, dan CMO, masing-masing dengan peran dan kebutuhan data spesifik untuk pengambilan keputusan strategis dan operasional.

### Contoh Pertanyaan Bisnis yang Akan Dijawab 🤔:
* Berapa rata-rata keterlambatan untuk rute Jakarta–Surabaya per bulan pada tahun 2024? 🕒
* Bandara mana yang memiliki total biaya operasional tertinggi dalam 3 bulan terakhir? 💸 (Membutuhkan data `Biaya_Operasional`)
* Bagaimana tren jumlah penumpang per jenis kelas layanan setiap kuartal? 📈 
* Jenis pesawat apa yang paling sering mengalami delay lebih dari 30 menit? ✈️⏳ (Membutuhkan data `Keterlambatan`) 
* Apakah pesawat yang lebih tua cenderung menyebabkan lebih banyak delay? 🕰️✈️ (Membutuhkan data `Keterlambatan`) 

---

## 🏗️ 6. Desain Gudang Data (diringkas dari Misi 2 & 3)

### Desain Konseptual 🗺️:
* **Model Skema:** Menggunakan **Star Schema** ⭐. Skema ini terdiri dari satu tabel fakta pusat (`Fakta_Penerbangan`) yang terhubung langsung ke beberapa tabel dimensi, dipilih karena kesederhanaan struktur dan kecepatan kueri untuk kebutuhan analitik
* **Tabel Fakta Utama:** `Fakta_Penerbangan` 📊.
    * **Ukuran (Measures) Sesuai DDL:** `Jumlah_Penumpang` 🧑‍🤝‍🧑, `Pendapatan` 💰, `Jumlah_Penerbangan` #️⃣.
    * (Catatan: Sumber data dan proses ETL juga menangani metrik penting lain seperti `Biaya_Operasional` dan `Keterlambatan (menit)`, yang krusial untuk beberapa analisis yang diidentifikasi 
    * **Foreign Keys:** `ID_Waktu` 🔑, `ID_Lokasi` 🔑, `ID_Penerbangan` 🔑, `ID_Pesawat` 🔑, `ID_KelasLayanan` 🔑, `ID_StatusPenerbangan` 🔑.
* **Tabel Dimensi  DIM:**
    * `Dim_Waktu` 📅: Menyimpan atribut waktu (Tanggal, Hari, Bulan, Tahun, Kuartal).
    * `Dim_Lokasi` 📍: Menyimpan atribut lokasi (Nama_Bandara, Kota, Negara).
    * `Dim_Penerbangan` ✈️🏷️: Menyimpan atribut penerbangan (Kode_Penerbangan, Maskapai, Waktu_Berangkat, Waktu_Tiba).
    * `Dim_Pesawat` 🛩️: Menyimpan atribut pesawat (Nomor_Pesawat, Tipe_Pesawat, Kapasitas).
    * `Dim_KelasLayanan` 💺: Menyimpan atribut kelas layanan (Nama_Kelas, Deskripsi).
    * `Dim_StatusPenerbangan` 🚦: Menyimpan atribut status penerbangan (Status, Deskripsi).
* **Granularitas:** Tingkat kedetailan data sangat tinggi, yaitu setiap catatan mewakili satu fakta penerbangan individual 🔎. Dimensi waktu memiliki granularitas hingga level tanggal.
* **Hubungan Antar Tabel:** Relasi *one-to-many* dari setiap tabel dimensi ke tabel fakta `Fakta_Penerbangan` 🔗. 
* **Diagram Skema:** Dapat dilihat pada Gambar 1 dalam laporan Misi Ketiga 🖼️.

### Desain Logikal 🧱:
* Desain konseptual ditranslasikan ke model relasional yang terdiri dari tabel-tabel 📋.
* Tipe data dipilih untuk efisiensi penyimpanan dan akurasi, contohnya INT untuk ID, VARCHAR untuk atribut deskriptif, dan BIGINT untuk `Pendapatan` guna menjaga presisi finansial 💾. 
* Skrip SQL DDL untuk pembuatan tabel (primary keys, foreign keys, atribut, dan tipe data) disediakan dalam file `create_tables.sql` .

### Desain Fisikal ⚙️:
* **Strategi Indexing 🚀:**
    * Indeks dibuat pada kolom-kolom foreign key di tabel `Fakta_Penerbangan`.
    * Indeks juga diterapkan pada kolom-kolom di tabel dimensi yang sering digunakan dalam klausa `WHERE`, `JOIN`, dan `GROUP BY` untuk optimalisasi query (misalnya, `Dim_Waktu(Bulan, Tahun)`, `Dim_Penerbangan(Maskapai)`).
    * Skrip SQL untuk pembuatan indeks disediakan dalam file `create_indexes.sql` atau terintegrasi dalam `create_tables.sql`
* **Optimalisasi Penyimpanan dan Organisasi Data 🗄️:**
    * Desain skema adaptif terhadap volume data dan kebutuhan analisis.
    * Pengelompokan data (sub-partisi manual) berdasarkan kategori tertentu untuk mempercepat pencarian data spesifik.
    * Konfigurasi penyimpanan fisik menggunakan RAID 10 dipertimbangkan untuk redundansi dan performa baca-tulis tinggi 💾✨. 
* **Partisi Tabel dan View 📊:**
    * Partisi pada tabel `Fakta_Penerbangan` berdasarkan kolom `Tahun` (dari `Dim_Waktu`) dipertimbangkan untuk efisiensi analisis tahunan 📅.
    * Penggunaan `VIEW` untuk menyederhanakan query SQL kompleks dan menyajikan data agregat. Contoh: `View_Kinerja_Maskapai_Tahunan` yang menampilkan total pendapatan dan jumlah penumpang per maskapai per tahun 📈.

---

## 🚀 7. Proses Implementasi

### Implementasi Skema Gudang Data di SQL Server 💾:
* **Skema Database:** Struktur tabel fakta dan dimensi diimplementasikan di SQL Server sesuai dengan desain logikal (star schema) ⭐.
* **Script SQL Pembuatan Tabel:**
    * `create_tables.sql` 📜: Berisi perintah DDL untuk membuat semua tabel dimensi (`Dim_Waktu`, `Dim_Lokasi`, `Dim_Penerbangan`, `Dim_Pesawat`, `Dim_KelasLayanan`, `Dim_StatusPenerbangan`) dan tabel fakta (`Fakta_Penerbangan`) beserta primary key, foreign key, dan constraint lainnya.
* **Relasi Antar Tabel:** Didefinisikan menggunakan foreign key pada tabel `Fakta_Penerbangan` yang merujuk ke primary key pada masing-masing tabel dimensi, membentuk star schema 🔗. 
* **Implementasi Indexing:**
    * `create_indexes.sql` (atau bagian dari `create_tables.sql`) ⚡: Berisi perintah SQL untuk membuat indeks pada kolom-kolom yang telah diidentifikasi untuk meningkatkan performa query.

### Proses ETL (Extract, Transform, Load) 🔄:
Proses ETL dirancang untuk mengekstrak data dari berbagai sistem sumber, mengubahnya menjadi format yang sesuai, dan memuatnya ke dalam data warehouse.

1.  **Extract (Ekstraksi Data) 📥:**
    * **Sumber Data Utama:** Sistem Reservasi Penerbangan 🎟️, Sistem Operasional Bandara & ATC 📡, Sistem Manajemen Armada ✈️, Sistem Pelaporan Keuangan 💹. Untuk implementasi awal, data dapat bersumber dari file dataset yang disediakan (Excel/CSV).
    * **Tools:** Python (dengan Pandas) 🐍, SSIS, atau skrip SQL.
    * Data dikumpulkan di *staging area* sebelum transformasi.

2.  **Transform (Transformasi Data) ✨:**
    * **Pembersihan Data:** Menangani data duplikat, memperbaiki inkonsistensi (misalnya, format nama bandara, kode pesawat) 🧹. 
    * **Normalisasi Format:** Konversi format tanggal/waktu ke standar `DATETIME`, konversi tipe data (string ke numerik) 🔄. 
    * **Enrichment dan Mapping:** Menghitung metrik turunan (misalnya, durasi keterlambatan dari selisih jadwal dan waktu aktual ⏳), menghubungkan data transaksi ke ID surrogate di tabel dimensi. Data yang ditransformasi mencakup `Jumlah_Penumpang` 🧑‍🤝‍🧑, `Pendapatan` 💰, `Biaya_Operasional` 💸, `Keterlambatan (menit)` ⏱️

3.  **Load (Pemuatan Data) 📤:**
    * Data yang sudah ditransformasi dimuat ke dalam tabel-tabel di Enterprise Data Warehouse.
    * Tabel dimensi diisi terlebih dahulu, diikuti oleh tabel fakta (`Fakta_Penerbangan`) untuk menjaga integritas referensial.
    * Proses pemuatan dapat dijadwalkan (misalnya, harian) dan mempertimbangkan teknik *incremental load* untuk efisiensi 🗓️. 
    * **Script SQL Pemuatan Data:** `insert_data.sql` atau dilakukan menggunakan wizard SSMS.

---

## 📊 8. Query OLAP / Analitik

Kumpulan query analitik berbasis SQL dirancang untuk melakukan analisis multidimensi terhadap data di warehouse 🧠. Query ini memanfaatkan fungsi agregat (SUM, AVG, COUNT), klausa GROUP BY, JOIN antar tabel fakta dan dimensi, serta ORDER BY.

* **File Script Query:** `analysis_queries.sql` 📜
* **Contoh Query Analitik (berdasarkan pertanyaan bisnis) 🤔:**
    * Menghitung total pendapatan dan jumlah penumpang per maskapai per tahun (menggunakan `View_Kinerja_Maskapai_Tahunan`) 💹🧑‍🤝‍🧑.
    * Menganalisis rata-rata keterlambatan penerbangan per rute per bulan ⏳ (membutuhkan data `Keterlambatan`).
    * Mengidentifikasi bandara dengan biaya operasional tertinggi 💸 (membutuhkan data `Biaya_Operasional`).
    * Melihat tren jumlah penumpang berdasarkan kelas layanan per kuartal 📈.
    * Menentukan jenis pesawat yang paling sering mengalami keterlambatan signifikan ✈️⏱️ (membutuhkan data `Keterlambatan`).

---

## 🎉 9. Hasil Implementasi

Bagian ini akan berisi:
* **Screenshots** 📸 skema database yang telah diimplementasikan di SQL Server.
* **Penjelasan fungsionalitas sistem** ⚙️, termasuk contoh eksekusi query analitik dan hasilnya.
* **Contoh data** ✅ yang ada di dalam tabel fakta dan dimensi setelah proses ETL.
* (Detail akan ditambahkan setelah implementasi penuh dan pengujian.)

---

## 🏛️ 10. Arsitektur Sistem

Arsitektur sistem data warehouse yang dirancang mengikuti alur standar 🌐:
1.  **Data Sources:** Berbagai sistem operasional penerbangan (reservasi, operasional bandara, keuangan, dll.) 📥.
2.  **ETL Process:** Data diekstrak, ditransformasi (dibersihkan, diintegrasikan), dan dimuat ke data warehouse 🔄.
3.  **Enterprise Data Warehouse (EDW):** Penyimpanan data terpusat yang terdiri dari tabel fakta dan tabel dimensi dengan skema bintang ⭐💾.
4.  **Data Marts (Opsional/Pengembangan Lanjutan):** Subset data dari EDW yang difokuskan untuk departemen atau kebutuhan analisis tertentu (misalnya, Operasional, Keuangan, Eksekutif) 🎯. 
5.  **BI Dashboard & Reporting Tools:** Alat seperti Power BI atau Tableau digunakan untuk visualisasi, analisis, dan pelaporan dari data di EDW atau data mart 📊📈. 
6.  **End Users:** Pengguna dari berbagai departemen (Tim Operasi, Eksekutif, Tim Pemasaran, Tim IT) yang memanfaatkan informasi untuk pengambilan keputusan 🧑‍💼👩‍💻.

Diagram arsitektur sistem dapat dilihat pada Gambar 2 dalam laporan Misi Ketiga 🖼️.

---

## 🤔 11. Evaluasi

(Bagian ini akan diisi setelah implementasi dan pengujian menyeluruh)
* **Apa yang Berhasil 👍:**
    * Contoh: Keberhasilan implementasi skema bintang di SQL Server.
    * Contoh: Proses ETL dapat berjalan sesuai jadwal dan memuat data dengan akurat.
* **Apa yang Belum Berhasil/Kekurangan 👎:**
    * Contoh: Kinerja query tertentu masih perlu dioptimalkan.
    * Contoh: Keterbatasan dalam data sumber awal (misalnya, tidak adanya data alasan keterlambatan secara detail).
* **Kendala Teknis 🚧:**
    * Contoh: Keterbatasan sumber daya hardware untuk pemrosesan data volume besar.
    * Contoh: Kompleksitas integrasi data dari sistem legacy.

---

## ➡️ 12. Rencana Pengembangan ke Depan

(Bagian ini akan diisi dengan rencana pengembangan lebih lanjut)
* Integrasi sumber data tambahan (misalnya, data cuaca real-time 🌦️, data feedback pelanggan dari media sosial 💬).
* Implementasi Data Marts yang lebih spesifik untuk kebutuhan analisis tiap departemen 📊.
* Pengembangan model Machine Learning 🤖 untuk analisis prediktif (misalnya, prediksi keterlambatan penerbangan, prediksi permintaan penumpang).
* Peningkatan proses ETL untuk mendukung pemuatan data secara real-time atau near real-time ⚡.
* Pengembangan dashboard interaktif yang lebih komprehensif dan *user-friendly* ✨.
* Mengatasi data gaps yang teridentifikasi, seperti standarisasi dan pencatatan alasan keterlambatan yang lebih detail serta data biaya operasional secara real-time 📝.

---

## 🔗 13. Link Dataset Sumber (Awal)

* Dataset awal yang digunakan dalam pengembangan dapat diakses melalui link berikut: [https://drive.google.com/drive/folders/1oFN4WFO6lZSKh9gCyviUGovs1tBwI9PR](https://drive.google.com/drive/folders/1oFN4WFO6lZSKh9gCyviUGovs1tBwI9PR)

---