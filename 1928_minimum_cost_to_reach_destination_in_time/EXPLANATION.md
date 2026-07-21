# Approach
Dijkstra ordered by total passing fee. Track the best arrival time per city and only expand when a path arrives strictly earlier (higher fee but more leftover time can unlock cheaper routes later). First time city `n-1` is popped is optimal.

# Complexity
Time O((n + e) * maxTime * log). Space O(n + e).
