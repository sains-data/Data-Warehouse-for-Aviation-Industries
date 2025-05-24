-- View untuk menampilkan total pendapatan dan jumlah penumpang per maskapai setiap tahunnya
CREATE VIEW View_Kinerja_Maskapai_Tahunan AS
SELECT
    dw.Tahun,
    dp.Maskapai,
    SUM(fp.Pendapatan) AS TotalPendapatan,
    SUM(fp.Jumlah_Penumpang) AS TotalPenumpang
FROM
    Fakta_Penerbangan fp
JOIN
    Dim_Waktu dw ON fp.ID_Waktu = dw.ID_Waktu
JOIN
    Dim_Penerbangan dp ON fp.ID_Penerbangan = dp.ID_Penerbangan
GROUP BY
    dw.Tahun,
    dp.Maskapai;