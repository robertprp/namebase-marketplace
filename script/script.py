from namebase_marketplace import marketplace
import time

import argparse


class Script():
    def __init__(self, m):
        self.m = m

    def sell_domains(self, price, description, custom_domains=True, domains=None):
        if domains is None:
            domains = []

        if custom_domains:
            my_domains_not_for_sale = domains
        else:
            my_domains_not_for_sale = self.m.get_my_domains()

        for domain in my_domains_not_for_sale:
            self.m.list_domain(domain=domain['name'], amount=price, description=description)
            time.sleep(0.5)

    def consent_potential_offers(self, domain, consent: bool):
        self.m.consent_offers(domain=domain, consent=consent)

    def remove_all_names_from_selling_page(self):
        selling_domains = self.m.get_my_onsale_domains()
        for domain in selling_domains['domains']:
            self.m.cancel_listing(domain=domain['name'])

    def edit_domain_sale_description(self, domain, description):
        domain_price = self.m.get_domain_price(domain=domain)
        self.m.list_domain(domain=domain, amount=domain_price, description=description)

    def get_domains_on_sale(self):
        domains_on_sale = self.m.get_my_onsale_domains()
        BASE_URL = 'https://www.namebase.io/domains/'
        for domain in domains_on_sale['domains']:
            print(f'{BASE_URL}{domain["name"]}')


if __name__ == '__main__':
    marketplace = marketplace.Marketplace()
    script = Script(marketplace)
    """Sell domains."""
    """This will put all your domains not for sale at a price of 200HNS with description TEST"""
    #script.sell_domains(price=200, description='Test', custom_domains=False)
    """This will put domains you give the method not for sale at a price of 200HNS with description TEST"""
    domains = ['mydomain', 'mysecondomain']
    #script.sell_domains( price=200, description='Test', custom_domains=True, domains=domains)

    """Consent Potential Offers."""
    script.consent_potential_offers( domain='domain',
                             consent=False)  # Do not allow people send offers to domain 'domain'.
    script.consent_potential_offers( domain='domain',
                             consent=True)  # Do allow people send offers to domain 'domain'.

    """Remove all my selling domains from sale """
    script.remove_all_names_from_selling_page()


    """Edit domain sale description"""
    new_description = 'New desc'
    domain = 'test_domain'
    script.edit_domain_sale_description(domain, new_description)

    """Get the list of all names I am selling with urls on namebase"""
    script.get_domains_on_sale()