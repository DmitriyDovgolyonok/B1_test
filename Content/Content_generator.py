import datetime as dt
import random
import numpy as np

from Utils.Consts import END_DATE, START_DATE, RU_CHARS, EN_CHARS
"""
Class for generating content inside files
"""
class ContentGenerator:
    def __init__(self, number_of_rows: int):
        self.number_of_rows = number_of_rows

    def get_content(self):
        content = ""
        for i in range(self.number_of_rows):
            content += self.get_row() + "\n"
        return content.strip("\n")

    def get_row(self):
        row = f"{self.random_date(START_DATE, END_DATE).strftime('%Y.%m.%d')}||" \
              f"{self.random_letters(EN_CHARS, 10)}||" \
              f"{self.random_letters(RU_CHARS, 10)}||" \
              f"{self.random_int()}||" \
              f"{self.random_float()}||"
        return row

    @staticmethod
    def random_date(start_date: dt.date, end_date: dt.date) -> dt.date:
        return start_date + (end_date - start_date) * random.random()

    @staticmethod
    def random_letters(symbols: list, size: int) -> str:

        random_letters = np.random.choice(symbols, size)
        random_letters_str = "".join(random_letters)
        return random_letters_str

    @staticmethod
    def random_int() -> int:
        return random.randrange(1, 100000)

    @staticmethod
    def random_float() -> float:
        return round(random.uniform(1, 2), 8)
