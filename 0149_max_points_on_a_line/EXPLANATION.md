# How We Solve Max Points on a Line

For each origin point, group other points by reduced slope.

## Steps

1. If there are at most two points, return that count.
2. Fix each point as an origin.
3. Normalize slopes with gcd and a consistent sign.
4. Count how many points share each slope with the origin.
5. Track the global maximum over all origins.
