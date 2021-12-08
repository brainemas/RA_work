import re

from commands import AbstractCommand
from files.Storage import Storage


class GetFileCommand(AbstractCommand):
    def __init__(self, storage: Storage):
        super().__init__(storage)
        self.__match = None

    @property
    def name(self) -> str:
        return 'OPEN_FILE'

    @property
    def help(self) -> str:
        return 'Prints file.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'^{self.name}$', command)
        return self.__match is not None

    def execute(self):
        try:
            name = str(input('Введите имя файла: '))
            if file := self._storage.open_file(name):
                print(file)
            else:
                print(f'ERROR: file "{name}" not found.')
        except ValueError as error:
            print(f'ERROR: {error}')
