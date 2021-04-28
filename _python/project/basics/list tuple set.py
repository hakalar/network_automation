# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

########################

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

# changing list_1 will change also list_2 because they are both the same mutable object
list_1[0] = 'Art'

print(list_1)
print(list_2)

###########################

# Tuples
# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Will throw an error
tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

###########################
# Sets - unordered and no duplicates
# if you add a duplicate to the set and print out the set, the duplicate value will not be printed

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}

print(cs_courses)


cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

######################
# List

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art','Education']

courses.append(courses_2)
courses.remove('Math')
courses.pop('Physics')

nums = [1,5,6,9,3,4]

courses.reverse()
courses.sort()
courses.sort(reverse=True)
print(max(nums))
print(min(nums))
print(sum(nums))

# sort without modification of the list
sorted_courses = sorted(courses)

# returns a ValueError if Art does not exist
print(courses.index('Art'))

# return true or false - used in conditionals
print ('Art' in courses)

for item in courses:
    print(item)

# enumerate returns index and value
for index, item in enumerate(courses):
    print(index, item)

# enumerate will number index from 1 and not 0
for index, item in enumerate(courses, start = 1):
    print(index, item)

course_str = ', '.join(courses)
print(course_str)

new_list = course_str.split(', ')
print(new_list)