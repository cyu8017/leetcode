# Approach
Store parent/children and lock owner per node. Upgrade checks unlocked ancestors, unlocks all locked descendants, then locks the node.

# Complexity
Per op O(n) worst. Space O(n).
