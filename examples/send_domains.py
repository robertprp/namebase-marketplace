import argparse
import sys
from namebase_marketplace import marketplace
from script.script_c import Script

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Send as many domains as you want through handshake chain domain.')

    parser.add_argument('--cookie', required=True,  help='Input your namebase cookie (namebase-main).')
    parser.add_argument('--domains', dest='domains', required=True, nargs="+",
                        help='Domains to send as: --domains domainexample1 domainexample2 domainexample3')
    parser.add_argument('--address', dest='address', required=True, type=str,
                        help='Whether to consent offers or not. Use --consent to consent offers and dont use this flag to unconsent/disallow offers.')

    args = parser.parse_args()
    marketplace = marketplace.Marketplace(namebase_cookie=args.cookie)
    script = Script(marketplace)
    address = args.address

    domains = args.domains
    print(domains)
    for domain in domains:
        res = script.send_domain_on_chain(domain=domain, hns_address=address)
        print (res)
