The data in this repository is presented at http://xcast.szabgab.com/

The list of podcasts can be found in ```data/sources.json```.
Each podcast has its own json file in the ```data/``` directory in which we list the episodes.
The name of the podcast is the name of the appropriate JSON file.
For example the episodes of the ```cmos``` podcast are listed in the ```data/cmos.json``` file.

For each episode in a podcast series we collect the following fields:

ep - the episode number
guests:   a list of the guest, each guest is represented her/his name in full-name  format.

The same value, followed by the .txt extension is used to hold information about that person
in the ```data/people/``` directory.
So if the person is called "Foo Bar Qux" then the file name will be ```foo-bar-qux.txt```

```
hosts:     A list of the hosts. Just like the list of the guest.
keywords:  A list of words (e.g. project names) that are important in the episode.
permalink: The URL of the episode.
title:     The title of the episode.
date:      The date of the episode.
```

The file looks like this:

```
[
  {
    "ep" : "EPISODE NUMBER",
    "guests": {
      "guest-name" : {}
    },
    "hosts" : {
        "host-name" : {}
    },
    "keywords": ["perl", "web", "dancer"],
    "permalink": "URL of the HTML page of the specific episode",
    "title" : "TITLE of the episodes",
    "date": "2016-08-23"
  },
  ...
]
```

Each person (both guests and hosts) have their own file in the ```data/people/``` directory.
These are text files in "field:value" format.

For each person we collect the following 4 fields, but some people might not have all 4:

```
name:      Full name
twitter:   account ID
github:    accoung ID
home:      URL of their personal home page
country:   Country name
```

The ```data/tags.csv``` file contains a mapping of keywords to URLs and descriptions.
It is still under 'design'. Don't bother with it for now.

```
keyword;http://...
```

Collection Process
-------------------
* Select the podcast you'd like to process. (e.g 'cmos' stored in data/cmos.json).
* Visit the main web-site of the process. (the URL can be found in the data/sources.json file).
* Find the next episode that has not been recorded in the data file. (data/cmos.json in our example).
* Find out the details need to be collected. (See the list of details above at the description of the files.)
* Save the data in the json file (data/cmos.json in our example)
* Save the information about the individual people in the (data/people/*.txt) file.
* Add the files to git, commit, push, send a pull-request.

* If you have a local copy of all the files, you can veryfy the correctness of
the format by running ```python3 xcast.py --html``` fFor this you'll have ```python3```
installed and the ```jinja2``` package.


Site layout
------------
```
/
/p/person-code
/s/source
/t/tag
```

TODO (or maybe not?):
-----------------------
* Include the episode number for each episode
* Add the GitHub/Twitter username of each person and the "home" page of each person.
* For each source add a description.
* Include talks from conferences
* Include screencasts and other non-conference videos.
* Include a picture of each person?
* The Floss Weekly had a lot of other "providers" to subscribe through. Check those out.
* The Floss Weekly has both an audio and video feed. Some other podcast might have too. Shall we include those too?
* Add Forkme on GitHub badge


SETUP
------
```
virtualenv venv3 -p python3
source venv3/bin/activate
pip install jinja2
```

Development server
-------------------
```python3 server.py```

http://localhost:8000/


Other sources we might add
----------------------------
* http://www.meta-cast.com/
* http://www.angryweasel.com/ABTesting/

