import argparse
import json
#import xcast
#from jinja2 import Template
from jinja2 import Environment, PackageLoader

# TODO: fetch source and create the first n entries
# TODO: generate html
def main():
    with open('data/sources.json') as fh:
        sources = json.load(fh)

    parser = argparse.ArgumentParser()
    parser.add_argument('--list', help = 'List sources', action='store_true')
    parser.add_argument('--html', help = 'Generate HTML', action='store_true')
    args = parser.parse_args()

    
    if args.list:
        for s in sources:
            print('{:20} {}'.format(s.get('name', ''), s.get('title', '')))
    elif args.html:
        env = Environment(loader=PackageLoader('xcast', 'templates'))
        template = env.get_template('index.html')
        with open('html/index.html', 'w') as fh:
            fh.write(template.render(source = sources))
    else:
        parser.print_help()


main()

