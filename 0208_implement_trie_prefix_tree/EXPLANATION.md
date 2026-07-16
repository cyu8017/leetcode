# How We Solve Implement Trie (Prefix Tree)

Store words in a character tree with an end-of-word flag on terminal nodes.

## Steps

1. Start each operation at the root.
2. On insert, create missing child nodes for each character.
3. Mark the final node as a complete word.
4. Search requires reaching a node marked as a word.
5. startsWith only requires that the prefix path exists.
