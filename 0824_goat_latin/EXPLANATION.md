# How We Solve Goat Latin

Transform each word by the vowel/consonant rules, then append index `'a'`s.

## Steps

1. Split the sentence into words.
2. Vowels keep order + `"ma"`; consonants rotate first letter + `"ma"`.
3. Append `"a" * word_index` and join with spaces.
