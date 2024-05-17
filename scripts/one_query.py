import logging
import asyncio
from monstr.client.client import Client


async def one_query(relay):
    async with Client(relay) as c:
        FILTER = [{'limit': 100}]
        events = await c.query(FILTER)
        results = []
        for c_evt in events:
            results.append((c_evt.created_at, c_evt.id, c_evt.kind, c_evt.content))
        return results


def querying(relay="ws://192.168.1.94:808/"):
    logging.getLogger().setLevel(logging.DEBUG)
    return asyncio.run(one_query(relay))
