import re
from asyncio.streams import StreamReader, StreamWriter
from commands import AbstractCommand
from files.Storage import Storage


class GetFileCommand(AbstractCommand):
    def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
        # super().__init__(storage)
        self.__match = None
        self._reader = reader
        self._writer = writer
        self._storage = storage

    @property
    def name(self) -> str:
        return 'OPEN_FILE'

    @property
    def help(self) -> str:
        return 'Prints file.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'^{self.name}$', command)
        return self.__match is not None

    async def execute(self):
        try:
            self._writeline('Введите имя файла:')
            name = str(await self._readline())
            if file := self._storage.open_file(name):
                self._writeline(f'Содержимое файла {name}:\n {file}')
            else:
                self._writeline(f'ERROR: file "{name}" not found.')
        except ValueError as error:
            self._writeline(f'ERROR: {error}')
