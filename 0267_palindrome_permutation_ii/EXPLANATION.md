# How We Solve Palindrome Permutation II

Build unique permutations of half the string and mirror them around a middle character.

## Steps

1. Count characters and reject more than one odd count.
2. Put any odd-count character in the middle.
3. Build the sorted half with half of each character count.
4. Backtrack unique permutations of the half.
5. Mirror each prefix to form full palindromes.
