import logging
import asyncio
from monstr.client.client import Client, ClientPool


async def one_query(relay):
    async with Client(relay) as c:
        events = await c.query(FILTER)
        for c_evt in events:
            print(c_evt.created_at, c_evt.id, c_evt.kind, c_evt.content)


if __name__ == '__main__':
    RELAY = "ws://localhost:8080"
    FILTER = [{'limit': 100}]
    logging.getLogger().setLevel(logging.DEBUG)
    asyncio.run(one_query(RELAY))
