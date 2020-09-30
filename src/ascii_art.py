from PIL import Image, ImageOps, ImageDraw, ImageFont
from tqdm import tqdm


class AsciiArtGenerator:
    def __init__(self):
        pass

    def load(self, file_name: str) -> None:
        self.image = Image.open(file_name)
        self.image = ImageOps.grayscale(self.image)
        self.pixels = self.image.load()

        self.width = self.image.width
        self.height = self.image.height

        self.font = ImageFont.truetype("fonts/consola.ttf", size=10)

    @staticmethod
    def _color_to_char(brightness: int) -> str:
        """
        Получаю на вход цвет пикселя, возвращаю соответствуюший ему символ.
        Чем темнее пиксель, тем больше символ занимает места на экране"""

        if brightness < 25:
            return "#"
        elif 25 < brightness < 60:
            return 'O'
        elif 60 < brightness < 100:
            return '?'
        elif 100 < brightness < 140:
            return '!'
        elif 140 < brightness < 180:
            return ';'
        elif 180 < brightness < 220:
            return ':'
        elif 220 < brightness < 235:
            return ','
        elif brightness > 235:
            return '.'
        else:
            return "."

    def create_new_image(self) -> None:
        self.new_image = Image.new('RGB', size=(self.width, self.height), color=(255, 255, 255))
        self.new_image = ImageOps.grayscale(self.new_image)

    def draw_chars(self) -> None:
        idraw = ImageDraw.Draw(self.new_image)

        for x in tqdm(range(0, self.width, 5)):
            for y in range(0, self.height, 5):
                color = self.pixels[x, y]  # узнаём значение цвета пикселя
                char = self._color_to_char(color)
                idraw.text((x, y), char, font=self.font, fill="black")

    def draw_chars_txt(self) -> None:
        self.ascii_image_txt = [[] for _ in range(self.height)]
        for x in tqdm(range(self.width)):
            for y in range(self.height):
                color = self.pixels[x, y]
                self.ascii_image_txt[y].append(self._color_to_char(color))

    def save_to_img(self, file_name: str) -> None:
        """Saves the result of program execution to a file"""
        self.new_image.save(file_name)

    def save_to_txt(self, file_name: str) -> None:
        """Saves the result of program execution to a file"""
        with open(file_name, "w") as f:
            for column in self.ascii_image_txt[::2]:
                f.writelines(''.join(column) + '\n')
