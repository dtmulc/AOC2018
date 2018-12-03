def cloth(infil):
	grid = [[0 for i in range(0,1000)] for j in range(0,1000)]
	overused = 0 
	data = open(infil, 'r+')
	lines = data.readlines()
	data.close()
	for space in lines:
		coords = space[space.index('@') + 2: space.index(':')]
		coords = coords.split(',')
		dim = space[space.index(':') + 2::].strip().split('x')
		row = int(coords[0])
		column = int(coords[1])
		x_len = int(dim[1])
		y_len = int(dim[0])
		for i in range(x_len):
			for j in range(y_len):
				grid[row + j][column + i] += 1				
	for line in grid:
		line_sum = sum(num >= 2 for num in line)
		overused += line_sum

	print(overused)

import sys, collections
def cloth2(infil):
	grid = [[0 for i in range(0,1000)] for j in range(0,1000)]
	overused = 0 
	plan_ok = {}
	data = open(infil, 'r+')
	lines = data.readlines()
	data.close()
	# for line in lines:
	# 	spc_id = line[1:line.index('@') - 1]
	# 	plan_ok[spc_id] = True
	# print(plan_ok)
	for space in lines:
		space_id = space[1:space.index('@') - 1]
		plan_ok[int(space_id)] = True
		coords = space[space.index('@') + 2: space.index(':')]
		coords = coords.split(',')
		dim = space[space.index(':') + 2::].strip().split('x')
		row = int(coords[0])
		column = int(coords[1])
		x_len = int(dim[1])
		y_len = int(dim[0])
		for i in range(x_len):
				for j in range(y_len):
					grid[row + j][column + i] += 1
	for line in lines:
		space_id = space[1:space.index('@') - 1]
		coords = space[space.index('@') + 2: space.index(':')]
		coords = coords.split(',')
		dim = space[space.index(':') + 2::].strip().split('x')
		row = int(coords[0])
		column = int(coords[1])
		x_len = int(dim[1])
		y_len = int(dim[0])
		overlap = False
		for x in range(x_len):
			for y in range(y_len):
				if grid[row + y][column + x] > 1:
					overlap = True
				
		if not overlap:
			print(space_id)
				
	# for line in grid:
	# 	spc_id = line[1:line.index('@') - 1]
	# 	for spot in line:
	# 		if spot[1] != '' and plan_ok[spc_id]:
	# 			print(spc_id)
	# for key in sorted(plan_ok):
		# print "%s: %s" % (key, plan_ok[key])
							
	# for line in grid:
	# 	not_overlap = [char for char in line if char[1] != 'X']
	# 	# overused += line_sum
	# for block in not_overlap:
	# 	if(block[0] != 0): print(block[1])

cloth2('../p3.txt')