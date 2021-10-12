import argparse
import sys
from namebase_marketplace import marketplace
from script.script_c import Script

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Consent offers on a specific domain. In order to disallow or not consent a domain to receive offers you just need to run the test without the --consent flag.')

    parser.add_argument('--cookie', required=True,  help='Input your namebase cookie (namebase-main).')
    parser.add_argument('--domain', dest='domain', required=True, type=str,
                        help='Domain to consent offers or not.')
    parser.add_argument('--consent', dest='consent', required=False, action='store_true', default=False,
                        help='Whether to consent offers or not. Use --consent to consent offers and dont use this flag to unconsent/disallow offers.')

    args = parser.parse_args()
    marketplace = marketplace.Marketplace(namebase_cookie=args.cookie)
    script = Script(marketplace)
    script.consent_potential_offers(domain=args.domain, consent=args.consent)

