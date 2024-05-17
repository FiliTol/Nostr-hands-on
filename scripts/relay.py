import asyncio
import logging
import websockets
from monstr.relay.relay import Relay
from monstr.event.persist_memory import RelayMemoryEventStore


async def run_relay():
    r = Relay(store=RelayMemoryEventStore())
    await r.start()


async def test_relay(relay):
    try:
        async with websockets.connect(relay) as websocket:
            return "Relay is reachable"
    except Exception as e:
        return "Relay is not reachable"


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    asyncio.run(run_relay())
