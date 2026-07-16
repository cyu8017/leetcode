# How We Solve Strobogrammatic Number

Compare digits from both ends using rotational symmetry pairs.

## Steps

1. Map each valid digit to its upside-down partner.
2. Use two pointers at the start and end.
3. Fail if the mapped start digit does not match the end digit.
4. Move both pointers inward.
5. Return true if every pair matches.
