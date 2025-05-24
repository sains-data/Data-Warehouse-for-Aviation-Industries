-- Index pada kolom foreign key di tabel Fakta_Penerbangan
CREATE INDEX idx_fp_id_waktu ON Fakta_Penerbangan(ID_Waktu);
CREATE INDEX idx_fp_id_lokasi ON Fakta_Penerbangan(ID_Lokasi);
CREATE INDEX idx_fp_id_penerbangan ON Fakta_Penerbangan(ID_Penerbangan);
CREATE INDEX idx_fp_id_pesawat ON Fakta_Penerbangan(ID_Pesawat);
CREATE INDEX idx_fp_id_kelaslayanan ON Fakta_Penerbangan(ID_KelasLayanan);
CREATE INDEX idx_fp_id_status ON Fakta_Penerbangan(ID_StatusPenerbangan);

-- Index pada tabel Dim_Waktu untuk query berdasarkan rentang waktu
CREATE INDEX idx_waktu_bulan_tahun ON Dim_Waktu(Bulan, Tahun);

-- Index pada tabel Dim_Penerbangan untuk agregasi per maskapai
CREATE INDEX idx_penerbangan_maskapai ON Dim_Penerbangan(Maskapai);

-- Index pada tabel Dim_StatusPenerbangan untuk laporan berdasarkan status penerbangan
CREATE INDEX idx_status_penerbangan_status ON Dim_StatusPenerbangan(Status);