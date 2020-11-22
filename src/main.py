from ascii_art import AsciiArtGenerator
from cla import CLA


class Application:
    def __init__(self):
        self.cla = CLA()
        self.args = self.cla.args
        self.output_is_txt = self.args.output_file[-4:] == ".txt"

        if (
            all((self.args.input_file, self.args.output_file))
            and self.args.color_bool is False and not self.output_is_txt
        ):
            self.default_pipeline()

        elif (
            all((self.args.input_file, self.args.output_file))
            and self.output_is_txt is True
        ):
            self.txt_output_pipeline()

        elif (
            all((self.args.input_file, self.args.output_file, self.args.color_bool))
            and not self.output_is_txt
        ):
            self.color_pipeline()

        else:
            self.main_menu()

    def default_pipeline(self):
        art = AsciiArtGenerator()
        art.load(self.args.input_file)
        art.create_new_image()
        art.draw_chars()
        art.save_to_img(self.args.output_file)

    def color_pipeline(self):
        art = AsciiArtGenerator()
        art.load(self.args.input_file)
        art.create_new_image(color=True)
        art.draw_color_chars()
        art.save_to_img(self.args.output_file)

    def txt_output_pipeline(self):
        art = AsciiArtGenerator()
        art.load(self.args.input_file)
        art.draw_chars_txt()
        art.save_to_txt(self.args.output_file)

    @staticmethod
    def main_menu():
        print(
            "Enter the command line arguments:\n1. Input file\n2. Output file\nExamples:"
        )
        print(">python main.py -i car.jpg -o output.png")
        print(">python main.py -i C:\\python\\ascii\\src\\car.jpg -o output.jpg")


if __name__ == "__main__":
    app = Application()
