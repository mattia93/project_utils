# Utilities for projects

This module contains utilities that can be useful in various projects.

## Table of contents

- [Modules](#modules)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Modules

The package contains the following modules:

- [config](#config)
- [dataframes](#dataframes)
- [datasets](#datasets)
- [files](#files)
- [nbwidgets](#nbwidgets)
- [plots](#plots)
- [strings](#strings)

### config

Utilities for working with configuration files.

- `get_caller_path`: Get the path of the calling script.

- `set_working_dir`: Set the working directory to the directory of the calling script.

- `get_script_name`: Get the name of the calling script.

- `get_list_from_config`: Get a list from a configuration file.

- `get_config`: Get a configuration object from a configuration file.

### dataframes

Utilities for working with pandas DataFrames.

- `get_unique_from_column`: Get the unique values from a column in a DataFrame.

- `standardize_column`: Standardize a column in a DataFrame.


### datasets

Utilities for working with datasets.

- `get_stratified_array_for_multiclass`:  Create a stratified array for a multiclass dataset.

### files

Utilities for working with files.

- `check_file_exists`: Check if a file exists.

### nbwidgets

Utilities for working with Jupyter notebook widgets.

- `create_slider`: Create a slider widget.

- `create_dropdown`: Create a dropdown widget.

- `create_button`: Create a button widget.

- `create_multi_selection`: Create a multi-selection widget.

### plots

Utilities for plotting.

- `line_scatter_plot`: Create a line scatter plot.

- `visualize_image`: Visualize an image.

### strings

Utilities for working with strings.

- `generate_random_string`: Generate a random string.

## Installation

To install the package copy it to the desired location and run the following command:

```bash
git clone https://github.com/mattia93/project_utils
```

## Usage

To use the package, import the desired module and call the desired function. For example:

```python
from project_utils.dataframes import get_unique_from_column
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

