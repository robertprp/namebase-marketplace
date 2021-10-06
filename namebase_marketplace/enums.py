__all__ = ['Utils']
API_VERSION = 'v0'


class Endpoint():
    MARKETPLACE = '/api/domains/marketplace/'
    SALE_HISTORY = '/api/domains/sold/'
    USER_INFO = '/api/user'
    OPEN_BID = f'/api/{API_VERSION}/auction/'  # + <DOMAIN>/bid
    MAKE_OFFER = f'/api/{API_VERSION}/marketplace/'
    OFFERS_RECEIVED = f'/api/{API_VERSION}/offers/received'
    OFFERS_HISTORY = f'/api/{API_VERSION}/offers/history'
    ACCEPT_OFFER_BID = f'/api/{API_VERSION}/offers/bid'
    DOMAIN_HISTORY = MAKE_OFFER
    LOGIN = '/auth/local/account-login'
    ENDING_SOON = '/api/domains/ending-soon/'  # + OFFSET
    GET_DOMAIN = '/api/domains/get/'
    WATCH_DOMAIN = '/api/domains/watch/'
    DLINK = '/api/user/dlinks'
    MY_SALE_DOMAINS = '/api/user/domains/listed'
    MY_DOMAINS = '/api/user/domains/not-listed/'
    API_DOMAINS = '/api/domains/'

class Utils():
    BID = '/bid'
    HISTORY = '/history'
    BUY_NOW = '/buynow'
    LIST = '/list'
    LISTED = '/listed'
    CANCEL = '/cancel'
    CONSENT = '/consent'
    SORT_KEY_ARRAY = ['bid', 'price', 'name', 'date']
    DEFAULT_SORT_KEY = 'bid'
    TRANSFER = '/transfer'
    SORT_DIRECTION_ARRAY = ['asc', 'desc']
    DEFAULT_OPTIONS_MY_DOMAINS = {"sortKey":"acquiredAt","sortDirection":"desc","limit":100}
    @staticmethod
    def parse_bid(amount):
        number_str = str(amount)
        if isinstance(amount, int):
            number_str += '.'
        while len(number_str) < 8:
            number_str += '0'
        return number_str

    @staticmethod
    def get_real_amount(amount):
        part1 = amount[:-6]
        part2 = amount[-6:]
        return float(f'{part1}.{part2}')