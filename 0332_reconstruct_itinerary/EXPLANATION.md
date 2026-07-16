# How We Solve Reconstruct Itinerary

Hierholzer DFS builds the Eulerian path in reverse lexicographic order.

## Steps

1. Push destinations in reverse-sorted order so pop yields lexicographically smallest.
2. DFS from JFK, appending airports after exhausting outgoing edges.
3. Reverse the postorder route to get the itinerary.
