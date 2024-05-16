import asyncio
import logging
import sys
import signal
from monstr.client.client import Client, ClientPool
from monstr.event.event import Event
from monstr.encrypt import Keys
from monstr.util import util_funcs


tail = util_funcs.str_tails


async def listen_notes(url):
    run = True

    def sigint_handler(signal, frame):
        nonlocal run
        run = False
    signal.signal(signal.SIGINT, sigint_handler)

    c = Client(url)
    await asyncio.create_task(c.run())
    await c.wait_connect()

    def my_handler(the_client: Client, sub_id: str, evt: Event):
        print(evt.created_at, evt.content)

    c.subscribe(handlers=my_handler,
                filters={
                    'limit': 100
                })

    while run:
        await asyncio.sleep(0.1)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    url = "ws://localhost:8080"
    FILTER = [{'limit': 100}]
    text = "Dunno why but something is not working"
    n_keys = source_key()

    asyncio.run(listen_notes(url))
    asyncio.run(do_post(url, text))
