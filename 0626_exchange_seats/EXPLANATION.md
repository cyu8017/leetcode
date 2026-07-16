# How We Solve Exchange Seats

Swap each odd id with the next even id, leaving a final odd seat alone.

## Steps

1. Map odd ids to `id + 1`, even ids to `id - 1`.
2. Keep the last id unchanged when the count is odd.
3. Order the result by the remapped id.
