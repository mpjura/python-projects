'''
**Sorting** - Implement two types of sorting algorithms: Merge sort and bubble sort.
'''

def merge_sort( numbers ):
	if len( numbers ) <= 1:
		return numbers

	middle = len( numbers ) / 2
	right  = merge_sort( n[ middle: ] )
	left   = merge_sort( n[ :middle ] )
	
	return merge( left, right )


def merge( left, right ):
	result = []

	while len( left ) > 0 or len ( right ) > 0:
		llen, rlen = len( left ), len( right)

		if llen > 0 and rlen > 0:
			if left[:1] <= right[:1]:
				result.append( left.pop(0) )
			else:
				result.append( right.pop(0) )
		
		elif llen > 0:
			result.append( left.pop(0) )
		
		elif rlen > 0:
			result.append( right.pop(0) )

	return result


string = raw_input('Enter a list of integers: ')
numbers = [ int( n.strip() ) for n in string.split(',') ]

print merge_sort( numbers )
