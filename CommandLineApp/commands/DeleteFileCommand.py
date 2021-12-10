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
        return 'Deletes file. DELETE_FILE {path/file_name}'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'DELETE_FILE', command)
        return self.__match is not None

    async def execute(self, command):
        try:
            # self._writeline('Введите имя файла для удаления:')
            # name = str(await self._readline())
            name = command.removeprefix('DELETE_FILE ')
            if re.match(rf"^(DELETE_FILE)$", command):
                self._writeline(f'ERROR: add attribute in command. Use HELP attribute.')
            elif re.match(rf"^(DELETE_FILE HELP)$", command):
                self._writeline('OK')
                self._writeline(str(self.help))
            elif self._storage.check_path(str(name)) is True:
                self._storage.delete_file(str(name))
                self._writeline('OK')
            elif self._storage.check_path(str(name)) is False:
                self._writeline(f'ERROR: File "{name}" not found.')
            else:
                self._writeline(f'Unknown: "{command}".')

            # if self._storage.check_path(name):
            #     self._storage.delete_file(name)
            #     self._writeline(f'Файл {name} удален.')
            # else:
            #     self._writeline(f'Файла {name} не существует.')
        except ValueError as error:
            self._writeline(f'ERROR: {error}')
