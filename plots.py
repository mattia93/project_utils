import matplotlib.pyplot as plt
from PIL import Image
from typing import Tuple


def line_scatter_plot(x: list, y: list, xlabel: str, ylabel: str, title: str, dpi=100) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a line and scatter plot.

    Args:
        x (list): x-axis values.
        y (list): y-axis values.
        xlabel (str): x-axis label.
        ylabel (str): y-axis label.
        title (str): title of the plot.
        dpi (int, optional): Dots per inch. Defaults to 100.

    Returns:
        Tuple[plt.Figure, plt.Axes]: Figure and Axes objects.
    """
    fig, ax = plt.subplots(dpi=dpi)
    ax.plot(x, y)
    ax.scatter(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    fig.autofmt_xdate()
    return fig, ax

def visualize_image(file_path: str, dpi=300) -> Tuple[plt.Figure, plt.Axes]:
    """
    Display an image.

    Args:
        file_path (str): Path to the image file.
        dpi (int, optional): Dots per inch. Defaults to 300.

    Returns:
        Tuple[plt.Figure, plt.Axes]: Figure and Axes objects.
    """
    img = Image.open(file_path)
    fig, ax = plt.subplots(dpi=dpi)
    ax.imshow(img)
    ax.axis('off')
    return fig, ax
