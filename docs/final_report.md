# Deep Learning for Predictive Maintenance in IIoT Automation

## 1. Project Overview

This project focuses on Remaining Useful Life (RUL) prediction for predictive maintenance in Industrial Internet of Things (IIoT) environments. The objective is to estimate the remaining operational cycles of turbofan engines before failure occurs using multivariate sensor time-series data.

---

## 2. Problem Statement

Unexpected machine failures in industrial environments can lead to production downtime, increased maintenance costs, and safety risks. Traditional maintenance approaches are often reactive or schedule-based, which may not accurately reflect the actual health condition of machinery.

Predictive maintenance aims to estimate Remaining Useful Life (RUL) using sensor data, enabling maintenance activities to be scheduled before critical failures occur.

---

## 3. Dataset

Dataset:
NASA C-MAPSS FD001

Source:
https://www.kaggle.com/datasets/behrad3d/nasa-cmaps

Characteristics:

- 100 engine units
- 21 sensor measurements
- Multivariate time-series
- Run-to-failure data

Files:

- train_FD001.txt
- test_FD001.txt
- RUL_FD001.txt

---

## 4. Methodology

### Data Preprocessing

Several preprocessing techniques were applied:

#### RUL Labeling

Remaining Useful Life labels were generated using Piece-wise Linear RUL.

#### Feature Scaling

MinMaxScaler normalization was applied.

#### Signal Denoising

Moving Average filtering was used to reduce sensor noise.

#### Sequence Generation

Sliding window sequence generation was applied for deep learning models.

---

## 5. Model Development

### Model 1: 1D-CNN

Conv1D architecture used as baseline.

Performance:

- RMSE: 14.46
- MAE: 11.00

---

### Model 2: CNN-LSTM

Hybrid architecture combining:

- Conv1D
- MaxPooling
- LSTM
- Dense Layers

Performance:

- RMSE: 13.24
- MAE: 9.68

---

### Model 3: Transformer

Self-Attention based architecture using:

- MultiHeadAttention
- LayerNormalization
- Feed Forward Network

Performance:

- RMSE: 16.54
- MAE: 12.10

---

## 6. Model Comparison

| Model | RMSE | MAE |
|---------|---------|---------|
| 1D-CNN | 14.46 | 11.00 |
| CNN-LSTM | 13.24 | 9.68 |
| Transformer | 16.54 | 12.10 |

---

## 7. Discussion

The CNN-LSTM architecture achieved the best overall performance.

The Conv1D layers successfully extracted local sensor degradation patterns, while LSTM captured temporal dependencies within the sequence data.

Although the Transformer architecture was successfully implemented, it did not outperform CNN-LSTM on the FD001 subset under the current configuration.

---

## 8. Conclusion

This project successfully implemented three deep learning architectures for Remaining Useful Life prediction.

Among all evaluated models, CNN-LSTM achieved the best performance:

- RMSE: 13.24
- MAE: 9.68

Therefore, CNN-LSTM is selected as the final predictive maintenance model.
