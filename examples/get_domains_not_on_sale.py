import argparse
import sys
from namebase_marketplace import marketplace
from script.script_c import Script

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get all my domains I dont have on sale.')

    parser.add_argument('--cookie', required=True,  help='Input your namebase cookie (namebase-main).')

    args = parser.parse_args()
    marketplace = marketplace.Marketplace(namebase_cookie=args.cookie)
    script = Script(marketplace)
    domains = script.get_domains_not_on_sale()
    print(' '.join(domains))
