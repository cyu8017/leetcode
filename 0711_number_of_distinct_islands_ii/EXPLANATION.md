# How We Solve Number of Distinct Islands II

Treat rotations/reflections as the same by taking a canonical transform of each shape.

## Steps

1. Flood-fill islands and collect cell coordinates.
2. Apply all 8 dihedral transforms; normalize each by shifting to the origin.
3. Store the minimum normalized shape in a set; return its size.
