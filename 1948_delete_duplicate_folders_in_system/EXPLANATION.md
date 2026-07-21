# Approach
Build a folder trie. Serialize each subtree structure; identical nonempty serials are duplicates. DFS and omit any folder whose subtree serial is marked duplicate (and its descendants).

# Complexity
Time O(total path length * log). Space O(total path length).
