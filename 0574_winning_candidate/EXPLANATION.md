# How We Solve Winning Candidate

Count votes per candidate and return the name with the most votes.

## Steps

1. Join `Candidate` to `Vote` on candidate id.
2. Group by candidate and count votes.
3. Order by count descending and take the top row.
