# module_using_sys.py
# 19-4-2016 mk


import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')


#  The command line arguments are:
#  /Users/marcel/Documents/git-test/module_sys.py
#
#
#  The PYTHONPATH is ['/Users/marcel/Documents/git-test',
#
