import requests
import json
import csv

url = 'api.capturedata.ie​'

with open('data.json', 'r') as infile:
  indata = json.load(infile)
  output = []

for data in indata:
  r = requests.post(url, json=data)
  output.append(json.loads(r.text))