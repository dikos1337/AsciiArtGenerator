from ascii_art import AsciiArtGenerator
from cla import CLA


class Application:
    def __init__(self):
        self.cla = CLA()
        self.args = self.cla.args

        if self.args.input_file and self.args.output_file:
            art = AsciiArtGenerator()
            art.load(self.args.input_file)
            art._create_new_image()
            art._draw_chars()
            art.save(self.args.output_file)
        else:
            self.main_menu()

    @staticmethod
    def main_menu():
        print("Enter the command line arguments:\n1. Input file\n2. Output file\nExamples:")
        print(">python main.py -i car.jpg -o output.png")
        print(">python main.py -i C:\\python\\ascii\\src\\car.jpg -o output.jpg")


if __name__ == "__main__":
    app = Application()
