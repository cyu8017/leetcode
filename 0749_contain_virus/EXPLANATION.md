# How We Solve Contain Virus

Each night, wall off the infected region that threatens the most uninfected cells, then spread the rest.

## Steps

1. Find infected regions, their frontiers, and wall perimeters.
2. Quarantine the region with the largest frontier (add its perimeter to the answer).
3. Let other regions infect their frontiers; repeat until no threats remain.
