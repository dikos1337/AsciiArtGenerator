from ascii_art import AsciiArtGenerator
from cla import CLA

if __name__ == "__main__":
    cla = CLA()
    args = cla.args

    if args.input_file and args.output_file:
        art = AsciiArtGenerator()
        art.load(args.input_file)
        art._create_new_image()
        art._draw_chars()
        art.save(args.output_file)
    else:
        print("Enter the command line arguments:\n1. Input file\n2. Output file\nExample:")
        print(">python main.py -i car.jpg -o output.png")
