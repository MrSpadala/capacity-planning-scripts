
"""MVA.py: Input the service time of queues in series and N, which is for how many requests 
in the system you want to calculate the results. It then outputs the mean response time,
mean throughput and how the requests are "spread" inside the different queues, for each
number of requests from 1 to N"""


# Author: Pietro Spadaccino


from matplotlib import pyplot as plt


def MVA(D_queues, N):

	# Vectors to plot later
	R_vect = []
	R_tot_vect = []
	X_vect = []
	N_req_vect = []

	#N_req[i] = users in queue i at previous MVA step
	N_req = [0] * len(D_queues)

	for i in range(1, N+1):
		# Use MVA equations
		R = [D_queues[j]*(1+N_req[j]) for j in range(len(D_queues))]
		R_tot = sum(R)
		X = i/R_tot
		N_req = [X*r for r in R]

		# Append results to vector
		R_vect.append(R)
		R_tot_vect.append(R_tot)
		X_vect.append(X)
		N_req_vect.append(N_req)

		status = f""">>> N = {i}
	R({i}) = {R_tot/1000:.3f} s
	X({i}) = {1000*X:.2f} requests/s
	n in queues: {[f'{n:.2f}' for n in N_req]}
	- - - - - - - - - - - - - - -
	"""
		print(status)

	plot(R_vect, R_tot_vect, X_vect, N_req_vect, N)



def plot(R, R_tot, X, N_req, N):
	n_queues = len(R[0])

	plt.title("Throughput")
	plt.plot(range(1,N+1), X)
	plt.show()

	plt.title("Response Time")
	plt.plot(range(1,N+1), R_tot, 'b--', label='System')
	for i in range(n_queues):  
		plt.plot(range(1,N+1), list(map(lambda x: x[i], R)), label=f'queue {i}')
	plt.legend()
	plt.show()

	plt.title("Requests inside queues")
	for i in range(n_queues):
		plt.plot(range(1,N+1), list(map(lambda x: x[i], N_req)), label=f'queue {i}')
	plt.legend()
	plt.show()



if __name__ == '__main__':
	n_queues = int(input("Number of queues in series: "))
	D_queues = []
	for i in range(n_queues):
		D = input(f"Insert service time (D) of queue {i} (in ms): ")
		D_queues.append(int(D))

	N = int(input("Input N (calculate MVA from 1 to N incoming requests ): "))

	MVA(D_queues, N)


