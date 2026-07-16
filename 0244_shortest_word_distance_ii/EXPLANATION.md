# How We Solve Shortest Word Distance II

Given a list of words, quickly find the smallest gap between two given words.

## Steps

1. When built, save every index where each word appears.
2. To query word1 and word2, walk their two index lists with two fingers.
3. Compute distance between current pair of indexes.
4. Keep the smallest distance seen.
5. Move the finger pointing to the smaller index forward.
6. Return the smallest distance.
