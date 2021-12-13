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
        return 'Add data to file. ADD_TO_FILE {file_name} {data for writing}'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'ADD_TO_FILE', command)
        return self.__match is not None

    async def execute(self, command):
        try:
            # self._writeline('Введите имя файла:')
            # name = str(await self._readline())
            name = command.removeprefix('ADD_TO_FILE ')
            data = re.split(r' ', command)
            if re.match(rf"^(ADD_TO_FILE)$", command):
                self._writeline(f'ERROR: no attributes in command. Use HELP attribute.')
            elif re.match(rf"^(ADD_TO_FILE HELP)$", command):
                self._writeline(str(self.help))
                self._writeline('OK')
            elif self._storage.check_path(str(data[1])) is True:
                self._storage.add_to_file(data[1], data[2])
                self._writeline('OK')
            elif self._storage.check_path(str(name)) is False:
                self._writeline(f'ERROR: File "{data[1]}" not found.')
            else:
                self._writeline(f'Unknown: "{command}".')

            # if self._storage.check_path(name):
            #     self._writeline('Введите данные для записи: ')
            #     data = str(await self._readline())
            #     self._storage.add_to_file(name, data)
            #     self._writeline('OK')
            # else:
            #     self._writeline(f'ERROR: file "{name}" not found.')
        except ValueError as error:
            self._writeline(f'ERROR: {error}')
