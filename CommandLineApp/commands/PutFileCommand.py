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
        return 'Inserts new file. PUT_FILE {path/file_name}'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'PUT_FILE', command)
        return self.__match is not None

    async def execute(self, command):
        try:
            # self._writeline('Введите имя файла:')
            # name = str(await self._readline())
            name = command.removeprefix('PUT_FILE ')
            if re.match(rf"^(PUT_FILE)$", command):
                self._writeline(f'ERROR: no attribute in command. Use HELP attribute.')
            elif re.match(rf"^(PUT_FILE HELP)$", command):
                self._writeline('OK')
                self._writeline(str(self.help))
            elif self._storage.check_path(str(name)) is False:
                self._storage.put_file(str(name))
                self._writeline('OK')
            elif self._storage.check_path(str(name)) is True:
                self._writeline(f'ERROR: "{name}" is already exists.')
            else:
                self._writeline(f'Unknown: "{command}".')

            # if self._storage.check_path(name):
            #     self._storage.put_file(name)
            #     self._writeline(f'Файл {name} добавлен.')
            # else:
            #     self._writeline(f'Файл {name} уже существует.')
        except (TypeError, ValueError) as error:
            self._writeline(f'ERROR: {error}')
