from commands import AbstractCommand
from files.Storage import Storage


class GetFilesCommand(AbstractCommand):
    def __init__(self, storage: Storage):
        super().__init__(storage)

    @property
    def name(self) -> str:
        return 'GET_FILES'

    @property
    def help(self) -> str:
        return 'Prints all files in folder.'

    def can_execute(self, command: str) -> bool:
        return self.name == command

    def execute(self):
        name = str(input('Введите имя папки: '))
        print('Содержимое папки:\n' + '\n'.join([str(file) for file in self._storage.get_all(name)]))
