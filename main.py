from File.File_generator import FileGenerator
from Utils.Consts import DIRECTORY_NAME
from File.Merge import merge_and_delete
from db import task4


def task1():
    test = FileGenerator(number_of_files = 100, number_of_rows = 10000)
    test.write(DIRECTORY_NAME)


def task2():
    string_to_delete = str(input("\nInput string to delete -> "))
    merge_and_delete(DIRECTORY_NAME, string_to_delete)


def main():
    task1()
    task2()
    task4()


if __name__ == '__main__':
    main()
