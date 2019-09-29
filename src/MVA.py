"""MVA.py: Input the service time of queues in series and N, which is for how many requests
in the system you want to calculate the results. It then outputs the mean response time,
mean throughput and how the requests are "spread" inside the different queues, for each
number of requests from 1 to N"""

# Author: Pietro Spadaccino

import argparse


def MVA(D_queues, N, plot=False):
    # Vectors to plot later
    R_vect = []
    R_tot_vect = []
    X_vect = []
    N_req_vect = []

    # N_req[i] = users in queue i at previous MVA step
    N_req = [0] * len(D_queues)

    for i in range(1, N + 1):
        # Use MVA equations
        R = [D_queues[j] * (1 + N_req[j]) for j in range(len(D_queues))]
        R_tot = sum(R)
        X = i / R_tot
        N_req = [X * r for r in R]

        # Append results to vector
        R_vect.append(R)
        R_tot_vect.append(R_tot)
        X_vect.append(X)
        N_req_vect.append(N_req)

        status = f""">>> N = {i}
	R({i}) = {R_tot / 1000:.3f} s
	X({i}) = {1000 * X:.2f} requests/s
	n in queues: {[f'{n:.2f}' for n in N_req]}
	- - - - - - - - - - - - - - -
	"""
        print(status)

    if plot:
        plot_results(R_vect, R_tot_vect, X_vect, N_req_vect, N)


def plot_results(R, R_tot, X, N_req, N):
    from matplotlib import pyplot as plt

    n_queues = len(R[0])

    plt.title("Throughput")
    plt.plot(range(1, N + 1), [1000 * x for x in X])  # convert from req/ms to req/s
    plt.xlabel('requests'), plt.ylabel('requests / s')
    plt.xticks(range(1, N + 1, 2))
    plt.xlim(1, N)
    plt.show()

    plt.title("Response Time")
    plt.plot(range(1, N + 1), R_tot, 'b--', label='System')
    for i in range(n_queues):
        plt.plot(range(1, N + 1), list(map(lambda x: x[i], R)), label=f'queue {i}')
    plt.xlabel('requests'), plt.ylabel('ms')
    plt.xticks(range(1, N + 1, 2))
    plt.xlim(1, N)
    plt.legend()
    plt.show()

    plt.title("Requests inside queues")
    for i in range(n_queues):
        plt.plot(range(1, N + 1), list(map(lambda x: x[i], N_req)), label=f'queue {i}')
    plt.xlabel('requests'), plt.ylabel('requests')
    plt.xticks(range(1, N + 1, 2))
    plt.xlim(1, N)
    plt.legend()
    plt.show()


def setup_parser():
    parser = argparse.ArgumentParser(description='MVA')
    parser.add_argument('--plot', help='plot MVA results on a graph', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = setup_parser()
    n_queues = int(input("Number of queues in series: "))
    D_queues = []
    for i in range(n_queues):
        D = input(f"Insert service time (D) of queue {i} (in ms): ")
        D_queues.append(int(D))

    N = int(input("Input N (calculate MVA from 1 to N incoming requests ): "))

    MVA(D_queues, N, plot=args.plot)
