from commands import AbstractCommand
from files.Storage import Storage
from asyncio.streams import StreamReader, StreamWriter


class GetFilesCommand(AbstractCommand):
    def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
        # super().__init__(storage)
        self._reader = reader
        self._writer = writer
        self._storage = storage

    @property
    def name(self) -> str:
        return 'GET_FILES'

    @property
    def help(self) -> str:
        return 'Prints all files in folder.'

    def can_execute(self, command: str) -> bool:
        return self.name == command

    async def execute(self):
        self._writeline('Введите имя папки:')
        name = str(await self._readline())
        self._writeline('Содержимое папки:\n' + '\n'.join([str(file) for file in self._storage.get_all(name)]))
