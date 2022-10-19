from Content.Content_generator import ContentGenerator
from Utils.Console import progress
import os
"""
Class for generating 100 files
"""

class FileGenerator:
    def __init__(self, number_of_rows: int, number_of_files: int):
        self.number_of_files = number_of_files
        self.row_generator = ContentGenerator(number_of_rows)

    def write(self, link: str):
        if not os.path.isdir(link):
            os.mkdir(link)
            print(f'Directory {link} was created')

        for i in range(self.number_of_files):
            with open(f'{link}/{i}.txt', 'w') as file:
                file.write(self.row_generator.get_content())
            progress(i, self.number_of_files)
            
