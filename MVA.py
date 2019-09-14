
"""MVA.py: Input the service time of queues in series and N, which is for how many requests 
in the system you want to calculate the results. It then outputs the mean response time,
mean throughput and how the requests are "spread" inside the different queues, for each
number of requests from 1 to N"""

__author__      = "Pietro Spadaccino"




def MVA(D_queues, N):

	n_prev = [0] * len(D_queues)    #n_prev[i] = users in queue i at previous MVA step

	for i in range(1, N+1):
		# Use MVA equations
		R = [D_queues[j]*(1+n_prev[j]) for j in range(len(D_queues))]
		R_tot = sum(R)
		X = i/R_tot
		n_prev = [X*r for r in R]

		status = f""">>> N = {i}
	R({i}) = {R_tot/1000:.3f} s
	X({i}) = {1000*X:.2f} requests/s
	n in queues: {[f'{n:.2f}' for n in n_prev]}
	- - - - - - - - - - - - - - -
	"""
		print(status)




if __name__ == '__main__':
	n_queues = int(input("Number of queues in series: "))
	D_queues = []
	for i in range(n_queues):
		D = input(f"Insert service time (D) of queue {i} (in ms): ")
		D_queues.append(int(D))

	N = int(input("Input N (calculate MVA from 1 to N incoming requests ): "))

	MVA(D_queues, N)


