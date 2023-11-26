# py-rembg

## Overview

py-rembg is a Python script that utilizes the `rembg` library to simplify background removal in images.


## Usage

1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/your-username/py-rembg.git
   ```

2. **Navigate to the project folder:**
   
   ```bash
   cd py-rembg
   ```

3. **Create a virtual environment (optional but recommended):**
   
   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**
   
   - On Linux/Mac:
   
     ```bash
     source venv/bin/activate
     ```
   
   - On Windows (Command Prompt):
   
     ```bash
     venv\Scripts\activate
     ```

5. **Install dependencies:**
   
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the script with any local file as input:**
   
   ```bash
   python main.py path/to/your/image.jpg
   ```

   - If you want to specify the output directory:
   
     ```bash
     python main.py path/to/your/image.jpg --output_path path/to/your/output_directory/
     ```

   - If you don't specify the output directory, the result will be in the `output` folder.
