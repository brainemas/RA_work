from commands import AbstractCommand, CommandFactory
from files.Storage import Storage
from asyncio.streams import StreamReader, StreamWriter
import asyncio
import logging
import Logger


class CommandProcessor(object):
    """
    Класс логики сервера (обработчик команд).
    """
    def __init__(self, storage: Storage):
        # внедряем зависимости (нам нужен только storage)
        self.__storage = storage

    # превращаем экземпляры класса Callable, чтобы завернуть в asyncio.start_server()
    async def __call__(self, reader: StreamReader, writer: StreamWriter):
        # получаем информацию о созданном соединении
        host, port = writer.transport.get_extra_info('peername')
        logging.info(f'Connected to: {host}:{port}')

        factory = CommandFactory(self.__storage, reader, writer)
        # factory = CommandFactory(Storage())

        while not writer.is_closing():
            # построчно читаем команды и выполняем их
            line = (await reader.readline()).decode().strip()
            command = factory.get_command(line)
            await command.execute(line)

        logging.info(f'Disconnected from {host}:{port}')


async def main():
    processor = CommandProcessor(Storage())

    # запускаем сервер на localhost:3333
    server = await asyncio.start_server(processor, 'localhost', 3333)
    logging.info('Server started')

    async with server:
        await server.serve_forever()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Logger.configure_logger('tcp_server_example')

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info('Server stopped')

    # factory = CommandFactory(Storage())
    #
    # while True:
    #     try:
    #         line = input('==> ')
    #         command: AbstractCommand = factory.get_command(line)
    #         command.execute()
    #     except KeyboardInterrupt:
    #         print('closing...')
    #         break
