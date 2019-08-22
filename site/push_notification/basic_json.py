__author__ = 'chance'

import json

file_name = "league.json"

with open (file_name) as f:
    data = json.load(f)

for member in data['members']:
    print(member)