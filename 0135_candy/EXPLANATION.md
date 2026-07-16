# How We Solve Candy

Two passes enforce the left and right neighbor rating constraints.

## Steps

1. Give every child one candy.
2. Left-to-right: if ratings rise, give one more than the left neighbor.
3. Right-to-left: if ratings rise going left, raise to beat the right neighbor.
4. Take the max of both constraints at each child.
5. Sum the candies.
