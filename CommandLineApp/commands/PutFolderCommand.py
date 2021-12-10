import re

from commands import AbstractCommand
from asyncio.streams import StreamReader, StreamWriter
from files.Storage import Storage


class PutFolderCommand(AbstractCommand):
    def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
        # super().__init__(storage)
        self.__match = None
        self._reader = reader
        self._writer = writer
        self._storage = storage

    @property
    def name(self) -> str:
        return 'PUT_FOLDER'

    @property
    def help(self) -> str:
        return 'Inserts new folder.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf"^{self.name}$", command)
        if self.__match is not None:
            return self.__match is not None
        else:
            if re.match(rf"^{self.name} HELP$", command) is not None:
                return self._writeline(str(PutFolderCommand.help))

    async def execute(self):
        try:
            self._writeline('Введите имя и путь папки:')
            name = str(await self._readline())
            if self._storage.check_path(name):
                self._storage.put_folder(name)
                self._writeline(f'Папка {name} добалена.')
            else:
                self._writeline(f'Папка {name} уже существует.')
        except (TypeError, ValueError) as error:
            self._writeline(f'ERROR: {error}')
