import asyncio

import pytest

import ohol.server_protocol
import ohol.fake


@pytest.mark.asyncio
async def test_protocol_parser():
    stream = ohol.server_protocol.make_stream(ohol.fake.DATA)
    parser = ohol.server_protocol.ProtocolParser(stream)
    async for i in parser.parse():
        print(i)
