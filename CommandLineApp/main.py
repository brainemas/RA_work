from commands import AbstractCommand, CommandFactory
from files.Storage import Storage

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    factory = CommandFactory(Storage())

    while True:
        try:
            line = input('==> ')
            command: AbstractCommand = factory.get_command(line)
            command.execute()
        except KeyboardInterrupt:
            print('closing...')
            break
