## FD001 Dataset Exploration

Pada tahap awal, tim menggunakan subset FD001 dari NASA C-MAPSS dataset. Dataset ini terdiri dari data training, data testing, dan file RUL aktual untuk data testing.

Aktivitas yang telah dilakukan:
1. Membaca file train_FD001.txt, test_FD001.txt, dan RUL_FD001.txt.
2. Memberikan nama kolom pada dataset, yaitu unit number, time cycle, operational settings, dan 21 sensor measurements.
3. Mengecek ukuran dataset dan jumlah unit mesin.
4. Mengecek missing values.
5. Menghitung label Remaining Useful Life (RUL) pada data training.
6. Membuat visualisasi awal tren RUL dan sensor untuk salah satu mesin.

Hasil awal menunjukkan bahwa dataset dapat digunakan untuk membangun model prediksi Remaining Useful Life berbasis data sensor time-series.
