import os
import sys
from monstr.encrypt import Keys


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
