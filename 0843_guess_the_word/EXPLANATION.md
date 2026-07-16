# How We Solve Guess the Word

Repeatedly guess the word that minimizes the worst-case remaining candidates.

## Steps

1. Among candidates, pick the guess with the smallest max match-bucket size.
2. Call `master.guess` and keep only words with the same match count.
3. Stop when the guess returns 6 matches.
