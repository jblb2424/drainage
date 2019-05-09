def cut(i, j):
	top, bottom, left, right = 0, 0, 0, 0

	'''
	Return itself if we already computed the best path
	'''
	if C[i][j] != -1:
		return C[i][j]


	####Recursive Cases####
	'''
	Try catch is used to detect if we're on an edge and the space above/below/ect does not exist
	Ignores the computation in that case
	'''

	try:
		if mpnTop[i][j] > mpnTop[i+1][j]:
			bottom = cut(i+1, j) + 1

	except:
		pass
	
	try:
		if mpnTop[i][j] > mpnTop[i-1][j] and i != 0:
			top =  cut(i-1, j) + 1
	except:
		pass
	
	try:
		if mpnTop[i][j] > mpnTop[i][j+1]:
			right =  cut(i, j+1) + 1
	except:
		pass

	try:
		if mpnTop[i][j] > mpnTop[i][j-1] and j != 0:
			left =  cut(i, j-1) + 1
	except:
		pass


	####Base Cases####
	'''
	Checks if we are at a "basin", where we checked every direction
	but all areas are of higher elevation. If so, return 1
	'''
	if top == 0 and bottom == 0 and left == 0 and right == 0:
		C[i][j] = 1
		return 1


	'''
	Return the maximum value from all computed diretions
	To get to this point, we have longest paths in our C matrix saved
	for every direction around the coordinate
	'''	
	
	C[i][j] = max([top, bottom, left, right])
	return C[i][j]

#### Giiven Read Code #####
f = open('test1-3.test', 'r')
C = []
for i in range(int(f.readline())):
	lsstInput = f.readline().split()
	stCity = lsstInput[0]
	numRows = int(lsstInput[1])
	mpnTop = [] #Input grid of elevations
	for row in range(numRows):
		mpnTop.append(list(map(lambda st: int(st), f.readline().split())))



	'''
	We assume all inputs will be squares.
	Generate our Copy array, fill it with -1s as dummy values
	'''
	for row in range(numRows):
		ar = []
		for col in range(numRows):
			ar.append(-1)
		C.append(ar)

	'''
	Calculate optimal path for every coordinate, and find the max of our C matrix
	'''
	for i in range(len(mpnTop)):
		for j in range(len(mpnTop)):
			cut(i,j)

	total_max = max([max(grid) for grid in C])
	print(stCity + ": " + str(total_max))

	C = []


	#print(mpnTop)












