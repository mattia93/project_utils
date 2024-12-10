import os

def check_file_exists(file: str) -> bool:
    """
    Raise a FileNotFoundError if the file does not exist

    Args:
        file (str): file path

    Returns:
        bool: True if the file exists

    Raises:
        FileNotFoundError: if the file does not exist
    """
    if not os.path.exists(file):
        raise FileNotFoundError(f"File {file} not found")
    return True
