# How We Solve Poor Pigs

Each pig can distinguish among several test outcomes across rounds; find the minimum pigs needed to cover all buckets.

## Steps

1. Compute how many outcome states one round provides.
2. Each pig multiplies the distinguishable state space by that base.
3. Increase the pig count until capacity is at least the number of buckets.
