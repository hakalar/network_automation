# use mm instead of my_module
import my_module as mm
import sys
# sys.path.append('/Users/xxx/Desktop/My-Modules')

# to be able to call find_index function directly
# but you dont have access to anything else from the module
from my_module import find_index

# do not do this, lose readibility
from my_module import find_index as fi, test

# do not do this, you lose track what comes from module and what from other places
from my_module import *

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')
print(index)

# locations from where modules are imported
print(sys.path)