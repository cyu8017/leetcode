# How We Solve Design Excel Sum Formula

Store cell values and optional formula cell lists; evaluate formulas recursively.

## Steps

1. `set` clears any formula and writes a concrete value.
2. `sum` expands single cells and ranges into a dependency list for that cell.
3. `get`/`sum` evaluate by summing dependencies (no cycles by problem guarantee).
