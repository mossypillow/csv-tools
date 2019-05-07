#!/bin/python3

from csv import DictWriter
from json import loads, dumps

# Load CSV file Sample file in same directory
# Parse Data
# Formats CSV to organize data by timestamp for reference.

# Bubble sort function to sort by specified key 'keysort'


def bubble_sort(arr, keysort):
    def swap(i, j):
        arr[i][keysort], arr[j][keysort] = arr[j][keysort], arr[i][keysort]

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1][keysort] > arr[i][keysort]:
                swap(i - 1, i)
                swapped = True

    return arr

# Open and parse Json file.


raw_file = open('jsonsample.txt', 'r')
raw_data = loads(raw_file.read())

# Open and write csv return file.

with open('exportreport.csv', 'w+') as exportreport:
    sorted_data = bubble_sort(raw_data, 'timestamp')
    itrobj = DictWriter(exportreport, raw_data[0].keys())
    itrobj.writerow(dict((kn, kn) for kn in raw_data[0].keys()))
    for row in sorted_data:
        itrobj = DictWriter(exportreport, row.keys())
        itrobj.writerow(row)
