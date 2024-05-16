import asyncio
import logging
from monstr.client.client import Client
from monstr.event.event import Event
from user_test import source_key


n_keys = source_key()


async def do_post(url, text):

    async with Client(url) as c:
        n_msg = Event(
            kind=Event.KIND_TEXT_NOTE, content=text, pub_key=n_keys.public_key_hex()
        )
        n_msg.sign(n_keys.private_key_hex())
        c.publish(n_msg)


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    url = "ws://localhost:8080"
    text = "Dunno why but something is not working"

    asyncio.run(do_post(url, text))
