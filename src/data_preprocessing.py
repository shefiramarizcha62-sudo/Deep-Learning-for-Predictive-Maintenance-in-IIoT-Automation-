# Data preprocessing script for NASA C-MAPSS dataset

import pandas as pd


def load_cmapss_data(file_path):
    columns = [
        "unit_number", "time_cycle",
        "setting_1", "setting_2", "setting_3",
        "sensor_1", "sensor_2", "sensor_3", "sensor_4", "sensor_5",
        "sensor_6", "sensor_7", "sensor_8", "sensor_9", "sensor_10",
        "sensor_11", "sensor_12", "sensor_13", "sensor_14", "sensor_15",
        "sensor_16", "sensor_17", "sensor_18", "sensor_19", "sensor_20",
        "sensor_21"
    ]

    data = pd.read_csv(
        file_path,
        sep=r"\s+",
        header=None,
        names=columns
    )

    return data


def add_rul_label(train_data):
    max_cycle = train_data.groupby("unit_number")["time_cycle"].max().reset_index()
    max_cycle.columns = ["unit_number", "max_cycle"]

    train_data = train_data.merge(max_cycle, on="unit_number", how="left")
    train_data["RUL"] = train_data["max_cycle"] - train_data["time_cycle"]

    return train_data
