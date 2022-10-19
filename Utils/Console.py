def progress(count: int, total: int):
    """
    Графичесое отображение прогресс бара
    """
    bar_len = 60
    filled_len = int(round(bar_len * count / int(total)))

    percents = round(100.0 * count / int(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    print(f'\r[{bar}] {percents}%', end = '')
