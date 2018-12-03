import sys
from collections import Counter

def p2(infil):
	data = open(infil, 'r+')
	lines = data.readlines()
	counter = [0, 0]
	for line in lines:
		most_common = [count for line, count in Counter(list(line)).most_common()]
		if 3 in most_common:counter[0] += 1
		if 2 in most_common: counter[1] += 1
	print(counter[0] * counter[1])

def part2(infil):
	data = open(infil, 'r+')
	lines = data.readlines()
	
	for line in range(0, len(lines) - 1):
		wrong = dict(zip(lines, [0] * len(lines)))
		# print(wrong)
		for k,v in wrong.items():
			for letter in range(0,len(k) - 1):
				if lines[line][letter] == k[letter]:
					pass
				else:
					wrong[k] += 1
		for k,v in wrong.items():
			if v == 1:
				s1, s2 = lines[line], k
	print(s1,s2)


part2('../p2.txt')