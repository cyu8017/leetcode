# How We Solve Longest Uncommon Subsequence II

Keep each string that is not a subsequence of any other string in the list.

## Steps

1. Test each candidate against every other string with a subsequence check.
2. Skip candidates that appear inside another string.
3. Return the maximum remaining length, or `-1`.
