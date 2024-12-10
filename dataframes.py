from typing import List, Union, Tuple
import pandas as pd
from project_utils.strings import generate_random_string
from sklearn.preprocessing import StandardScaler
import numpy as np

def get_unique_from_columns(df: pd.DataFrame, target_column: Union[str, List[str]]) -> List[str]:
    """
    Get unique values from a column or a list of columns.

    Args:
        df (pd.DataFrame): The dataframe.
        target_column (Union[str, List[str]]): The column or columns to get the unique values from. If a list is passed, a new column is created with the values joined by a space.

    Returns:
        List[str]: List of unique values.
    """
    if isinstance(target_column, str):
        return df[target_column].unique()
    else:
        temp_column = df.columns[0]
        while temp_column in df.columns:
            temp_column = generate_random_string()
        new_var = temp_column
        df[new_var] = df[target_column].apply(lambda x: ' '.join(x))
        unique_values = df[temp_column].unique()
        df.drop(columns=[temp_column], inplace=True)
        return unique_values
    

def standardize_column(column: pd.Series, verbose: bool = False) -> Tuple[pd.Series, StandardScaler]:
    """
    Standardize a column.

    Args:
        column (pd.Series): Column to be standardized.
        verbose (bool, optional): Print the mean and standard deviation of the column. Defaults to False.

    Returns:
        Tuple[pd.Series, StandardScaler]: Tuple containing the standardized column and the StandardScaler object.
    """
    scaler = StandardScaler()
    scaler.fit(column.values.reshape(-1, 1))
    if verbose:
        print(f'{column.name}: mean={scaler.mean_}, std={np.sqrt(scaler.var_)}')
    return scaler.transform(column.values.reshape(-1, 1)), scaler