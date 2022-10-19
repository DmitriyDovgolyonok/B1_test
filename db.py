import sqlite3
import os
from contextlib import closing


def create_table(table_name: str, connection, cursor):

    query = f"""CREATE TABLE IF NOT EXISTS {table_name} (
                date CHAR(10),
                en_string CHAR(10),
                ru_string CHAR(10),
                int_number INT,
                float_number DECIMAL(10, 8)
                );"""

    cursor.execute(query)
    connection.commit()


def drop_table(table_name: str, connection, cursor):
    query = f"DROP TABLE IF EXISTS {table_name};"
    cursor.execute(query)
    connection.commit()


def insert_rows_into_table(table_name: str, rows: list, connection, cursor):

    query = f"""INSERT INTO {table_name} VALUES {", ".join(rows)};"""
    cursor.execute(query)
    connection.commit()


def fill_table_from_files(files_dir: str, table_name: str, connection, cursor):

    file_names_list = os.listdir(files_dir)
    num_of_files = len(file_names_list)
    for i, file_name in enumerate(file_names_list):
        file_path = os.path.join(files_dir, file_name)
        with open(file_path, "r") as fr:
            print(f"Files scanned: {i + 1}\t\tFiles remaining: {num_of_files - i - 1}")
            file_len = sum(1 for _ in fr)
        with open(file_path, "r") as fr:
            rows = []
            counter = 1
            for row in fr:
                row = row.split("||")
                row_str = f"('{row[0]}', '{row[1]}', '{row[2]}', {row[3]}, {row[4].replace(',', '.')})"
                rows.append(row_str)

                if counter % 100000 == 0 and counter >= 100000:
                    insert_rows_into_table(table_name, rows, connection, cursor)
                    print(f"Rows imported: {counter}\t\tRows remaining: {file_len - counter}")
                    rows = []
                counter += 1
            if counter < 100000:
                insert_rows_into_table(table_name, rows, connection, cursor)
            del rows


def task4():
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        drop_table("test", sqlite_connection, cursor)
        create_table('test', sqlite_connection, cursor)
        fill_table_from_files('merge_result/', 'test', sqlite_connection, cursor)

        with closing(sqlite3.connect('sqlite_python.db')) as connection:

            cursor = connection.cursor()
            # SQL запрос на нахождение суммы ряда int_number
            cursor.execute("""
                                   select sum(int_number) from test 
                                   """)
            sum = cursor.fetchone()

            # SQL запрос на нахождение медианты столбца float_number
            cursor.execute("""
                                select float_number from test
                                order by float_number
                                limit 1
                                offset (select count(*) from test) / 2
                                """)

            avg = cursor.fetchone()

            print(f"Sum -> {sum[0]}")
            print(f"Median --> {avg[0]}")

    except Exception:
        print(Exception)