#!/bin/env python3

import os
import argparse
from rembg import remove

def remove_background(input_path, output_path):
    try:
        # Check if the output directory exists, create it if not
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Created output directory: {output_dir}")

        with open(input_path, 'rb') as input_file:
            input_data = input_file.read()

        output_data = remove(input_data)

        with open(output_path, 'wb') as output_file:
            output_file.write(output_data)

        print(f"Background removed successfully. Output saved to {output_path}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")

    except Exception as e:
        print(f"Error: {e}")

def generate_default_output_path(input_path):
    # Extract the filename without extension from the input path
    filename = os.path.splitext(os.path.basename(input_path))[0]
    # Generate the default output filename using os.path.join
    return os.path.join("output", f"output_{filename}.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove background from an image using rembg.")
    
    parser.add_argument(
        "input_path",
        type=str,
        help="Path to the input image file."
    )

    parser.add_argument(
        "--output_path",
        type=str,
        help="Path to save the output image file. If not provided, a default filename will be generated."
    )

    args = parser.parse_args()

    # If output_path is not provided, generate a default output filename
    if not args.output_path:
        args.output_path = generate_default_output_path(args.input_path)

    remove_background(args.input_path, args.output_path)
