from dataclasses import dataclass
from datetime import datetime


@dataclass
class Folder:
    name: str
    datetime: datetime
    author: str


@dataclass
class File:
    name: str
    size: int
    datetime: datetime
    author: str
    parent: Folder


GLOBAL_FOLDERS = []
GLOBAL_FILES = []


def get_all_folders():
    return GLOBAL_FOLDERS


def get_all_files():
    return GLOBAL_FILES


def add_folder(folder: Folder):
    GLOBAL_FOLDERS.append(folder)


def add_file(file: File):
    GLOBAL_FILES.append(file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
