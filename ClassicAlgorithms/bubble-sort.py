'''
**Sorting** - Implement two types of sorting algorithms: Merge sort and bubble sort.
'''

def bubble_sort( numbers ):
	l = len( numbers )

	while True:
		swapped = False

		for i in range(1, l):
			if numbers[i-1] > numbers[i]:
				t = numbers[i]
				numbers[i] = numbers[i-1]
				numbers[i-1] = t
				swapped = True
		l -= 1
		if not swapped:
			break

	return numbers

numbers = raw_input('Enter a list of numbers: ')

print bubble_sort( [ int( n.strip() ) for n in numbers.split(',') ] )
