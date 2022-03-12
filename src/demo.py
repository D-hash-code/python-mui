import json
import pandas as pd
import re
from pprint import pprint


def sentence_case(string):
    if string != '':
        result = re.sub('([A-Z])', r' \1', string)
        return result[:1].upper() + result[1:].lower()
    return


# Let's see what this data looks like as a dataframe
df = pd.read_csv('input.csv', index_col='id')
print(df.head())

# to export this into a MUI data grid friendly format we'll need to do a couple of things

# we will handle a dictionary that will ultimately be converted into JSON

output_dict = {}

# 1. let's form the column json blob

print("Here's the list of columns: ", list(df.columns))

output_dict['columns'] = [{
    "field": "id",
    "headerName": "ID",
    "width": 90
}]
for c in list(df.columns):
    output_dict['columns'].append({"field": c, "headerName": sentence_case(c), "width": 100})
print('-----------------------------------')

print("Here's the Dictionary so far:")
pprint(output_dict)
print('-----------------------------------')

# 2. Let's get the rows ready now

row_dict = df.to_dict('records')
print('-----------------------------------')
print('Here are some of the rows')
pprint(row_dict[:len(row_dict) // 2])

output_dict['rows'] = []
ind = list(df.index)
print('-----------------------------------')
for e, (i, r) in enumerate(zip(ind, row_dict)):
    if e < 4:
        print(f"index: {i}, row: {r}")

    r['id'] = i
    output_dict['rows'].append(r)

print('-----------------------------------')
print("Here's the Dictionary so far:")
pprint(output_dict)

# Looks like we have a match with our desired output
# Let's convert this to a JSON blob and write to a file

jsonFile = open("program_output.json", "w")
jsonFile.write(json.dumps(output_dict))
jsonFile.close()

# TODO: Package up into function
# TODO: Deal with varying cases where the index and columns are weirdly configured
# TODO: Replace NaNs with nulls
