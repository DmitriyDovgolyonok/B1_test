# Тестовое задание N1

В качестве среды разработки рекомендуется использоваться [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/).

В качестве СУБД - [SQLiteStudio](https://sqlitestudio.pl/)

### Условие
>Сгенерировать 100 текстовых файлов со следующей структурой, каждый из которых содержит
100 000 строк
> 
> Реализовать объединение файлов в один. При объединении должна быть возможность
удалить из всех файлов строки с заданным сочетанием символов, например, «abc» с выводом
информации о количестве удаленных строк
> 
> Создать процедуру импорта файлов с таким набором полей в таблицу в СУБД. При импорте
должен выводится ход процесса (сколько строк импортировано, сколько осталось)
> 
> Реализовать хранимую процедуру в БД (или скрипт с внешним sql-запросом), который считает
сумму всех целых чисел и медиану всех дробных чисел

#### Запуск

1. Клонировать проект.
2. Открыть с помощью PyCharm
3. Настроить интепретатор
4. Запуск 
    ```bash
       python main.py

### Скринкаст

![screencast](https://github.com/DmitriyDovgolyonok/B1_test/blob/master/screencast/22-27-28.gif)
