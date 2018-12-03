import sys
def freq_func(infil):
	i = 0
	j = 0
	freq_chk = 0
	freq_reached = []
	freq_reached.append(0)
	eval_str = '0'
	# sec_count = 0
	data = open(infil, 'r+')
	freqs = data.readlines()
	for line in freqs:
		freqs[i] = line.strip()
		i += 1
	eval_str += ' '.join(freqs)
	print(eval(eval_str))
	
	#failed attempt at part 2. I think logically it makes sense but I keep running into weird time out issues running it in windows cmd
	while True:
		for freq in freqs:
			freq = int(freq)
			freq_chk += freq
			if freq_chk in freq_reached:
				return(freq_chk)
			else:
				freq_reached.append(freq_chk)
				# print(len(freq_reached))
		# sec_count += 1
		# print(freq_reached)
		# print()
	# print(sorted(freq_reached))

freq_func(sys.argv[1])
