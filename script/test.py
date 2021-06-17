from namebase_marketplace import marketplace
def get_domains_on_sale(m):
    domains_on_sale = m.get_my_onsale_domains()
    BASE_URL = 'https://www.namebase.io/domains/'
    for domain in domains_on_sale['domains']:
        print(f'{BASE_URL}{domain["name"]}')

if __name__ == '__main__':
    m = marketplace.Marketplace()
    l = m.get_my_domains()
    print(l)
