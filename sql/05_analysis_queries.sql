-- 05_analysis_queries.sql
-- Kumpulan query analitik untuk Data Warehouse Penerbangan

-- ------------------------------------------------------------------------------------
-- Query 1: Rata-rata keterlambatan untuk rute tertentu per bulan pada tahun tertentu.
-- Contoh: Rute Jakarta (dari Soekarno-Hatta) ke Surabaya (Juanda) pada tahun 2024.
-- Membutuhkan kolom Keterlambatan_Menit di Fakta_Penerbangan
-- ------------------------------------------------------------------------------------
SELECT
    W.Tahun,
    W.Bulan,
    L_Asal.Kota AS Kota_Asal,
    L_Tujuan.Kota AS Kota_Tujuan,
    AVG(FP.Keterlambatan_Menit) AS Rata_Rata_Keterlambatan_Menit
FROM
    Fakta_Penerbangan FP
JOIN
    Dim_Waktu W ON FP.ID_Waktu = W.ID_Waktu
JOIN
    Dim_Lokasi L_Asal ON FP.ID_Lokasi = L_Asal.ID_Lokasi -- Asumsi ID_Lokasi di Fakta adalah Lokasi Keberangkatan
-- Untuk rute, kita mungkin perlu join Dim_Lokasi dua kali jika ada ID_Lokasi_Tujuan di Fakta_Penerbangan,
-- atau jika Dim_Penerbangan menyimpan informasi rute yang bisa di-join.
-- Untuk saat ini, kita asumsikan analisis per bandara keberangkatan atau perlu modifikasi skema/query.
-- Jika Dim_Penerbangan memiliki ID_Lokasi_Asal dan ID_Lokasi_Tujuan, join akan lebih kompleks.
-- Anggap saja kita ingin melihat keterlambatan dari bandara asal:
-- JOIN Dim_Lokasi L_Tujuan ON FP.ID_Lokasi_Tujuan = L_Tujuan.ID_Lokasi (Jika ada kolom ini)
WHERE
    W.Tahun = 2024
    AND L_Asal.Kota = 'Tangerang' -- Contoh: Merepresentasikan Jakarta via Soekarno-Hatta
    -- AND L_Tujuan.Kota = 'Surabaya' -- Jika ada informasi tujuan yang bisa di-filter
    AND FP.Keterlambatan_Menit IS NOT NULL -- Hanya hitung yang ada data keterlambatannya
GROUP BY
    W.Tahun,
    W.Bulan,
    L_Asal.Kota,
    L_Tujuan.Kota -- Jika ada
ORDER BY
    W.Bulan;

-- ------------------------------------------------------------------------------------
-- Query 2: Bandara mana yang memiliki total biaya operasional tertinggi dalam 3 bulan terakhir.
-- Membutuhkan kolom Biaya_Operasional di Fakta_Penerbangan.
-- Anggap ID_Lokasi di Fakta_Penerbangan adalah bandara operasional terkait.
-- ------------------------------------------------------------------------------------
SELECT
    TOP 5 -- Ambil 5 bandara teratas
    L.Nama_Bandara,
    L.Kota,
    SUM(FP.Biaya_Operasional) AS Total_Biaya_Operasional
FROM
    Fakta_Penerbangan FP
JOIN
    Dim_Lokasi L ON FP.ID_Lokasi = L.ID_Lokasi
JOIN
    Dim_Waktu W ON FP.ID_Waktu = W.ID_Waktu
WHERE
    -- Asumsi "3 bulan terakhir" dari tanggal tertentu, misal Mei 2025
    W.Tanggal >= DATEADD(MONTH, -3, '2025-05-31') AND W.Tanggal <= '2025-05-31'
    -- Atau jika ingin dinamis dari tanggal saat ini (GETDATE())
    -- W.Tanggal >= DATEADD(MONTH, -3, GETDATE()) AND W.Tanggal <= GETDATE()
GROUP BY
    L.Nama_Bandara,
    L.Kota
ORDER BY
    Total_Biaya_Operasional DESC;

-- ------------------------------------------------------------------------------------
-- Query 3: Tren jumlah penumpang per jenis kelas layanan setiap kuartal.
-- ------------------------------------------------------------------------------------
SELECT
    W.Tahun,
    W.Kuartal,
    KL.Nama_Kelas,
    SUM(FP.Jumlah_Penumpang) AS Total_Penumpang
FROM
    Fakta_Penerbangan FP
JOIN
    Dim_Waktu W ON FP.ID_Waktu = W.ID_Waktu
JOIN
    Dim_KelasLayanan KL ON FP.ID_KelasLayanan = KL.ID_KelasLayanan
GROUP BY
    W.Tahun,
    W.Kuartal,
    KL.Nama_Kelas
ORDER BY
    W.Tahun,
    W.Kuartal,
    KL.Nama_Kelas;

-- ------------------------------------------------------------------------------------
-- Query 4: Jenis pesawat apa yang paling sering mengalami delay lebih dari 30 menit.
-- Membutuhkan kolom Keterlambatan_Menit di Fakta_Penerbangan dan ID_StatusPenerbangan yang relevan (misal Status 'Tertunda').
-- ------------------------------------------------------------------------------------
SELECT
    P.Tipe_Pesawat,
    COUNT(FP.ID_FaktaPenerbangan) AS Jumlah_Kejadian_Delay_Lebih_30_Menit
FROM
    Fakta_Penerbangan FP
JOIN
    Dim_Pesawat P ON FP.ID_Pesawat = P.ID_Pesawat
JOIN
    Dim_StatusPenerbangan SP ON FP.ID_StatusPenerbangan = SP.ID_StatusPenerbangan
WHERE
    SP.Status = 'Tertunda' -- Filter hanya untuk status tertunda
    AND FP.Keterlambatan_Menit > 30 -- Filter keterlambatan lebih dari 30 menit
GROUP BY
    P.Tipe_Pesawat
ORDER BY
    Jumlah_Kejadian_Delay_Lebih_30_Menit DESC;

-- ------------------------------------------------------------------------------------
-- Query 5: Apakah pesawat yang lebih tua cenderung menyebabkan lebih banyak delay?
-- Ini lebih kompleks dan mungkin memerlukan analisis statistik atau pengelompokan usia pesawat.
-- Sebagai contoh sederhana, kita bisa melihat rata-rata keterlambatan per tipe pesawat
-- (Jika Dim_Pesawat memiliki kolom Usia_Pesawat atau Tanggal_Pembuatan).
-- Asumsi Dim_Pesawat memiliki kolom Usia_Pesawat (dalam tahun).
-- Membutuhkan kolom Keterlambatan_Menit di Fakta_Penerbangan.
-- ------------------------------------------------------------------------------------
-- Langkah 1: Jika Dim_Pesawat tidak punya Usia_Pesawat, tapi punya Tahun_Pembuatan
-- ALTER TABLE Dim_Pesawat ADD Usia_Pesawat INT;
-- UPDATE Dim_Pesawat SET Usia_Pesawat = YEAR(GETDATE()) - Tahun_Pembuatan; -- (Jika ada Tahun_Pembuatan)

-- Query jika Usia_Pesawat ada di Dim_Pesawat:
SELECT
    P.Tipe_Pesawat,
    -- P.Usia_Pesawat, -- Jika ingin melihat per usia spesifik
    CASE
        WHEN P.Usia_Pesawat <= 5 THEN '0-5 Tahun'
        WHEN P.Usia_Pesawat > 5 AND P.Usia_Pesawat <= 10 THEN '6-10 Tahun'
        WHEN P.Usia_Pewasat > 10 AND P.Usia_Pesawat <= 15 THEN '11-15 Tahun'
        ELSE '>15 Tahun'
    END AS Kelompok_Usia_Pesawat,
    AVG(FP.Keterlambatan_Menit) AS Rata_Rata_Keterlambatan_Menit,
    COUNT(FP.ID_FaktaPenerbangan) AS Jumlah_Penerbangan_Diobservasi
FROM
    Fakta_Penerbangan FP
JOIN
    Dim_Pesawat P ON FP.ID_Pesawat = P.ID_Pesawat
WHERE
    FP.Keterlambatan_Menit IS NOT NULL
    AND P.Usia_Pesawat IS NOT NULL -- Pastikan data usia ada
GROUP BY
    P.Tipe_Pesawat,
    CASE
        WHEN P.Usia_Pesawat <= 5 THEN '0-5 Tahun'
        WHEN P.Usia_Pesawat > 5 AND P.Usia_Pesawat <= 10 THEN '6-10 Tahun'
        WHEN P.Usia_Pewasat > 10 AND P.Usia_Pesawat <= 15 THEN '11-15 Tahun'
        ELSE '>15 Tahun'
    END
ORDER BY
    Kelompok_Usia_Pesawat,
    Rata_Rata_Keterlambatan_Menit DESC;

-- ------------------------------------------------------------------------------------
-- Query 6: Menggunakan View yang sudah dibuat (View_Kinerja_Maskapai_Tahunan)
-- Untuk melihat total pendapatan dan jumlah penumpang per maskapai per tahun.
-- ------------------------------------------------------------------------------------
SELECT
    Tahun,
    Maskapai,
    TotalPendapatan,
    TotalPenumpang
FROM
    View_Kinerja_Maskapai_Tahunan
ORDER BY
    Tahun,
    Maskapai;


-- ------------------------------------------------------------------------------------
-- Query 7: Jumlah Penerbangan per Maskapai per Bulan
-- ------------------------------------------------------------------------------------
SELECT
    W.Tahun,
    W.Bulan,
    P.Maskapai,
    SUM(FP.Jumlah_Penerbangan) AS Total_Penerbangan_Maskapai_Bulanan -- Atau COUNT(FP.ID_FaktaPenerbangan) jika Jumlah_Penerbangan di fakta = 1 per baris
FROM
    Fakta_Penerbangan FP
JOIN
    Dim_Waktu W ON FP.ID_Waktu = W.ID_Waktu
JOIN
    Dim_Penerbangan P ON FP.ID_Penerbangan = P.ID_Penerbangan
GROUP BY
    W.Tahun,
    W.Bulan,
    P.Maskapai
ORDER BY
    W.Tahun,
    W.Bulan,
    P.Maskapai;