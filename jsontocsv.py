#!/bin/python3
from requests import get
from csv import DictWriter
from json import loads
from datetime import datetime

# Timestamps report_filename
# Pulls sample data json response from jsonplaceholder
# Converts response to json
# Converts json to csv
# Saves json file as "report_export*timestamp*.csv"

# File Name for Export

CurTime = datetime.now()
timestamp = str(datetime.timestamp(CurTime))
report_filename = "ReportExport-"+timestamp+".csv"

# Requests data and ingest

raw_request = get('https://jsonplaceholder.typicode.com/todos/1')
export_parsed = loads(raw_request.text)

# Write export_parsed to CSV file

with open(report_filename, 'w', newline='') as file:
    itrobj = DictWriter(file, export_parsed.keys())
    itrobj.writerow(dict((kn, kn) for kn in export_parsed.keys()))
    itrobj.writerow(export_parsed)
