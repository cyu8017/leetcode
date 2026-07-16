# How We Solve Find the Duplicate Number

Floyd cycle detection on the index-as-pointer graph finds the duplicate.

## Steps

1. Move slow one step and fast two steps until they meet.
2. Reset slow to the start and advance both one step at a time.
3. The meeting point is the duplicate value.
