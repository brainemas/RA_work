from datetime import datetime


GLOBAL_FOLDERS = []
GLOBAL_FILES = {}


class Folder:
    def __init__(self, name: str, d: datetime, author: str):
        self.name = name
        self.d = d
        self.author = author

    @staticmethod
    def get_all_folders():
        return GLOBAL_FOLDERS

    def add_folder(self):
        GLOBAL_FOLDERS.append(self)

    @property
    def folder_name(self):
        return self.name

    @folder_name.setter
    def folder_name(self, name: str):
        self.name = name


class File:
    def __init__(self, name: str, size: int, d: datetime, author: str, parent: Folder):
        self.name = name
        self.size = size
        self.d = d
        self.author = author
        self.parent = parent

    @property
    def file_name(self) -> str:
        return self.name

    @file_name.setter
    def file_name(self, name: str):
        self.name = name

    @staticmethod
    def get_all_files():
        return GLOBAL_FILES

    @staticmethod
    def add_file(self):
        GLOBAL_FILES[self.name] = self
        
    @staticmethod
    def remove_file(name):
        del GLOBAL_FILES[name]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    F = Folder('folder_1', datetime(2021, 11, 22), 'stass')
    F.folder_name = "renamed_folder"
    print(f.file_name, 'находится в папке', f.parent)

    f = File('file_1', 10, datetime(2021, 11, 22), 'stass', F.folder_name)
    print(f.file_name)
    
    f.add_file(f)

    f1 = File('file_2', 10, datetime(2021, 11, 22), 'stass', F.folder_name)
    f1.file_name = 'renamed_file'
    print(f1.file_name)
    
    f1.add_file(f1)
    
    print(f.get_all_files())
    
    f.remove_file(f.file_name)
    print(f.get_all_files())
