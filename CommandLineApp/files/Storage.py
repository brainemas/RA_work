from datetime import datetime
from files.Folder import Folder
from files.File import File
from pathlib import Path, PurePath, PurePosixPath
import time
import pathlib
import json


class ReadOnlyStorage(object):
    def __init__(self):
        self._files = []
        self._folders = []

    def get_all(self, path: str):
        with open("config.json", "r") as config:
            conf = json.load(config)
        P = Path(conf["path"]) / Path(path)
        for child in P.iterdir():
            self._files.append(PurePosixPath(child).name)
        return self._files

    def put_file(self, name: str):
        if Path(name).exists():
            print('Такой файл уже существует.')
        else:
            Path(name).touch()
            print('Файл', name, 'добавлен.')
            File(name, Path(name).stat().st_size, time.ctime(Path(name).stat().st_ctime), Path(name).stat().st_uid, PurePath(name).parent)

    def put_folder(self, name: str):
        if Path(name).exists():
            print('Такая папка уже существует.')
        else:
            Path(name).mkdir()
            print('Папка', name, 'добавлена.')
            Folder(name, datetime.today(), Path(name).stat().st_uid)

    def open_file(self, name: str):
        return Path(name).read_text()

    def add_to_file(self, name: str, data: str):
        Path(name).write_text(data)
        print(f'Данные записаны в файл {name}')

    def check_path(self, path):
        return Path(path).exists()


class Storage(ReadOnlyStorage):
    def delete_file(self, name: str):
        if self.check_path(name):
            if Path(name).stat().st_size > 0:
                Path(name).write_text('')
            Path(name).unlink()
            print('Файл удален.')
        else:
            print('Такого файла не существует.')

    def delete_folder(self, name: str):
        if self.check_path(name):
            for file in self.get_all(name):
                self.delete_file(pathlib.Path(name) / file)
            Path(name).rmdir()
            print('Папка удалена.')
        else:
            print('Такой папки не существует.')
