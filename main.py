from datetime import datetime


GLOBAL_FOLDERS = []


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
        self.__data = {
            'name': name,
            'size': size,
            'd': d,
            'author': author,
            'parent': parent,
        }
        
    def __repr__(self):
        return f'File(name = {self.file_name}, size = {self.__data["size"]}, d = {self.__data["d"]}, author = {self.__data["author"]}, parent = {self.__data["parent"]})'

    @property
    def file_name(self) -> str:
        return self.__data['name']

    @file_name.setter
    def file_name(self, name: str):
        self.__data['name'] = name


class FileStorage:
    def __init__(self):
        self.__files = {}

    def get_all(self):
        return self.__files.values()

    def put_one(self, name):
        self.__files[name] = name

    def delete_one(self, name):
        del self.__files[name]


class FileManager:
    def __init__(self):
        self.__storage = FileStorage()

    def get_all_files(self):
        return self.__storage.get_all()

    def add_file(self, name):
        self.__storage.put_one(name)

    def remove_file(self, name):
        self.__storage.delete_one(name)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    F = Folder('folder_1', datetime(2021, 11, 22), 'stass')
    F.folder_name = "renamed_folder"
    print(F.name)

    file = FileManager()
    f = File('file_1', 10, datetime(2021, 11, 21), 'stass', F.folder_name)
    print(f.file_name)
    
    file.add_file(f)

    f1 = File('file_2', 10, datetime(2021, 11, 22), 'stass', F.folder_name)
    f1.file_name = 'renamed_file'
    print(f1.file_name)
    
    file.add_file(f1)
    
    print(file.get_all_files())

    file.remove_file(f)
    print(file.get_all_files())
