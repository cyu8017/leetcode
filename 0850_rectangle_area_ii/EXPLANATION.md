# How We Solve Rectangle Area II

Vertical sweep line with active y-intervals; area modulo `10^9+7`.

## Steps

1. Emit enter/leave events at each rectangle's left and right x.
2. Between events, add `covered_y_length * Δx`.
3. Merge overlapping active y-segments to get covered length.
