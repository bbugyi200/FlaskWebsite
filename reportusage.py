""" reportusage.py

Retrieves data from website views by using Flask-Track-Usage plugin.
Includes IPs among other information. This data is formatted and then
sent to a text file. """

from __future__ import print_function
from manage import UsageData
from datetime import timedelta
from sys import argv
import sys

sys.stdout = open('usagedata.txt', 'w')

badIPs = {'home': '173.72.47.206'}

Filter = False

try:
    if argv[1] == '--filter':
        Filter = True
except IndexError:
    pass

for hit in UsageData.get_usage():
    if not Filter or (hit['remote_addr'] not in badIPs.values()):
        # DATE
        date = hit['date']
        td = timedelta(hours=-5)
        date += td
        fmtdate = date.strftime('%m/%d/%Y - %H:%M:%S')
        print(fmtdate)
        hit.pop('date')

        for key, item in hit.items():
            print('{0}: {1}'.format(key, item))

        # SPACE
        print()
