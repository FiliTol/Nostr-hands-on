import logging
import asyncio
from client import listen_notes, do_post, source_key


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.DEBUG)
    url = "ws://localhost:8080"
    FILTER = [{'limit': 100}]
    text = "Dunno why but something is not working"
    n_keys = source_key()

    asyncio.run(listen_notes(url))
    asyncio.run(do_post(url, text))
