
"""markov.py: Input the length of the Markov chain, the arrival rate and the 
service rate for each state (autocomplete from previous input also available)
and prints probability to be in each state alongside with mean response time,
mean throughput and mean requests waiting in the system"""

__author__      = "Pietro Spadaccino"




def markov(n_states):
	lambda_from = [0] * n_states   #lambda_from[i]: lambda from state i to state i+1
	mu_to = [0] * n_states         #mu_to[i]: mu to state i from state i-1


	def autocomplete(is_lambda, i):
		print("Autocomplete")
		to_update = lambda_from if is_lambda else mu_to
		val = to_update[i-1]
		for j in range(i, n_states):
			to_update[j] = val
			if is_lambda:
				print(f" -> Lambda from {j} to {j+1}: {val}")
			else:
				print(f" <- Mu from {j+1} to {j}: {val}")


	# Input lambda
	for i in range(n_states):
		l = input(f" -> Lambda from {i} to {i+1} {'(empty to autocomplete from previous)' if i else ''}: ")
		if l=="":
			autocomplete(True, i)
			break
		lambda_from[i] = float(l)

	# Input mu
	for i in range(n_states):
		l = input(f" <- Mu from {i+1} to {i} {'(empty to autocomplete from previous)' if i else ''}: ")
		if l=="":
			autocomplete(False, i)
			break
		mu_to[i] = float(l)



	# Calculate coefficients (Pi = coefficients[i+1]*P0)
	coefficients = [lambda_from[0] / mu_to[0]]
	for i in range(1, n_states):
		c = coefficients[i-1] * lambda_from[i] / mu_to[i]
		coefficients.append(c)

	P0 = 1/(sum(coefficients)+1)     # equation P0+c1P0+c2P0+...=1
	P = [c*P0 for c in coefficients]


	# Format response
	s_format = ""
	for i in range(n_states):
		s_format += f"P{i+1} = {P[i]:.2f}\n"
	result = f"\nP0 = {P0:.2f}\n{s_format}"

	print(result)

	print(f">>> Utilization factor (1-P0): {1-P0:.3f}\n")
	print(f">>> Fraction of lost requests (P{n_states}): {P[-1]:.3f}\n")


	# Calculate N,X,R mean
	X_mean = sum([p*x for p,x in zip(P, mu_to)])
	N_mean = sum([p*n for p,n in zip(P, range(1, n_states))])
	R_mean = N_mean / X_mean

	# Print means and their normalized value. The normalized value is the
	# actual value, since there is no "throughput" or "response time" when
	# we have no request in the system, when we are in state 0
	print(f">>> X mean = {X_mean:.2f} requests/s")
	print(f">>> X mean normalized = {X_mean/(1-P0):.2f} requests/s\n")

	print(f">>> N mean = {N_mean:.2f} requests\n")

	print(f">>> R mean = {R_mean:.2f} s")
	print(f">>> R mean normalized = {R_mean*(1-P0):.2f} s\n")




if __name__ == '__main__':
	n_states = int(input("Max number of requests waiting inside the system: "))
	markov(n_states)

