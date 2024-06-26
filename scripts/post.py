from monstr.client.client import Client, ClientPool
from monstr.event.event import Event
from monstr.encrypt import Keys
import logging
import asyncio


def source_key(key: str = "nsec1al8wfs9g70etrcxzgxrfma9km9ae2n8jsl4rf7fjt6s3hvtrjawsnrjsv4") -> Keys:
    if key:
        if len(key) > 1:
            k = Keys(priv_k=key)
        else:
            the_key: str = key
            if the_key.startswith("nsec"):
                k = Keys(priv_k=the_key)
            else:
                k = Keys(pub_k=the_key)
    else:
        k = Keys()
    return k


def view_pubkey(key: Keys = source_key()) -> str:
    return str(key.public_key_bech32())


async def do_post(text, relay):
    n_keys = source_key()
    async with Client(relay) as c:
        n_msg = Event(
            kind=Event.KIND_TEXT_NOTE, content=text, pub_key=n_keys.public_key_hex()
        )
        n_msg.sign(n_keys.private_key_hex())
        c.publish(n_msg)


def posting(text, relay):
    logging.getLogger().setLevel(logging.DEBUG)
    asyncio.run(do_post(text, relay))
