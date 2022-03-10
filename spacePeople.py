import requests

data = requests.get('http://api.open-notify.org/astros.json')
json = data.json()

print(json)

for man in json['people']:
    print(man['name'])
    