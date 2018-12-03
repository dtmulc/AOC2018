import sys, itertools
def freq(infil):
	i = 0
	freq_chk = 0
	freq_reached = []
	freq_reached.append(0)
	# eval_str = '0'
	# sec_count = 0
	data = open(infil, 'r+')
	freqs = data.readlines()
	for line in freqs:
		freqs[i] = line.strip()
		i += 1
	# eval_str += ' '.join(freqs)
	# print(eval(eval_str))
	while True:
		for freq in itertools.cycle(freqs):
			freq = int(freq)
			freq_chk += freq
			if freq_chk in freq_reached:
				return(freq_chk)
			else:
				freq_reached.append(freq_chk)
				print(len(freq_reached))
		# sec_count += 1
		# print(freq_reached)
		# print()
	# print(sorted(freq_reached))

infil = sys.argv[1]
freq(infil)