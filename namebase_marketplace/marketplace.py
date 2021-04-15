"""
Description:
    Implements Python client library for Namebase marketplace API.
"""
from namebase_marketplace.enums import Endpoint, Utils
from namebase_marketplace.utils import Request

import requests
import urllib.parse

DEFAULT_API_ROOT = "https://www.namebase.io"


def get_cookies(email, pwd):
    if email is None or pwd is None:
        return None
    params = {
        'email': email,
        'password': pwd,
        'token': ''
    }
    res = requests.post(DEFAULT_API_ROOT + Endpoint.LOGIN, params=params)
    cookies = res.cookies.get_dict()
    return cookies


def encode_dict(dictionary):
    if dictionary:
        lowered_dict = dict([(k, str(v).lower()) for k, v in dictionary.items()])
        return urllib.parse.urlencode(lowered_dict)
    else:
        return ''


class Marketplace:
    def __init__(self, email=None, pwd=None, api_root=DEFAULT_API_ROOT):
        headers = {
            "Accept": 'application/json',
            "Content-Type": 'application/json',
        }
        self.cookies = get_cookies(email=email, pwd=pwd)
        self.request = Request(api_base_url=api_root,
                               headers=headers,
                               cookies=self.cookies,
                               timeout=30)

    def get_user_info(self):
        """" GET USER INFO """
        return self.request.get(Endpoint.USER_INFO)

    def get_marketplace_domains(self, offset=0, options=None):
        """ Returns 100 sorted names, paginated by an offset parameter. For example, offset=0 will get the first 100
        listings and offset=100 will return listings 101-200.

        ref: https://github.com/namebasehq/api-documentation/blob/master/marketplace-api.md#parameters
        """

        mark = '?'
        if options is None:
            options = {}
            mark = ''
        return self.request.get(Endpoint.MARKETPLACE + f'{offset}{mark}{encode_dict(options)}')

    def get_sale_history(self, offset=0, options=None):
        mark = '?'
        if options is None:
            options = {}
            mark = ''
        return self.request.get(Endpoint.SALE_HISTORY + f'{offset}{mark}{encode_dict(options)}')

    def get_domain_sale_history(self, domain: str):
        return self.request.get(Endpoint.MARKETPLACE + f'{domain}' + Utils.HISTORY)

    def list_domain(self, domain: str, options: dict):
        return self.request.post(Endpoint.MARKETPLACE + f'{domain}{Utils.LIST}&{encode_dict(options)}')

    def update_domain(self, domain: str, options: dict):
        return self.list_domain(domain=domain, options=options)

    def cancel_listing(self, domain: str):
        return self.request.post(Endpoint.MARKETPLACE + f'{domain}{Utils.CANCEL}')

    def purchase_now(self, domain: str):
        return self.request.post(Endpoint.MARKETPLACE + f'{domain}{Utils.BUY_NOW}')

    def open_bid(self, domain: str, bid_amount, blind_amount):
        params = {
            "bidAmount": Utils.parse_bid(amount=bid_amount),
            "blindAmount": Utils.parse_bid(amount=blind_amount)
        }
        return self.request.post(Endpoint.OPEN_BID + f'{domain}{Utils.BID}', params=params)

    def create_bid(self, domain: str, bid_amount, blind_amount):
        """@Wrapper method"""
        return self.open_bid(domain=domain, bid_amount=bid_amount, blind_amount=blind_amount)

    def get_ending_soon(self, offset=0, options=None):
        mark = '?'
        if options is None:
            options = {}
            mark = ''
        return self.request.get(Endpoint.ENDING_SOON + f'{offset}{mark}{encode_dict(options)}')

    def make_offer(self, domain: str, amount):
        params = {"buyOfferAmount": Utils.parse_bid(amount=amount)}
        return self.request.post(Endpoint.OPEN_BID + f'{domain}{Utils.BID}', params=params)

    def get_domain_info(self, domain: str):
        return self.request.get(Endpoint.GET_DOMAIN + f'{domain}')

    def add_to_watchlist(self, domain: str):
        return self.request.post(Endpoint.WATCH_DOMAIN + f'{domain}', params={})  # as in namebase
