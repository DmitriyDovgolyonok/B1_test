import datetime as dt
"""
 онстанты используемые внутри проекта
"""
END_DATE = dt.date.today()
START_DATE = END_DATE - dt.timedelta(days = 365 * 5 + 1)
EN_CHARS = [chr(i) for i in list(range(65, 91)) + list(range(97, 123))]
RU_CHARS = [chr(i) for i in list(range(1040, 1104))]

DIRECTORY_NAME = "./txt_files"
