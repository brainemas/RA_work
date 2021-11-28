from Folder import Folder
from File import File
from typing import Iterable


class ReadOnlyStorage(object):
    def __init__(self):
        self._files = {}
        self._folders = {}

    def get_all(self) -> Iterable[File]:
        return self._files.values()

    def put_file(self, file: File):
        self._files[file.name] = file

    def put_folder(self, folder: Folder):
        self._folders[folder.name] = folder


class Storage(ReadOnlyStorage):
    def delete_file(self, name: str):
        del self._files[name]

    def delete_folder(self, name: str):
        del self._folders[name]
