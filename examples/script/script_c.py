import sys

from namebase_marketplace import marketplace
import time


class Script:
    def __init__(self, m):
        self.m = m

    def sell_domains(self, price, description, custom_domains=True, domains=None):
        if domains is None:
            domains = []
        if custom_domains:

            my_domains_not_for_sale = domains
            for domain in my_domains_not_for_sale:
                self.m.list_domain(domain=domain, amount=price, description=description)
                time.sleep(0.5)
                print(f'[===] Successfully listed domain: {domain} at a price {price} with description {description}')
        else:
            my_domains_not_for_sale = self.m.get_my_domains()
            for domain in my_domains_not_for_sale:
                self.m.list_domain(domain=domain['name'], amount=price, description=description)
                time.sleep(0.5)
                print(f'[===] Successfully listed domain: {domain["name"]} at a price {price} with description {description}')




    def consent_potential_offers(self, domain, consent: bool):
        l = self.m.consent_offers(domain=domain, consent=consent)
        print(l)
    def remove_all_names_from_selling_page(self):
        selling_domains = self.m.get_my_onsale_domains()
        for domain in selling_domains['domains']:
            self.m.cancel_listing(domain=domain['name'])
            time.sleep(0.3)
            print(f'[{"+" * 10}] Domain {domain["name"]} was removed from marketplace. [{"+" * 10}]')
    def edit_domain_sale_description(self, domain, description):
        domain_price = self.m.get_domain_price(domain=domain)
        self.m.cancel_listing(domain=domain)
        time.sleep(0.5)
        self.m.list_domain(domain=domain, amount=domain_price, description=description)


    def get_domains_on_sale(self):
        domains_on_sale = self.m.get_my_onsale_domains()
        BASE_URL = 'https://www.namebase.io/domains/'
        for domain in domains_on_sale['domains']:
            print(f'{BASE_URL}{domain["name"]}')
        return [domain['name'] for domain in domains_on_sale['domains']]
    def get_domains_not_on_sale(self):
        print('If you have a lot of domains this might take a bit. Be patient.')
        return self.m.get_my_domains()
    def send_domain_on_chain(self, domain, hns_address):
        res = self.m.transfer_domain_on_chain(domain=domain, hns_address=hns_address)
        return res

    def should_accept_offer(self, offerAmount, threshold):
        return float(offerAmount) >= threshold

    def get_best_offer(self, bestBidId, domain_history):
        negotiations = domain_history['negotiations']
        for negotiation in negotiations:
            history = negotiation['history']
            for hist in history['bids']:
                amount = hist['amount']
                id = hist['bidId']
                isAccepted = hist['isAccepted']
                if id == bestBidId and not isAccepted:
                    return {"id": id, "amount": float(amount)}

        return {}

    def filter_out_offers(self, offers, threshold):
        return [offer for offer in offers if float(offer['offer']) >= threshold]

    def get_offers_to_accept(self, threshold):
        offers = self.m.get_offers()
        filtered_offers = self.filter_out_offers(offers=offers, threshold=threshold)
        should_accept_offers = []
        for offer in filtered_offers:
            try:
                ownerId = offer['ownerId']
                name = offer['name']
                history = self.m.get_offers_domain_history(domainOwnerId=ownerId)
                bestBidId = history['negotiations'][0]['bestBidId']
                if bestBidId:
                    best_offer = self.get_best_offer(bestBidId=bestBidId,
                                                     domain_history=history)
                    offerAmount = best_offer['amount']
                    id = best_offer['id']
                    should_accept = self.should_accept_offer(offerAmount=offerAmount,
                                                             threshold=threshold)
                    if should_accept:
                        should_accept_offers.append({"id": id, "amount": offerAmount, "domain_name": name})
            except:
                continue
        print("Should I accept all this following offers? Current minimum bid threshold is: " + str(threshold))

        for offer in should_accept_offers:
            print(f"Domain Name: {offer['domain_name']} - Bid Amount: {offer['amount']} HNS")

        decision = input('Input Y (Yes) / N (No): ').lower()
        if decision == 'yes' or decision == 'y':
            for offer in should_accept_offers:
                self.m.accept_offer(offer_id=offer['id'])
                print(f"NEW SALE - Name {offer['domain_name']} was just sold for {offer['amount']} HNS.")
        else:
            print('Please, relaunch the script whenever you want to sell domains. Bye.')
            sys.exit(0)

# if __name__ == '__main__':
#     marketplace = marketplace.Marketplace()
#     script = Script(marketplace)
#     """Sell domains."""
#     """This will put all your domains not for sale at a price of 200HNS with description TEST"""
#     #script.sell_domains(price=200, description='Test', custom_domains=False)
#     """This will put domains you give the method not for sale at a price of 200HNS with description TEST"""
#     domains = ['mydomain', 'mysecondomain']
#     #script.sell_domains( price=200, description='Test', custom_domains=True, domains=domains)
#
#     """Consent Potential Offers."""
#     script.consent_potential_offers( domain='domain',
#                              consent=False)  # Do not allow people send offers to domain 'domain'.
#     script.consent_potential_offers( domain='domain',
#                              consent=True)  # Do allow people send offers to domain 'domain'.
#
#     """Remove all my selling domains from sale """
#     script.remove_all_names_from_selling_page()
#
#
#     """Edit domain sale description"""
#     new_description = 'New desc'
#     domain = 'test_domain'
#     script.edit_domain_sale_description(domain, new_description)
#
#     """Get the list of all names I am selling with urls on namebase"""
#     script.get_domains_on_sale()
