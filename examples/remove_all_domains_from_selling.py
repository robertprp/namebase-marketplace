import argparse
import sys
from namebase_marketplace import marketplace
from script.script_c import Script

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='REMOVE EVERY DOMAIN FROM MARKETPLACE.')

    parser.add_argument('--cookie', required=True,  help='Input your namebase cookie (namebase-main).')
    parser.add_argument('--remove', dest='remove', required=True,
                        help='By activating this flag, you agree to remove every domain you own from marketplace.')

    args = parser.parse_args()
    marketplace = marketplace.Marketplace(namebase_cookie=args.cookie)
    script = Script(marketplace)
    script.remove_all_names_from_selling_page()