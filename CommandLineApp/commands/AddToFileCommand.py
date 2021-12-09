import re
from asyncio.streams import StreamReader, StreamWriter
from commands import AbstractCommand
from files.Storage import Storage


class AddToFileCommand(AbstractCommand):
    def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
        # super().__init__(storage)
        self.__match = None
        self._reader = reader
        self._writer = writer
        self._storage = storage

    @property
    def name(self) -> str:
        return 'ADD_TO_FILE'

    @property
    def help(self) -> str:
        return 'Add data to file.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'^{self.name}$', command)
        return self.__match is not None

    async def execute(self):
        try:
            self._writeline('Введите имя файла:')
            name = str(await self._readline())
            if self._storage.check_path(name):
                self._writeline('Введите данные для записи: ')
                data = str(await self._readline())
                self._storage.add_to_file(name, data)
                self._writeline('OK')
            else:
                self._writeline(f'ERROR: file "{name}" not found.')
        except ValueError as error:
            self._writeline(f'ERROR: {error}')
