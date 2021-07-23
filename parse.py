import csv
import json
import requests


def parse_files(csvFile, jsonFile):
  url = 'api.capturedata.ie​'
  headers = {
      "content-type": "application/json; charset=UTF-8",
  }
  data = {}

  with open(csvFile) as csvf:
    csvReader = csv.DictReader(csvf)

    for rows in csvReader:
      key = rows['ID']
      data[key] = rows

  with open(jsonFile, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, indent=2))
    r = requests.post(url, data=jsonf, headers=headers)
    print(r, r.text)


csvFile = r'data.csv'
jsonFile = r'data.json'
parse_files(csvFile, jsonFile)