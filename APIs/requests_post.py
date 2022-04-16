import requests
from pprint import pprint
import json  # dump, dumps, load, loads

headers = {"Content-Type":"application/json"}
# data = json.dumps({"postcodes" : ["OX49 5NU", "M32 0JG", "NE30 1DP"]})

data = {"postcodes" : ["OX49 5NU", "M32 0JG", "NE30 1DP"]}
# I don't need to convert it in a json file, just change the keyword from data to json

# print(data, type(data))

r = requests.post(
    url="https://api.postcodes.io/postcodes",
    headers=headers,
    json=data
)

# print(r)
# # print(r.json().get("error"))
# print(r.json())

# for each postcode, print POSTCODE: region, parliamentary_constituency

content = r.json()
result = content.get('result')
# print(result[0].get('result'))

# print(result[0].get('result').get('postcode'), result[0].get('result').get('region'), result[0]['result']['codes']['parliamentary_constituency'])
# print(result[1].get('result').get('postcode'), result[0].get('result').get('region'), result[0]['result']['codes']['parliamentary_constituency'])
# print(result[2].get('result').get('postcode'), result[0].get('result').get('region'), result[0]['result']['codes']['parliamentary_constituency'])
for item in result:
    print(item.get('result').get('postcode'), item.get('result').get('region'),
          item['result']['codes']['parliamentary_constituency'])

for postcode in result:
    single_result = postcode['result']
    if single_result is not None:
        print(f"{single_result['postcode']}: {single_result['region']}, {single_result['codes']['parliamentary_constituency']}")
    else:
        print(f"{postcode['query']}: No postcode found")