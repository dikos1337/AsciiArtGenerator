from ascii_art import AsciiArtGenerator
import sys

if __name__ == "__main__":
    args = sys.argv

    if len(args) == 3:
        input_file = args[1]
        output_file = args[2]

        art = AsciiArtGenerator()
        art.load(input_file)
        art._create_new_image()
        art._draw_chars()
        art.save(output_file)
    else:
        print("Enter the command line arguments:\n1. Input file\n2. Output file\nExample:")
        print(">python main.py car.jpg output.png")