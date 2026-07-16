# How We Solve Largest Palindrome Product

Construct palindromes from n-digit prefixes and search for valid factor pairs.

## Steps

1. Build candidate palindromes from descending n-digit numbers.
2. Test divisors downward from the upper n-digit bound.
3. Return the largest valid palindrome product modulo 1337.
