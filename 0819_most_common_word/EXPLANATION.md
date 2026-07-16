# How We Solve Most Common Word

Normalize words to lowercase letters only; pick the top non-banned count.

## Steps

1. Extract `[a-z]+` tokens from the paragraph.
2. Skip banned words while counting.
3. Return the most frequent remaining word.
