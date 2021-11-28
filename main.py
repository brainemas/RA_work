from datetime import datetime
from File import File
from Folder import Folder
from FileManager import FileManager


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    "создаем папку, переименовываем папку и выводим название папки"
    F = Folder('folder_1', datetime(2021, 11, 22), 'stass')
    F.name = "renamed_folder"
    print(F.name)

    "создаем менеджера файлов, создаем файл и выводим имя файла"
    FM = FileManager()
    f = File('file_1', 10, datetime(2021, 11, 21), 'stass', F.name)
    print(f.name)

    "добавляем созданный файл в менеджер файлов"
    FM.add_file(f)

    "создаем второй файл, переименовываем его и выводим имя"
    f1 = File('file_2', 10, datetime(2021, 11, 22), 'stass', F.name)
    f1.name = 'renamed_file'
    print(f1.name)
    
    "добавляем второй файл в менеджер файлов и выводим список всех файлов"
    FM.add_file(f1)
    print(FM.get_all_files())

    "Удаляем из списка первый файл и выводим список со вторым файлом"
    FM.remove_file(f.name)
    print(FM.get_all_files())
