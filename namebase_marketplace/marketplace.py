"""
Description:
    Implements Python client library for Namebase marketplace API.
"""
from namebase_marketplace.enums import Endpoint, Utils
from namebase_marketplace.utils import Request

import requests
import urllib.parse
import json

DEFAULT_API_ROOT = "https://www.namebase.io"


def _get_cookies(email, pwd):
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


def encode_dict(dictionary, lower=True):
    if dictionary:
        lowered_dict = dict([(k, str(v).lower() if lower else str(v)) for k, v in dictionary.items()])
        return urllib.parse.urlencode(lowered_dict)
    else:
        return ''


class Marketplace:
    def __init__(self, email=None, pwd=None, namebase_cookie=None, api_root=DEFAULT_API_ROOT):
        headers = {
            "Accept": 'application/json',
            "Content-Type": 'application/json',
        }

        self.cookies = _get_cookies(email=email, pwd=pwd) if not namebase_cookie else {"namebase-main" : namebase_cookie}
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
        return self.request.get(Endpoint.DOMAIN_HISTORY + f'{domain}' + Utils.HISTORY)

    def list_domain(self, domain: str, amount, description="", asset="HNS", options={}):
        """
        @:param options: dict

        You can send options to this endpoint as an example:
        options = {"amount":"4344","asset":"HNS","description":"test"}
        """
        params = {"amount": Utils.parse_bid(amount), "asset": asset, "description": description}
        mark = '?'
        if options is None:
            options = {}
            mark = ''
        return self.request.post(Endpoint.DOMAIN_HISTORY + f'{domain}{Utils.LIST}{mark}{encode_dict(options)}',
                                 data=params, json_data=params)

    def update_domain(self, domain: str, amount, description="", asset="HNS", options={}):
        """
        @:param options: dict

        You can send options to this endpoint as an example:
        options = {"amount":"4344","asset":"HNS","description":"test"}
        """
        return self.list_domain(domain=domain, amount=amount, description=description, asset=asset, options=options)

    def cancel_listing(self, domain: str):
        """ Removes domain from marketplace. """
        return self.request.post(Endpoint.DOMAIN_HISTORY + f'{domain}{Utils.CANCEL}', data={}, json_data={})

    def purchase_now(self, domain: str, listing_id: str):
        params = {"listingId": listing_id}
        return self.request.post(Endpoint.DOMAIN_HISTORY + f'{domain}{Utils.BUY_NOW}', data=params, json_data=params)

    def open_bid(self, domain: str, bid_amount, blind_amount):
        params = {
            "bidAmount": Utils.parse_bid(amount=bid_amount),
            "blindAmount": Utils.parse_bid(amount=blind_amount)
        }

        return self.request.post(Endpoint.OPEN_BID + f'{domain}{Utils.BID}', data=params)

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
        return self.request.post(Endpoint.MAKE_OFFER + f'{domain}{Utils.BID}', data=params, json_data=params)

    def get_domain_info(self, domain: str):
        return self.request.get(Endpoint.GET_DOMAIN + f'{domain}')

    def get_domain_price(self, domain: str):
        res = self.request.get(Endpoint.MAKE_OFFER + f'{domain}')
        if not res['listing']:
            raise Exception("Domain is not listed.")
        else:
            return Utils.get_real_amount(res['listing']['amount'])

    def add_to_watchlist(self, domain: str):
        return self.request.post(Endpoint.WATCH_DOMAIN + f'{domain}', params={}, data={})  # as in namebase

    def remove_from_watchlist(self, domain: str):
        return self.add_to_watchlist(domain=domain)

    def get_my_domains(self, offset=0, options={}):
        if not options:
            options = "sortKey=acquiredAt&sortDirection=desc"
        url = Endpoint.MY_DOMAINS + f'/{offset}?{options}'
        response = self.request.get(url)
        response_domains = response['domains']
        domains = []
        while len(response_domains) > 0:
            [domains.append(i) for i in response_domains]
            offset += 1
            url = Endpoint.MY_DOMAINS + f'/{offset}?{options}'
            response_domains = self.request.get(url)
            response_domains = response_domains['domains']
        return domains

    def get_my_onsale_domains(self):
        return self.request.get(Endpoint.MY_SALE_DOMAINS)

    def consent_offers(self, domain: str, consent: bool):
        params = {"doesConsentToOffers": consent}
        return self.request.post(Endpoint.DOMAIN_HISTORY + f'{domain}{Utils.CONSENT}', data=params,
                                 json_data=params)  # as in namebase

    def transfer_domain_on_chain(self, domain: str, hns_address: str):
        """
        Test response: {"transferId":"<transferID>","type":"internal","success":true}
        """
        params = {"address" : hns_address}
        return self.request.post(Endpoint.API_DOMAINS + f'{domain}' + Utils.TRANSFER, data=params, json_data=params)

    def get_offers(self):
        query_string_params = {
            'offset' : 0,
            'sortKey': "createdAt",
            'sortDirection': 'desc'
        }
        # default offset is set to 15 per request
        res = self.request.get(Endpoint.OFFERS_RECEIVED + f'?{encode_dict(query_string_params, lower=False)}')
        n_domains = res['totalCount']
        domains = res['domains']
        doms = []
        while n_domains > 0:
            for domain in domains:
                name = domain['domain']
                highestOffer = domain['highestCurrentOffer']
                domainOwnerId = domain['domainOwnerId']
                domainInfo = {
                    "name": name,
                    "offer": highestOffer,
                    "ownerId": domainOwnerId
                }
                doms.append(domainInfo)
            query_string_params['offset'] = query_string_params['offset'] + 15
            n_domains = n_domains - 15
            res = self.request.get(Endpoint.OFFERS_RECEIVED + f'?{encode_dict(query_string_params, lower=False)}')
            domains = res['domains']

        return doms
    def accept_offer(self, offer_id):
        params = {
            'bidId': offer_id
        }
        return self.request.post(Endpoint.ACCEPT_OFFER_BID, data=params, json_data=params)
    def get_offers_domain_history(self, domainOwnerId):
        params = {
            'domainOwnerId' : domainOwnerId
        }
        return self.request.get(Endpoint.OFFERS_HISTORY + f'?{encode_dict(params, lower=False)}')