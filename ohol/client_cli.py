# -*- coding: utf-8 -*-
"""Console script for ohol."""
import asyncio

import click

import ohol.client


async def run():
    # host = '167.114.233.197'
    # host = 'server14.onehouronelife.com'
    host = 'onehour.world'
    port = 8005
    client = await ohol.client.Client.connect(host, port)
    # await client.login('', '')
    #
    # commands = client.process_server_messages()
    # async for cmd in commands:
    #     print(cmd)

    print('player count', client.current_players)
    print('max players', client.max_players)

@click.command()
def main(args=None):
    """Console script for ohol."""


    loop = asyncio.get_event_loop()

    client = loop.run_until_complete(run())
    loop.close()


if __name__ == "__main__":
    main()
