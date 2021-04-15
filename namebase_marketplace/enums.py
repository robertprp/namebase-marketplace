__all__ = ['Utils']
API_VERSION = 'v0'

from enum import Enum


class Endpoint():
    MARKETPLACE = '/api/domains/marketplace/'
    SALE_HISTORY = '/api/domains/sold/'
    USER_INFO = '/api/user'
    OPEN_BID = f'/api/{API_VERSION}/auction/'  # + <DOMAIN>/bid
    LOGIN = '/auth/local/account-login'
    ENDING_SOON = '/api/domains/ending-soon/'  # + OFFSET
    GET_DOMAIN = '/api/domains/get/'
    WATCH_DOMAIN = '/api/domains/watch/'

class Utils():
    BID = '/bid'
    HISTORY = '/history'
    BUY_NOW = '/buynow'
    LIST = '/list'
    CANCEL = '/cancel'
    SORT_KEY_ARRAY = ['bid', 'price', 'name', 'date']
    DEFAULT_SORT_KEY = 'bid'
    SORT_DIRECTION_ARRAY = ['asc', 'desc']

    @staticmethod
    def parse_bid(amount):
        number_str = str(amount)
        if isinstance(amount, int):
            number_str += '.'
        while len(number_str) < 8:
            number_str += '0'
        return number_str
