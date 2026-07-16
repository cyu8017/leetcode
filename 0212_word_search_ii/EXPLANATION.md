# How We Solve Word Search II

Build a trie from the dictionary, then DFS the board while pruning dead trie branches.

## Steps

1. Insert every word into a trie and store the word at its terminal node.
2. DFS from each board cell following trie edges.
3. When a terminal node is reached, record that word and clear it to avoid duplicates.
4. Mark visited cells, explore four directions, then restore the cell.
5. Prune trie branches that have no remaining children.
