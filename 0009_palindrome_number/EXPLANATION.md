# How We Solve Palindrome Number

Check if a number reads the same backward.

## Steps

1. Negative numbers are not palindromes.
2. Build half the digits in reverse.
3. Each step: take last digit, add to reversed pile, chop original.
4. Stop when original <= reversed.
5. Compare original and reversed (odd length allows middle digit).
6. Return true or false.
