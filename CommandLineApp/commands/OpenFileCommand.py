import re
from asyncio.streams import StreamReader, StreamWriter
from commands import AbstractCommand
from files.Storage import Storage


class OpenFileCommand(AbstractCommand):
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
        return 'Prints file. OPEN_FILE {path/file_name}'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'OPEN_FILE', command)
        return self.__match is not None

    async def execute(self, command):
        try:
            # self._writeline('Введите имя файла:')
            # name = str(await self._readline())
            name = command.removeprefix('OPEN_FILE ')
            if re.match(rf"^(OPEN_FILE)$", command):
                self._writeline(f'ERROR: no attribute in command. Use HELP attribute.')
            elif re.match(rf"^(OPEN_FILE HELP)$", command):
                self._writeline(str(self.help))
                self._writeline('OK')
            elif self._storage.check_path(str(name)) is True:
                self._writeline(self._storage.open_file(str(name)))
                self._writeline('OK')
            elif self._storage.check_path(str(name)) is False:
                self._writeline(f'ERROR: File "{name}" not found.')
            else:
                self._writeline(f'Unknown: "{command}".')

            # if file := self._storage.open_file(name):
            #     self._writeline(f'Содержимое файла {name}:\n {file}')
            # else:
            #     self._writeline(f'ERROR: file "{name}" not found.')
        except ValueError as error:
            self._writeline(f'ERROR: {error}')
