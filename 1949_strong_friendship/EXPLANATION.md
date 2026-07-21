# Approach
Make friendship undirected. For each edge `(u,v)`, count shared neighbors; keep pairs with at least 3 common friends.

# Complexity
Time depends on join size. Space O(|E|).
