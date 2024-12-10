import numpy as np

def generate_random_string(length: int = 10) -> str:
    """
    Generate a random string of given length.

    Args:
    - length: int, length of the string to generate

    Returns:
    - str, the generated string
    """
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(np.random.choice(list(allowed_chars), length))