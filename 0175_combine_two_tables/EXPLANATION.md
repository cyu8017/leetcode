# How We Solve Combine Two Tables

Left join `Address` onto `Person` so every person appears once.

## Steps

1. Select first name, last name, city, and state.
2. Start from the `Person` table.
3. Left join `Address` on matching `personId`.
4. Missing addresses become null city/state.
5. Return the joined rows.
