import argparse
import sys
from namebase_marketplace import marketplace
from script.script_c import Script

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sell domains.')

    parser.add_argument('--cookie', required=True,  help='Input your namebase cookie (namebase-main).')
    parser.add_argument('--enumerate', dest='enum',  nargs='+', default=[], required=False,
                        help='Enumerate domains to be put on marketplace, you must own these domains!!! , as an example: --enumerate domain1 domain2 domain3')
    parser.add_argument('--all', required=False,  action='store_true',
                        help='Put on marketplace every domain you own and its not listed on namebase marketplace already with a description and a common price.')
    parser.add_argument('--price', required='--enumerate' in sys.argv or '--all' in sys.argv, dest='price', type=float, help='Input the price of the domains to be put on marketplace')
    parser.add_argument( '--description', required='--enumerate' in sys.argv or '--all' in sys.argv, type=str, dest='description', nargs='+', default=[],
                       help='Input the description of the domains to be put on marketplace')

    args = parser.parse_args()
    if args.enum and args.all:
        parser.error("--ennumerate can't be spawned along --all. Use one or the other. Not together.")

    marketplace = marketplace.Marketplace(namebase_cookie=args.cookie)
    script = Script(marketplace)
    description = ' '.join(args.description)
    if args.all:
        script.sell_domains(price=args.price, description=description, custom_domains=False)
    elif args.enum:
        script.sell_domains(price=args.price, description=description, custom_domains=True, domains=args.enum)