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
    # print(FM.get_all_files(folder))

    "Получение информации о файле/папке"
    file = input('Введите имя файла и путь: ')
    print('Размер:', Path(file).stat().st_size)
    print('Владелец:', Path(file).stat().st_uid)
    print('Дата создания:', time.ctime(Path(file).stat().st_ctime))


    "создаем папку, переименовываем папку и выводим название папки"
    # F = Folder('folder_1', datetime(2021, 11, 22), 'stass')
    # F.name = "renamed_folder"
    # print(F.name)
    # "создаем менеджера файлов, создаем файл и выводим имя файла"
    # FM = FileManager()
    # f = File('file_1', 10, datetime(2021, 11, 21), 'stass', F.name)
    # print(f.name)
    #
    # "добавляем созданный файл в менеджер файлов"
    # FM.add_file(f)
    #
    # "создаем второй файл, переименовываем его и выводим имя"
    # f1 = File('file_2', 10, datetime(2021, 11, 22), 'stass', F.name)
    # f1.name = 'renamed_file'
    # print(f1.name)
    #
    # "добавляем второй файл в менеджер файлов и выводим список всех файлов"
    # FM.add_file(f1)
    # print(FM.get_all_files())
    #
    # "Удаляем из списка первый файл и выводим список со вторым файлом"
    # FM.remove_file(f.name)
    # print(FM.get_all_files())
