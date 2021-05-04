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
<img src="https://static.pepy.tech/badge/namebase-marketplace/week"/>
<a href="https://lgtm.com/projects/g/pretended/namebase-marketplace/context:python"><img alt="Language grade: Python" src="https://img.shields.io/lgtm/grade/python/g/pretended/namebase-marketplace.svg?logo=lgtm&logoWidth=18"/></a>
  
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

EXAMPLE WITHOUT AUTHENTICATION:
```python
from namebase_marketplace.marketplace import *
marketplace = Marketplace()
marketplace.get_marketplace_domains(offset=100) # Get 101-200 latest marketplace domains with default options
```

On some endpoints you can pass options, please refer them to the following documentation: https://github.com/namebasehq/api-documentation/blob/master/marketplace-api.md

### Donations

I have made this library open-sourced and free to use. However, if you consider this library has helped you, or you just want to sponsor me, donations are welcomed to one of my HANDSHAKE addresses. 

> hs1qynh72cuj7lawdcmvjtls4kk0p4auzmj5qq6v3r
