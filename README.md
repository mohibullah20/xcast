Collecting information about interviews and presentations
of Open Source projects and Technology in general.


Collecting information from several podcasts.
The list of podcasts can be found in data/srouces.json
and it needs a lot more items.


For each podcast save the list of episodes in a single json file together with the information about each participant.
That would mean that we have duplicate information about people who participate in multiple podcasts which is probably not a large
number, but it will probably also mean it is going to be hard to cross-refrence these people.
We can have JSON format where each person is either have full-details in the podcast-specific json file
or has an id there and has all the information in a separate file.

/
/p/person-code



SETUP
------
virtualenv venv3 -p python3
source venv3/bin/activate
pip install jinja2

