import argparse
import sys
from namebase_marketplace import marketplace
from script.script_c import Script

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='EDIT DOMAIN DESCRIPTION.')

    parser.add_argument('--cookie', required=True,  help='Input your namebase cookie (namebase-main).')
    parser.add_argument('--domain', dest='domain', required=True, type=str,
                        help='Domain to change description.')
    parser.add_argument('--description', dest='description',nargs='+', default=[], required=True,
                        help='New description to put on domain')

    args = parser.parse_args()
    marketplace = marketplace.Marketplace(namebase_cookie=args.cookie)
    script = Script(marketplace)
    description = ' '.join(args.description)
    script.edit_domain_sale_description(domain=args.domain, description=description)