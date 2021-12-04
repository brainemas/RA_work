from Folder import Folder
from File import File
from pathlib import Path
from Storage import Storage


class FileManager:
    def __init__(self):
        self.__storage = Storage()

    def get_all_files(self, path: str):
        return self.__storage.get_all(path)

    def add_file(self, name: str):
        self.__storage.put_file(name)

    def remove_file(self, name: str):
        self.__storage.delete_file(name)

    def add_folder(self, name: str):
        self.__storage.put_folder(name)

    def remove_folder(self, name: str):
        self.__storage.delete_folder(name)

    def open_file(self, name: str):
        print(Path(name).read_text())

    def add_to_file(self, name: str, data: str):
        Path(name).write_text(data)
