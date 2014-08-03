'''
**Count Words in a String** - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
'''

string = raw_input('Enter a string: ')

print 'There are %s words in that string.' % len( string.split(' ') )
