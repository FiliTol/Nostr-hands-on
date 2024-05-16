import logging
import asyncio
from monstr.client.client import Client, ClientPool

DEFAULT_RELAY = "ws://localhost:8080"
FILTER = [
    {
        'limit': 100
    }
]


async def one_query(relay=DEFAULT_RELAY):
    async with Client(relay) as c:
        events = await c.query(FILTER)
        for c_evt in events:
            print(c_evt.created_at, c_evt.id, c_evt.kind, c_evt.content)


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    asyncio.run(one_query())
