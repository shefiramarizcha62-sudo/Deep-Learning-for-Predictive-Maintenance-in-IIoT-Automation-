# Checkpoint 4 Summary

## Activities

* Implemented a Transformer-based model using Multi-Head Self-Attention for Remaining Useful Life (RUL) prediction.
* Reused the preprocessing pipeline developed in previous checkpoints, including normalization, denoising, and sequence generation.
* Trained the Transformer model on the NASA C-MAPSS FD001 dataset.
* Evaluated model performance using RMSE and MAE metrics.
* Compared Transformer performance with the baseline 1D-CNN and CNN-LSTM models.

## Model Performance

| Model       | RMSE  | MAE   |
| ----------- | ----- | ----- |
| 1D-CNN      | 14.46 | 11.00 |
| CNN-LSTM    | 13.24 | 9.68  |
| Transformer | 16.54 | 12.10 |

## Findings

The CNN-LSTM model achieved the best performance among all evaluated architectures. Although the Transformer model successfully captured temporal dependencies through the self-attention mechanism, its performance was lower than CNN-LSTM on the NASA C-MAPSS FD001 dataset.

## Supporting Results

* Transformer training loss visualization
* Transformer prediction visualization
* Saved Transformer model (`transformer_model.keras`)
* Experimental metrics stored in `transformer_results.txt`

## Current Progress

The project has successfully implemented and evaluated three deep learning architectures for Remaining Useful Life (RUL) prediction:

1. Baseline 1D-CNN
2. CNN-LSTM Hybrid
3. Transformer with Self-Attention

Based on the current experiments, CNN-LSTM is the best-performing model and will be considered the primary candidate for further optimization and final deployment.
