# How We Solve Substring with Concatenation of All Words

Find starts where s is made of all given words glued together (same length words).

## Steps

1. Count how many times each word is needed.
2. Try each possible alignment offset (0 .. wordLength-1).
3. Slide a window word-by-word across s.
4. Track word counts in the current window.
5. If a bad word appears, reset the window.
6. When window uses all words correctly, save the start index.
7. Return all start indexes (sorted).
