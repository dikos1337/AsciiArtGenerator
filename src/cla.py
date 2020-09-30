import argparse


class CLA:
    """Command line arguments class"""
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Some description!')
        self.parser.add_argument('-i', action="store", dest="input_file", type=str)
        self.parser.add_argument('-o', action="store", dest="output_file", type=str)
        self.args = self.parser.parse_args()


if __name__ == "__main__":
    """debug and testing"""
    cla = CLA()
    print(cla.args)
    print(cla.args.input_file)
    print(cla.args.output_file)
