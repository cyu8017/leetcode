# How We Solve Number of Atoms

Parse the formula with a stack of counters for nested parentheses.

## Steps

1. On `(`, push a new counter; on `)`, multiply and merge into the parent.
2. Parse atom names and optional counts into the current counter.
3. Emit atoms in sorted order with counts > 1 shown.
