Collecting information about interviews and presentations
of Open Source projects and Technology in general.


Collecting information from several podcasts.

The list of podcasts can be found in data/srouces.json and it needs a lot more items.
Each podcast has its own json file in the data/ directory in which we list the episodes.
Each person (both guests and hosts) have their own file in the data/people/ directory.

For each episode in a podcast series we collect:

```
  {
    "ep" : "EPISODE NUMBER",       (was not included in every case, but should be added)
    "guests": {
      "guest-name" : {}
    },
    "hosts" : {
        "host-name" : {}
    },
    "topics" : [                (has not been used in most cases, I am not sure if we need this)
      {
        "name": "TOPIC NAME",
        "url": "http://..."
      }
    ],
    "keywords": ["perl", "web", "dancer"],
    "permalink": "URL of the HTML page of the specific episode",
    "title" : "TITLE of the episodes",
    "date": "2016-08-23"
  },
```


For each person we collect:
```
name:      Full name
twitter:   account ID
github:    accoung ID
home:      URL of their personal home page
```

Site layout
------------
```
/
/p/person-code
/s/source
```

TODO:
-----
* Include the episode number for each episode
* Add the GitHub/Twitter username of each person and the "home" page of each person.
* For each source add a description.
* Include talks from conferences
* Include screencasts and other non-conference videos.
* Include a picture of each person?
* The Floss Weekly had a lot of other "providers" to subscribe through. Check those out.
* The Floss Weekly has both an audio and vidoe feed. Some other podcast might have too. Shall we include those too?
* TODO add icons for RSS feed and iTunes subscribe button
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

