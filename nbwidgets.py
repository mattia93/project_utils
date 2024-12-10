from ipywidgets import widgets
from typing import List, Tuple, Union

def create_slider(description: str,
                  min_value: int, 
                  max_value: int, 
                  value: Union[Tuple[int, int], None] = None,
                  step: int = 1,
                  continuous_update: bool = False,
                  orientation: str = 'horizontal') -> widgets.IntRangeSlider:
    """
    Create a slider widget

    Args:
        description (str): Label of the slider
        min_value (int): minimum value of the slider
        max_value (int): maximum value of the slider
        value (Union[Tuple[int, int], None], optional): initial value of the slider. Defaults to None.
        step (int, optional): step of the slider. Defaults to 1.    
        continuous_update (bool, optional): Describes whether the slider should update the value as it is changed (True) or only once it is released (False). Defaults to False.
        orientation (str, optional): orientation of the slider. Can be 'horizontal' or 'vertical'. Defaults to 'horizontal'.
    Returns:
        widgets.IntRangeSlider: the slider widget
    """
    if value is None or len(value) != 2:
        value = [min_value, max_value]
    return widgets.IntRangeSlider(
        value= value,
        min=min_value,
        max=max_value,
        step=step,
        description=description,
        disabled=False,
        continuous_update=continuous_update,
        orientation=orientation,
        readout=True,
        readout_format='d',
    )

def create_multi_selection(description: str, 
                           options: List[str], 
                           value: Union[List[str], None]=None) -> widgets.SelectMultiple:
    """
    Create a multiple selection widget

    Args:
        description (str): label of the widget
        options (List[str]): list of options
        value (Union[List[str], None], optional): initial value of the widget. Defaults to None.

    Returns:
        widgets.SelectMultiple: the multiple selection widget
    """
    return widgets.SelectMultiple(
    options=options,
    description=description,
    value = value,
    disabled=False
    )

def create_dropdown(description: str,
                    options: List[str],
                    value: Union[str, None] = None) -> widgets.Dropdown:
    """
    Create a dropdown widget

    Args:
        description (str): label of the widget
        options (List[str]): list of options
        value (Union[str, None], optional): initial value of the widget. Defaults to None.

    Returns:
        widgets.Dropdown:  the dropdown widget
    """
    return widgets.Dropdown(
        options=options,
        value=value,
        description=description,
        disabled=False,
    )


def create_button(description: str, 
                  button_style: str = '',
                  tooltip: str = 'Click me') -> widgets.Button:
    """
    Create a button widget

    Args:
        description (str): label of the button
        button_style (str, optional): style of the button. Can be 'primary', 'success', 'info', 'warning', 'danger' or ''. Defaults to ''.
        tooltip (str, optional): tooltip of the button. Defaults to 'Click me'.

    Returns:
        widgets.Button: the button widget
    """
    return widgets.Button(
        description=description,
        disabled=False,
        button_style=button_style,
        tooltip=tooltip,
    )
