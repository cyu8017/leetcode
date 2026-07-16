# How We Solve Find the Celebrity

Eliminate non-celebrities with one pass, then verify the survivor.

## Steps

1. Start with person 0 as the candidate.
2. If the candidate knows someone, that person becomes the new candidate.
3. After elimination, verify everyone knows the candidate.
4. Verify the candidate knows nobody.
5. Return the candidate or -1 if verification fails.
