#!/bin/python3
import requests
import csv
import json

#import certifi

# Use Airship API to pull a report in CSV format.
# "Write a program that returns data as a CSV file and Timestamp, Username, Event Name, Numbers of records recorded, Event ID"

#http = urllib3.PoolManager(ca_certs=certifi.where())
#r = http.request('Fetch', 'https://jsonplaceholder.typicode.com/todos/1')
#rjson = json(r)
# for thing in rjson:
#    print(thing)
# print(r.status)


raw_request = requests.get('https://jsonplaceholder.typicode.com/todos/1')
export_parsed = requests.compat.json.loads(raw_request.text)

with open('report_export.csv', 'w', newline='') as file:

    for thing in export_parsed:
        file.write(thing)
