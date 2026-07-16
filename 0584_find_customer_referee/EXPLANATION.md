# How We Solve Find Customer Referee

Keep customers whose referee is not 2, including those with no referee.

## Steps

1. Select names from `Customer`.
2. Filter with `referee_id != 2 OR referee_id IS NULL`.
