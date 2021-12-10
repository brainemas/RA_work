import re

from commands import AbstractCommand
from asyncio.streams import StreamReader, StreamWriter
from files.File import File
from files.Storage import Storage


class PutFileCommand(AbstractCommand):
    def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
        # super().__init__(storage)
        self.__match = None
        self._reader = reader
        self._writer = writer
        self._storage = storage

    @property
    def name(self) -> str:
        return 'PUT_FILE'

    @property
    def help(self) -> str:
        return 'Inserts new file.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'^{self.name}$', command)
        return self.__match is not None

    async def execute(self):
        try:
            self._writeline('Введите имя файла:')
            name = str(await self._readline())
            if self._storage.check_path(name):
                self._storage.put_file(name)
                self._writeline(f'Файл {name} добавлен.')
            else:
                self._writeline(f'Файл {name} уже существует.')
        except (TypeError, ValueError) as error:
            self._writeline(f'ERROR: {error}')
