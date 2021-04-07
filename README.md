Namebase Marketplace Api for Python
==

<p>
<a href="https://namebase-marketplace.readthedocs.io/en/latest/">
<img src="https://readthedocs.org/projects/namebase-exchange-python/badge/?version=latest" alt="Open Issues"/>
</a>
<a href="/issues">
<img src="https://img.shields.io/github/issues/pretended/namebase-marketplace" alt="Open Issues"/>
</a>
<a href="https://pypi.org/project/namebase-marketplace/">
<img src="https://img.shields.io/pypi/v/namebase-marketplace.svg" alt="PyPI"/>
</a>
<a href="/LICENCE">
<img src="https://img.shields.io/github/license/pretended/namebase-marketplace" alt="MIT Licence"/>
</a>


Python 3.6+ client for interacting with Namebase Marketplace API.

## Usage
Instantiating the Marketplace object can be done either by using email and password or None.
Only post requests can be made authenticated.

Websocket API is not provided.
## Installation

### Requirements

- Python 3.6 or greater

### Install

> pip install namebase-marketplace

### Usage

Core REST API for Namebase MARKETPLACE
```python
from namebase_marketplace.marketplace import *
marketplace = Marketplace(email="YOUR EMAIL", pwd="YOUR PASSWORD")
marketplace.get_user_info()
marketplace.open_bid(domain='domain', bid_amount=0.4, blind_amount=100)
```

On some endpoints you can pass options, please refer them to the following documentation: https://github.com/namebasehq/api-documentation/blob/master/marketplace-api.md
