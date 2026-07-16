# How We Solve Group Anagrams

Put words that use the same letters into the same group.

## Steps

1. For each word, sort its letters to make a key.
2. Words with the same key are anagrams — put them in one bucket.
3. Sort words inside each bucket alphabetically.
4. Order buckets by where their words first appear in the input.
5. Return the list of buckets.
