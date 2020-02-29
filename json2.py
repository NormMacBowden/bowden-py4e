import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_367897.json'
uh = urllib.request.urlopen(url)

data = uh.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)["comments"]
print('User count:', len(info))

print(sum([int(i["count"]) for i in info])) # here, info is a list of dictionaries, where i is a dictionary