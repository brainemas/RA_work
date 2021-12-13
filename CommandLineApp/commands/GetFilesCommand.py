import json
import re
from commands import AbstractCommand
from files.Storage import Storage
from asyncio.streams import StreamReader, StreamWriter
from pathlib import Path


class GetFilesCommand(AbstractCommand):
    def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
        # super().__init__(storage)
        self._reader = reader
        self._writer = writer
        self._storage = storage
        self.__match = None

    @property
    def name(self) -> str:
        return 'GET_FILES'

    @property
    def help(self) -> str:
        return 'Prints all files in folder.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'GET_FILES', command)
        if self.__match is not None:
            return self.__match is not None

    async def execute(self, command):
        # self._writeline('Введите имя папки:')
        # name = str(await self._readline())
        path = command.removeprefix('GET_FILES ')
        if re.match(rf"^(GET_FILES)$", command):
            self._writeline(';;'.join([str(file) for file in self._storage.get_all(Path().cwd())]))
        elif re.match(rf"^(GET_FILES HELP)$", command):
            self._writeline(str(self.help))
        elif Path(path).resolve().parent != Path().cwd():
            self._writeline('Access denied.')
        else:
            if Path(path).is_dir():
                self._writeline(';;'.join([str(file) for file in self._storage.get_all(str(path))]))
            else:
                self._writeline(f'Unknown: "{command}".')
