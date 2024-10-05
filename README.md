# NumPost

NumPost is a Python script that converts images into a NumWorks calculator-compatible script. The output script draws an image using a specific color palette, making it easy to display graphics on your calculator.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
  - [Python Version](#python-version)
  - [Executable Version](#executable-version)
- [Usage](#usage)
  - [Using the Python Script](#using-the-python-script)
  - [Using the Executable (NumPost.exe)](#using-the-executable-numpostexe)
- [How to Build the Executable](#how-to-build-the-executable)
- [Examples](#examples)
- [License](#license)
- [Developer](#developer)

## Features

- Converts images to a NumWorks-compatible format.
- Customizable color palette with 16 colors.
- Easy integration with NumWorks calculator scripts.
- Resizes images to fit the calculator screen (80x60 pixels).

## Requirements

### Python Version

If you are using the Python script, the following requirements must be met:

- **Python**: This project requires Python (version 3.x).
- **Pillow Library**: This library is needed for image processing. You can install it using:
  ```bash
  pip install Pillow
  ```

### Executable Version

If you are using the precompiled executable (NumPost.exe), no installations or libraries are required. Simply download and run it on any Windows machine.

### Website Version

There is also a web-based version of NumPost available. However, the output may differ due to the use of different libraries, and the overall image quality is generally better in the Python and executable versions. For optimal results, it's recommended to use the Python script or the executable.

## Usage

### Using the Python Script

To use the Python script, follow these steps:

1. Ensure you have Python and Git installed on your system.
2. Clone the repository
  ```bash
  git clone https://github.com/Soleil-des-chats/NumPost.git
  ```
3. Then navigate into the folder
   ```bash
   cd NumPost
   ```
4. Install the Pillow library (if running the script):
   ```bash
   pip install Pillow
   ```
5. Run the script with the following command:
   ```bash
   python generate_script.py <image_path> <output_path>
   ```
   - Replace `<image_path>` with the path to your image file.
   - Replace `<output_path>` with the desired output file path for the generated script.

### Using the Executable (NumPost.exe)

If you prefer not to deal with libraries or Python installations, you can use the precompiled executable `NumPost.exe`:

1. Download `NumPost.exe` from the [Releases](https://github.com/YourUsername/NumPost/releases) section of this repository.
2. Open a command prompt (Windows).
3. Navigate to the directory containing `NumPost.exe`.
4. Run the executable with the following command:
   ```bash
   NumPost <image_path> <output_path>
   ```
   - Replace `<image_path>` with the path to your image file and `<output_path>` with the desired output path.

## How to Build the Executable

To build the executable yourself, follow these steps:

1. Install [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/) if you haven't already:
   ```bash
   pip install pyinstaller
   ```
2. Run the following command to create the executable:
   ```bash
   pyinstaller --onefile generate_script.py
   ```
3. After the build completes, find `NumPost.exe` in the `dist` folder.

## Examples

Here are a few examples of how to use the script and executable:

### Example 1: Using the Python Script

```bash
python generate_script.py path/to/image.png path/to/output_script.py
```

### Example 2: Using the Executable

```bash
NumPost path/to/image.png path/to/output_script.py
```

Both commands will convert the image located at `path/to/image.png` into a script that can be run on the NumWorks calculator, saving it as `output_script.py`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developer

This project is developed by **Titimousse**. 
