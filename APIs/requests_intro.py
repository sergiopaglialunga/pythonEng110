import requests

r = requests.get("https://api.postcodes.io/postcodes/M44D")

# print(r, type(r))
print(r.status_code)
# print(r.headers, type(r.headers))
# print(r.headers['Date'])
print(r.content)

if r.status_code == 200:
    content = r.content
    print(content, type(content))
    content_json = r.json()
    print(content_json, type(content_json))
    result = content_json['result']
    print(result['eastings'],result['northings'])
    print(result.get('eastings'),result.get('northings'))

# Print the easting and northings for this profile

