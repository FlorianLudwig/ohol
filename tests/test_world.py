import pytest

import ohol.world
import ohol.server_protocol


@pytest.mark.asyncio
async def test_tile():
    tile = ohol.world.Tile(x=0, y=0)
    message = bytes(tile)
    print('tile')
    print(repr(message))
    stream = ohol.server_protocol.make_stream(message)

    tile_data = await ohol.server_protocol.parse_command(stream)
    assert tile_data[0] == b'MC'
    assert tile_data[1] == tile.size_x
    assert tile_data[2] == tile.size_y
    assert tile_data[3] == tile.x
    assert tile_data[4] == tile.y

    # assert tile_data[5] == tile.data
