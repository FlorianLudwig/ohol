import asyncio
import zlib


class Client:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.current_players = 0
        self.max_players = 0
        self.sequence_no = -1

    @classmethod
    async def connect(cls, host, port=8005):
        reader, writer = await asyncio.open_connection(host, port)
        client = cls(reader, writer)
        await client.read_connection_header()
        return client

    async def read_connection_header(self):
        header = await self.reader.readuntil(b'\n#')
        print(header.split(b'\n'))
        prefix, player_status, sequence_no, suffix = header.split(b'\n')
        assert prefix == b'SN'
        current_players, max_players = player_status.split(b'/')
        self.current_players = int(current_players)
        self.max_players = int(max_players)
        self.sequence_no = int(sequence_no)

    async def login(self, login):
        # TODO implement proper login
        self.writer.write(login)
        result = await self.reader.readuntil(b'\n#')
        print('result', result)
        return result == b'ACCEPTED\n#'

    async def process_server_messages(self):
        parser = ProtocolParser(self.reader)

    def send_cmd(self, command):
        if isinstance(command, str):
            command = command.encode('ascii')
        self.writer.write(command)

    def use(self, x, y):
        """
        is for bare-hand or held-object action on target object in non-empty
        grid square, including picking something up (if there's no bare-handed
        action), and picking up a container."""
        self.send_cmd('USE {} {}#\n'.format(x, y))

    def baby(self, x, y):
        self.send_cmd('BABY {} {}#\n'.format(x, y))

    """
    USE x y#
    BABY x y#
    SELF x y i#
    UBABY x y i#
    REMV x y i#
    SREMV x y c i#
    DROP x y c#
    KILL x y#
    """
