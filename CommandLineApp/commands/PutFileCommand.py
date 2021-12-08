import json
import re

from commands import AbstractCommand

from files.File import File
from files.Storage import Storage


class PutFileCommand(AbstractCommand):
    def __init__(self, storage: Storage):
        super().__init__(storage)
        self.__match = None

    @property
    def name(self) -> str:
        return 'PUT_FILE'

    @property
    def help(self) -> str:
        return 'Inserts new file.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'^{self.name}$', command)
        return self.__match is not None

    def execute(self):
        try:
            name = str(input('Введите имя файла: '))
            self._storage.put_file(name)
        except (TypeError, ValueError) as error:
            print(f'ERROR: {error}')
