from commands import *
from files.Storage import Storage
from asyncio.streams import StreamReader, StreamWriter


class CommandFactory(object):
    class __HelpCommand(AbstractCommand):
        def __init__(self, factory, storage: Storage, reader: StreamReader, writer: StreamWriter):
            self.__factory = factory
            self._reader = reader
            self._writer = writer
            self._storage = storage

        @property
        def name(self) -> str:
            return 'HELP'

        @property
        def help(self) -> str:
            return 'Prints this help.'

        def can_execute(self, command: str) -> bool:
            return command == self.name

        async def execute(self):
            for command in self.__factory.commands:
                self._writeline(f'{command.name}: {command.help}')

    class __UnknownCommand(AbstractCommand):
        def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
            self.__command = None
            self._reader = reader
            self._writer = writer
            self._storage = storage

        @property
        def name(self) -> str:
            raise NotImplementedError

        @property
        def help(self) -> str:
            raise NotImplementedError

        def can_execute(self, command: str) -> bool:
            self.__command = command
            return True

        async def execute(self):
            self._writeline(f'Unknown command: "{self.__command}".')

    def __init__(self, storage: Storage, reader: StreamReader, writer: StreamWriter):
        self.commands = [
            self.__HelpCommand(self, storage, reader, writer),
            OpenFileCommand(storage, reader, writer),
            GetFilesCommand(storage, reader, writer),
            PutFileCommand(storage, reader, writer),
            PutFolderCommand(storage, reader, writer),
            DeleteFileCommand(storage, reader, writer),
            DeleteFolderCommand(storage, reader, writer),
            AddToFileCommand(storage, reader, writer)
        ]
        self._reader = reader
        self._writer = writer
        self._storage = storage

    def get_command(self, line: str) -> AbstractCommand:
        for command in self.commands + [self.__UnknownCommand(self._storage, self._reader, self._writer)]:
            if command.can_execute(line):
                return command
