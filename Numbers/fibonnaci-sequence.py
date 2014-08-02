def fib( n ):
	
	if n <= 2:
		return n if n < 2 else 1

	k = n / 2

	a = fib( k )
	b = fib( k + 1 )

	if n % 2 == 1:
		return int( a*a + b*b )
	else:
		return int( a * ( b*2 - a ) )

def get_input():
	return raw_input("Enter Fibonnaci sequence length ('q' to quit): ")


def main():
	i = get_input()

	while i != 'q' and int( i ) >= 0:
		print fib( int( i ) )
		i = get_input()

if __name__ == '__main__':
	main()