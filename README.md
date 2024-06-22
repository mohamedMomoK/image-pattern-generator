# Image Pattern Generator

## Description

The **Image Pattern Generator** is a Python tool that processes images from an input folder and creates patterned versions based on a specified layout. The patterned images are saved in a separate output folder. The script includes error handling for invalid image formats and missing files, and offers customizable options such as the number of repetitions per row and column and adjustable image quality.

## Features

- **Batch Processing**: Processes all images in the specified input folder.
- **Customizable Patterns**: Define the number of repetitions per row and column for the pattern layout.
- **Error Handling**: Handles invalid image formats and missing files gracefully.
- **Adjustable Quality**: Specify image quality during saving.

## Requirements

- Python 3
- Pillow library

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/<your-username>/image-pattern-generator.git
    cd image-pattern-generator
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare your images**:
   - Place your input images in the `input_images` folder.

2. **Run the script**:
    ```bash
    python src/main.py <input_folder> <output_folder> <repetitions> [quality]
    ```
   - `<input_folder>`: Path to the folder containing input images.
   - `<output_folder>`: Path to the folder where patterned images will be saved.
   - `<repetitions>`: Number of repetitions per row and column.
   - `[quality]` (optional): Image quality for saving, from 1 (worst) to 95 (best).

### Example

```bash
python src/main.py input_images output_images 3 85
