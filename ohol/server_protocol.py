import asyncio
import zlib


def parse_ints(data) -> list:
    """parse space separated ascii ints"""
    return map(int, data.strip().split(b' '))


def make_stream(data) -> asyncio.StreamReader:
    """create asyncio.StreamReader from static data"""
    stream = asyncio.StreamReader()
    stream._buffer = bytearray(data)
    return stream


async def read_compressed_message(stream: asyncio.StreamReader) -> bytes:
    """used by MC and CM"""
    chunk = await stream.readuntil(b'\n')
    binary_raw_size, binary_compressed_size = parse_ints(chunk)
    chunk = await stream.read(1 + binary_compressed_size)
    assert chunk[0] == 35  # chr(35) == '#'
    data = zlib.decompress(chunk[1:])
    assert len(data) == binary_raw_size
    return data


async def parse_command(stream: asyncio.StreamReader):
    """read and parse one server message from stream"""
    command = await stream.read(3)
    if command == b'MC\n':
        chunk = await stream.readuntil(b'\n')
        size_x, size_y, x, y = parse_ints(chunk)
        map_data = await read_compressed_message(stream)
        return (b'MC', size_x, size_y, x, y, map_data)

    if command == b'CM\n':
        message = await read_compressed_message(stream)
        return (await parse_command(make_stream(message)))

    if command == b'PU\n':
        player_lines = await stream.readuntil(b'\n#')
        player_lines = player_lines[:-2]
        player_lines = player_lines.split(b'\n')
        return (b'PU', player_lines)

    if command == b'PM\n':
        pass

    else:
        raise AttributeError('parse error. unknown command {}'.format(command))


class ProtocolParser:
    def __init__(self, reader):
        self.reader = reader

    async def parse(self):

        while True:
            message = await parse_command(self.reader)
            if not message:
                return
            yield message
