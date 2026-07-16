# How We Solve Isomorphic Strings

Maintain two maps so the character mapping is a bijection.

## Steps

1. Pair characters from `s` and `t` in order.
2. Map each `s` character to its `t` partner.
3. Map each `t` character back to its `s` partner.
4. Reject any conflict with an earlier mapping.
5. Return true if every pair is consistent.
