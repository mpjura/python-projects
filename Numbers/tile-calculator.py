'''
**Find Cost of Tile to Cover W x H Floor** - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
'''

def main():
	tile = float( raw_input('Tile cost per square foot: ') )
	w = float( raw_input('Width of room in feet: ') )
	h = float( raw_input('Height of room in feet: ') )

	print 'Total cost: %.2f' % ( w * h * tile )


if __name__ == '__main__':
	main()