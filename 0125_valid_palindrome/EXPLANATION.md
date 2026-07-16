# How We Solve Valid Palindrome

Ignore non-alphanumeric characters and compare case-insensitively.

## Steps

1. Place two pointers at the ends of the string.
2. Skip characters that are not letters or digits.
3. Compare the lowercased pair.
4. Move inward while they match.
5. Return true if the pointers meet without a mismatch.
