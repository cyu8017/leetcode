# How We Solve Minimum Genetic Mutation

Treat each valid gene as a graph node; edges connect genes one letter apart.

## Steps

1. BFS from the start gene through the bank.
2. Try changing each position to A/C/G/T and enqueue unvisited bank genes.
3. Return the step count when the end gene is reached, or -1 if unreachable.
