import random


class RandWord:
    def __init__(self):
        self.file_loc = "src/words.txt"
        self.words_txt()
        self.random_number()

    def words_txt(self):
        with open(self.file_loc, 'r') as file:
            self.words = file.readlines()
        self.words_lines = len(self.words)

    def random_number(self):
        self.random_number = random.randint(0, self.words_lines)

    def __str__(self):
        return str(self.words[self.random_number].strip())
