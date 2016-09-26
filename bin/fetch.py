import argparse
import json

def main():
    with open('data/sources.json') as fh:
        sources = json.load(fh)

    parser = argparse.ArgumentParser()
    parser.add_argument('--list', help = 'List sources', action='store_true')
    args = parser.parse_args()

    
    if args.list:
        for s in sources:
            print('{:20} {}'.format(s.get('name', ''), s.get('title', '')))
    else:
        parser.print_help()


main()

