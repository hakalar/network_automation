import json
import urllib.request
import requests

response = requests.get('http://api.stackexchange.com//2.2/questions?order=desc&sort=activity&site=stackoverflow')

# print(type(response.json()))
# print(response.json())

data = response.json()

# print(json.dumps(data, indent=2))
# print(type(json.dumps(data)))

# print(len(data['items']))

owners_reputation = dict()

for item in data['items']:
    # print(item['owner'])
    user_id = item['owner']['user_id']
    reputation = item['owner']['reputation']
    # print(user_id, reputation)
    owners_reputation[user_id] = reputation

# print(owners_reputation)

# for user_id in owners_reputation:
#     print(user_id)
#     print(owners_reputation[user_id])

# Throws an error
print('Test\n')
print(owners_reputation['13399023'])


