import os

# print all methods available for os
print(dir(os))

# print current working directory
print(os.getcwd())

# change working directory
os.chdir('/Users/xxx/Desktop')

# list directory
print(os.listdir())

# create directory
os.mkdir('OS-Demo-2')

# create directory structure
os.makedirs('OS-Demo-2/Sub-Dir-1')

os.rmdir('OS-Demo-2')
os.removedirts('OS-Demo-2/Sub-Dir-1')

os.rename('original.txt', 'renamed.txt')

# info about file
print(os.stat('demo.txt'))

# info about file, size in Bites
print(os.stat('demo.txt').st_size)

from datetime import datetime

# info about file, last modification time
print(os.stat('demo.txt').st_mtime)
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# print all directory tree
for dirpath, dirnames, filenames in os.walk('/Users/xxx/Desktop'):
    print('Dirpath: ', dirpath)
    print('Directories', dirnames)
    print('Files: ', filenames)

# set path to a file in your home directory
print(os.environ.get('HOME'))
file_path = os.path.join(os.environ.get('HOME'), 'test.txt')

with open (file_path, 'w'):
    pass

# returns path, no file name
os.path.basename('/tmp/test.txt')
# returns file name, no path
os.path.dirname('/tmp/test.txt')
# returns 2 variables - path, file name
os.path.split('/tmp/test.txt')
# check if the path exists - true/false
os.path.exist('/tmp/test.txt')
# check if this is dir - true/false
os.path.isdir('/tmp/efefefefe')
# check if this is file - true/false
os.path.isfile('/tmp./fefefefef')

# returns 2 variables: parth+file name, extension
os.path.splitext('/tmp/test.txt')



