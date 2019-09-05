## What is this?

These are a couple of small scripts for students attending "Capacity Planning" course at Sapienza univeristy with prof. Bruno Ciciani. What they do is just calculate numerically the solution of two of the most recurring problem during the course, which are:
  - When you have a generic `M/M/x/y` queue (`x` servers, `y` finite length) represented by a Markov chain with `y+1` states (0, 1, ..., `y`) and you want to know the probabilities to be in each state, to calculate the _average throughput_, _average response time_, the _utilization factor_, the _expected number of waiting requests_ and the _fraction of lost requests_.
  - Mean Value Analysis (MVA): calculate the response time, the throughput and identify the bottleneck when you have _multiple M/M/1 queues in serial_
  
__NB__ These scripts don't do any magic, they just return the numerical value once the problem is set. The numerical solution is not required during the exam, since it may take a long time to do these calculations by hand, but I think that sometimes having the actual numbers could be interesting and makes you understand if you made some serious mistakes.


For any mistake/error that you find feel free to open a pull request
