""" reportusage.py

Retrieves data from website views by using Flask-Track-Usage plugin.
Includes IPs among other information. This data is formatted and then
sent to a text file. """

from __future__ import print_function
from manage import UsageData
from datetime import timedelta
from sys import argv
import sys
import json
import requests

sys.stdout = open('usagedata.txt', 'w')

badVals = {'remote_addr': '173.72.47.206',
           'xforwardedfor': '173.72.47.206',
           'browser': 'seamonkey'}

user_agent_keys = ['platform', 'version', 'language', 'browser']

Filter = False

try:
    if argv[1] == '--filter':
        Filter = True
except IndexError:
    pass

for hit in UsageData.get_usage():
    valid = True
    if Filter:
        for key, item in badVals.items():
            if key in user_agent_keys:
                if hit['user_agent'][key] == item:
                    valid = False
            elif hit[key] == item:
                    valid = False
    if valid:
        # Print Date
        date = hit['date']
        timediff = timedelta(hours=-5)
        date += timediff
        fmtdate = date.strftime('%m/%d/%Y - %H:%M:%S')
        print(fmtdate)
        hit.pop('date')

        # Print Everything Else
        for key, item in hit.items():
            print('{0}: {1}'.format(key, item))

        IPAdd = hit['remote_addr']
        freeGeoText = requests.get('http://freegeoip.net/json/' + IPAdd).text
        GeoDict = json.load(freeGeoText)

        # Print freegeoip.net data
        for key, item in GeoDict.items():
            print('{0}: {1}'.format(key, item))

        print()
