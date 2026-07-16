# How We Solve Design Add and Search Words Data Structure

Store words in a trie and search with DFS when a dot wildcard appears.

## Steps

1. Each trie node maps characters to child nodes and marks word endings.
2. `addWord` walks the trie and sets the final node as a word.
3. `search` walks character by character for literal letters.
4. On `.`, try every child recursively.
5. A match succeeds only if the path ends on a word node.
