import re
from asyncio.streams import StreamReader, StreamWriter
from commands import AbstractCommand
from files.Storage import Storage


class DeleteFolderCommand(AbstractCommand):
    def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
        # super().__init__(storage)
        self.__match = None
        self._reader = reader
        self._writer = writer
        self._storage = storage

    @property
    def name(self) -> str:
        return 'DELETE_FOLDER'

    @property
    def help(self) -> str:
        return 'Deletes folder.'

    def can_execute(self, command: str) -> bool:
        self.__match = re.match(rf'DELETE_FOLDER', command)
        return self.__match is not None

    async def execute(self, command):
        try:
            # self._writeline('Введите имя папки для удаления:')
            # name = str(await self._readline())
            name = command.removeprefix('DELETE_FOLDER ')
            if re.match(rf"^(DELETE_FOLDER)$", command):
                self._writeline(f'ERROR: add attribute in command.')
            elif re.match(rf"^(DELETE_FOLDER HELP)$", command):
                self._writeline('OK')
                self._writeline(str(self.help))
            elif self._storage.check_path(str(name)) is True:
                self._storage.delete_folder(str(name))
                self._writeline('OK')
            elif self._storage.check_path(str(name)) is False:
                self._writeline(f'ERROR: Folder "{name}" not found.')
            else:
                self._writeline(f'Unknown: "{command}".')


            # if self._storage.check_path(name):
            #     self._storage.delete_folder(name)
            #     self._writeline(f'Папка {name} удалена.')
            # else:
            #     self._writeline(f'Папки {name} не существует.')
        except ValueError as error:
            self._writeline(f'ERROR: {error}')
