'''
**Count Vowels** - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.
'''

count, vowels = 0, ['a','e','i','o','u']

summary = dict.fromkeys( vowels, 0 )

string = raw_input('Enter a string: ')

for c in string:
	if c in vowels:
		count += 1
		summary[ c ] += 1

print '%s has %s vowels.' % ( string, count )
print summary
