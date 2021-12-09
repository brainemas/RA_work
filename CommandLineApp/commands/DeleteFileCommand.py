import re
from asyncio.streams import StreamReader, StreamWriter
from commands import AbstractCommand
from files.Storage import Storage


class DeleteFileCommand(AbstractCommand):
    def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
        # super().__init__(storage)
        self.__match = None
        self._reader = reader
        self._writer = writer
        self._storage = storage

    @property
    def name(self) -> str:
        return 'DELETE_FILE'

    @property
    def help(self) -> str:
        return 'Deletes file.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'^{self.name}$', command)
        return self.__match is not None

    async def execute(self):
        try:
            self._writeline('Введите имя файла для удаления:')
            name = str(await self._readline())
            self._storage.delete_file(name)
            self._writeline(f'Файл {name} удален.')
        except ValueError as error:
            self._writeline(f'ERROR: {error}')
