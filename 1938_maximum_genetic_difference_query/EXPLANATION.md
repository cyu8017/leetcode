# Approach
DFS the parent tree while maintaining a binary trie of node values on the root-to-current path. Answer each query as the maximum XOR against the query value, then backtrack.

# Complexity
Time O((n + q) * bits). Space O(n * bits).
