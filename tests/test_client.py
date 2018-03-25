import asyncio

import pytest

import ohol.client
import ohol.fake


@pytest.mark.asyncio
async def test_protocol_parser():
    stream = ohol.client.make_stream(ohol.fake.DATA)
    parser = ohol.client.ProtocolParser(stream)
    async for i in parser.parse():
        print(i)
