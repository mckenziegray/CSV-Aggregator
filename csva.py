from sys import argv
from os import path
import csv

file_name = None

for a in argv[1:]:
    if path.isfile(a):
        file_name = a
        break

if file_name is None:
    print("Error: No valid file path given")
    quit(0)
elif path.splitext(file_name)[1] != ".csv":
    print("Error: File given is not CSV")
    quit(0)

cols_to_report = []
counts = {}

with open(file_name) as csv_file:
    reader = csv.DictReader(csv_file)
    
    cols_to_report = set(reader.fieldnames).intersection(map(str.capitalize, map(str.lower, argv)))

    if len(cols_to_report) == 0:
        # NOTE: Not sure what to do about columns with spaces in them, such as 'First Name'
        cols_to_report = reader.fieldnames

    for row in reader:
        for col in cols_to_report:
            if not col in counts:
                counts[col] = {}

            # Make sure the cell actually has a value
            if not row[col]:
                continue

            if row[col] in counts[col]:
                counts[col][row[col]] += 1
            else:
                counts[col][row[col]] = 1

# Sorts the dictionary by value
# Results in a list of tuples
for key in counts:
    sorted_count = sorted(counts[key].items(), key=lambda kv: kv[1], reverse=True)
    for tpl in sorted_count:
        print(f"{tpl[0]}: {tpl[1]}")
    print("-------------------------------")
