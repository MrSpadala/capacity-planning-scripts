"""markov.py: Input the length of the Markov chain, the arrival rate and the
service rate for each state (autocomplete from previous input also available)
and prints probability to be in each state alongside with mean response time,
mean throughput and mean requests waiting in the system"""

# Authors: Pietro Spadaccino, Luigi Russo


import argparse


def markov(n_states, draw=False):
    lambda_from = [0] * n_states  # lambda_from[i]: lambda from state i to state i+1
    mu_to = [0] * n_states  # mu_to[i]: mu to state i from state i-1

    def autocomplete(is_lambda, i):
        print("Autocomplete")
        to_update = lambda_from if is_lambda else mu_to
        val = to_update[i - 1]
        for j in range(i, n_states):
            to_update[j] = val
            if is_lambda:
                print(f" -> Lambda from state {j} to state {j + 1}: {val}")
            else:
                print(f" <- Mu from state {j + 1} to state {j}: {val}")

    # Input lambda
    for i in range(n_states):
        val = input(f" -> Lambda from state {i} to state {i + 1} {'(empty to autocomplete from previous)' if i else ''}: ")
        if val == "":
            autocomplete(True, i)
            break
        lambda_from[i] = float(val)

    # Input mu
    for i in range(n_states):
        val = input(f" <- Mu from state {i + 1} to state {i} {'(empty to autocomplete from previous)' if i else ''}: ")
        if val == "":
            autocomplete(False, i)
            break
        mu_to[i] = float(val)

    # Calculate coefficients (Pi = coefficients[i+1]*P0)
    coefficients = [lambda_from[0] / mu_to[0]]
    for i in range(1, n_states):
        c = coefficients[i - 1] * lambda_from[i] / mu_to[i]
        coefficients.append(c)

    P0 = 1 / (sum(coefficients) + 1)  # equation P0+c1P0+c2P0+...=1
    P = [c * P0 for c in coefficients]


    print("\n\n~ ~ ~  Results  ~ ~ ~")

    # Format response
    s_format = ""
    for i in range(n_states):
        s_format += f"P{i + 1} = {P[i]:.3f}\n"
    result = f"\nProbability Pi of being in state i"
    result += f"\nP0 = {P0:.3f}\n{s_format}"

    print(result)

    print(f">>> Utilization factor (1-P0): {1 - P0:.3f}\n")
    print(f">>> Fraction of lost requests (P{n_states}): {P[-1]:.3f}\n")

    # Calculate N,X,R mean
    X_mean = sum([p * x for p, x in zip(P, mu_to)])
    N_mean = sum([p * n for p, n in zip(P, range(1, n_states))])
    R_mean = N_mean / X_mean

    # Print means and their normalized value. The normalized value is the
    # actual value, since there is no "throughput" or "response time" when
    # we have no request in the system, when we are in state 0
    print(f">>> X mean = {X_mean:.2f} requests/s")
    print(f">>> X mean normalized = {X_mean / (1 - P0):.2f} requests/s\n")

    print(f">>> N mean = {N_mean:.2f} requests\n")

    print(f">>> R mean = {R_mean:.2f} s")
    print(f">>> R mean normalized = {R_mean / (1 - P0):.2f} s\n")

    # let's draw the Markov chain (if necessary)
    if draw:
        try:
            from graphviz import Digraph
        except ImportError:
            raise Exception(graphviz_err)

        graph_name = f"Markov_{n_states}_states"
        dot = Digraph(comment=graph_name, format='png')
        with dot.subgraph() as s:
            s.attr(rank='same')
            for i in range(n_states + 1):
                if i == 0:
                    dot.node(str(i), f"{i}\n({P0:.2f})")
                else:
                    dot.node(str(i), f"{i}\n({P[i - 1]:.2f})")
            for i in range(n_states):
                dot.edge(str(i), str(i + 1), label=str(lambda_from[i]))
                dot.edge(str(i + 1), str(i), label=str(mu_to[i]))
        dot.graph_attr['rankdir'] = 'LR'  # set an intuitive orientation

        try:
            dot.render(f"output/{graph_name}.gv", view=True)
        except Exception as e:
            print(graphviz_err, '\n\n\n')
            raise e


def setup_parser():
    # set the main parser
    parser = argparse.ArgumentParser(description='Markov Chain')
    parser.add_argument('--draw', help='output the Markov chain as png image', action='store_true')

    # create the parser
    return parser.parse_args()


graphviz_err = '''\nPackage "graphviz" missing or not correctly installed. Fix by:
\t1. Run "pip install graphviz", or pip3
\t2. (Linux only) Run "sudo apt install graphviz"
\t2. (Winzozz only) Go here https://graphviz.gitlab.io/_pages/Download/Download_windows.html download and extract the zip wherever you want (maybe in Program Files). Then add "bin" folder to your PATH environment variable'''

if __name__ == '__main__':
    args = setup_parser()
    n_states = int(input("Max number of requests waiting inside the system: "))
    if n_states > 0:
        markov(n_states, draw=args.draw)
