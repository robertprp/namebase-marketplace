import argparse
import sys
from namebase_marketplace import marketplace
from script.script_c import Script

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Accept offers over a predefined threshold.')

    parser.add_argument('--cookie', required=True,  help='Input your namebase cookie (namebase-main).')
    parser.add_argument('--threshold', dest='threshold', required=True, type=float,
                        help='Minimum amount to accept an offer.')

    args = parser.parse_args()
    marketplace = marketplace.Marketplace(namebase_cookie=args.cookie)
    script = Script(marketplace)
    offers = script.get_offers_to_accept(threshold=args.threshold)

