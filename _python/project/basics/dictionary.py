student = {'name': 'John', 'age': 25, 'courses': ['Math','CompSci']}

print(student['name'])
print(student.get('name'))

# calling non existant key
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

# add phone number, update name
student['phone'] = '555-555'
student['name'] = 'Jane'
print(student['name'])

# add phone number, update name all at once
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5557'})

# delete key and its value
del student['age']

# deletes and returns age and value
age = student.pop('age')

# looping through dictionary - returns 3, because we have 3 keys
print(len(student))


print(student.keys())
print(student.values())

# return pairs - keys and values
print(student.items())

# looping through dictionary
for key in student:
    print(key)

# looping through dictionary
for key, value in student.items():
    print(key, value)