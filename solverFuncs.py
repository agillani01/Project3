def check_rows_valid(puzzle):
	for i in range(len(puzzle)):
		if check_row(puzzle[i]) == False: 
			return False 	
	return True
	 
def check_row(row):
	for i in range(len(row)):
		for j in range(len(row)):			
			if row[i] == row[j] and i != j and row[i] != 0 and row[j] != 0 or row[i] > 5 and row[j] > 5:		
				return False
	return True

def check_columns_valid(puzzle):
	for i in range(len(puzzle)):		
		if check_column(puzzle, i) == False: 
			return False		
	return True

def check_column(puzzle, col_num):
	col_list = []
	for i in range(len(puzzle)):
		item = puzzle[i][col_num] 	
		col_list.append(item) 
	for j in range(len(col_list)): 
		for k in range(len(col_list)):
			if col_list[j] == col_list[k] and j != k and col_list[j] != 0 and col_list[k] != 0 or col_list[j] > 5 and col_list[k] > 5:
				return False
	return True
###
def check_cages_valid(puzzle, cages): 
	for i in range(len(cages)):
		if check_cage(puzzle, cages[i]) == False:
			return False
	return True
###
def check_cage(puzzle, cage):
	a = 0
	need_sum = cage[0]
	full = True
	for i in range(2, len(cage)):
		square = cage[i] 
		row = square_to_row(square) 
		col = square_to_col(square, row)	
		value = puzzle[row][col]
		if value == 0:
			full = False
		a += value 

	if full == False and a >= need_sum: 
		return False
	elif full == True and a == need_sum: 
		return True
	elif full == False and a < need_sum:
		return True
	elif full == True and a != need_sum:
		return False

def square_to_row(square):
	if square <= 4:
		row = 0
	elif square > 4 and square <= 9:
		row = 1
	elif square > 9 and square <= 14:
		row = 2
	elif square > 14 and square <= 19:
		row = 3
	else:
		row = 4
	return row

def square_to_col(square, row):
	col = square - (row * 5) 
	return col

def check_valid(puzzle, cages):
	if check_cages_valid(puzzle, cages) and check_columns_valid(puzzle) and check_rows_valid(puzzle):
		return True	
	return False

def get_cages():
	num_of_cages = int(input('Number of cages: '))
	list_of_cages = []
	for i in range(num_of_cages):
		list_of_strings = []
		list_of_ints = [] 
		user_input = input('Cage number ' +  str(i) + ': ')
		list_of_strings = user_input.split()
		list_of_ints = [int(i) for i in list_of_strings]
		list_of_cages.append(list_of_ints)
	return list_of_cages
