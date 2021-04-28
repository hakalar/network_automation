import json

people_string = """
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-email.com"],
            "has_license": false
        },
        {
            "name": "Jone Doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
"""

data = json.loads(people_string)
print(data)
print(type(data))
print(type(data['people']))

# remove phone number and convert back to json string
for person in data['people']:
    print(person)
    print(person['name'])
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print (new_string)

