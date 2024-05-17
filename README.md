# Basic Nostr relay and client

Sharing and syncing text across different devices is a trivial task to
accomplish with the usage of proprietary tools, closed source applications
and technologies. Even though these are practical and useful strategies, sometimes
the data at hand requires a more cautious approach, which means that sharing the
text and content with a third party server could be annoying and even dangerous.

Some solutions in the FOSS community use bluetooth technologies or direct wifi
connections to solve this issue. Nonetheless, sometimes these tools can present
some challenges and cannot enable long-term storage of the shared data.

I propose a basic alternative to tackle one subset of use-cases, specifically
the sharing of content across devices belonging to the same private network with
the usage of a Nostr relay. This approach exploits some features of open protocols
and is extremely extensible according to the needs of the user(s).

The project contains two elements:

- a basic client application, used to push and retrieve text notes from the relay;
- a basic nostr relay, which stores the text notes in-memory.

Both the client and the relay are implemented using the python `monstr` library, which is a work-in-progress library with possibly some missing features.
As the upstream library will be updated, new features will be implemented
in the project.

## Warnings
Since the client and the relay are extremely basic and with no ecryption schemes
implemented, it's suggested to not employ this product in adversarial contexts
and with no sensitive or private information.
A closed, private, non adversarial and safe network is the most suited environment
to test this project as of now.

## Future improvements

The current state of the Client doesn't enable interoperability between the basic client of this project and the Nostr-compatible clients out there. This feature will be enabled once the note formatting - as processed by the client - will be standardized.
On the contrary, the relay is already compatible with the broader ecosistem of Nostr clients.

### Client

- [ ]  Box to insert custom relay in the user interface;
- [ ] Text content is deleted from the input form once the submission to the relay succeded;
- [ ] Subscription-based retrieval of data from relay (once `monstr` implements the proper handler features);
- [ ] Time limit on the retrieved data from the relay;
- [ ] NIP1-compatible formatting for shared notes;
- [ ] NIP-compatible encryption scheme for text notes, as described in the DM specs for Nostr clients;
- [ ] Better styling of the client application.

### Relay

- [ ] SQLite integration for long-term storage of notes.

