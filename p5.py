#!C:\Python27\python 
import string
INFIL = '../p5.txt'
def chain_reaction(infil):
	data = open(infil, 'r+')
	polymer = list(data.read())
	data.close()
	done = False
	while not done:
		removed_count = 0
		try:
			for i in range(0, len(polymer) - 1):
				reactor = polymer[i]
				reactant = polymer[i + 1]
				if reactor.isupper() and reactant.islower() and reactor.lower() == reactant.lower(): 
					del polymer[i]
					del polymer[i]
					i += 1
					removed_count += 1
				elif reactor.islower() and reactant.isupper() and reactor.lower() == reactant.lower():
					del polymer[i]
					del polymer[i]
					i += 1
					removed_count += 1
			if removed_count == 0:
				done = True
		except:
			pass
	return(len(polymer))
def p2(infil):
	data = open(infil, 'r+')
	polymer = list(data.read())
	data.close()
	lens = {}
	for char in string.ascii_lowercase:
		done = False
		polynew = polymer[:]
		for let in polymer:
			if let == char:
				polynew.remove(let)
			elif let == char.upper():
				polynew.remove(let)
		while not done:
			removed_count = 0
			try:
				for i in range(0, len(polynew) - 1):
					reactor = polynew[i]
					reactant = polynew[i + 1]
					if reactor.isupper() and reactant.islower() and reactor.lower() == reactant.lower(): 
						del polynew[i]
						del polynew[i]
						i += 1
						removed_count += 1
					elif reactor.islower() and reactant.isupper() and reactor.lower() == reactant.lower():
						del polynew[i]
						del polynew[i]
						i += 1
						removed_count += 1
				if removed_count == 0:
					done = True
			except:
				pass
		lens[char] = len(polynew)
	smallest_poly = 999999999999
	removed_base = ''
	for k,v in lens.items():
		if (v < smallest_poly):
			removed_base = k
			smallest_poly = v
	print('Polymer of length: ' + str(smallest_poly) + ' can be produced by removing base: ' + removed_base)
print('The smallest fully reacted polymer is of length: ' + str(chain_reaction(INFIL)))
p2(INFIL)