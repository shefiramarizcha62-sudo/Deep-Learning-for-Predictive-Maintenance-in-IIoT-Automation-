# Checkpoint 4 Summary

## Aktivitas yang Dilakukan

* Mengimplementasikan model Transformer berbasis Multi-Head Self-Attention untuk prediksi Remaining Useful Life (RUL).
* Menggunakan pipeline preprocessing yang telah dikembangkan pada checkpoint sebelumnya, meliputi normalisasi data, denoising sinyal, dan pembentukan sequence time-series.
* Melatih model Transformer menggunakan dataset NASA C-MAPSS FD001.
* Melakukan evaluasi performa model menggunakan metrik RMSE dan MAE.
* Membandingkan performa model Transformer dengan model baseline 1D-CNN dan CNN-LSTM.

## Hasil Performa Model

| Model       | RMSE  | MAE   |
| ----------- | ----- | ----- |
| 1D-CNN      | 14.46 | 11.00 |
| CNN-LSTM    | 13.24 | 9.68  |
| Transformer | 16.54 | 12.10 |

## Temuan dan Analisis

Hasil eksperimen menunjukkan bahwa model CNN-LSTM memberikan performa terbaik dibandingkan model 1D-CNN dan Transformer pada dataset NASA C-MAPSS FD001. Meskipun Transformer berhasil memanfaatkan mekanisme Self-Attention untuk mempelajari hubungan antar time-step pada data sensor, performanya masih berada di bawah CNN-LSTM pada konfigurasi dan dataset yang digunakan.

Peningkatan performa dari 1D-CNN ke CNN-LSTM menunjukkan bahwa penambahan komponen LSTM mampu menangkap pola degradasi mesin secara temporal dengan lebih baik. Oleh karena itu, CNN-LSTM dipilih sebagai model terbaik pada tahap penelitian saat ini.

## Bukti Pendukung

* Grafik Training Loss Transformer
* Grafik Prediksi RUL Transformer
* Model Transformer yang telah disimpan (`transformer_model.keras`)
* Hasil evaluasi Transformer (`transformer_results.txt`)
* Tabel perbandingan performa seluruh model

## Progress Saat Ini

Proyek telah berhasil mengimplementasikan dan mengevaluasi tiga arsitektur deep learning untuk prediksi Remaining Useful Life (RUL), yaitu:

1. Baseline 1D-CNN
2. CNN-LSTM Hybrid
3. Transformer berbasis Self-Attention

Berdasarkan hasil eksperimen yang diperoleh, CNN-LSTM menjadi model dengan performa terbaik dan akan digunakan sebagai dasar untuk tahap optimasi lebih lanjut pada pengembangan sistem predictive maintenance.
