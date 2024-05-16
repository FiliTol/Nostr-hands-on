import os
from monstr.encrypt import Keys

test = os.environ["VIRTUAL_ENV"]

print(test)
#PRIVKEY_NOSTR = os.environ['PRIVKEY_NOSTR']
#k = Keys.get_key(PRIVKEY_NOSTR)
#
#print(PRIVKEY_NOSTR)