from __future__ import print_function
from manage import UsageData
from datetime import timedelta
import sys

sys.stdout = open('usagedata.txt', 'w')

for hit in UsageData.get_usage():
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
