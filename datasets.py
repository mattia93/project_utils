import pandas as pd
import numpy as np
from typing import Tuple
from sklearn.preprocessing import StandardScaler


def get_stratified_array_for_multiclass(df: pd.DataFrame, max_bins: int = 10) -> np.ndarray:
    """
    Create a stratified array for a multiclass dataset.

    Args:
        df (pd.DataFrame): Dataframe with the columns to be stratified. Each column is a feature.
        max_bins (int, optional): Maximum number of bins to create. Defaults to 10.

    Returns:
        np.ndarray: Array with the stratified labels.
    """
    label = ['' for _ in range(df.shape[0])]
    for column in df.columns:
        number_bins = max_bins
        if df[column].value_counts().shape[0] < max_bins:
            number_bins = df[column].value_counts().shape[0]
        bins = np.linspace(0, df.shape[0]-1, number_bins, dtype=int)
        bins = [df[column].sort_values().reset_index(drop=True)[int(i)] for i in bins]
        bin_index = np.digitize(df[column], bins)
        for i in range(df.shape[0]):
            label[i] += str(bin_index[i]) + '_'
    return np.asanyarray(label)