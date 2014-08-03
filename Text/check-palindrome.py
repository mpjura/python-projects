s = raw_input('Enter a string: ')

print '%s is' % s,

if s != s[::-1]:
	print 'not',

print 'a palindrome.'
