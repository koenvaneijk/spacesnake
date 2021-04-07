# 🌌🐍 spacesnake - Python decentralized on IPFS

Leveraging decentralized storage technology [IPFS](https://ipfs.io) for hash-verified Python script/module distribution! Create unstoppable Python applications which can be accessed from anywhere in the universe. Enjoy the assurance that no changes were made to your script (as long as the hash matches).
## Contents
- [Get started](#get-started)
- [Features](#features)
- [How it works](#how-it-works)
- [Uploading your Python scripts to IPFS](#uploading-your-python-scripts-to-IPFS)

## Get started
Install from PyPi
```bash
pip install spacesnake
```
__Note__: Make sure your local [IPFS](https://ipfs.io/) node is running. The easiest way to set up a local IPFS node is by installing [IPFS Desktop](https://github.com/ipfs/ipfs-desktop). By default, spacesnake expects your IPFS node to be at [http://127.0.0.1:5001], but you can override this with the `SPACESNAKE_IPFS_NODE_URL` environment variable.

__Warning__: IPFS is still experimental and [work in progress](https://github.com/ipfs/ipfs#current-state-of-ipfs). Also, [security](https://github.com/ipfs/ipfs#a-word-on-security).

__Warning__: Always inspect scripts/hashes before you run them. Only run scripts from trusted sources. 

To inspect an example "Hello world!" script from IPFS:
```python
spacesnake script QmPzrKNqpMVypixkQDVAQc8MeF8PTuKtnwr91hfE3DAJ6j --inspect
```

To run an example "Hello world!" script straight from IPFS:
```bash
spacesnake script QmPzrKNqpMVypixkQDVAQc8MeF8PTuKtnwr91hfE3DAJ6j
```
Or importing modules:
```python
import spacesnake # Required for IPFS imports to work
from QmcEuJMSci6SeMUu1xTCtVZmu8FHCnSKUUGp7nav6cuDEj import SnakeSpace

snake = SnakeSpace()
snake.fire_lazers()
```
## Features
- Import IPFS paths straight from your Python scripts!
- Run Python scripts and modules straight from IPFS
- Push your scripts/modules to IPFS to make them available globally and forever.

## How it works
- The `spacesnake` CLI wraps the [runpy](https://docs.python.org/3/library/runpy.html) module from the Python standard library, with some IPFS-sauce.
- `spacesnake` also implements an [importer](https://docs.python.org/3/glossary.html#term-importer), which takes care of all the IPFS storage and caching magic behind the scenes!

The best way to make sure your script remains available to the world is by sharing with as many people as you can. That way, redundancy across the IPFS network increases for your script or module! Alternatively, you can use pinning services like [Pinata](https://pinata.cloud/) to guarantee to some extent your scripts remain available.

## Uploading your Python scripts to IPFS
You can use the `spacesnake` CLI to easily publish a script or module to IPFS, or you can use IPFS desktop to pin the file manually. Using the CLI takes care of import resolution so it makes sure your entire script is published!

Like so:
```bash
spacesnake push my_script.py
```
After confirmation returns the hash of the IPFS pin in `stdout`:
```
QmPzrKNqpMVypixkQDVAQc8MeF8PTuKtnwr91hfE3DAJ6j
```
You can skip confirmation with the `-y` flag:
```bash
spacesnake push my_script.py -y
```
You can then run the script:
```bash
spacesnake script QmPzrKNqpMVypixkQDVAQc8MeF8PTuKtnwr91hfE3DAJ6j
```

## To do
- Add tests!
- Add IPFS gateway support (eliminates the need for a local IPFS node, but requires a trusted IPFS gateway)
- Add script encryption/decryption with key or passphrase/password
- Add [IPNS](https://docs.ipfs.io/concepts/ipns/) support for pointers to IPFS CIDs

## Feedback?
- [Create an issue](https://github.com/koenvaneijk/spacesnake/issues/new), or even better, [submit a pull request](https://github.com/koenvaneijk/spacesnake/pulls).
- Send an e-mail to [vaneijk.koen@gmail.com](mailto:vaneijk.koen@gmail.com).