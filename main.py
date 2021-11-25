from dataclasses import dataclass
from datetime import datetime
from typing import Iterable


@dataclass
class Folder:
    name: str
    d: datetime
    author: str


@dataclass
class File:
    name: str
    size: int
    d: datetime
    author: str
    parent: Folder


class Storage:
    def __init__(self):
        self.__files = {}
        self.__folders = {}

    def get_all(self) -> Iterable[File]:
        return self.__files.values()

    def put_file(self, file: File):
        self.__files[file.name] = file

    def delete_file(self, name: str):
        del self.__files[name]

    def put_folder(self, folder: Folder):
        self.__folders[folder.name] = folder

    def delete_folder(self, name: str):
        del self.__folders[name]


class FileManager:
    def __init__(self):
        self.__storage = Storage()

    def get_all_files(self):
        return self.__storage.get_all()

    def add_file(self, name: File):
        self.__storage.put_file(name)

    def remove_file(self, name: str):
        self.__storage.delete_file(name)

    def add_folder(self, name: Folder):
        self.__storage.put_folder(name)

    def remove_folder(self, name: str):
        self.__storage.delete_folder(name)


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
