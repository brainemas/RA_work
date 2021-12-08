import re

from commands import AbstractCommand
from files.Storage import Storage


class AddToFileCommand(AbstractCommand):
    def __init__(self, storage: Storage):
        super().__init__(storage)
        self.__match = None

    @property
    def name(self) -> str:
        return 'ADD_TO_FILE'

    @property
    def help(self) -> str:
        return 'Add data to file.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'^{self.name}$', command)
        return self.__match is not None

    def execute(self):
        try:
            name = str(input('Введите имя файла: '))
            if self._storage.check_path(name):
                data = str(input('Введите данные для записи: '))
                self._storage.add_to_file(name, data)
            else:
                print(f'ERROR: file "{name}" not found.')
        except ValueError as error:
            print(f'ERROR: {error}')
