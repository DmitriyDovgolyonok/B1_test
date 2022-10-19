import os

"""
Function to implement merge and remove substring from files
"""
def merge_and_delete(files_dir, string: str, final_dir = 'merge_result') -> int:
    if not os.path.isdir(final_dir):
        os.mkdir(final_dir)
        print(f'Directory {final_dir} was created')

    merge_path = os.path.join(final_dir, "merge.txt")
    count = 0

    with open(merge_path, "w", encoding = "latin-1") as f:
        file_names_list = os.listdir(files_dir)
        for file_name in file_names_list:
            file_path = os.path.join(files_dir, file_name)
            with open(file_path, "r", encoding = "latin-1") as fr:
                for row in fr:
                    if (string is not None) and (string in row):
                        count += 1
                        continue

                    f.write(row)

        print(f'Number of deleted rows -> {count}')

    return count
