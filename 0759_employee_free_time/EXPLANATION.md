# How We Solve Employee Free Time

Merge all busy intervals globally; gaps between merges are common free time.

## Steps

1. Flatten every employee’s intervals and sort by start.
2. Merge overlapping busy ranges.
3. Emit `[prevEnd, nextStart]` for each gap.
