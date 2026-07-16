# Approach: Find parents for every node, then handle two cases when moving
# subtree `p` under `q`.

# If `q` already parents `p`, nothing changes. If `q` lies inside `p`'s subtree,
# detach `q` first and put it in `p`'s old place (or make it the new root) so the
# tree stays connected, then attach `p` under `q`. Otherwise simply detach `p`
# and append it to `q`'s children.

# Time: O(n). Space: O(n) for the parent map and recursion stack.
