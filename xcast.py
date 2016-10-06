import argparse
import glob
import json
import os
import re
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
        episodes = []
        people = read_people()
        #print(people)
        #exit()
        for s in sources:
            print("Processing source {}".format(s['name']))
            file = 'data/' + s['name'] + '.json'
            if os.path.exists(file):
                with open(file) as fh:
                    try:
                        episodes.extend(json.load(fh))
                    except json.decoder.JSONDecodeError as e:
                        print("ERROR: Could not read in {}".format(file))
                        print(e)
                        pass

        for e in episodes:
            for g in e['guests'].keys():
                if g not in people:
                    exit("ERROR: '{}' is not in the list of people".format(g))
                    #people[g] = {
                    #    'info': e['guests'][g],
                    #    'episodes' : []
                    #}
                people[g]['episodes'].append(e)
            #print(e)

        env = Environment(loader=PackageLoader('xcast', 'templates'))
        person_template = env.get_template('person.html')
        if not os.path.exists('html/p/'):
            os.mkdir('html/p/')
        people_list = []
        for p in people.keys():
            print(p)
            print(people[p])
            with open('html/p/' + p, 'w') as fh:
                fh.write(person_template.render(id = p, person = people[p]))

        main_template = env.get_template('index.html')
        with open('html/index.html', 'w') as fh:
            fh.write(main_template.render(sources = sources, people = people, people_ids = sorted(people.keys()) ))
    else:
        parser.print_help()

def read_people():
    people = {}
    for filename in glob.glob("data/people/*.txt"):
        this = {}
        nickname = os.path.basename(filename)
        nickname = nickname[0:-4]
        #print(nickname)
        with open(filename) as fh:
            for line in fh:
                line = line.rstrip('\n')
                k,v = re.split(r'\s*:\s*', line, maxsplit=1)
                #print(v)
                this[k] = v
        people[nickname] = {
            'info': this,
            'episodes' : []
        }

    return people


main()

