# -*- coding: utf-8 -*-

"""Console script for ohol."""
import asyncio

import click

import ohol.client


@click.command()
def main(args=None):
    """Console script for ohol."""
    host = '167.114.233.197'
    port = 8005

    loop = asyncio.get_event_loop()
    client_connect = ohol.client.Client.connect(host, port)
    client = loop.run_until_complete(client_connect)
    loop.close()
    print('player count', client.current_players)
    print('max players', client.max_players)


if __name__ == "__main__":
    main()
