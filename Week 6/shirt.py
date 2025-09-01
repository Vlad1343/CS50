import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) != 3:
        sys.exit("Too few command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_extensions = {'.jpg', '.jpeg', '.png'}
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_extensions or output_ext not in valid_extensions:
        sys.exit("Invalid input or output format")

    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    if not os.path.exists(input_file):
        sys.exit("Input does not exist")

    try:
        shirt = Image.open("shirt.png")
        shirt_size = shirt.size
        input_image = Image.open(input_file)
        input_image = ImageOps.fit(input_image, shirt_size)
        input_image.paste(shirt, (0, 0), shirt)
        input_image.save(output_file)
    except FileNotFoundError:
        sys.exit("File not found")
    except Exception as e:
        sys.exit(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
