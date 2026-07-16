# How We Solve Brick Wall

A vertical cut crosses fewest bricks where the most row edges already align.

## Steps

1. For each row, record every internal prefix-sum edge position.
2. Count how often each edge position appears across rows.
3. Answer is `rows - max_frequency` (or `rows` if no internal edges).
