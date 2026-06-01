# Deep Learning for Predictive Maintenance in IIoT Automation

This project focuses on predictive maintenance for Industrial IoT using the NASA C-MAPSS dataset. The objective is to predict the Remaining Useful Life (RUL) of turbofan engines based on multivariate sensor time-series data.

## Dataset
NASA C-MAPSS dataset:
https://www.kaggle.com/datasets/behrad3d/nasa-cmaps

## Team
Team B

## Project Theme
Industrial IoT (IIoT) & Predictive Maintenance

## Initial Plan
1. Understand the dataset structure.
2. Perform exploratory data analysis.
3. Calculate RUL labels.
4. Build baseline models.
5. Develop deep learning models for RUL prediction.
6. Evaluate model performance using MAE/RMSE.

## Current Progress

- Dataset Exploration ✅
- RUL Labeling ✅
- Preprocessing Pipeline ✅
- Signal Denoising ✅
- Sequence Generation ✅
- Baseline 1D-CNN Model ✅
- CNN-LSTM Hybrid ✅
- Transformer Model ✅
- Model Comparison Analysis ✅
- Final Report Documentation ✅

## Experimental Results

| Model | RMSE | MAE |
|---------|---------|---------|
| 1D-CNN | 14.46 | 11.00 |
| CNN-LSTM | 13.24 | 9.68 |
| Transformer | 16.54 | 12.10 |

## Best Model

CNN-LSTM achieved the best performance and was selected as the final predictive maintenance model.

## Repository Structure

```text
data/
docs/
notebooks/
results/
src/
````
## Baseline Model Performance

| Model | RMSE | MAE |
|---|---|---|
| 1D-CNN | 14.46 | 11.00 |
| CNN-LSTM | 13.24 | 9.68 |
