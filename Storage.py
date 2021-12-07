from datetime import datetime
from Folder import Folder
from File import File
from pathlib import Path, PurePath, PurePosixPath
import time


class ReadOnlyStorage(object):
    def __init__(self):
        self._files = {}
        self._folders = {}

    def get_all(self, path: str):
        for child in Path(path).iterdir():
            return PurePosixPath(child).name

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

    def check_path(self, path):
        return Path(path).exists()


class Storage(ReadOnlyStorage):
    def delete_file(self, name: str):
        if Path(name).stat().st_size > 0:
            Path(name).write_text('')
        Path(name).unlink()
        print('Файл удален.')

    def delete_folder(self, name: str):
        Path(name).rmdir()
        print('Папка удалена.')
