# How We Solve Shortest Word Distance

Track the latest positions of both words while scanning the list once.

## Steps

1. Initialize the last seen index of each word to -1.
2. Walk through the word list in order.
3. Update the index when word1 or word2 appears.
4. If the other word was seen already, update the minimum distance.
5. Return the smallest gap found.
