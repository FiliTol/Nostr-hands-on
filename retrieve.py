import asyncio
import logging
import signal
from monstr.client.client import Client
from monstr.event.event import Event
from monstr.util import util_funcs
from monstr.client import event_handlers


tail = util_funcs.str_tails


async def listen_notes(url):
    run = True

    def sigint_handler(signal, frame):
        nonlocal run
        run = False
    signal.signal(signal.SIGINT, sigint_handler)

    def my_handler(the_client: Client, sub_id: str, evt: Event):
        print(evt.created_at, evt.id, evt.kind, evt.content)

    # TODO: need some changes in the library source, specifically in:
    # - monstr.client.event_handlers.py --> for EventHandler class the do_event method must be completed

    def on_connect(the_client: Client):
        the_client.subscribe(handlers=None, filters={'limit': 100})

    c = Client(url, on_connect=on_connect)
    await asyncio.create_task(c.run())
    await c.wait_connect()

    while run:
        await asyncio.sleep(0.1)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    url = "ws://localhost:8080"

    asyncio.run(listen_notes(url))
