import streamlit as st
import pandas as pd

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon="⚙️",
    layout="wide"
)

# ==================================
# HEADER
# ==================================

st.title("⚙️ Deep Learning for Predictive Maintenance in IIoT")

st.markdown("""
### Remaining Useful Life (RUL) Prediction using Deep Learning

**Dataset:** NASA C-MAPSS FD001

**Domain:** Industrial IoT (IIoT) & Predictive Maintenance

**Objective:** Predict Remaining Useful Life (RUL) of turbofan engines using multivariate sensor time-series data.
""")

# ==================================
# PROJECT OVERVIEW
# ==================================

st.header("📌 Project Overview")

st.write("""
Unexpected machine failures can cause downtime, maintenance costs, and production losses.

This project explores deep learning architectures for Remaining Useful Life (RUL) prediction using NASA C-MAPSS sensor data.

Three architectures were implemented and compared:

- 1D-CNN
- CNN-LSTM
- Transformer
""")

# ==================================
# DATASET INFORMATION
# ==================================

st.header("📂 Dataset Information")

st.write("""
Dataset : NASA C-MAPSS FD001

Number of Engine Units : 100

Sensor Features : 21

Data Type : Multivariate Time-Series

Target Variable : Remaining Useful Life (RUL)
""")

# ==================================
# MODEL COMPARISON
# ==================================

st.header("📊 Model Performance Comparison")

comparison = pd.DataFrame({
    "Model": [
        "1D-CNN",
        "CNN-LSTM",
        "Transformer"
    ],
    "RMSE": [
        14.46,
        13.24,
        16.54
    ],
    "MAE": [
        11.00,
        9.68,
        12.10
    ]
})

st.dataframe(
    comparison,
    use_container_width=True
)

# ==================================
# MODEL ARCHITECTURES
# ==================================

st.header("🧠 Model Architectures")

architecture = pd.DataFrame({

    "Model": [
        "1D-CNN",
        "CNN-LSTM",
        "Transformer"
    ],

    "Architecture": [
        "Conv1D + Dense",
        "Conv1D + LSTM + Dense",
        "Multi-Head Attention + Dense"
    ]
})

st.dataframe(
    architecture,
    use_container_width=True
)

# ==================================
# CHARTS
# ==================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("RMSE Comparison")

    st.bar_chart(
        comparison.set_index("Model")["RMSE"]
    )

with col2:

    st.subheader("MAE Comparison")

    st.bar_chart(
        comparison.set_index("Model")["MAE"]
    )

# ==================================
# BEST MODEL
# ==================================

st.header("🏆 Best Model")

st.success("""
CNN-LSTM achieved the best performance.

RMSE : 13.24

MAE : 9.68
""")

# ==================================
# CNN-LSTM RESULTS
# ==================================

st.header("📈 CNN-LSTM Results")

col1, col2 = st.columns(2)

with col1:

    st.image(
        "results/figures/cnn_lstm_loss.png",
        caption="CNN-LSTM Training Loss"
    )

with col2:

    st.image(
        "results/figures/cnn_lstm_prediction.png",
        caption="CNN-LSTM Prediction"
    )

# ==================================
# TRANSFORMER RESULTS
# ==================================

st.header("🤖 Transformer Results")

col1, col2 = st.columns(2)

with col1:

    st.image(
        "results/figures/transformer_loss.png",
        caption="Transformer Training Loss"
    )

with col2:

    st.image(
        "results/figures/transformer_prediction.png",
        caption="Transformer Prediction"
    )

# ==================================
# CONCLUSION
# ==================================

st.header("📖 Conclusion")

st.write("""
Three deep learning architectures were successfully implemented for Remaining Useful Life prediction.

Experimental results show that CNN-LSTM achieved the best overall performance.

The Conv1D layers effectively extracted local degradation patterns while the LSTM layer captured temporal dependencies within sensor sequences.

Therefore, CNN-LSTM was selected as the final predictive maintenance model.
""")

# ==================================
# REPOSITORY
# ==================================

st.header("🔗 Repository")

st.markdown(
    "[GitHub Repository](https://github.com/shefiramarizcha62-sudo/Deep-Learning-for-Predictive-Maintenance-in-IIoT-Automation-)"
)

# ==================================
# FOOTER
# ==================================

st.markdown("---")

st.caption(
    "Deep Learning for Predictive Maintenance in IIoT Automation | Capstone Project"
)
