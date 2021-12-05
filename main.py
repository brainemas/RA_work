from FileManager import FileManager
import time
from pathlib import *

from FileManager import FileManager

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    FM = FileManager()
    "создаем папку с произвольным названием в текущей директории"
    # folder = input('Введите название папки для создания: ')
    # FM.add_folder(folder)

    "удаляем папку"
    # folder = input('Введите название папки для удаления: ')
    # FM.remove_folder(folder)

    "создаем файл"
    # file = input('Введите имя файла и путь: ')
    # FM.add_file(file)

    "удаляем файл"
    # file = input('Введите имя файла и путь для удаления: ')
    # FM.remove_file(file)

    "Получаем список файлов в указанной папке"
    # folder = input('Введите название папки: ')
    # FM.get_all_files(folder)

    "Получение информации о файле/папке"
    # file = input('Введите имя файла и путь: ')
    # print('Размер:', Path(file).stat().st_size)
    # print('Владелец:', Path(file).stat().st_uid)
    # print('Дата создания:', time.ctime(Path(file).stat().st_ctime))

    "открываем файл"
    # file = input('Введите имя файла и путь: ')
    # FM.open_file(file)

    "запись в файл"
    # file = input('Введите имя файла и путь: ')
    # data = input('Введите данные для записи: ')
    # FM.add_to_file(file, data)

    "удаляем непустой файл"
    # file = input('Введите имя файла и путь для удаления: ')
    # FM.remove_file(file)
